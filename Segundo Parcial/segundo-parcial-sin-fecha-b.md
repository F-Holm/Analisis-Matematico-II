# 2.º Parcial (sin fecha) — B

Análisis Matemático II — UTN-FRBA. Son cuatro recortes de los ejercicios prácticos (P1 a P4) de un mismo examen; no se ven fecha, curso ni parte teórica.

Enunciados (fotos, sin resolución oficial): [P1](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-sin-fecha-B-P1.jpeg), [P2](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-sin-fecha-B-P2.jpeg), [P3](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-sin-fecha-B-P3.jpeg) y [P4](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-sin-fecha-B-P4.jpeg).

Las resoluciones son propias (no hay solución de la cátedra). Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios prácticos

### P1) Circulación con Stokes en un cuarto de cilindro

Sea $\bar f: R^3 \to R^3$ tal que $\bar f(x,y,z) = (e^{x^2} - 2y + 2xy^3z^4;\ 3x^2y^2z^4 + 2x - \mathop{\mathrm{sen}}(y);\ 4x^2y^3z^3 + e^z)$ y sea S la porción de superficie definida por $x^2 + z^2 = 1,\ 0 \le y \le 2,\ 0 \le x,\ 0 \le z$ con C su curva borde. Determinar la circulación del campo $\bar f$ lo largo de la curva C, indicando claramente el sentido de circulación adoptado.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Separar la parte conservativa.**

$$\bar f = \nabla\left(x^2y^3z^4 + \int_0^x e^{u^2}du + \cos y + e^z\right) + (-2y,\ 2x,\ 0)$$

La parte gradiente no aporta sobre una curva cerrada.

**Paso 2 — Rotor.** $\nabla\times\bar f = \nabla\times(-2y, 2x, 0) = (0,\ 0,\ 2 + 2) = (0, 0, 4)$.

**Paso 3 — Parametrización.** $\vec T(u,y) = (\cos u,\ y,\ \mathop{\mathrm{sen}}u)$, $0 \le u \le \frac{\pi}{2}$, $0 \le y \le 2$. Se elige la normal exterior (alejándose del eje $y$): $\vec n = (\cos u,\ 0,\ \mathop{\mathrm{sen}}u)$, con $\Vert\vec T'_u\wedge\vec T'_y\Vert = 1$.

**Paso 4 — Stokes.**

$$\oint_C\bar f\cdot d\bar s = \int_0^2\negthinspace\negthinspace\int_0^{\pi/2}(0,0,4)\cdot(\cos u, 0, \mathop{\mathrm{sen}}u)\thinspace du\thinspace dy = \int_0^2\negthinspace\negthinspace\int_0^{\pi/2}4\mathop{\mathrm{sen}}u\thinspace du\thinspace dy = 8$$

**Paso 5 — Sentido del borde.** Con la normal exterior el borde se recorre $(1,0,0)\to(1,2,0)\to(0,2,1)\to(0,0,1)\to(1,0,0)$ (los arcos sobre $y = 2$ e $y = 0$ son cuartos de circunferencia).

</details>

**Respuesta:** Recorriendo $(1,0,0)\to(1,2,0)\to(0,2,1)\to(0,0,1)\to(1,0,0)$ (normal exterior del cilindro), la circulación vale $8$; en sentido contrario, $-8$.

</details>

---

### P2) Flujo saliente con Gauss

Calcular el flujo del campo vectorial $\bar f(x,y,z) = (2x - z\cos(y^2);\ -2y + x^5z^3;\ e^{xy} - xz)$ a través de la frontera del macizo M definido por : $x + z \le 9;\ y + z \le 9;\ x \ge 0;\ y \ge 0;\ z \ge 0$

Indicar la orientación elegida para la superficie.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Divergencia.**

$$\operatorname{div}\bar f = 2 - 2 - x = -x$$

**Paso 2 — Gauss** (normal exterior): $\Phi = -\iiint_M x\thinspace dV$.

**Paso 3 — Región.** Para cada $z \in [0, 9]$: $0 \le x \le 9 - z$ y $0 \le y \le 9 - z$ (un cuadrado).

**Paso 4 — Calcular.**

$$\iiint_M x\thinspace dV = \int_0^9\left(\int_0^{9 - z}x\thinspace dx\right)\left(\int_0^{9 - z}dy\right)dz = \int_0^9\frac{(9 - z)^3}{2}\thinspace dz = \frac{9^4}{8} = \frac{6561}{8}$$

</details>

**Respuesta:** Con normal exterior, $\Phi = -\dfrac{6561}{8}$.

</details>

---

### P3) Área encerrada por una línea de campo

Determinar, usando integrales dobles, el área de la región limitada por la curva de la familia de líneas de campo de $\bar f(x,y) = \left(\frac{y}{x^2 + y^2};\ \frac{-9x}{x^2 + y^2}\right)$ que pasa por (1,0).

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Líneas de campo.** $\frac{dy}{dx} = \frac{Q}{P} = \frac{-9x}{y}$ (el denominador común se cancela):

$$y\thinspace dy = -9x\thinspace dx \Rightarrow \frac{y^2}{2} = -\frac{9x^2}{2} + C \Rightarrow 9x^2 + y^2 = K$$

**Paso 2 — Por $(1,0)$.** $K = 9$: la elipse $x^2 + \frac{y^2}{9} = 1$.

**Paso 3 — Área con integral doble.** Cambio a polares "elípticas": $x = r\cos\theta$, $y = 3r\mathop{\mathrm{sen}}\theta$, jacobiano $3r$, con $0 \le r \le 1$, $0 \le \theta \le 2\pi$:

$$A = \int_0^{2\pi}\negthinspace\negthinspace\int_0^1 3r\thinspace dr\thinspace d\theta = 3\pi$$

</details>

**Respuesta:** La línea de campo es $9x^2 + y^2 = 9$ y el área encerrada es $3\pi$.

</details>

---

### P4) Área de un trozo de plano

Calcular el área de la porción de plano definida por $x^2 + y^2 \le 3;\ 0 \le z = 6 - y - x$ ; $x \ge 0; y \ge 0$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Región.** En el disco de radio $\sqrt3$, $x + y \le \sqrt6 < 6$, así que $z \ge 0$ se cumple siempre. Queda el cuarto de disco del primer cuadrante.

**Paso 2 — Elemento de área.** $z = 6 - x - y$: $dS = \sqrt{1 + 1 + 1}\thinspace dA = \sqrt3\thinspace dA$.

**Paso 3 — Calcular.** $A = \sqrt3\cdot\frac{\pi\cdot 3}{4} = \frac{3\sqrt3}{4}\pi$.

</details>

**Respuesta:** $A = \dfrac{3\sqrt3}{4}\pi$.

</details>

---

[Volver al menú principal](../README.md)
