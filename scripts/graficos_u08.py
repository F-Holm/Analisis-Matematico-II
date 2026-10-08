"""Gráficos SVG de la Unidad 8. Uso: python3 scripts/graficos_u08.py"""
import os, sys
from math import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgplot import Plot, COLORS

D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 'Unidad 08 - Curvas e Integrales de Linea', 'img')
os.makedirs(D, exist_ok=True)

# Ej 02) sector x^2+y^2 <= 4, y >= x, x >= 0
p = Plot(-0.6, 2.6, -0.6, 2.6, width=260, grid=0.5)
p.region(lambda x, y: x*x + y*y <= 4 and y >= x and x >= 0)
p.segment(0, 0, sqrt(2), sqrt(2), color=COLORS[1], width=3)
p.segment(0, 0, 0, 2, color=COLORS[1], width=3)
p.curve(lambda t: (2*cos(t), 2*sin(t)), pi/4, pi/2, color=COLORS[1], width=3)
p.text(0.9, 0.55, 'y = x', color=COLORS[1])
p.save(f'{D}/tp08-ej02.svg')

# Ej 11) región x^2 <= y <= 1, 0 <= x <= 1, frontera con sentido positivo
p = Plot(-0.3, 1.4, -0.3, 1.4, width=260, grid=0.5)
p.region(lambda x, y: x*x <= y <= 1 and 0 <= x <= 1)
p.fx(lambda x: x*x, 0, 1, color=COLORS[1], width=2.5)
p.segment(1, 1, 0, 1, color=COLORS[1], width=2.5)
p.segment(0, 1, 0, 0, color=COLORS[1], width=2.5)
p.arrow(0.55, 0.3025, 0.62, 0.3844, color=COLORS[1], width=2.5)
p.arrow(0.55, 1, 0.45, 1, color=COLORS[1], width=2.5)
p.arrow(0, 0.55, 0, 0.45, color=COLORS[1], width=2.5)
p.text(0.62, 0.25, 'C₁', color=COLORS[1]); p.text(0.45, 1.08, 'C₂', color=COLORS[1]); p.text(-0.25, 0.75, 'C₃', color=COLORS[1])
p.save(f'{D}/tp08-ej11.svg')
