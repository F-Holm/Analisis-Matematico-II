"""Gráficos SVG de la Unidad 7. Uso: python3 scripts/graficos_u07.py"""
import os, sys
from math import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgplot import Plot, COLORS

D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 'Unidad 07 - Taylor y Extremos', 'img')
os.makedirs(D, exist_ok=True)

# Ej 09) región x^2 + y^2 <= 2x y puntos de máximo y mínimo
p = Plot(-0.5, 2.5, -1.3, 1.3, width=300, grid=0.5)
p.region(lambda x, y: x*x + y*y <= 2*x)
p.implicit(lambda x, y: x*x + y*y - 2*x)
p.point(1, 0, label='máx (1,0)', color=COLORS[1])
p.point(0, 0, label='mín (0,0)', color=COLORS[2], dx=-20, dy=18)
p.point(2, 0, label='(2,0)', dx=-10, dy=18)
p.save(f'{D}/tp07-ej09.svg')

# Ej 11) chapa circular con los extremos en la frontera
p = Plot(-2.6, 2.6, -2.6, 2.6, width=300)
p.region(lambda x, y: x*x + y*y <= 4)
p.implicit(lambda x, y: x*x + y*y - 4)
for s in (1, -1):
    p.point(1, s*sqrt(3), color=COLORS[1], label='máx' if s > 0 else None)
    p.point(-4/3, s*2*sqrt(5)/3, color=COLORS[2], label='mín' if s > 0 else None, dx=-30)
p.save(f'{D}/tp07-ej11.svg')

# Ej 18) elipse y punto (1,7)
p = Plot(-2, 4, -2, 8, width=220)
p.implicit(lambda x, y: (x - 1)**2/4 + (y - 2)**2/9 - 1)
p.point(1, 7, label='(1,7)')
p.point(1, 5, color=COLORS[2], label='más cercano (1,5)')
p.point(1, -1, color=COLORS[1], label='más alejado (1,−1)')
p.segment(1, 7, 1, -1, dash=True, color='#999', width=1.2)
p.save(f'{D}/tp07-ej18.svg')

# Ej 20) recta 4x+4y=5, parábola y=-x^2 y el camino más corto
p = Plot(-1.5, 2.5, -2, 2, width=280, grid=0.5)
p.fx(lambda x: 5/4 - x, color=COLORS[0])
p.fx(lambda x: -x*x, color=COLORS[1])
p.segment(0.5, -0.25, 1, 0.25, color=COLORS[2], width=3)
p.point(0.5, -0.25, label='(1/2, −1/4)', dx=-70, dy=14)
p.point(1, 0.25, label='(1, 1/4)')
p.save(f'{D}/tp07-ej20.svg')
