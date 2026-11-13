# 2.º Parcial (18/06/2019) — Curso semipresencial

Análisis Matemático II — UTN-FRBA. Primer cuatrimestre de 2019.

Enunciado y resolución de la cátedra: [Parcial2-2019-06-18-Resuelto.pdf](../aula-virtual/Parciales/Segundo-Parcial/Parcial2-2019-06-18-Resuelto.pdf).

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Conservativo ⇒ jacobiana simétrica

Sea $\vec f: A \subset \mathbb{R}^2 \to \mathbb{R}^2$, $A$ abierto, $\vec f = (P,Q) \in C^1$. Demuestre que si $\vec f$ es conservativo, entonces $Q'_x = P'_y$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Hipótesis.** $\vec f$ conservativo significa que existe $\phi$ con $\nabla\phi = \vec f$, es decir $\phi'_x = P$ y $\phi'_y = Q$.

**Paso 2 — Regularidad.** Como $P, Q \in C^1$, las derivadas segundas de $\phi$ existen y son continuas: $\phi \in C^2(A)$.

**Paso 3 — Schwarz.** Para $\phi \in C^2$ en un abierto, las derivadas cruzadas coinciden:

$$Q'_x = (\phi'_y)'_x = \phi''_{yx} = \phi''_{xy} = (\phi'_x)'_y = P'_y \quad\blacksquare$$

</details>

**Respuesta:** Con $\vec f = \nabla\phi$ y $\phi \in C^2$, el teorema de Schwarz da $Q'_ x = \phi''_ {yx} = \phi''_ {xy} = P'_ y$ (ver la teoría de la Unidad 8).

</details>

---

### T2) Teorema de Stokes

Enuncie el teorema de Stokes. Determine la veracidad de la siguiente afirmación:

"Si $\vec f: \mathbb{R}^3 \to \mathbb{R}^3$ es un campo vectorial $C^1$ tal que $\mathop{\mathrm{rot}}(\vec f) = (2,-2,3)$, entonces la circulación de $\vec f$ a lo largo de la curva $C$ borde de la superficie $x + y + z = 4$, en el primer octante, orientada en sentido $(4,0,0) \to (0,0,4) \to (0,4,0) \to (4,0,0)$ es $24$." **JUSTIFICAR**

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** si $S$ es una superficie orientable y suave a trozos, cuyo borde $\partial S$ es una curva cerrada suave a trozos con orientación compatible (regla de la mano derecha), y $\vec f \in C^1$ en un abierto que contiene a $S$, entonces:

$$\oint_{\partial S}\vec f\cdot d\vec s = \iint_S\mathop{\mathrm{rot}}\vec f\cdot\breve n\thinspace d\sigma$$

**Paso 1 — Orientación.** Con $A = (4,0,0)$, $B = (0,0,4)$ y $C = (0,4,0)$:

$$(B - A)\times(C - B) = (-4, 0, 4)\times(0, 4, -4) = (-16,\ -16,\ -16)$$

El recorrido indicado corresponde a la normal $\breve n = -\dfrac{(1,1,1)}{\sqrt3}$, que apunta "hacia abajo", hacia el origen.

**Paso 2 — Integrando.** $\mathop{\mathrm{rot}}\vec f\cdot\breve n = \dfrac{-(2 - 2 + 3)}{\sqrt3} = -\dfrac{3}{\sqrt3} = -\sqrt3$, constante.

**Paso 3 — Área.** Es un triángulo equilátero de lado $4\sqrt2$: $A = \dfrac{\sqrt3}{4}(4\sqrt2)^2 = 8\sqrt3$.

**Paso 4 — Circulación.**

$$\oint_C\vec f\cdot d\vec s = -\sqrt3\cdot8\sqrt3 = -24 \ne 24$$

</details>

**Respuesta:** La afirmación es **falsa**: con la orientación dada la normal compatible es $-(1,1,1)/\sqrt3$, y la circulación vale $-\sqrt3\cdot\text{área}(S) = -24$, que es negativa.

</details>

---

## Ejercicios prácticos

### P1) Masa de una superficie

Calcule la masa de la superficie $\Sigma$ definida por $y = \sqrt{x^2 + z^2}$, $1 \le y \le 3$, si su densidad en cada punto es proporcional a la distancia desde el punto al **plano** $xz$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Densidad.** La distancia al plano $xz$ es $|y|$, así que $\delta = k|y| = k\thinspace y$.

**Paso 2 — Parametrización** (cono de eje $y$): $\vec T(u,v) = (u,\ \sqrt{u^2+v^2},\ v)$, con $D: 1 \le u^2 + v^2 \le 9$.

$$\lVert\vec T'_u\times\vec T'_v\rVert = \sqrt{1 + \frac{u^2}{u^2+v^2} + \frac{v^2}{u^2+v^2}} = \sqrt2$$

**Paso 3 — Masa.**

$$M = \iint_D k\sqrt{u^2+v^2}\thinspace\sqrt2\thinspace du\thinspace dv = \sqrt2\thinspace k\int_0^{2\pi}\negthinspace\negthinspace\int_1^3 r\cdot r\thinspace dr\thinspace d\theta = 2\sqrt2\thinspace k\pi\thinspace\frac{27 - 1}{3} = \frac{52\sqrt2\thinspace k\pi}{3}$$

</details>

**Respuesta:** $M = \dfrac{52\sqrt2\thinspace k\pi}{3}$.

</details>

---

### P2) Circulación de un campo conservativo más otro

Sean $\vec f: \mathbb{R}^2 \to \mathbb{R}^2$, $\vec f = (P,Q)$, un campo $C^1$ y conservativo; $\vec g(x,y) = (xy,\ \mathop{\mathrm{sen}}(y^4))$ y $\vec h = \vec f + \vec g$. Calcule la circulación de $\vec h$ a lo largo de la curva $C: x^2 + y^2 = 6x$. Indique claramente la orientación elegida para el cálculo.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Curva.** Completando cuadrados: $(x - 3)^2 + y^2 = 9$, circunferencia de centro $(3,0)$ y radio 3. La recorremos en sentido **positivo** (antihorario).

**Paso 2 — Separar.**

$$\oint_C\vec h\cdot d\vec s = \underbrace{\oint_C\vec f\cdot d\vec s}_{=\thinspace0 \text{ (conservativo)}} + \oint_C\vec g\cdot d\vec s$$

**Paso 3 — Green para $\vec g$.** $Q'_x - P'_y = 0 - x = -x$.

$$\oint_C\vec g\cdot d\vec s = \iint_D -x\thinspace dA = -\bar x\cdot\text{Área} = -3\cdot9\pi = -27\pi$$

El centroide del disco es $\bar x = 3$. En polares, $x = 3 + r\cos\theta$, y $\int_0^3\negthinspace\int_0^{2\pi}(3 + r\cos\theta)\thinspace r\thinspace d\theta\thinspace dr = 27\pi$.

</details>

**Respuesta:** $\oint_{C^+}\vec h\cdot d\vec s = -27\pi$ (recorrida en sentido antihorario; en sentido horario daría $27\pi$).

</details>

---

### P3) Flujo a través de un casquete esférico

Sea $\vec f(x,y,z) = (x^2 + z^3,\ x^4 - 2xy,\ z)$. Calcule el flujo de $\vec f$ a través de la superficie $S$ definida $x^2 + y^2 + z^2 = 5$, $z \ge 1$. Indique en un gráfico cómo elige orientar a la superficie.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Divergencia.** $\mathop{\mathrm{div}}\vec f = 2x - 2x + 1 = 1$.

**Paso 2 — Cerrar.** Agregamos la tapa $T$: $z = 1$, $x^2 + y^2 \le 4$. El sólido es $V$: $x^2 + y^2 + z^2 \le 5$, $z \ge 1$. Con normales salientes, $S$ apunta "hacia arriba" (hacia afuera de la esfera) y $T$ hacia abajo:

$$\iint_S + \iint_T = \iiint_V 1\thinspace dV$$

**Paso 3 — Volumen del casquete.** Por secciones horizontales:

$$V = \pi\int_1^{\sqrt5}(5 - z^2)\thinspace dz = \pi\left[5z - \frac{z^3}{3}\right]_1^{\sqrt5} = \pi\left(\frac{10\sqrt5}{3} - \frac{14}{3}\right) = \frac{2\pi(5\sqrt5 - 7)}{3}$$

**Paso 4 — Flujo por la tapa.** $\breve n = (0,0,-1)$ ⇒ $\vec f\cdot\breve n = -z = -1$:

$$\iint_T = -\text{Área}(T) = -4\pi$$

**Paso 5 — Resultado.**

$$\iint_S\vec f\cdot d\vec\sigma = \frac{2\pi(5\sqrt5 - 7)}{3} + 4\pi \approx 21{,}32$$

</details>

**Respuesta:** Con $S$ orientada hacia afuera de la esfera (hacia arriba): $\dfrac{2\pi(5\sqrt5 - 7)}{3} + 4\pi$.

</details>

---

### P4) Ecuación diferencial y línea de campo

- a) Halle la solución de $y'' + 4y' = -10e^x$, que verifica $y(0) = 3$, $y'(0) = -2$.
- b) Dado el campo vectorial $\vec f(x,y) = (x,\ 2y)$, halle la línea de campo de $\vec f$ que pasa por $(3,-4)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)**

- *Homogénea:* $\lambda^2 + 4\lambda = \lambda(\lambda + 4)$ ⇒ $y_H = C_1 + C_2e^{-4x}$.
- *Particular:* $y_P = Ae^x$ ⇒ $Ae^x + 4Ae^x = -10e^x$ ⇒ $A = -2$.
- *S.G.:* $y = C_1 + C_2e^{-4x} - 2e^x$.

*Condiciones:*

- $y'(0) = -4C_2 - 2 = -2 \Rightarrow C_2 = 0$;
- $y(0) = C_1 - 2 = 3 \Rightarrow C_1 = 5$.

**b)** $\dfrac{dy}{dx} = \dfrac{2y}{x}$ ⇒ $\displaystyle\int\frac{dy}{y} = \int\frac2x\thinspace dx$ ⇒ $y = kx^2$. Por $(3,-4)$: $-4 = 9k \Rightarrow k = -\frac49$.

</details>

**Respuesta:**

- a) $y(x) = 5 - 2e^x$.
- b) $y = -\dfrac49x^2$.

</details>

---

[← Volver al menú principal](../README.md)
