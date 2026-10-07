"""Generador mínimo de gráficos 2D en SVG (Python puro, sin dependencias).

Uso:
    p = Plot(xmin, xmax, ymin, ymax, width=360)
    p.region(lambda x, y: x*x + y*y < 4)          # sombrea donde el predicado es verdadero
    p.curve(lambda t: (cos(t), sin(t)), 0, 2*pi)   # curva paramétrica
    p.fx(lambda x: x**2, -2, 2)                    # gráfico de y = f(x)
    p.implicit(lambda x, y: x*x + y*y - 1)         # curva F(x, y) = 0
    p.point(1, 2, filled=True, label='A')
    p.save('archivo.svg')
"""
import math

COLORS = ['#1f6fd1', '#d1491f', '#2a9d3c', '#8e3fbf', '#c49000', '#0f8f8f', '#b0306a']


class Plot:
    def __init__(self, xmin, xmax, ymin, ymax, width=360, height=None, grid=1.0,
                 xlabel='x', ylabel='y', ticks=True):
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.W = width
        self.H = height or int(width * (ymax - ymin) / (xmax - xmin))
        self.pad = 24
        self.items_bg, self.items, self.items_fg = [], [], []
        self.grid, self.xlabel, self.ylabel, self.ticks = grid, xlabel, ylabel, ticks

    def X(self, x):
        return self.pad + (x - self.xmin) / (self.xmax - self.xmin) * self.W

    def Y(self, y):
        return self.pad + (self.ymax - y) / (self.ymax - self.ymin) * self.H

    def region(self, pred, color='#1f6fd1', opacity=0.28, res=2):
        """Sombrea {(x,y) : pred(x,y)} muestreando por filas de `res` px."""
        rows = []
        for py in range(0, int(self.H), res):
            y = self.ymax - (py + res / 2) / self.H * (self.ymax - self.ymin)
            run = None
            for px in range(0, int(self.W) + res, res):
                x = self.xmin + (px + res / 2) / self.W * (self.xmax - self.xmin)
                try:
                    ok = px < self.W and pred(x, y)
                except (ValueError, ZeroDivisionError, OverflowError):
                    ok = False
                if ok and run is None:
                    run = px
                elif not ok and run is not None:
                    rows.append(f'<rect x="{self.pad+run}" y="{self.pad+py}" width="{px-run}" height="{res}"/>')
                    run = None
        self.items_bg.append(f'<g fill="{color}" fill-opacity="{opacity}" shape-rendering="crispEdges">' + ''.join(rows) + '</g>')

    def _poly(self, pts, color, width, dash):
        segs, cur = [], []
        for p in pts:
            if p is None or not all(map(math.isfinite, p)) or abs(p[1]) > 1e6:
                if len(cur) > 1:
                    segs.append(cur)
                cur = []
                continue
            cur.append(p)
        if len(cur) > 1:
            segs.append(cur)
        d = ' '.join('M' + ' L'.join(f'{self.X(x):.1f},{self.Y(y):.1f}' for x, y in s) for s in segs)
        da = ' stroke-dasharray="6,4"' if dash else ''
        self.items.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{da}/>')

    def curve(self, f, t0, t1, color=None, width=2, dash=False, n=600):
        color = color or COLORS[0]
        pts = []
        for i in range(n + 1):
            t = t0 + (t1 - t0) * i / n
            try:
                x, y = f(t)
                if not (self.xmin - 1 <= x <= self.xmax + 1 and self.ymin - 1 <= y <= self.ymax + 1):
                    pts.append(None)
                    continue
                pts.append((x, y))
            except (ValueError, ZeroDivisionError, OverflowError):
                pts.append(None)
        self._poly(pts, color, width, dash)

    def fx(self, f, x0=None, x1=None, **kw):
        x0 = self.xmin if x0 is None else x0
        x1 = self.xmax if x1 is None else x1
        self.curve(lambda t: (t, f(t)), x0, x1, **kw)

    def implicit(self, F, color=None, width=2, dash=False, n=240):
        """Curva de nivel F(x,y)=0 por marching squares simple."""
        color = color or COLORS[0]
        dx = (self.xmax - self.xmin) / n
        dy = (self.ymax - self.ymin) / n

        def v(i, j):
            try:
                return F(self.xmin + i * dx, self.ymin + j * dy)
            except (ValueError, ZeroDivisionError, OverflowError):
                return float('nan')
        vals = [[v(i, j) for j in range(n + 1)] for i in range(n + 1)]
        segs = []
        for i in range(n):
            for j in range(n):
                c = [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]
                vv = [vals[a][b] for a, b in c]
                if any(map(math.isnan, vv)):
                    continue
                pts = []
                for k in range(4):
                    a, b = vv[k], vv[(k + 1) % 4]
                    if (a < 0) != (b < 0):
                        t = a / (a - b)
                        (i0, j0), (i1, j1) = c[k], c[(k + 1) % 4]
                        pts.append((self.xmin + (i0 + t * (i1 - i0)) * dx, self.ymin + (j0 + t * (j1 - j0)) * dy))
                if len(pts) >= 2:
                    segs.append((pts[0], pts[1]))
                if len(pts) == 4:
                    segs.append((pts[2], pts[3]))
        d = ' '.join(f'M{self.X(a[0]):.1f},{self.Y(a[1]):.1f} L{self.X(b[0]):.1f},{self.Y(b[1]):.1f}' for a, b in segs)
        da = ' stroke-dasharray="6,4"' if dash else ''
        self.items.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{da}/>')

    def segment(self, x0, y0, x1, y1, color='#333', width=2, dash=False):
        self._poly([(x0, y0), (x1, y1)], color, width, dash)

    def arrow(self, x0, y0, x1, y1, color='#333', width=1.6):
        self.items_fg.append(f'<line x1="{self.X(x0):.1f}" y1="{self.Y(y0):.1f}" x2="{self.X(x1):.1f}" y2="{self.Y(y1):.1f}" stroke="{color}" stroke-width="{width}" marker-end="url(#a)"/>')

    def point(self, x, y, filled=True, label=None, color='#222', dx=6, dy=-6):
        fill = color if filled else 'white'
        self.items_fg.append(f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="4" fill="{fill}" stroke="{color}" stroke-width="1.5"/>')
        if label:
            self.text(x, y, label, dx=dx, dy=dy, color=color)

    def text(self, x, y, s, dx=0, dy=0, color='#222', size=13):
        self.items_fg.append(f'<text x="{self.X(x)+dx:.1f}" y="{self.Y(y)+dy:.1f}" font-size="{size}" font-family="sans-serif" fill="{color}">{s}</text>')

    def save(self, path, title=None):
        W, H, p = self.W + 2 * self.pad, self.H + 2 * self.pad, self.pad
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.0f} {H:.0f}">',
               '<rect width="100%" height="100%" fill="white"/>']
        if title:
            out.append(f'<title>{title}</title>')
        g = []
        if self.grid:
            k = math.ceil(self.xmin / self.grid)
            while k * self.grid <= self.xmax:
                g.append(f'<line x1="{self.X(k*self.grid):.1f}" y1="{p}" x2="{self.X(k*self.grid):.1f}" y2="{p+self.H}"/>')
                k += 1
            k = math.ceil(self.ymin / self.grid)
            while k * self.grid <= self.ymax:
                g.append(f'<line x1="{p}" y1="{self.Y(k*self.grid):.1f}" x2="{p+self.W}" y2="{self.Y(k*self.grid):.1f}"/>')
                k += 1
        out.append('<g stroke="#e4e4e4" stroke-width="1">' + ''.join(g) + '</g>')
        out += self.items_bg
        ax = []
        if self.ymin <= 0 <= self.ymax:
            ax.append(f'<line x1="{p}" y1="{self.Y(0):.1f}" x2="{p+self.W+8}" y2="{self.Y(0):.1f}" marker-end="url(#a)"/>')
        if self.xmin <= 0 <= self.xmax:
            ax.append(f'<line x1="{self.X(0):.1f}" y1="{p+self.H}" x2="{self.X(0):.1f}" y2="{p-8}" marker-end="url(#a)"/>')
        out.append('<defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#555"/></marker></defs>')
        out.append('<g stroke="#555" stroke-width="1.3">' + ''.join(ax) + '</g>')
        if self.ticks and self.grid:
            t = []
            k = math.ceil(self.xmin / self.grid)
            while k * self.grid <= self.xmax:
                v = k * self.grid
                if abs(v) > 1e-9 and self.ymin <= 0 <= self.ymax:
                    t.append(f'<text x="{self.X(v):.1f}" y="{self.Y(0)+14:.1f}" text-anchor="middle">{v:g}</text>')
                k += 1
            k = math.ceil(self.ymin / self.grid)
            while k * self.grid <= self.ymax:
                v = k * self.grid
                if abs(v) > 1e-9 and self.xmin <= 0 <= self.xmax:
                    t.append(f'<text x="{self.X(0)-5:.1f}" y="{self.Y(v)+4:.1f}" text-anchor="end">{v:g}</text>')
                k += 1
            out.append('<g font-size="10" font-family="sans-serif" fill="#666">' + ''.join(t) + '</g>')
        if self.ymin <= 0 <= self.ymax:
            out.append(f'<text x="{p+self.W+4}" y="{self.Y(0)-6:.1f}" font-size="13" font-family="sans-serif" font-style="italic" fill="#333">{self.xlabel}</text>')
        if self.xmin <= 0 <= self.xmax:
            out.append(f'<text x="{self.X(0)+6:.1f}" y="{p-4}" font-size="13" font-family="sans-serif" font-style="italic" fill="#333">{self.ylabel}</text>')
        out += self.items + self.items_fg
        out.append('</svg>')
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(out))
