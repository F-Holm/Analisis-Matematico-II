"""Gráficos SVG de la Unidad 3. Uso: python3 scripts/graficos_u03.py"""
import os, sys
from math import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgplot import Plot, COLORS

D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 'Unidad 03 - Limite y Continuidad', 'img')
os.makedirs(D, exist_ok=True)

# Ej 04 b) (u, |u|), u en [-1, 2]
p = Plot(-1.5, 2.5, -0.5, 2.5, width=260)
p.curve(lambda u: (u, abs(u)), -1, 2)
p.point(-1, 1, label='g(-1)'); p.point(2, 2, label='g(2)', dx=-40)
p.save(f'{D}/tp03-ej04b.svg')

# Ej 04 e) (x, x^2), |x| > 1
p = Plot(-2.2, 2.2, -0.5, 4.5, width=260)
p.fx(lambda x: x*x, -2.1, -1, color=COLORS[0])
p.fx(lambda x: x*x, 1, 2.1, color=COLORS[0])
p.fx(lambda x: x*x, -1, 1, color='#bbb', dash=True, width=1.2)
p.point(-1, 1, filled=False); p.point(1, 1, filled=False)
p.save(f'{D}/tp03-ej04e.svg')

# Ej 04 f) con la corrección: (u, u^2+1) si u >= 0 ; (u, u^2) si u < 0
p = Plot(-2, 2, -0.5, 4.5, width=260)
p.fx(lambda x: x*x, -2, -0.001)
p.fx(lambda x: x*x + 1, 0, 1.85)
p.point(0, 1, label='g(0) = (0,1)'); p.point(0, 0, filled=False)
p.save(f'{D}/tp03-ej04f.svg')

# Ej 05 o) curvas de nivel de x^3/(x^2 - y^2) que llegan al origen: y^2 = x^2 - x^3/k
p = Plot(-1, 1, -1, 1, width=300, grid=0.5)
for k, c in [(0.5, 0), (1, 1), (2, 2), (-0.5, 3), (-1, 4)]:
    p.implicit(lambda x, y, k=k: y*y - (x*x - x**3/k), color=COLORS[c])
p.fx(lambda x: x, color='#bbb', dash=True, width=1.2)
p.fx(lambda x: -x, color='#bbb', dash=True, width=1.2)
p.point(0, 0, filled=False)
p.save(f'{D}/tp03-ej05o.svg')

# Ej 06 a) dominio |x| < 1, x != 0
p = Plot(-2, 2, -2, 2, width=280)
p.region(lambda x, y: abs(x) < 1 and abs(x) > 0.02)
for x0 in (-1, 0, 1):
    p.curve(lambda t, x0=x0: (x0, t), -2, 2, color=COLORS[1], dash=True)
p.save(f'{D}/tp03-ej06.svg')

# Ej 10 a) curvas de nivel de x^3/(x^2+y): y = x^3/k - x^2
p = Plot(-1, 1, -1.2, 0.8, width=300, grid=0.5)
for k, c in [(0.5, 0), (1, 1), (2, 2), (-1, 3), (-0.5, 4)]:
    p.fx(lambda x, k=k: x**3/k - x*x, color=COLORS[c])
p.fx(lambda x: -x*x, color='#bbb', dash=True, width=1.2)
p.point(0, 0, filled=False)
p.save(f'{D}/tp03-ej10a.svg')

# Ej 12 a) dominio de continuidad
p = Plot(-3, 3, -3, 3, width=280)
p.region(lambda x, y: y <= 0 and x*x + y*y <= 4, color=COLORS[2])
p.curve(lambda t: (2*cos(t), 2*sin(t)), pi, 2*pi, color=COLORS[2])
p.segment(-2, 0, 2, 0, color=COLORS[1], width=3, dash=True)
p.point(-2, 0); p.point(2, 0)
p.save(f'{D}/tp03-ej12a.svg')

# Ej 13 b) curva de nivel 1 de x^3/(x^2+y^2): y^2 = x^2 (x - 1)
p = Plot(-0.5, 2.5, -2.5, 2.5, width=240, grid=0.5)
p.implicit(lambda x, y: y*y - x*x*(x - 1), color=COLORS[0])
p.point(0, 0, filled=False)
p.save(f'{D}/tp03-ej13b.svg')
