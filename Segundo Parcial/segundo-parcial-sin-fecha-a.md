# 2.º Parcial (sin fecha) — A

Análisis Matemático II — UTN-FRBA. La foto no muestra fecha ni curso.

Enunciado (fotos, sin resolución oficial): [Parcial2-sin-fecha-A.jpeg](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-sin-fecha-A.jpeg) (otra foto del mismo examen: [Parcial2-sin-fecha-A-foto2.jpeg](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-sin-fecha-A-foto2.jpeg)).

Las resoluciones son propias (no hay solución de la cátedra). Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Parte práctica

### P1) Flujo a través de un cilindro parabólico

Calcular el flujo del campo vectorial $\bar f: R^3 \to R^3$ tal que $\bar f(x,y,z) = (-2x + y\thinspace;\ z^2 + x^2;\ 4x^2)$ a través de la porción superficie $z = 4 - x^2$ con $0 \le y \le z$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $\vec T(x,y) = (x,\ y,\ 4 - x^2)$ con $0 \le y \le 4 - x^2$, que exige $-2 \le x \le 2$.

**Paso 2 — Normal hacia arriba.** $\vec n = (-z'_x, -z'_y, 1) = (2x, 0, 1)$.

**Paso 3 — Producto escalar.**

$$\bar f\cdot\vec n = (-2x + y)\thinspace 2x + 4x^2 = 2xy$$

**Paso 4 — Integrar.**

$$\Phi = \int_{-2}^2\negthinspace\negthinspace\int_0^{4 - x^2}2xy\thinspace dy\thinspace dx = \int_{-2}^2 x(4 - x^2)^2\thinspace dx = 0$$

(integrando impar en un intervalo simétrico).

</details>

**Respuesta:** $\Phi = 0$ (con cualquier orientación).

</details>

---

### P2) Masa de un cilindro cortado por dos planos

Calcule la masa del sólido de $R^3$ definido por $x^2 + y^2 \le 9$; $z + y \le 3$ ; $y - z \le 3$, si la densidad en cada punto es proporcional a la distancia al eje z.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Límites en $z$.** $y - 3 \le z \le 3 - y$. Como en el disco $y \le 3$, la altura $6 - 2y$ nunca es negativa.

**Paso 2 — Densidad.** $\delta = k\sqrt{x^2 + y^2} = k\thinspace r$.

**Paso 3 — Cilíndricas.**

$$M = \int_0^{2\pi}\negthinspace\negthinspace\int_0^3\negthinspace\negthinspace\int_{r\mathop{\mathrm{sen}}\theta - 3}^{3 - r\mathop{\mathrm{sen}}\theta}k\thinspace r\cdot r\thinspace dz\thinspace dr\thinspace d\theta = k\int_0^{2\pi}\negthinspace\negthinspace\int_0^3 r^2(6 - 2r\mathop{\mathrm{sen}}\theta)\thinspace dr\thinspace d\theta$$

**Paso 4 — Calcular.** El término con $\mathop{\mathrm{sen}}\theta$ se anula:

$$M = k\cdot 2\pi\cdot 6\cdot\frac{27}{3} = 108\pi k$$

</details>

**Respuesta:** $M = 108\pi k$ ($k$: constante de proporcionalidad).

</details>

---

### P3) Circulación de un campo conservativo en el espacio

Sea $\bar f: R^3 \to R^3$ tal que $\bar f(x,y,z) = (2xy^3z + x^2;\ 3y^2zx^2 + \mathop{\mathrm{sen}}(y);\ x^2y^3 - 4)$, calcule la circulación de $\bar f$ a lo largo de la curva intersección de las superficies $x^2 + z^2 = 9$ con $z \ge 0$ ; $y + z = 3$ desde el punto (3,3,0) al (-3,3,0)

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Rotor.**

- $R'_y - Q'_z = 3x^2y^2 - 3x^2y^2 = 0$.
- $P'_z - R'_x = 2xy^3 - 2xy^3 = 0$.
- $Q'_x - P'_y = 6xy^2z - 6xy^2z = 0$.

$\bar f \in C^1(\mathbb{R}^3)$ con rotor nulo ⇒ conservativo.

**Paso 2 — Potencial.**

- $\varphi = \int(2xy^3z + x^2)\thinspace dx = x^2y^3z + \frac{x^3}{3} + D(y,z)$.
- $\varphi'_y = 3x^2y^2z + D'_y = 3x^2y^2z + \mathop{\mathrm{sen}}y \Rightarrow D = -\cos y + E(z)$.
- $\varphi'_z = x^2y^3 + E'(z) = x^2y^3 - 4 \Rightarrow E = -4z$.

$$\varphi = x^2y^3z + \frac{x^3}{3} - \cos y - 4z$$

**Paso 3 — Circulación.**

$$\varphi(-3,3,0) - \varphi(3,3,0) = (-9 - \cos 3) - (9 - \cos 3) = -18$$

</details>

**Respuesta:** $-18$.

</details>

---

### P4) Circulación con Green en un sector de corona

Sea $\bar f: R^2 \to R^2$ tal que $\bar f(x,y) = (2xye^{x^2} + x - 1;\ e^{x^2} + x^2 - y^2)$ , calcule la circulación de $\bar f$ en sentido positivo a lo largo de la curva frontera de la región D

$$D = \{(x,y) \in R^2: 1 \le x^2 + y^2 \le 9;\ y \ge 0;\ y \ge x\}$$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Green.**

$$Q'_x - P'_y = (2xe^{x^2} + 2x) - 2xe^{x^2} = 2x$$

**Paso 2 — Región en polares.** $y \ge 0$ e $y \ge x$: $\frac{\pi}{4} \le \theta \le \pi$; $1 \le r \le 3$.

**Paso 3 — Calcular.**

$$\oint = \int_{\pi/4}^{\pi}\negthinspace\negthinspace\int_1^3 2r\cos\theta\cdot r\thinspace dr\thinspace d\theta = 2\cdot\frac{26}{3}\left[\mathop{\mathrm{sen}}\theta\right]_{\pi/4}^{\pi} = \frac{52}{3}\left(0 - \frac{\sqrt2}{2}\right) = -\frac{26\sqrt2}{3}$$

</details>

**Respuesta:** $-\dfrac{26\sqrt2}{3}$.

</details>

---

## Parte teórica

### T1) Flujo del rotor por un cono

Calcule el flujo del rotor del campo $\bar f(x,y,z) = (x + y,\ y - x + z,\ -2x^2 + \mu(x,y,z))$ con $\mu \in C^2$ a través de la superficie S definida por $z = 5 - \sqrt{y^2 + x^2}$ con $z \ge 1$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Stokes.** $\iint_S(\nabla\times\bar f)\cdot\vec n\thinspace dS = \oint_{\partial S}\bar f\cdot d\bar s$. El borde de $S$ está en $z = 1$: $\sqrt{x^2 + y^2} = 4$, la circunferencia de radio 4.

**Paso 2 — Orientación.** Con la normal del cono hacia arriba, el borde se recorre en sentido antihorario visto desde arriba: $\vec\alpha(t) = (4\cos t,\ 4\mathop{\mathrm{sen}}t,\ 1)$.

**Paso 3 — Circulación.** $dz = 0$, así que la tercera componente (y $\mu$) no aporta:

$$\bar f\cdot\vec\alpha' = (4\cos t + 4\mathop{\mathrm{sen}}t)(-4\mathop{\mathrm{sen}}t) + (4\mathop{\mathrm{sen}}t - 4\cos t + 1)(4\cos t) = -16 + 4\cos t$$

$$\oint = \int_0^{2\pi}(-16 + 4\cos t)\thinspace dt = -32\pi$$

**Verificación con el disco** $z = 1$, $r \le 4$, normal $(0,0,1)$: $(\nabla\times\bar f)_z = Q'_x - P'_y = -1 - 1 = -2$ ⇒ $-2\cdot 16\pi = -32\pi$ ✓.

</details>

**Respuesta:** Con normal hacia arriba, el flujo del rotor es $-32\pi$ ($32\pi$ con la normal opuesta).

</details>

---

### T2) Condición para que un campo sea conservativo

a) Enuncie la condición necesaria y suficiente para que un campo resulte conservativo.

b) Sea $f(x,y) = \ln(x^2 + y^2)$ y sea $\bar g(x,y) = \nabla f(x,y)$ , calcule la circulación de $\bar g$ a lo largo de la curva $x^2 + y^2 = 4$ . Justifique claramente el procedimiento usado.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** Sea $\vec g$ continuo en un abierto conexo $D$. $\vec g$ es conservativo (admite función potencial) en $D$ **si y solo si** $\oint_C\vec g\cdot d\vec s = 0$ para toda curva cerrada suave a trozos $C \subset D$ (equivalentemente, las integrales de línea solo dependen de los extremos).

Condición necesaria: si $\vec g \in C^1$ es conservativo, su jacobiana es simétrica; en un dominio simplemente conexo esa condición también es suficiente.

**b) Paso 1.** $f$ es $C^1$ en $\mathbb{R}^2 - \{0\}$ y la circunferencia $x^2 + y^2 = 4$ no pasa por el origen. $\bar g = \nabla f$ es un campo de gradientes en ese dominio, con potencial $f$.

**Paso 2.** Para una curva cerrada contenida en el dominio de $f$:

$$\oint_C\nabla f\cdot d\vec s = f(\text{fin}) - f(\text{inicio}) = 0$$

No hace falta que el dominio sea simplemente conexo: el potencial ya se conoce. (Contraste: el campo $\left(\frac{-y}{x^2 + y^2}, \frac{x}{x^2 + y^2}\right)$ tiene jacobiana simétrica pero no es un gradiente en $\mathbb{R}^2 - \{0\}$.)

</details>

**Respuesta:** b) $\oint_C\bar g\cdot d\vec s = 0$, porque $\bar g$ es el gradiente de $f = \ln(x^2 + y^2)$, que está definida sobre toda la curva.

</details>

---

[Volver al menú principal](../README.md)
