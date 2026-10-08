"""Gráficos SVG de la Unidad 9. Uso: python3 scripts/graficos_u09.py"""
import os, sys
from math import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgplot import Plot, COLORS

D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 'Unidad 09 - Integrales Multiples', 'img')
os.makedirs(D, exist_ok=True)
R = COLORS[1]

# 01 a) y >= 2x^2+1, x+y <= 4
p = Plot(-2.5, 2, -0.5, 6, width=260)
p.region(lambda x, y: y >= 2*x*x + 1 and x + y <= 4)
p.fx(lambda x: 2*x*x + 1, color=R); p.fx(lambda x: 4 - x, color=R)
p.point(-1.5, 5.5, label='(−3/2, 11/2)'); p.point(1, 3, label='(1,3)')
p.save(f'{D}/tp09-ej01a.svg')

# 01 b) x^2 <= y < sqrt(2-x^2)
p = Plot(-1.8, 1.8, -0.4, 1.8, width=280, grid=0.5)
p.region(lambda x, y: x*x <= y < sqrt(max(0, 2 - x*x)) and x*x < 2)
p.fx(lambda x: x*x, -1.4, 1.4, color=R)
p.curve(lambda t: (sqrt(2)*cos(t), sqrt(2)*sin(t)), 0, pi, color=R, dash=True)
p.point(-1, 1, label='(−1,1)', dx=-45); p.point(1, 1, label='(1,1)')
p.save(f'{D}/tp09-ej01b.svg')

# 01 c) dominio del campo
p = Plot(-1, 3.5, -2.5, 3.5, width=280)
p.region(lambda x, y: x + y > 2 and y >= 2*x - 2 and y < 2*x + 2 - x*x)
p.fx(lambda x: 2 - x, color=R, dash=True); p.fx(lambda x: 2*x - 2, color=R)
p.fx(lambda x: 2*x + 2 - x*x, color=R, dash=True)
p.point(4/3, 2/3, label='(4/3, 2/3)'); p.point(0, 2, filled=False); p.point(2, 2, filled=False)
p.save(f'{D}/tp09-ej01c.svg')

# 01 d) y = x^3, y = x
p = Plot(-1.5, 1.5, -1.5, 1.5, width=260, grid=0.5)
p.region(lambda x, y: (x >= 0 and x**3 <= y <= x) or (x < 0 and x <= y <= x**3))
p.fx(lambda x: x**3, color=R); p.fx(lambda x: x, color=R)
p.save(f'{D}/tp09-ej01d.svg')

# 01 e) y > 2|x|, x^2+y^2 < 20
p = Plot(-5, 5, -1, 5, width=300)
p.region(lambda x, y: y > 2*abs(x) and x*x + y*y < 20)
p.fx(lambda x: 2*abs(x), -2.5, 2.5, color=R, dash=True)
p.curve(lambda t: (sqrt(20)*cos(t), sqrt(20)*sin(t)), 0, pi, color=R, dash=True)
p.point(2, 4, label='(2,4)'); p.point(-2, 4, label='(−2,4)', dx=-45)
p.save(f'{D}/tp09-ej01e.svg')

# 01 f) x^2+y^2 < 4, x < 2 - y^2
p = Plot(-2.5, 2.5, -2.5, 2.5, width=280)
p.region(lambda x, y: x*x + y*y < 4 and x < 2 - y*y)
p.implicit(lambda x, y: x*x + y*y - 4, color=R, dash=True)
p.curve(lambda t: (2 - t*t, t), -2.3, 2.3, color=R, dash=True)
p.point(-1, sqrt(3), label='(−1, √3)', dx=-60); p.point(-1, -sqrt(3), label='(−1, −√3)', dx=-65, dy=16)
p.save(f'{D}/tp09-ej01f.svg')

# 02 a) 0 <= y <= sen x
p = Plot(-0.3, 3.5, -0.4, 1.4, width=300, grid=0.5)
p.region(lambda x, y: 0 <= x <= pi and 0 <= y <= sin(x))
p.fx(sin, 0, pi, color=R)
p.save(f'{D}/tp09-ej02a.svg')

# 02 d) x^2-1 <= y <= 1-x^2
p = Plot(-1.5, 1.5, -1.5, 1.5, width=260, grid=0.5)
p.region(lambda x, y: x*x - 1 <= y <= 1 - x*x)
p.fx(lambda x: 1 - x*x, -1.2, 1.2, color=R); p.fx(lambda x: x*x - 1, -1.2, 1.2, color=R)
p.save(f'{D}/tp09-ej02d.svg')

# 02 e) región de la suma de integrales
p = Plot(-0.5, 4.5, -0.5, 1.5, width=320, grid=0.5)
p.region(lambda x, y: 0 <= y <= 1 and y <= x <= 4)
p.segment(0, 0, 1, 1, color=R); p.segment(1, 1, 4, 1, color=R); p.segment(4, 1, 4, 0, color=R)
p.curve(lambda t: (1, t), 0, 1, color='#999', dash=True, width=1.2)
p.save(f'{D}/tp09-ej02e.svg')

# 02 f) e^x <= y <= e^{2x}, 0 <= x <= ln 2
p = Plot(-0.2, 1, -0.3, 4.5, width=220, grid=0.5)
p.region(lambda x, y: 0 <= x <= log(2) and exp(x) <= y <= exp(2*x))
p.fx(exp, 0, log(2), color=R); p.fx(lambda x: exp(2*x), 0, log(2), color=R)
p.curve(lambda t: (log(2), t), 2, 4, color=R)
p.curve(lambda t: (t, 2), 0, log(2), color='#999', dash=True, width=1.2)
p.save(f'{D}/tp09-ej02f.svg')

# 05 c) región entre y = x^2 - 4 e y = x + 2
p = Plot(-3, 4, -4.5, 6, width=260)
p.region(lambda x, y: x*x - 4 <= y <= x + 2)
p.fx(lambda x: x*x - 4, color=R); p.fx(lambda x: x + 2, color=R)
p.point(-2, 0, label='(−2,0)', dx=-45); p.point(3, 5, label='(3,5)')
p.save(f'{D}/tp09-ej05c.svg')

# 06 a) |x+y| <= 2, y <= x+2 <= 4
p = Plot(-4, 3, -5, 4, width=260)
p.region(lambda x, y: abs(x + y) <= 2 and y <= x + 2 and x + 2 <= 4)
p.fx(lambda x: 2 - x, color=R); p.fx(lambda x: -2 - x, color=R); p.fx(lambda x: x + 2, color=R)
p.curve(lambda t: (2, t), -5, 5, color=R)
p.save(f'{D}/tp09-ej06a.svg')

# 06 c) |x|+|y| <= 4
p = Plot(-5, 5, -5, 5, width=260)
p.region(lambda x, y: abs(x) + abs(y) <= 4)
p.save(f'{D}/tp09-ej06c.svg')

# 06 d) y >= |x|, x + 2y <= 3
p = Plot(-3.5, 1.5, -0.5, 2.5, width=280, grid=0.5)
p.region(lambda x, y: y >= abs(x) and x + 2*y <= 3)
p.fx(abs, color=R); p.fx(lambda x: (3 - x)/2, color=R)
p.point(1, 1, label='(1,1)'); p.point(-3, 3, label='(−3,3)')
p.save(f'{D}/tp09-ej06d.svg')

# 07 b) x^2 + 2y^2 <= 4, x >= sqrt2 |y|
p = Plot(-2.5, 2.5, -1.8, 1.8, width=300, grid=0.5)
p.region(lambda x, y: x*x + 2*y*y <= 4 and x >= sqrt(2)*abs(y))
p.implicit(lambda x, y: x*x + 2*y*y - 4, color='#999', dash=True, width=1.2)
p.fx(lambda x: x/sqrt(2), 0, 2.5, color=R); p.fx(lambda x: -x/sqrt(2), 0, 2.5, color=R)
p.save(f'{D}/tp09-ej07b.svg')

# 09) x >= y, x + 4y <= 4, y >= 0
p = Plot(-0.5, 4.5, -0.5, 1.5, width=320, grid=0.5)
p.region(lambda x, y: x >= y >= 0 and x + 4*y <= 4)
p.fx(lambda x: x, 0, 1.2, color=R); p.fx(lambda x: (4 - x)/4, color=R)
p.point(0.8, 0.8, label='(4/5, 4/5)')
p.save(f'{D}/tp09-ej09.svg')

# 10 a) rho <= 2cos(phi), 0 <= phi <= pi/2
p = Plot(-0.5, 2.5, -1.2, 1.5, width=280, grid=0.5)
p.region(lambda x, y: (x - 1)**2 + y*y <= 1 and y >= 0)
p.implicit(lambda x, y: (x - 1)**2 + y*y - 1, color='#999', dash=True, width=1.2)
p.save(f'{D}/tp09-ej10a.svg')

# 10 b) -pi/6 <= phi <= pi/3, x <= sqrt3
p = Plot(-0.5, 2.5, -1.5, 3.5, width=240, grid=0.5)
p.region(lambda x, y: 0 <= x <= sqrt(3) and -x/sqrt(3) <= y <= sqrt(3)*x)
p.fx(lambda x: sqrt(3)*x, 0, sqrt(3), color=R); p.fx(lambda x: -x/sqrt(3), 0, sqrt(3), color=R)
p.curve(lambda t: (sqrt(3), t), -1, 3, color=R)
p.save(f'{D}/tp09-ej10b.svg')

# 12 a) proyección: y >= x^2/2, x + y <= 4, x >= 0
p = Plot(-0.5, 4.5, -0.5, 4.5, width=260)
p.region(lambda x, y: x >= 0 and x*x/2 <= y <= 4 - x)
p.fx(lambda x: x*x/2, 0, 3, color=R); p.fx(lambda x: 4 - x, color=R)
p.point(2, 2, label='(2,2)')
p.save(f'{D}/tp09-ej12a.svg')

# 13) proyección: y entre x y 2x, x + y <= 6
p = Plot(-0.5, 4, -0.5, 6, width=240)
p.region(lambda x, y: x <= y <= 2*x and x + y <= 6)
p.fx(lambda x: x, 0, 4, color=R); p.fx(lambda x: 2*x, 0, 3, color=R); p.fx(lambda x: 6 - x, color=R)
p.point(2, 4, label='(2,4)'); p.point(3, 3, label='(3,3)')
p.save(f'{D}/tp09-ej13.svg')
