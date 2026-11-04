# 1.er Parcial — Tema 1 (15/10/2019)

Análisis Matemático II — UTN-FRBA. Segundo cuatrimestre de 2019.

Enunciado y resolución de la cátedra: [Parcial1-2019-10-15-Resuelto.pdf](../aula-virtual/Parciales/Primer-Parcial/Parcial1-2019-10-15-Resuelto.pdf).

> Para aprobar los TP, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Derivada direccional máxima

Sea $f: \mathbb{R}^2 \to \mathbb{R}$. Demuestre que si $f$ es diferenciable en $(x_0,y_0)$ y $\nabla f(x_0,y_0) \ne (0,0)$, entonces existe la derivada direccional máxima y esta vale $\Vert\nabla f(x_0,y_0)\Vert$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Fórmula de la derivada.** Como $f$ es diferenciable, para todo versor $\breve r$:

$$f'(\vec A, \breve r) = \nabla f(\vec A)\cdot\breve r = \lVert\nabla f(\vec A)\rVert\thinspace\lVert\breve r\rVert\cos\theta = \lVert\nabla f(\vec A)\rVert\cos\theta$$

donde $\theta$ es el ángulo entre $\nabla f(\vec A)$ y $\breve r$.

**Paso 2 — Cota.** Como $\cos\theta \le 1$, resulta $f'(\vec A, \breve r) \le \lVert\nabla f(\vec A)\rVert$ para todo $\breve r$.

**Paso 3 — Se alcanza.** Como $\nabla f(\vec A) \ne \vec 0$, se puede tomar $\breve r_0 = \dfrac{\nabla f(\vec A)}{\lVert\nabla f(\vec A)\rVert}$ ($\theta = 0$):

$$f'(\vec A, \breve r_0) = \frac{\nabla f\cdot\nabla f}{\lVert\nabla f\rVert} = \lVert\nabla f(\vec A)\rVert$$

Entonces el máximo existe, se alcanza en la dirección del gradiente y vale $\lVert\nabla f(x_0,y_0)\rVert$. $\blacksquare$

</details>

**Respuesta:** $f'(\vec A,\breve r) = \lVert\nabla f\rVert\cos\theta \le \lVert\nabla f\rVert$, con igualdad para $\breve r = \nabla f/\lVert\nabla f\rVert$.

</details>

---

### T2) Solución general y particular

Defina solución general y solución particular de una ecuación diferencial de primer orden.

Halle $f$ sabiendo que $y_p = \dfrac{x^4 + 2x^2}{2}$ es una solución de la ecuación $y' - \dfrac2x\thinspace y = f(x)$ y encuentre, con la función hallada, la solución general de la ecuación.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Definiciones:**

- **S.G.:** familia de soluciones que depende de **una** constante arbitraria esencial (igual al orden).
- **S.P.:** una solución que se obtiene de la S.G. dándole un valor a la constante, por ejemplo con una condición inicial.

**Paso 1 — Hallar $f$.** Reemplazamos $y_p$ (con $y_p' = 2x^3 + 2x$):

$$f(x) = 2x^3 + 2x - \frac2x\cdot\frac{x^4 + 2x^2}{2} = 2x^3 + 2x - x^3 - 2x = x^3$$

**Paso 2 — Homogénea.** $y' = \dfrac2x\thinspace y \Rightarrow \dfrac{dy}{y} = \dfrac{2\thinspace dx}{x} \Rightarrow y_H = kx^2$.

**Paso 3 — S.G.** (lineal: $y = y_H + y_P$):

$$y = kx^2 + \frac{x^4 + 2x^2}{2}$$

Como el término $x^2$ se puede absorber en $k$, también se escribe $y = Cx^2 + \dfrac{x^4}{2}$.

</details>

**Respuesta:** $f(x) = x^3$; S.G.: $y = kx^2 + \dfrac{x^4 + 2x^2}{2}$, $k \in \mathbb{R}$.

</details>

---

## Ejercicios prácticos

### E1) Continuidad y derivadas direccionales

Sea $f(x,y) = \begin{cases} \dfrac{x\mathop{\mathrm{sen}}(y)}{y}, & \text{si } y \ne 0, \cr 0, & \text{si } y = 0. \end{cases}$

Analice la continuidad y la existencia de derivadas en distintas direcciones de $f$ en $(0,0)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Continuidad.**

- Para $y \ne 0$: $f = \underbrace{x}_{\to0}\cdot\underbrace{\dfrac{\mathop{\mathrm{sen}}y}{y}}_{\to1} \to 0$.
- Sobre $y = 0$: $f = 0$.

El límite es $0 = f(0,0)$ ⇒ **continua**.

**Derivadas direccionales.** Con $\breve r = (a,b)$, $a^2 + b^2 = 1$:

- **Si $b \ne 0$:**

$$\lim_{t\to0}\frac{f(at, bt) - 0}{t} = \lim_{t\to0}\frac{1}{t}\cdot\frac{at\mathop{\mathrm{sen}}(bt)}{bt} = \lim_{t\to0}a\thinspace\frac{\mathop{\mathrm{sen}}(bt)}{bt} = a$$

- **Si $b = 0$** (es decir $\breve r = (\pm1, 0)$): $f(at, 0) = 0$ ⇒ la derivada es $0$.

Existe en **todas** las direcciones:

$$f'(\vec 0, (a,b)) = \begin{cases} a & b \ne 0 \cr 0 & b = 0 \end{cases}$$

> **Observación:** la resolución manuscrita de la cátedra da "$= a$" para todas las direcciones, pero con $b = 0$ la función vale 0 sobre el eje $x$, así que ahí la derivada es 0. Esto muestra además que $f$ **no es diferenciable** en el origen: $\nabla f(\vec 0) = (0,0)$ y, sin embargo, $f'(\vec 0,(a,b)) = a \ne 0$ para $b \ne 0$, $a \ne 0$.

</details>

**Respuesta:** $f$ es continua en $(0,0)$ y derivable en toda dirección: $f'(\vec 0,(a,b)) = a$ si $b \ne 0$ y $0$ si $b = 0$.

</details>

---

### E2) Aproximación lineal con un plano tangente dado

Sea $f: \mathbb{R}^2 \to \mathbb{R}$ una función diferenciable tal que el plano tangente al gráfico de $f$ en $(4, 2, f(4,2))$ es el plano normal a la curva $C$ definida por

$$C: \begin{cases} z = x^2 - 3y^2 \cr x = 2y \end{cases}$$

Calcule mediante una aproximación lineal conveniente $f(3.94;\ 2.04)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrizar $C$.** Con $y = t$: $x = 2t$ y $z = 4t^2 - 3t^2 = t^2$ ⇒ $\vec\alpha(t) = (2t, t, t^2)$.

**Paso 2 — Punto.** $(x, y) = (4, 2) \Rightarrow t = 2$, y entonces $z = 4$. Por lo tanto $f(4,2) = 4$.

**Paso 3 — Plano normal.** $\vec\alpha'(t) = (2, 1, 2t)$, así que $\vec\alpha'(2) = (2, 1, 4)$:

$$2(x - 4) + (y - 2) + 4(z - 4) = 0 \ \Rightarrow\ 2x + y + 4z = 26$$

**Paso 4 — Linealización.** Este plano es el tangente a la gráfica de $f$:

$$z = L(x,y) = \frac{26 - 2x - y}{4}$$

**Paso 5 — Calcular.**

$$f(3{,}94;\ 2{,}04) \approx \frac{26 - 7{,}88 - 2{,}04}{4} = \frac{16{,}08}{4} = 4{,}02$$

</details>

**Respuesta:** $f(3.94;\ 2.04) \approx \dfrac{26 - 2(3.94) - 2.04}{4} = 4.02$.

</details>

---

### E3) Composición con una implícita

Sean $z = f(x,y)$ la función definida implícitamente por la ecuación $xy + z + \ln(xz - 5) = 11$ en un entorno de $(2,4,z_0)$ y $\vec g(u,v) = (u^2 - 2v^2,\ 3u - 2v^2)$. Halle, si existen, la derivada direccional máxima y las direcciones de derivada direccional nula de $h = f\circ\vec g$ en $(2,1)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Punto intermedio.** $\vec g(2,1) = (4 - 2,\ 6 - 2) = (2, 4)$.

**Paso 2 — $z_0$.** $2\cdot4 + z_0 + \ln(2z_0 - 5) = 11$. Con $z_0 = 3$: $8 + 3 + \ln1 = 11$ ✓.

**Paso 3 — Cauchy-Dini.** $F = xy + z + \ln(xz - 5) - 11$ es $C^1$ donde $xz > 5$. En $(2,4,3)$:

- $F'_x = y + \dfrac{z}{xz - 5} = 4 + 3 = 7$.
- $F'_y = x = 2$.
- $F'_z = 1 + \dfrac{x}{xz - 5} = 1 + 2 = 3 \ne 0$.

Entonces:

$$f'_x(2,4) = -\frac73, \qquad f'_y(2,4) = -\frac23$$

**Paso 4 — Jacobiana de $\vec g$ en $(2,1)$.**

$$D\vec g = \begin{pmatrix} 2u & -4v \cr 3 & -4v \end{pmatrix} = \begin{pmatrix} 4 & -4 \cr 3 & -4 \end{pmatrix}$$

**Paso 5 — Regla de la cadena.**

$$\nabla h(2,1) = \left(-\tfrac73,\ -\tfrac23\right)\begin{pmatrix} 4 & -4 \cr 3 & -4 \end{pmatrix} = \left(-\tfrac{28}{3} - 2,\ \tfrac{28}{3} + \tfrac83\right) = \left(-\tfrac{34}{3},\ 12\right)$$

**Paso 6 — Máxima.**

$$\lVert\nabla h\rVert = \sqrt{\frac{1156}{9} + 144} = \frac{\sqrt{2452}}{3} = \frac{2\sqrt{613}}{3} \approx 16{,}51$$

**Paso 7 — Nulas:** son los versores perpendiculares a $\nabla h \parallel (-17, 18)$, es decir $\pm\dfrac{(18, 17)}{\sqrt{613}}$.

> **Observación:** en la resolución manuscrita el producto quedó como $(-34/9,\ 36/9)$, con un factor 3 de más en el denominador. La dirección de derivada nula coincide, porque $(4, 34/9) \parallel (18, 17)$, pero el valor máximo correcto es $\lVert(-34/3,\ 12)\rVert$.

</details>

**Respuesta:** $\nabla h(2,1) = (-34/3,\ 12)$; derivada direccional máxima $= 2\sqrt{613}/3 \approx 16.51$; direcciones de derivada nula: $\breve r = \pm(18, 17)/\sqrt{613}$.

</details>

---

### E4) Familia ortogonal y puntos críticos

- a) Halle el haz de curvas ortogonal a la familia $y^3 - Cx = 0$.
- b) Halle los puntos críticos de $f(x,y) = x^2 + xy^2 - x$ y clasifíquelos.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)**

- Derivando: $3y^2y' = C = \dfrac{y^3}{x}$ ⇒ $y' = \dfrac{y}{3x}$.
- Ortogonal ($y' \to -1/y'$): $y' = -\dfrac{3x}{y}$ ⇒ $y\thinspace dy = -3x\thinspace dx$.
- Integrando: $\dfrac{y^2}{2} = -\dfrac{3x^2}{2} + c$ ⇒ $3x^2 + y^2 = C$, que es una familia de elipses.

**b)** *Puntos críticos:*

$$f'_x = 2x + y^2 - 1 = 0, \qquad f'_y = 2xy = 0$$

- $x = 0$ ⇒ $y^2 = 1$ ⇒ $(0, 1)$ y $(0, -1)$.
- $y = 0$ ⇒ $x = \frac12$ ⇒ $\left(\frac12, 0\right)$.

*Hessiano:* $Hf = \begin{pmatrix} 2 & 2y \cr 2y & 2x \end{pmatrix}$.

- $(0, \pm1)$: $\det = 0 - 4 < 0$ ⇒ **puntos silla**.
- $\left(\frac12, 0\right)$: $\det = 2\cdot1 = 2 > 0$, con $f''_{xx} = 2 > 0$ ⇒ **mínimo local**, $f = \frac14 - \frac12 = -\frac14$.

</details>

**Respuesta:**

- a) $3x^2 + y^2 = C$.
- b) Puntos críticos $(0,1)$, $(0,-1)$, $(1/2, 0)$; $f(0,\pm1)$ no son extremos (puntos silla); $f(1/2, 0) = -1/4$ es mínimo local.

</details>

---

[← Volver al menú principal](../README.md)
