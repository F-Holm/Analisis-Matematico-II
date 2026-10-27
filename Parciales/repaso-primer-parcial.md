# Repaso para el 1.er Parcial

Análisis Matemático II — UTN-FRBA.

Ejercicios de las diapositivas de repaso de la cátedra: [Repaso-Primer-Parcial.pdf](../aula-virtual/Parciales/Primer-Parcial/Repaso-Primer-Parcial.pdf). Algunos están resueltos a mano en las diapositivas; en esos casos las respuestas coinciden con las de abajo.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

> Dos diapositivas resuelven ejercicios de la guía que ya están en este repositorio: el plano tangente horizontal de $z = e^{(x-1)^2+y^2}$ ([TP5 – 06](../Unidad%2005%20-%20Diferenciabilidad/practica.md)) y la superficie $z\thinspace e^{y-2x} - 5 = 0$ ([TP5 – 19](../Unidad%2005%20-%20Diferenciabilidad/practica.md)).

---

### R1) Recta tangente a una curva definida por un sistema

El siguiente sistema de ecuaciones define implícitamente una curva en un entorno del punto $A = (5, 0, 4)$

$$\begin{cases} \ln(x - z) + y + x = 5 \cr e^{yz} + z - x = 0 \end{cases}$$

Halle la intersección de la recta tangente a dicha curva en el punto $A$ con el plano de ecuación $x + z = 10$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Gradientes en $A$** (allí $x - z = 1$ y $e^{yz} = 1$):

- $F_1 = \ln(x - z) + y + x - 5$: $\nabla F_1 = \left(\dfrac{1}{x-z} + 1,\ 1,\ -\dfrac{1}{x-z}\right) = (2,\ 1,\ -1)$.
- $F_2 = e^{yz} + z - x$: $\nabla F_2 = (-1,\ z\thinspace e^{yz},\ y\thinspace e^{yz} + 1) = (-1,\ 4,\ 1)$.

**Paso 2 — Dirección tangente.**

$$\vec d = \nabla F_1\wedge\nabla F_2 = \begin{vmatrix} \breve\imath & \breve\jmath & \breve k \cr 2 & 1 & -1 \cr -1 & 4 & 1 \end{vmatrix} = (5,\ -1,\ 9)$$

**Paso 3 — Recta tangente.** $\vec X = (5 + 5t,\ -t,\ 4 + 9t)$.

**Paso 4 — Intersección con $x + z = 10$.** $9 + 14t = 10 \Rightarrow t = \frac{1}{14}$.

</details>

**Respuesta:** $\left(\dfrac{75}{14},\ -\dfrac{1}{14},\ \dfrac{65}{14}\right)$.

</details>

---

### R2) Plano tangente a partir de la dirección de máximo crecimiento

Sea $f: \mathbb{R}^2 \to \mathbb{R}$ diferenciable, tal que $f(1,2) = 5$. Sabiendo que su derivada direccional en $(1,2)$ es máxima en la dirección del versor $\left(\frac{1}{\sqrt2}, \frac{1}{\sqrt2}\right)$ y que $f'_x(1,2) = 3\sqrt2$:

- a) Halle una ecuación para el plano tangente a la superficie gráfica de $f$ en el punto $(1, 2, f(1,2))$.
- b) Calcule un valor aproximado de $f(1.01,\ 1.98)$ utilizando una aproximación lineal.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Gradiente.** La derivada máxima es en la dirección del gradiente ⇒ $\nabla f(1,2) = \lambda(1, 1)$, con $\lambda > 0$. Como $f'_x = 3\sqrt2$, resulta $\nabla f(1,2) = (3\sqrt2,\ 3\sqrt2)$.

**a)** $z = 5 + 3\sqrt2\thinspace(x - 1) + 3\sqrt2\thinspace(y - 2)$.

**b)**

$$f(1{,}01;\ 1{,}98) \approx 5 + 3\sqrt2\thinspace(0{,}01) + 3\sqrt2\thinspace(-0{,}02) = 5 - 0{,}03\sqrt2 \approx 4{,}9576$$

</details>

**Respuesta:**

- a) $z = 5 + 3\sqrt2\thinspace(x - 1) + 3\sqrt2\thinspace(y - 2)$.
- b) $f(1.01;\ 1.98) \approx 5 - 0.03\sqrt2 \approx 4.958$.

</details>

---

### R3) Valor de $k$ para que sea continua

Determinar el valor de $k \in \mathbb{R}$ para que $f$ sea continua en todo $\mathbb{R}$.

$$f(x,y) = \begin{cases} \dfrac{x^3 - x\thinspace(y + 1)^2}{x^2 + (y + 1)^2} & \text{si } (x,y) \ne (0,-1) \cr k & \text{si } (x,y) = (0,-1) \end{cases}$$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Fuera de $(0,-1)$** $f$ es un cociente de polinomios con denominador no nulo ⇒ continua.

**Paso 2 — Límite en $(0,-1)$.** Con $w = y + 1$:

$$f = \underbrace{x}_{\to0}\cdot\underbrace{\frac{x^2 - w^2}{x^2 + w^2}}_{|\cdot|\le1} \to 0$$

**Paso 3 — Continuidad.** Hace falta $k = \lim f = 0$.

</details>

**Respuesta:** $k = 0$.

</details>

---

### R4) Extremos locales

Sea $f(x,y) = x^2\thinspace e^y + y^3 - 3y$ analice si $f$ produce extremos locales, indique si son máximos o mínimos.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Puntos críticos.**

- $f'_x = 2x\thinspace e^y = 0 \Rightarrow x = 0$.
- $f'_y = x^2e^y + 3y^2 - 3 = 0 \Rightarrow y = \pm1$.

**Paso 2 — Hessiano.** $f''_{xx} = 2e^y$, $f''_{xy} = 2xe^y$ y $f''_{yy} = x^2e^y + 6y$.

- $(0,1)$: $H = 2e\cdot6 - 0 = 12e > 0$, con $f''_{xx} = 2e > 0$ ⇒ **mínimo local**, $f(0,1) = 1 - 3 = -2$.
- $(0,-1)$: $H = \frac2e\cdot(-6) < 0$ ⇒ punto silla.

</details>

**Respuesta:** $f(0,1) = -2$ es mínimo local; en $(0,-1)$ hay un punto silla.

</details>

---

### R5) Direcciones de derivada máxima, mínima y nula de una composición

Sean $f, \vec g$ definidos en $\mathbb{R}^2$ con $f(u,v) = u^2v + v^3$ y $D\vec g(x,y) = \begin{pmatrix} \mathop{\mathrm{sen}}(y - 2) & x\cos(y - 2) \cr 3 & 2y \end{pmatrix}$ la matriz jacobiana de $\vec g$. Sabiendo que $\vec g(1,2) = (3,1)$ y que $h = f\circ\vec g$, **halle** los versores según los cuales la función $h$ tiene derivadas direccionales máxima, mínima y nula en el punto $(1,2)$ y **calcule** los versores de dichas derivadas.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Jacobiana de $\vec g$ en $(1,2)$.** $D\vec g(1,2) = \begin{pmatrix} 0 & 1 \cr 3 & 4 \end{pmatrix}$.

**Paso 2 — Gradiente de $f$ en $\vec g(1,2) = (3,1)$.** $\nabla f = (2uv,\ u^2 + 3v^2) = (6,\ 12)$.

**Paso 3 — Regla de la cadena.**

$$\nabla h(1,2) = (6,\ 12)\begin{pmatrix} 0 & 1 \cr 3 & 4 \end{pmatrix} = (36,\ 54) = 18\thinspace(2,\ 3)$$

**Paso 4 — Direcciones y valores.** $\lVert\nabla h\rVert = 18\sqrt{13}$.

- Máxima: $\breve r = \dfrac{(2,3)}{\sqrt{13}}$, con valor $18\sqrt{13}$.
- Mínima: $\breve r = -\dfrac{(2,3)}{\sqrt{13}}$, con valor $-18\sqrt{13}$.
- Nula: $\breve r = \pm\dfrac{(3,-2)}{\sqrt{13}}$, con valor $0$.

(El enunciado dice "calcule los versores de dichas derivadas"; se interpreta como "calcule los valores de dichas derivadas".)

</details>

**Respuesta:** $\nabla h(1,2) = (36, 54)$. Máxima según $(2,3)/\sqrt{13}$, valor $18\sqrt{13}$; mínima según $-(2,3)/\sqrt{13}$, valor $-18\sqrt{13}$; nula según $\pm(3,-2)/\sqrt{13}$.

</details>

---

### R6) Diferencia entre una función y su plano tangente

Dadas: $\Sigma$ la gráfica de $f$ con $f(x,y) = x^2 + \ln(x) - 2x\cos(x + y - 1)$, $z = p(x,y)$ la ecuación del plano tangente a $\Sigma$ en $(1, 0, z_0)$. Siendo $h = f - p$, **analice** si $h(1,0)$ es extremo local y de qué tipo.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Observación clave.** Como $p$ es el plano tangente, $h(1,0) = 0$ y $\nabla h(1,0) = \vec 0$. Además $p$ es lineal, así que **el Hessiano de $h$ es el de $f$**.

**Paso 2 — Derivadas segundas de $f$** con $u = x + y - 1$, que vale 0 en $(1,0)$:

- $f'_x = 2x + \dfrac1x - 2\cos u + 2x\mathop{\mathrm{sen}}u$ y $f'_y = 2x\mathop{\mathrm{sen}}u$.
- $f''_{xx} = 2 - \dfrac{1}{x^2} + 4\mathop{\mathrm{sen}}u + 2x\cos u \to 2 - 1 + 0 + 2 = 3$.
- $f''_{xy} = 2\mathop{\mathrm{sen}}u + 2x\cos u \to 2$.
- $f''_{yy} = 2x\cos u \to 2$.

**Paso 3 — Clasificar.** $\det H = 3\cdot2 - 4 = 2 > 0$, con $f''_{xx} = 3 > 0$ ⇒ **mínimo local**.

</details>

**Respuesta:** $h(1,0) = 0$ es mínimo local.

</details>

---

### R7) Curva perpendicular a un conjunto de nivel

Sea S el conjunto de nivel 1 de $f(x,y,z) = \dfrac{x + y}{x^2 + y^2}$. Demostrar que la curva parametrizada por $\gamma(t) = (1 - 2t,\ t^2 - 2t + 1,\ t^3 + 2)$ es perpendicular a S en (1,1,2)

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parámetro del punto.** $\gamma(0) = (1, 1, 2)$, y $\gamma'(t) = (-2,\ 2t - 2,\ 3t^2)$ ⇒ $\gamma'(0) = (-2,\ -2,\ 0)$.

**Paso 2 — Superficie.** $\dfrac{x + y}{x^2 + y^2} = 1 \iff F(x,y,z) = x^2 + y^2 - x - y = 0$, con $(x,y) \ne (0,0)$. Es un cilindro.

**Paso 3 — Normal.** $\nabla F = (2x - 1,\ 2y - 1,\ 0)$ ⇒ $\nabla F(1,1,2) = (1,\ 1,\ 0)$.

**Paso 4 — Comparar.** $\gamma'(0) = -2\thinspace(1,1,0)$ es paralelo a la normal ⇒ la curva es perpendicular a $S$ en ese punto. $\blacksquare$

</details>

**Respuesta:** $\gamma'(0) = (-2,-2,0) \parallel \nabla F(1,1,2) = (1,1,0)$, con $F = x^2 + y^2 - x - y$.

</details>

---

### R8) Mínimo local usando el polinomio de Taylor

Sabiendo que $f: \mathbb{R}^2 \to \mathbb{R}$ es una función de clase $C^2$, cuyo polinomio de Taylor de segundo orden en el punto (1,-1) es $p(x,y) = 4 - x^2 + y^2 + xy + y$, demostrar que $g(x,y) = [f(x,y)]^2 + 6x^2$ alcanza un mínimo local en (1,-1)

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Datos de $f$ en $(1,-1)$** (iguales a los de $p$):

- $f = 4 - 1 + 1 - 1 - 1 = 2$;
- $f'_x = -2x + y = -3$ y $f'_y = 2y + x + 1 = 0$;
- $f''_{xx} = -2$, $f''_{xy} = 1$ y $f''_{yy} = 2$.

**Paso 2 — Gradiente de $g$.**

- $g'_x = 2f\thinspace f'_x + 12x = 2\cdot2\cdot(-3) + 12 = 0$.
- $g'_y = 2f\thinspace f'_y = 0$.

Es un punto crítico.

**Paso 3 — Hessiano de $g$.**

- $g''_{xx} = 2(f'_x)^2 + 2f\thinspace f''_{xx} + 12 = 18 - 8 + 12 = 22$.
- $g''_{xy} = 2f'_xf'_y + 2f\thinspace f''_{xy} = 0 + 4 = 4$.
- $g''_{yy} = 2(f'_y)^2 + 2f\thinspace f''_{yy} = 0 + 8 = 8$.

$\det = 22\cdot8 - 16 = 160 > 0$ y $g''_{xx} > 0$ ⇒ **mínimo local**. $\blacksquare$

</details>

**Respuesta:** $\nabla g(1,-1) = \vec 0$ y $Hg(1,-1) = \begin{pmatrix} 22 & 4 \cr 4 & 8 \end{pmatrix}$ es definido positivo ⇒ mínimo local.

</details>

---

### R9) Derivadas respecto de un vector

**Defina** derivada direccional. Siendo $f(x,y) = \dfrac{x^2y + y^2\mathop{\mathrm{sen}}(x)}{x^2 + y^2}$ si $(x,y) \ne (0,0)$, $f(x,y) = 0$ si $(x,y) = (0,0)$, **analice** si existe $f'((0,0),\ \vec r)$ para distintos $\vec r \in \mathbb{R}^2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Definición:** $f'(\vec A, \vec r) = \displaystyle\lim_{h\to0}\frac{f(\vec A + h\vec r) - f(\vec A)}{h}$, si el límite existe. Si $\lVert\vec r\rVert = 1$ es la derivada direccional.

**Cálculo** con $\vec r = (a, b) \ne \vec 0$:

$$\frac{f(ha, hb)}{h} = \frac{h^3a^2b + h^2b^2\mathop{\mathrm{sen}}(ha)}{h^3(a^2 + b^2)} = \frac{a^2b}{a^2 + b^2} + \frac{b^2}{a^2 + b^2}\cdot\frac{\mathop{\mathrm{sen}}(ha)}{h}$$

Como $\dfrac{\mathop{\mathrm{sen}}(ha)}{h} \to a$:

$$f'(\vec 0, \vec r) = \frac{a^2b + ab^2}{a^2 + b^2} = \frac{ab(a + b)}{a^2 + b^2}$$

Existe para **todo** $\vec r$. Para un versor, $f'(\vec 0, \breve r) = ab(a + b)$.

No es lineal en $\vec r$, así que $f$ no es diferenciable en el origen. Por ejemplo, $\nabla f(\vec 0) = (0,0)$ pero $f'(\vec 0, (1,1)/\sqrt2) = 1/\sqrt2 \ne 0$.

</details>

**Respuesta:** Existe para todo $\vec r = (a,b)$: $f'(\vec 0, \vec r) = \dfrac{ab(a+b)}{a^2 + b^2}$.

</details>

---

### R10) Aproximación con una función implícita

Siendo $h = f(\vec g(x,y))$, **calcule** aproximadamente $h(1.02,\ 1.98)$ cuando la matriz jacobiana $D\vec g(1,2) = \begin{pmatrix} 1 & 3 \cr 2 & 4 \end{pmatrix}$, $\vec g(1,2) = (3,4)$, estando $f(u,v)$ definida implícitamente por la ecuación $w + u\ln(w + v - 9) - 2u = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — $w_0$.** $w + 3\ln(w - 5) - 6 = 0$. Con $w_0 = 6$: $6 + 0 - 6 = 0$ ✓. Entonces $h(1,2) = f(3,4) = 6$.

**Paso 2 — Derivadas de $F$** en $(3,4,6)$, donde $w + v - 9 = 1$:

- $F'_u = \ln(w + v - 9) - 2 = -2$.
- $F'_v = \dfrac{u}{w + v - 9} = 3$.
- $F'_w = 1 + \dfrac{u}{w + v - 9} = 4$.

Entonces $f'_u = \dfrac24 = \dfrac12$ y $f'_v = -\dfrac34$.

**Paso 3 — Regla de la cadena.**

$$\nabla h(1,2) = \left(\tfrac12,\ -\tfrac34\right)\begin{pmatrix} 1 & 3 \cr 2 & 4 \end{pmatrix} = \left(-1,\ -\tfrac32\right)$$

**Paso 4 — Aproximación.**

$$h(1{,}02;\ 1{,}98) \approx 6 - 1(0{,}02) - \tfrac32(-0{,}02) = 6{,}01$$

</details>

**Respuesta:** $h(1.02;\ 1.98) \approx 6.01$.

</details>

---

### R11) Aproximación a partir de un plano tangente

Siendo $h(x,y) = f(x^2 - y,\ xy^2)$, **calcule** aproximadamente $h(2.01,\ 0.99)$ sabiendo que la superficie de ecuación $z = f(u,v)$ tiene plano tangente de ecuación $u + 2v - z = 5$ en el punto $(3,2,z_0)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Datos de $f$.** $z_0 = 3 + 4 - 5 = 2$ y $\nabla f(3,2) = (1,\ 2)$, de $z = u + 2v - 5$.

**Paso 2 — Punto.** $(x,y) = (2,1)$ ⇒ $(u,v) = (4 - 1,\ 2) = (3,2)$ ✓. Entonces $h(2,1) = 2$.

**Paso 3 — Derivadas de $u = x^2 - y$, $v = xy^2$** en $(2,1)$: $u'_x = 4$, $u'_y = -1$, $v'_x = y^2 = 1$ y $v'_y = 2xy = 4$.

**Paso 4 — Regla de la cadena.**

- $h'_x = 1\cdot4 + 2\cdot1 = 6$.
- $h'_y = 1\cdot(-1) + 2\cdot4 = 7$.

**Paso 5 — Aproximación.**

$$h(2{,}01;\ 0{,}99) \approx 2 + 6(0{,}01) + 7(-0{,}01) = 1{,}99$$

</details>

**Respuesta:** $h(2.01;\ 0.99) \approx 1.99$.

</details>

---

### R12) Distancia a lo largo de una recta tangente

Sea **C** la curva definida como intersección de las superficies de ecuaciones $y = x^2$ y $e^{xz-1} - xy + \ln(yz) = 0$. Si $L_0$ es la recta tangente a **C** en $A = (1,1,1)$, calcule la distancia desde $A$ hasta el punto en que $L_0$ interseca al plano de ecuación $x + y = 8$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Gradientes en $A$.**

- $F_1 = y - x^2$: $\nabla F_1 = (-2x,\ 1,\ 0) = (-2,\ 1,\ 0)$.
- $F_2 = e^{xz-1} - xy + \ln(yz)$: $\nabla F_2 = \left(z\thinspace e^{xz-1} - y,\ -x + \dfrac1y,\ x\thinspace e^{xz-1} + \dfrac1z\right) = (0,\ 0,\ 2)$.

**Paso 2 — Dirección.** $\vec d = (-2,1,0)\wedge(0,0,2) = (2,\ 4,\ 0)$.

**Paso 3 — Intersección.** $L_0: (1 + 2t,\ 1 + 4t,\ 1)$, con $x + y = 2 + 6t = 8 \Rightarrow t = 1$. El punto es $(3, 5, 1)$.

**Paso 4 — Distancia.** $\lVert(3,5,1) - (1,1,1)\rVert = \lVert(2,4,0)\rVert = 2\sqrt5$.

</details>

**Respuesta:** $2\sqrt5$.

</details>

---

### R13) Continuidad, derivadas direccionales y diferenciabilidad

*Ejercicio resuelto en la pizarra (el enunciado se reconstruye de la resolución):* Dada $f(x,y) = \begin{cases} y^2\cos\negthinspace\left(\dfrac{1}{x^2 + y^2}\right) & (x,y) \ne (0,0) \cr 0 & (x,y) = (0,0) \end{cases}$, analizar continuidad, existencia de derivadas direccionales y diferenciabilidad en el origen.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Continuidad.** $y^2 \to 0$ y el coseno está acotado ⇒ $f \to 0 = f(0,0)$.

**Derivadas direccionales.** Con $\breve r = (a,b)$:

$$\lim_{h\to0}\frac{h^2b^2\cos\negthinspace\left(\frac{1}{h^2}\right)}{h} = \lim_{h\to0}\underbrace{h\thinspace b^2}_{\to0}\cdot\underbrace{\cos(1/h^2)}_{\text{acot.}} = 0$$

Todas valen 0, así que $\nabla f(\vec 0) = (0,0)$.

**Diferenciabilidad.** Hay que ver si

$$\lim_{(h,k)\to\vec 0}\frac{f(h,k) - 0 - 0}{\sqrt{h^2 + k^2}} = \lim\underbrace{\frac{k}{\sqrt{h^2 + k^2}}}_{\text{acot.}}\cdot\underbrace{k}_{\to0}\cdot\underbrace{\cos\negthinspace\left(\frac{1}{h^2+k^2}\right)}_{\text{acot.}} = 0$$

Vale 0 ⇒ **es diferenciable**.

</details>

**Respuesta:** $f$ es continua en el origen, $f'(\vec 0, \breve r) = 0$ para todo $\breve r$, y $f$ es diferenciable en $(0,0)$.

</details>

---

[← Volver al menú principal](../README.md)
