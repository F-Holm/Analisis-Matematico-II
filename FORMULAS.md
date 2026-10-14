# Resumen de fórmulas — Análisis Matemático II

Todas las fórmulas de las 12 unidades. El detalle y los ejemplos están en el `teoria.md` de cada unidad.

---

## Unidad 1 — Ecuaciones diferenciales (1.ª parte)

| Tipo | Forma | Método |
|---|---|---|
| Variables separables | $f(y)\,y' = g(x)$ | $\int f(y)\,dy = \int g(x)\,dx + C$ |
| Lineal | $y' + P(x)\,y = Q(x)$ | $y = y_H + y_P$, con $y_H = Ce^{-\int P}$ e $y_P = K(x)e^{-\int P}$ |
| Factor integrante | $y' + Py = Q$ | $y = e^{-\int P}\left[\int Qe^{\int P}dx + C\right]$ |
| Homogénea | $y' = g(y/x)$ | $y = zx$, $\ y' = z + xz'$ |
| Bernoulli | $y' + qy = fy^n$ | $z = y^{1-n}$ |
| Reducción de orden | falta $y$ | $w = y'$ |

**Familias de curvas:**

- EDO de una familia: derivar y eliminar los parámetros.
- Familia ortogonal: reemplazar $y' \to -1/y'$.
- Tangente en $(x,y)$: $Y - y = y'(X - x)$. Normal: $Y - y = -\frac{1}{y'}(X - x)$.

---

## Unidad 2 — Funciones de varias variables y topología

- Distancia: $d(\vec x,\vec y) = \sqrt{\sum(x_i - y_i)^2}$. Bola abierta: $B(\vec a, r) = \{d(\vec x,\vec a) < r\}$.
- Conjunto de nivel: $C_k = \{\vec x \in D : f(\vec x) = k\}$.
- Clausura: $\bar A = A\cup A' = A\cup\partial A$. Compacto = cerrado + acotado.
- Dominios: $\sqrt{A} \Rightarrow A \ge 0$; $\ \ln A \Rightarrow A > 0$; $\ 1/A \Rightarrow A \ne 0$; $\ \arcsin A \Rightarrow |A| \le 1$.

---

## Unidad 3 — Límite y continuidad

| Herramienta | Para probar |
|---|---|
| Dos caminos (rectas $y - y_0 = m(x - x_0)$, parábolas, $y = kx^p$) con límites distintos | que **no** existe |
| Iterados distintos | que **no** existe |
| Polares que dependen de $\theta$ | que **no** existe |
| Curva de nivel $k$ que pasa por el punto | que **no** existe |
| Infinitésimo × acotada | que existe (y vale 0) |
| Polares: $\lvert f - L\rvert \le g(r)\,h(\theta)$ con $g \to 0$ y $h$ acotada | que existe |

**Límites notables:**

$$\frac{\operatorname{sen}u}{u} \to 1, \qquad \frac{1 - \cos u}{u^2} \to \frac12, \qquad \frac{e^u - 1}{u} \to 1, \qquad u\ln u \to 0$$

**Continuidad:** $\lim f = f(\vec x_0)$. Weierstrass: continua en un compacto ⇒ alcanza máximo y mínimo.

---

## Unidad 4 — Derivabilidad

- Respecto de un vector: $f'(\vec A,\vec r) = \lim\limits_{h\to0}\dfrac{f(\vec A + h\vec r) - f(\vec A)}{h} = g'(0)$, con $g(t) = f(\vec A + t\vec r)$.
- Homogeneidad: $f'(\vec A,\lambda\vec r) = \lambda f'(\vec A,\vec r)$.
- Recta tangente a una curva: $\vec X = \vec g(t_0) + u\,\vec g'(t_0)$. Plano normal: $\vec g'(t_0)\cdot(\vec X - \vec g(t_0)) = 0$.
- Schwarz: $f''_{xy} = f''_{yx}$ si las derivadas mixtas son continuas.
- Laplaciano: $\Delta f = \sum f''_{x_ix_i}$. Ecuación de onda: $y''_{tt} = a^2y''_{xx}$.

---

## Unidad 5 — Diferenciabilidad

- Definición: $\lim\limits_{\vec h\to0}\dfrac{f(\vec A + \vec h) - f(\vec A) - \nabla f(\vec A)\cdot\vec h}{\lVert\vec h\rVert} = 0$.
- $C^1$ ⇒ diferenciable ⇒ continua y $f'(\vec A,\vec r) = \nabla f\cdot\vec r$.
- Derivada máxima $= \lVert\nabla f\rVert$, en la dirección de $\nabla f$. Nula si $\breve r \perp \nabla f$.
- Plano tangente: $z = z_0 + f'_x(x - x_0) + f'_y(y - y_0)$. Normal $(f'_x, f'_y, -1)$, o $\nabla F$, o $\vec X'_u\times\vec X'_v$.
- Aproximación: $f(\vec A + \vec h) \approx f(\vec A) + \nabla f\cdot\vec h$.
- Errores: $\varepsilon_w = \sum\lvert f'_{x_i}\rvert\,\varepsilon_{x_i}$. Para $w = x^ay^b$: $\varepsilon_{\text{rel}} = \lvert a\rvert\varepsilon_{\text{rel}\,x} + \lvert b\rvert\varepsilon_{\text{rel}\,y}$.

---

## Unidad 6 — Compuestas e implícitas

- Regla de la cadena: $D(\vec f\circ\vec g)(\vec A) = D\vec f(\vec g(\vec A))\cdot D\vec g(\vec A)$.
- Por variables: $z'_x = f'_u u'_x + f'_v v'_x$.
- Sobre una curva: $\frac{d}{dt}f(\vec X(t)) = \nabla f\cdot\vec X'$.
- Implícita (Cauchy-Dini), con $F \in C^1$, $F(\vec A) = 0$ y $F'_z(\vec A) \ne 0$:

$$z'_x = -\frac{F'_x}{F'_z}, \qquad z'_y = -\frac{F'_y}{F'_z}$$

- Tangente a $F = 0\ \cap\ G = 0$: $\vec d = \nabla F\times\nabla G$.

---

## Unidad 7 — Taylor y extremos

$$P_2 = f + f'_xh + f'_yk + \tfrac12\left(f''_{xx}h^2 + 2f''_{xy}hk + f''_{yy}k^2\right)$$

- Puntos críticos: $\nabla f = \vec 0$ (o $f$ no diferenciable).
- Hessiano: $H = f''_{xx}f''_{yy} - (f''_{xy})^2$.
  - $H > 0$ y $f''_{xx} > 0$ ⇒ mínimo; $H > 0$ y $f''_{xx} < 0$ ⇒ máximo.
  - $H < 0$ ⇒ punto silla. $H = 0$ ⇒ no decide.
- Lagrange: $\nabla f = \lambda\nabla g$, $g = 0$.
- Extremos absolutos en un compacto: interior + frontera, y comparar valores.
- Implícita en un punto estacionario: $f''_{ij} = -F''_{ij}/F'_z$.

---

## Unidad 8 — Curvas e integrales de línea

| Concepto | Fórmula |
|---|---|
| Longitud | $\int_a^b\lVert\vec g'(t)\rVert\,dt$ |
| Campo escalar | $\int_C f\,ds = \int f(\vec g)\lVert\vec g'\rVert\,dt$ |
| Campo vectorial | $\int_C\vec f\cdot d\vec s = \int\vec f(\vec g)\cdot\vec g'\,dt$ |
| Campo conservativo | $\int_C\nabla\phi\cdot d\vec s = \phi(B) - \phi(A)$ |
| Condición necesaria | $D\vec f$ simétrica ($P'_y = Q'_x$, …) |
| Curvatura | $cf = \lVert\vec g'\times\vec g''\rVert/\lVert\vec g'\rVert^3$ |
| Torsión | $ct = -\dfrac{(\vec g'\times\vec g'')\cdot\vec g'''}{\lVert\vec g'\times\vec g''\rVert^2}$ |
| Triedro | $T = \frac{\vec g'}{\lVert\vec g'\rVert}$, $\ B = \frac{\vec g'\times\vec g''}{\lVert\vec g'\times\vec g''\rVert}$, $\ N = B\times T$ |

Masa $\int\delta\,ds$, centro de masa $\frac1M\int x\,\delta\,ds$, momento de inercia $\int d^2\,\delta\,ds$.

---

## Unidad 9 — Integrales múltiples

| Coordenadas | Cambio | Elemento |
|---|---|---|
| Polares | $x = \rho\cos\varphi$, $y = \rho\operatorname{sen}\varphi$ | $dA = \rho\,d\rho\,d\varphi$ |
| Polares elípticas | $x = a\rho\cos\varphi$, $y = b\rho\operatorname{sen}\varphi$ | $dA = ab\,\rho\,d\rho\,d\varphi$ |
| Cilíndricas | $(\rho\cos\varphi, \rho\operatorname{sen}\varphi, z)$ | $dV = \rho\,d\rho\,d\varphi\,dz$ |
| Esféricas | $(r\operatorname{sen}\theta\cos\varphi,\ r\operatorname{sen}\theta\operatorname{sen}\varphi,\ r\cos\theta)$ | $dV = r^2\operatorname{sen}\theta\,dr\,d\theta\,d\varphi$ |
| General | $T(u,v)$ | $dx\,dy = \lvert\partial(x,y)/\partial(u,v)\rvert\,du\,dv$ |

- Volumen: $\iint_D(z_{\text{techo}} - z_{\text{piso}})\,dA$.
- Integral de Gauss: $\int_{-\infty}^{\infty}e^{-u^2}du = \sqrt\pi$.

---

## Unidad 10 — Integrales de superficie

- Normal: $\vec N = \vec X'_u\wedge\vec X'_v$; para un gráfico $z = f$: $(-f'_x, -f'_y, 1)$.
- Elemento de área: $d\sigma = \lVert\vec N\rVert\,du\,dv$. Área $= \iint\lVert\vec N\rVert$.
- Campo escalar: $\iint f\,d\sigma = \iint f\,\lVert\vec N\rVert\,du\,dv$.
- Flujo: $\iint\vec f\cdot\breve n\,d\sigma = \pm\iint\vec f\cdot\vec N\,du\,dv$ (signo según la orientación).
- Superficie implícita: $d\sigma = \frac{\lVert\nabla G\rVert}{\lvert G'_z\rvert}dx\,dy$.
- Esfera de radio $R$: $d\sigma = R^2\operatorname{sen}\theta\,d\theta\,d\varphi$, $\ \breve n = \vec X/R$.

---

## Unidad 11 — Teoremas integrales

| Operador / Teorema | Fórmula |
|---|---|
| Divergencia | $P'_x + Q'_y + R'_z$ |
| Rotor | $(R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y)$ |
| Green | $\oint_{\partial D^+}P\,dx + Q\,dy = \iint_D(Q'_x - P'_y)\,dA$ |
| Área | $\oint x\,dy = -\oint y\,dx = \frac12\oint(x\,dy - y\,dx)$ |
| Gauss | $\oint\!\!\oint_{\partial H}\vec f\cdot\breve n\,d\sigma = \iiint_H\operatorname{div}\vec f\,dV$ |
| Stokes | $\oint_{\partial S}\vec f\cdot d\vec s = \iint_S\operatorname{rot}\vec f\cdot\breve n\,d\sigma$ |
| Identidades | $\operatorname{rot}\nabla\phi = \vec 0$, $\ \operatorname{div}\operatorname{rot}\vec g = 0$ |
| Ley de Gauss | flujo de $kq\vec r/r^3 = 4\pi kq$ si la superficie rodea al origen |

**¿Admite potencial?**

1. ¿$D\vec f$ es simétrica? Si no, no admite.
2. ¿El dominio es simplemente conexo? Si sí, admite.
3. Si tiene agujeros: admite sólo si la circulación alrededor de cada uno es 0.

---

## Unidad 12 — Ecuaciones diferenciales (2.ª parte)

- **Exacta** $M\,dx + N\,dy = 0$: si $M'_y = N'_x$, la solución es $U = C$ con $\nabla U = (M,N)$.
- **Factor integrante:** $\mu(x) = e^{\int(M'_y - N'_x)/N\,dx}$ o $\mu(y) = e^{\int(N'_x - M'_y)/M\,dy}$.
- **Líneas de campo:** $\dfrac{dx}{P} = \dfrac{dy}{Q} = \dfrac{dz}{R}$.
- **Coeficientes constantes:** ecuación característica.
  - Raíces reales $r$: $e^{rx}$. Raíces repetidas: se multiplica por $x$.
  - Raíces complejas $\alpha\pm\beta i$: $e^{\alpha x}(C_1\cos\beta x + C_2\operatorname{sen}\beta x)$.
- **Coeficientes indeterminados:** se propone una $y_P$ de la forma de $f$; si coincide con una solución de la homogénea, se multiplica por $x^m$.
- **Variación de parámetros:** $C_1' = -y_2f/W$, $\ C_2' = y_1f/W$, con $W = y_1y_2' - y_2y_1'$.
- **Sistemas:** $\vec X' = A\vec X$ ⇒ $\vec X = \sum C_ie^{\lambda_it}\vec v_i$ (autovalores y autovectores).

---

[← Volver al menú principal](README.md)
