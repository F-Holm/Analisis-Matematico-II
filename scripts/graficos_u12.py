"""Gráficos SVG de la Unidad 12. Uso: python3 scripts/graficos_u12.py"""
import os, sys
from math import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgplot import Plot, COLORS

D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 'Unidad 12 - Ecuaciones Diferenciales II', 'img')
os.makedirs(D, exist_ok=True)

# Ej 10 a1) x(t) en mm, oscilación amortiguada
p = Plot(0, 3, 0, 70, width=320, height=200, grid=10, xlabel='t [s]', ylabel='x [mm]')
p.fx(lambda t: 50 - 50*exp(-2*t)*cos(5*t) - 20*exp(-2*t)*sin(5*t), 0, 3)
p.fx(lambda t: 50, 0, 3, color='#999', dash=True, width=1.2)
p.save(f'{D}/tp12-ej10a1.svg')

# Ej 10 a2) x(t) en mm, sin oscilaciones
p = Plot(0, 3, 0, 70, width=320, height=200, grid=10, xlabel='t [s]', ylabel='x [mm]')
p.fx(lambda t: 50 + 22.5*exp(-29*t/3) - 72.5*exp(-3*t), 0, 3)
p.fx(lambda t: 50, 0, 3, color='#999', dash=True, width=1.2)
p.save(f'{D}/tp12-ej10a2.svg')

# Ej 13: líneas de campo
def campo(p, f, xs, ys, L=0.35):
    for x in xs:
        for y in ys:
            u, v = f(x, y)
            n = hypot(u, v)
            if n > 1e-9:
                p.arrow(x, y, x + L*u/n, y + L*v/n, color='#888', width=1)

g = 0.5
p = Plot(-3, 3, -3, 3, width=280)
for K, c in [(-8, 0), (-1, 1), (1, 2), (8, 3)]:
    p.implicit(lambda x, y, K=K: (x - y)*(x + 2*y)**2 - K, color=COLORS[c])
p.fx(lambda x: x, color=COLORS[5]); p.fx(lambda x: -x/2, color=COLORS[5])
campo(p, lambda x, y: (2*y - x, x), [i*1.0 for i in range(-3, 4)], [i*1.0 for i in range(-3, 4)])
p.save(f'{D}/tp12-ej13a.svg')

p = Plot(-3, 3, -3, 3, width=280)
for K, c in [(-4, 0), (-1, 1), (1, 2), (4, 3)]:
    p.implicit(lambda x, y, K=K: y*y - x*x - K, color=COLORS[c])
p.fx(lambda x: x, color=COLORS[5]); p.fx(lambda x: -x, color=COLORS[5])
campo(p, lambda x, y: (y, x), [i*1.0 for i in range(-3, 4)], [i*1.0 for i in range(-3, 4)])
p.save(f'{D}/tp12-ej13b.svg')

p = Plot(-3, 3, -3, 3, width=280)
for K, c in [(-1, 0), (-0.3, 1), (0.3, 2), (1, 3)]:
    p.fx(lambda x, K=K: K*x*x, color=COLORS[c])
p.curve(lambda t: (0, t), -3, 3, color=COLORS[5])
campo(p, lambda x, y: (x/2, y), [i*1.0 for i in range(-3, 4)], [i*1.0 for i in range(-3, 4)])
p.save(f'{D}/tp12-ej13c.svg')
