# 2.º Parcial (24/11/2020) — Curso Z2004

Análisis Matemático II — UTN-FRBA. Segundo cuatrimestre de 2020.

Enunciado (foto, sin resolución oficial): [Parcial2-2020-11-24-Z2004.jpeg](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-2020-11-24-Z2004.jpeg).

Las resoluciones son propias (no hay solución de la cátedra). Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios

### P1) Circulación proporcional al área

Sea $\bar f(x,y) = (3x^7 + 4yg(x); 2g'(x) + 3y + 5x)$, con $g \in C^1$. Halle g tal que $\bar f(0,1) = (8,\ 3 - 4\sqrt2)$; y que la circulación de $\bar f$ a lo largo de toda curva C simple, suave y cerrada con orientación positiva valga 5 veces el área de la región encerrada por la curva.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

> Para que $Q = 2g'(x) + 3y + 5x$ sea $C^1$ hace falta $g \in C^2$; se supone así.

**Paso 1 — Green.** Para toda curva $C$ cerrada, simple y positiva que encierra una región $D$:

$$\oint_C\bar f\cdot d\bar s = \iint_D(Q'_x - P'_y)\thinspace dA = 5\iint_D dA$$

Para que valga en **toda** región hace falta $Q'_x - P'_y = 5$ en todo punto.

**Paso 2 — Ecuación para $g$.**

$$Q'_x - P'_y = 2g''(x) + 5 - 4g(x) = 5 \quad\Longrightarrow\quad g'' - 2g = 0$$

Ecuación característica $r^2 - 2 = 0 \Rightarrow r = \pm\sqrt2$:

$$g(x) = C_1e^{\sqrt2 x} + C_2e^{-\sqrt2 x}$$

**Paso 3 — Condiciones.** $\bar f(0,1) = (4g(0),\ 2g'(0) + 3)$:

- $4g(0) = 8 \Rightarrow C_1 + C_2 = 2$.
- $2g'(0) + 3 = 3 - 4\sqrt2 \Rightarrow g'(0) = -2\sqrt2 \Rightarrow \sqrt2(C_1 - C_2) = -2\sqrt2 \Rightarrow C_1 - C_2 = -2$.

Entonces $C_1 = 0$, $C_2 = 2$.

</details>

**Respuesta:** $g(x) = 2e^{-\sqrt2\thinspace x}$.

</details>

---

### P2) Volumen y flujo saliente con Gauss

a) Determine el volumen del sólido H definido por $x^2 + y^2 \le 4y$ ; $y \le z \le 4$

b) Sea h: R → R una función $C^1$, calcule el flujo de $\bar f(x,y,z) = (h(z) + \mathop{\mathrm{sen}}(y^2) + 3;\ z^3 - 2y;\ 3z)$ a través de la superficie S frontera del sólido H. Indicar la orientación elegida para S

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a) Paso 1 — Proyección.** $x^2 + y^2 \le 4y \iff x^2 + (y - 2)^2 \le 4$: disco $D$ de centro $(0,2)$ y radio 2. En él $0 \le y \le 4$, así que $y \le 4$ y el techo $z = 4$ queda siempre por encima del piso $z = y$.

**Paso 2 — Volumen.**

$$V = \iint_D(4 - y)\thinspace dA = 4\cdot\text{Área}(D) - \iint_D y\thinspace dA = 4\cdot 4\pi - \bar y\cdot\text{Área}(D) = 16\pi - 2\cdot 4\pi = 8\pi$$

($\bar y = 2$ es la ordenada del centro del disco.) En polares: $x = r\cos\theta$, $y = r\mathop{\mathrm{sen}}\theta$, $0 \le r \le 4\mathop{\mathrm{sen}}\theta$, $0 \le \theta \le \pi$ da el mismo resultado.

**b) Paso 1 — Divergencia.**

$$\mathop{\mathrm{div}}\bar f = \frac{\partial}{\partial x}\left(h(z) + \mathop{\mathrm{sen}}(y^2) + 3\right) + \frac{\partial}{\partial y}(z^3 - 2y) + \frac{\partial}{\partial z}(3z) = 0 - 2 + 3 = 1$$

**Paso 2 — Gauss.** $S$ es cerrada y $\bar f \in C^1(\mathbb{R}^3)$. Con normal exterior:

$$\Phi = \iiint_H 1\thinspace dV = V = 8\pi$$

</details>

**Respuesta:** a) $V = 8\pi$. b) Con normal exterior, $\Phi = 8\pi$.

</details>

---

### P3) Circulación con Stokes en un cilindro parabólico

Calcule la circulación de $\bar f(x,y,z) = (x^5 + y + 5,\ z + \mathop{\mathrm{sen}}(y^2),\ z^{10} - 3x + 3)$, a lo largo del borde de la superficie S, en el primer octante, definida por $y = 4 - x^2$, $0 \le z \le 4$, indicar la orientación elegida para la superficie

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Rotor.** Con $P = x^5 + y + 5$, $Q = z + \mathop{\mathrm{sen}}(y^2)$, $R = z^{10} - 3x + 3$:

$$\nabla\times\bar f = (R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y) = (0 - 1,\ 0 + 3,\ 0 - 1) = (-1,\ 3,\ -1)$$

**Paso 2 — Parametrización.** $\vec T(x,z) = (x,\ 4 - x^2,\ z)$ con $0 \le x \le 2$ (primer octante: $y \ge 0$), $0 \le z \le 4$.

$\vec T'_x\times\vec T'_z = (1,-2x,0)\times(0,0,1) = (-2x, -1, 0)$. Se elige la opuesta, $\vec n = (2x, 1, 0)$, que apunta hacia afuera del cilindro (lejos del eje $z$).

**Paso 3 — Stokes.**

$$\oint_{\partial S}\bar f\cdot d\bar s = \iint_D(-1, 3, -1)\cdot(2x, 1, 0)\thinspace dx\thinspace dz = \int_0^4\negthinspace\negthinspace\int_0^2(3 - 2x)\thinspace dx\thinspace dz = 4\cdot(6 - 4) = 8$$

**Paso 4 — Sentido del borde.** Con esa normal el borde se recorre $(0,4,0)\to(0,4,4)\to(2,0,4)\to(2,0,0)\to(0,4,0)$.

</details>

**Respuesta:** Con normal $\vec n = (2x, 1, 0)$ (hacia afuera del cilindro), la circulación vale $8$ (con la orientación opuesta, $-8$).

</details>

---

### P4) Área de un tronco de cono

El área de la porción de superficie descripta por $7 - \sqrt{x^2 + y^2} = z$, $4 \le z \le 6$, $x \ge 0, y \ge 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Región en polares.** $z = 7 - r$, así que $4 \le z \le 6 \iff 1 \le r \le 3$. El primer cuadrante es $0 \le \theta \le \frac{\pi}{2}$.

**Paso 2 — Elemento de área.** Para $z = f(x,y)$: $dS = \sqrt{1 + f'^2_x + f'^2_y}\thinspace dA$. En un cono $f'^2_x + f'^2_y = \frac{x^2 + y^2}{x^2 + y^2} = 1$, así que $dS = \sqrt2\thinspace dA$.

**Paso 3 — Calcular.**

$$A = \int_0^{\pi/2}\negthinspace\negthinspace\int_1^3\sqrt2\thinspace r\thinspace dr\thinspace d\theta = \sqrt2\cdot\frac{\pi}{2}\cdot\frac{9 - 1}{2} = 2\sqrt2\thinspace\pi$$

</details>

**Respuesta:** $A = 2\sqrt2\thinspace\pi$.

</details>

---

[Volver al menú principal](../README.md)
