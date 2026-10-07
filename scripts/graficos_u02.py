"""Gráficos SVG de la Unidad 2. Uso: python3 scripts/graficos_u02.py"""
import os, sys
from math import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgplot import Plot, COLORS

D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 'Unidad 02 - Funciones de Varias Variables y Topologia', 'img')

# Ej 03 a) disco ∩ semiplano
p = Plot(-2.5, 2.5, -2.5, 2.5, width=300)
p.region(lambda x, y: x*x + y*y <= 4 and x + y >= 1)
p.implicit(lambda x, y: x*x + y*y - 4, color='#999', dash=True, width=1.2)
p.fx(lambda x: 1 - x, color='#999', dash=True, width=1.2)
p.save(f'{D}/tp02-ej03a.svg')

# Ej 03 b) media elipse
p = Plot(-1, 1, -0.8, 0.8, width=300, grid=0.5)
p.region(lambda x, y: 4*x*x + 7*y*y <= 2 and x >= 0)
p.implicit(lambda x, y: 4*x*x + 7*y*y - 2, color='#999', dash=True, width=1.2)
p.save(f'{D}/tp02-ej03b.svg')

# Ej 03 c) x^2 - y^2 <= 3, x + y >= 2
p = Plot(-4, 6, -4, 6, width=300)
p.region(lambda x, y: x*x - y*y <= 3 and x + y >= 2)
p.implicit(lambda x, y: x*x - y*y - 3, color='#999', dash=True, width=1.2)
p.fx(lambda x: 2 - x, color='#999', dash=True, width=1.2)
p.save(f'{D}/tp02-ej03c.svg')

# Ej 04) xy <= 4
p = Plot(-6, 6, -6, 6, width=300, grid=2)
p.region(lambda x, y: x*y <= 4)
p.implicit(lambda x, y: x*y - 4, color=COLORS[0])
p.point(4, 1, label='(4,1)')
p.point(1, 4, label='(1,4)')
p.point(2.5, 2.5, filled=False, label='(2.5,2.5)', color=COLORS[1])
p.segment(4, 1, 1, 4, color=COLORS[1], dash=True)
p.save(f'{D}/tp02-ej04.svg')

# Ej 05 dominios
p = Plot(-4, 3, -5, 5, width=280)
p.region(lambda x, y: (x + 1)*(y - 2*x) > 0)
p.fx(lambda x: 2*x, dash=True, color=COLORS[1])
p.curve(lambda t: (-1, t), -5, 5, dash=True, color=COLORS[1])
p.save(f'{D}/tp02-ej05a.svg')

p = Plot(-2, 2, -2, 3, width=240)
p.region(lambda x, y: -1 < x <= 1 and y > x)
p.fx(lambda x: x, -1, 1, dash=True, color=COLORS[1])
p.curve(lambda t: (1, t), 1, 3, color=COLORS[1])
p.curve(lambda t: (-1, t), -1, 3, dash=True, color=COLORS[1])
p.save(f'{D}/tp02-ej05b.svg')

p = Plot(-2.5, 2.5, -6, 2, width=260)
p.region(lambda x, y: -1 <= y + x*x <= 1)
p.fx(lambda x: 1 - x*x, color=COLORS[1])
p.fx(lambda x: -1 - x*x, color=COLORS[1])
p.save(f'{D}/tp02-ej05c.svg')

p = Plot(-1, 4, -1, 4, width=260)
p.region(lambda x, y: x*y > 0 and x + y < 2)
p.fx(lambda x: 2 - x, dash=True, color=COLORS[1])
p.save(f'{D}/tp02-ej05e.svg')

p = Plot(-3, 3, -1, 3, width=280)
p.region(lambda x, y: y >= 0 and x != 0 and abs(x + y) > 0.03 and abs(x) > 0.03)
p.fx(lambda x: -x, -3, 1, dash=True, color=COLORS[1])
p.curve(lambda t: (0, t), 0, 3, dash=True, color=COLORS[1])
p.save(f'{D}/tp02-ej05f.svg')

p = Plot(-0.5, 2.5, -1.2, 1.2, width=300, grid=0.5)
p.region(lambda x, y: x <= x*x + y*y < 2*x)
p.implicit(lambda x, y: x*x + y*y - 2*x, dash=True, color=COLORS[1])
p.implicit(lambda x, y: x*x + y*y - x, color=COLORS[1])
p.point(0, 0, filled=False)
p.save(f'{D}/tp02-ej05h.svg')

p = Plot(-3, 3, -3, 3, width=280)
p.region(lambda x, y: (y >= -2*x and y >= 0) or (y <= -2*x and y <= 0))
p.fx(lambda x: -2*x, -1.5, 1.5, color=COLORS[1])
p.point(0, 0, filled=False)
p.save(f'{D}/tp02-ej05j.svg')

# Ej 06 curvas de nivel
p = Plot(-4, 4, -4, 4, width=280)
for k, c in [(-4, 3), (-3, 2), (-2, 0), (0, 1), (2, 4), (6, 5)]:
    if k == -2:
        p.fx(lambda x: 0, color=COLORS[c]); p.curve(lambda t: (0, t), -4, 4, color=COLORS[c])
    else:
        p.implicit(lambda x, y, k=k: x*y - (k + 2), color=COLORS[c])
p.save(f'{D}/tp02-ej06a.svg')

p = Plot(-4, 4, -2, 4, width=280)
for k, c in [(-2, 0), (-1, 1), (0, 2), (1, 3), (2, 4), (3, 5)]:
    p.fx(lambda x, k=k: k - abs(x), color=COLORS[c])
p.save(f'{D}/tp02-ej06d.svg')

p = Plot(-2, 2, -1.6, 1.6, width=300, grid=0.5)
for k, c in [(0.5, 0), (1, 1), (2, 2), (-0.5, 3), (-1, 4), (-2, 5)]:
    p.implicit(lambda x, y, k=k: (x - 1/(2*k))**2 + y*y - 1/(4*k*k), color=COLORS[c])
p.curve(lambda t: (0, t), -1.6, 1.6, color=COLORS[6])
p.point(0, 0, filled=False)
p.save(f'{D}/tp02-ej06f.svg')

# Ej 12) anillo + puntos 1/n
p = Plot(-1.7, 1.7, -1.7, 1.7, width=300, grid=0.5)
p.region(lambda x, y: 1 <= x*x + y*y <= 2)
p.implicit(lambda x, y: x*x + y*y - 1, color=COLORS[0])
p.implicit(lambda x, y: x*x + y*y - 2, color=COLORS[0])
for n in range(1, 13):
    p.point(1/n, 0)
p.point(0, 0, filled=False, color=COLORS[1], label='(0,0) ∉ S', dx=-30, dy=18)
p.save(f'{D}/tp02-ej12.svg')
