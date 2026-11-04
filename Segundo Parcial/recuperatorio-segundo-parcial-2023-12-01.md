# Recuperatorio del 2.º Parcial (01/12/2023) — Curso Z2051

Análisis Matemático II — UTN-FRBA.

Enunciado (foto, sin resolución oficial): [Recuperatorio2-2023-12-01-Z2051.jpeg](../aula-virtual/Parciales/Segundo-Parcial/fotos/Recuperatorio2-2023-12-01-Z2051.jpeg).

Las resoluciones son propias (no hay solución de la cátedra). Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Parte práctica

### 1) Trabajo sobre media elipse en el plano xz

Sean $\bar f(x,y,z) = (xy;\ x^2 + h(y);\ 5 + yz - x^2)$ con h una función de clase $C^1$ y C la curva simple dada por $x^2 + 4(z - 2)^2 = 16$ con $x \le 0$ en el plano xz. Calcular el trabajo realizado por el campo $\bar f$ sobre C con orientación desde el (0, 0, 0) hacia el (0, 0, 4).

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** En el plano $xz$ ($y = 0$), $\frac{x^2}{16} + \frac{(z - 2)^2}{4} = 1$ con $x \le 0$:

$$\vec\alpha(t) = (-4\mathop{\mathrm{sen}}t,\ 0,\ 2 - 2\cos t), \qquad 0 \le t \le \pi$$

Va de $\vec\alpha(0) = (0,0,0)$ a $\vec\alpha(\pi) = (0,0,4)$ con $x \le 0$ ✓.

**Paso 2 — Campo sobre la curva.** Con $y = 0$: $\bar f = (0,\ x^2 + h(0),\ 5 - x^2)$, y $\vec\alpha'(t) = (-4\cos t,\ 0,\ 2\mathop{\mathrm{sen}}t)$. Solo aporta la tercera componente:

$$\bar f\cdot\vec\alpha' = (5 - 16\mathop{\mathrm{sen}}^2t)\thinspace 2\mathop{\mathrm{sen}}t$$

**Paso 3 — Integrar.** Con $\int_0^\pi\mathop{\mathrm{sen}}t\thinspace dt = 2$ y $\int_0^\pi\mathop{\mathrm{sen}}^3t\thinspace dt = \frac43$:

$$W = 10\cdot 2 - 32\cdot\frac43 = 20 - \frac{128}{3} = -\frac{68}{3}$$

</details>

**Respuesta:** $W = -\dfrac{68}{3}$.

</details>

---

### 2) Flujo a través de un trozo de paraboloide

Sea S la superficie definida por $z = x^2 + y^2$ con $x^2 + y^2 \le 6$, $2 \le z$ y sea el campo $\bar f(x,y,z) = (x, x, 0)$ Hallar el flujo de $\bar f$ a través de S. Indicar la orientación elegida.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Región.** $2 \le r^2 \le 6$: corona $\sqrt2 \le r \le \sqrt6$.

**Paso 2 — Normal hacia arriba.** $\vec n = (-z'_x, -z'_y, 1) = (-2x, -2y, 1)$.

**Paso 3 — Producto escalar.** $\bar f\cdot\vec n = -2x^2 - 2xy$.

**Paso 4 — Polares.** El término $-2xy$ se anula al integrar en $\theta$ ($\int_0^{2\pi}\cos\theta\mathop{\mathrm{sen}}\theta\thinspace d\theta = 0$):

$$\Phi = \int_0^{2\pi}\negthinspace\negthinspace\int_{\sqrt2}^{\sqrt6}-2r^2\cos^2\theta\cdot r\thinspace dr\thinspace d\theta = -2\pi\cdot\frac{36 - 4}{4} = -16\pi$$

</details>

**Respuesta:** Con normal hacia arriba (hacia el interior del paraboloide), $\Phi = -16\pi$; con la normal opuesta, $16\pi$.

</details>

---

### 3) EDO de tercer orden

Hallar las soluciones de la ecuación diferencial $y''' + 4y'' + 5y' = 4x$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Homogénea.** $r^3 + 4r^2 + 5r = r(r^2 + 4r + 5) = 0 \Rightarrow r = 0$, $r = -2 \pm i$:

$$y_h = C_1 + e^{-2x}(C_2\cos x + C_3\mathop{\mathrm{sen}}x)$$

**Paso 2 — Particular.** El segundo miembro es un polinomio de grado 1 y $r = 0$ es raíz simple ⇒ $y_p = x(Ax + B) = Ax^2 + Bx$.

$y_p' = 2Ax + B$, $y_p'' = 2A$, $y_p''' = 0$:

$$8A + 5(2Ax + B) = 4x \Rightarrow 10A = 4,\quad 8A + 5B = 0 \Rightarrow A = \frac25,\ B = -\frac{16}{25}$$

</details>

**Respuesta:** $y = C_1 + e^{-2x}(C_2\cos x + C_3\mathop{\mathrm{sen}}x) + \dfrac25x^2 - \dfrac{16}{25}x$.

</details>

---

### 4) Parámetro para un volumen dado

Halle $a \in R^+$ tal que el volumen encerrado por las superficies $z = \sqrt{x^2 + y^2}$ y $z = a(x^2 + y^2)$ sea igual a $\frac{\pi}{6}$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Intersección.** $r = ar^2 \Rightarrow r = 0$ o $r = \frac1a$. Para $0 < r < \frac1a$: $ar^2 < r$, el cono está arriba.

**Paso 2 — Volumen en función de $a$.**

$$V(a) = \int_0^{2\pi}\negthinspace\negthinspace\int_0^{1/a}(r - ar^2)\thinspace r\thinspace dr\thinspace d\theta = 2\pi\left(\frac{1}{3a^3} - \frac{1}{4a^3}\right) = \frac{\pi}{6a^3}$$

**Paso 3 — Igualar.** $\frac{\pi}{6a^3} = \frac{\pi}{6} \Rightarrow a^3 = 1 \Rightarrow a = 1$.

</details>

**Respuesta:** $a = 1$.

</details>

---

## Parte teórica

### T1) Teorema de Green y área

a) Enuncie el teorema de Green.

b) Calcular el área de la región definida por $x^2 + (y - 1)^2 \le 4$, $x \le 0$ usando integrales de línea.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a) Enunciado:** si $D \subset \mathbb{R}^2$ es una región acotada cuya frontera $C$ es una curva cerrada, simple, suave a trozos y orientada positivamente, y $\vec f = (P,Q)$ es $C^1$ en un abierto que contiene a $D$, entonces

$$\oint_C P\thinspace dx + Q\thinspace dy = \iint_D(Q'_x - P'_y)\thinspace dx\thinspace dy$$

**b) Paso 1 — Campo conveniente.** $\vec f = (0, x)$: $Q'_x - P'_y = 1$, así que $\text{Área}(D) = \oint_C x\thinspace dy$.

**Paso 2 — Frontera (sentido positivo).** Es el semicírculo izquierdo de centro $(0,1)$ y radio 2:

- $C_1$ (arco): $(2\cos t,\ 1 + 2\mathop{\mathrm{sen}}t)$, $\frac{\pi}{2} \le t \le \frac{3\pi}{2}$.
- $C_2$ (segmento sobre $x = 0$): de $(0,-1)$ a $(0,3)$.

**Paso 3 — Integrar.** En $C_2$, $x = 0$ ⇒ aporta 0. En $C_1$, $dy = 2\cos t\thinspace dt$:

$$\text{Área} = \int_{\pi/2}^{3\pi/2}2\cos t\cdot 2\cos t\thinspace dt = 4\cdot\frac{\pi}{2} = 2\pi$$

(Coincide con la mitad del área de un círculo de radio 2.)

</details>

**Respuesta:** b) $\text{Área} = 2\pi$.

</details>

---

### T2) Condición para la existencia de potencial

a) Enuncie la condición necesaria y suficiente para la existencia de función potencial

b) Calcule la circulación del campo $\bar f(x,y) = \left(\frac{2x}{x^2 + y^2};\ \frac{2y}{x^2 + y^2}\right)$ a lo largo de la curva $x^2 + 4y^2 = 4$ con $x \le 1$. Justifique claramente el procedimiento usado.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** Sea $\vec f$ continuo en un abierto conexo $D$. $\vec f$ admite función potencial en $D$ **si y solo si** su circulación sobre toda curva cerrada (suave a trozos) contenida en $D$ es nula (equivalentemente, la integral de línea entre dos puntos no depende del camino).

Condición necesaria práctica: si $\vec f \in C^1$ admite potencial, su matriz jacobiana es simétrica. Si además $D$ es simplemente conexo, la simetría también es suficiente.

**b) Paso 1 — Potencial.** $\varphi(x,y) = \ln(x^2 + y^2)$ cumple $\nabla\varphi = \bar f$ en todo el dominio $\mathbb{R}^2 - \{0\}$. Entonces $\bar f$ es un campo de gradientes allí (aunque el dominio no sea simplemente conexo) y la integral depende solo de los extremos.

**Paso 2 — Extremos.** $x = 1$ en la elipse: $4y^2 = 3 \Rightarrow y = \pm\frac{\sqrt3}{2}$. La curva va de $\left(1, \frac{\sqrt3}{2}\right)$ a $\left(1, -\frac{\sqrt3}{2}\right)$ pasando por $(-2, 0)$ (o al revés). En ambos extremos $x^2 + y^2 = \frac74$.

**Paso 3 — Circulación.**

$$\int_C\bar f\cdot d\bar s = \ln\tfrac74 - \ln\tfrac74 = 0$$

</details>

**Respuesta:** b) La circulación vale $0$ en cualquier sentido, porque $\bar f = \nabla\ln(x^2 + y^2)$ y los dos extremos están a la misma distancia del origen.

</details>

---

[Volver al menú principal](../README.md)
