# 2.º Parcial (27/11/2020) — Curso Z2051

Análisis Matemático II — UTN-FRBA. Segundo cuatrimestre de 2020.

Enunciado (foto, sin resolución oficial): [Parcial2-2020-11-27-Z2051.jpeg](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-2020-11-27-Z2051.jpeg).

Las resoluciones son propias (no hay solución de la cátedra). Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios

### P1) Campo conservativo con una función incógnita

Sea $\bar f(x,y) = (yg''(x) + x^2 - x;\ \cos(y) + g(x) + x)$, con $g \in C^1$. Halle g tal que $g(0) = 1$ ; $g'(0) = 0$; y $\bar f$ resulte conservativo. Para la función g hallada calcular la circulación del campo $\bar f$ a lo largo de la curva parametrizada por $\bar\alpha: [0,2\pi] \to R^2:\ \bar\alpha(t) = (t.\cos(t) - \pi;\ t^3.\mathop{\mathrm{sen}}(2t))$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

> Para que aparezca $g''$ en el campo hace falta $g \in C^2$ (y $C^3$ para que $P \in C^1$); se supone así.

**Paso 1 — Condición de simetría.** En $\mathbb{R}^2$ (simplemente conexo) $\bar f$ es conservativo si y solo si $P'_y = Q'_x$:

$$P'_y = g''(x), \qquad Q'_x = g'(x) + 1 \quad\Longrightarrow\quad g'' - g' = 1$$

**Paso 2 — Resolver para $g'$.** Llamando $u = g'$: $u' - u = 1 \Rightarrow u = Ce^x - 1$. Con $g'(0) = 0$: $C = 1$, así que $g'(x) = e^x - 1$.

**Paso 3 — Integrar.** $g(x) = e^x - x + D$, y $g(0) = 1 \Rightarrow D = 0$:

$$g(x) = e^x - x, \qquad g''(x) = e^x$$

**Paso 4 — Campo y potencial.** $\bar f = (ye^x + x^2 - x,\ \cos y + e^x)$.

- $\varphi = \int(ye^x + x^2 - x)\thinspace dx = ye^x + \frac{x^3}{3} - \frac{x^2}{2} + D(y)$.
- $\varphi'_y = e^x + D'(y) = \cos y + e^x \Rightarrow D(y) = \mathop{\mathrm{sen}}y$.

$$\varphi(x,y) = ye^x + \frac{x^3}{3} - \frac{x^2}{2} + \mathop{\mathrm{sen}}y$$

**Paso 5 — Extremos de la curva.** $\bar\alpha(0) = (-\pi, 0)$ y $\bar\alpha(2\pi) = (2\pi - \pi,\ 8\pi^3\mathop{\mathrm{sen}}(4\pi)) = (\pi, 0)$.

**Paso 6 — Circulación.**

$$\int_C\bar f\cdot d\bar s = \varphi(\pi,0) - \varphi(-\pi,0) = \left(\frac{\pi^3}{3} - \frac{\pi^2}{2}\right) - \left(-\frac{\pi^3}{3} - \frac{\pi^2}{2}\right) = \frac{2\pi^3}{3}$$

</details>

**Respuesta:** $g(x) = e^x - x$; la circulación vale $\dfrac{2\pi^3}{3}$.

</details>

---

### P2) Volumen entre cono y paraboloide, y flujo con Gauss

a) Determine el volumen del sólido H definido por $z \le 20 - x^2 - y^2$; $z \ge \sqrt{x^2 + y^2}$

b) Sea h: R → R una función $C^1$, calcule el flujo de $\bar f(x,y,z) = (-3x^2;\ 3xy^2;\ z + \mu(x))$ a través de la superficie S frontera del sólido H. Indicar la orientación elegida para S

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

> El enunciado presenta $h$ pero el campo usa $\mu(x)$; se entiende que es la misma función $C^1$.

**a) Paso 1 — Intersección.** En cilíndricas: $20 - r^2 = r \Rightarrow r^2 + r - 20 = 0 \Rightarrow r = 4$.

**Paso 2 — Volumen.**

$$V = \int_0^{2\pi}\negthinspace\negthinspace\int_0^4(20 - r^2 - r)\thinspace r\thinspace dr\thinspace d\theta = 2\pi\left(10\cdot16 - \frac{256}{4} - \frac{64}{3}\right) = 2\pi\cdot\frac{224}{3} = \frac{448\pi}{3}$$

**b) Paso 1 — Divergencia.**

$$\operatorname{div}\bar f = -6x + 6xy + 1$$

($\mu(x)$ no depende de $z$.)

**Paso 2 — Gauss con normal exterior.**

$$\Phi = \iiint_H(-6x + 6xy + 1)\thinspace dV$$

**Paso 3 — Simetría.** $H$ es simétrico respecto del plano $x = 0$ ($x \to -x$), y $-6x$ y $6xy$ son impares en $x$: sus integrales se anulan. Queda

$$\Phi = \iiint_H dV = \frac{448\pi}{3}$$

</details>

**Respuesta:** a) $V = \dfrac{448\pi}{3}$. b) Con normal exterior, $\Phi = \dfrac{448\pi}{3}$.

</details>

---

### P3) Circulación sobre el borde de un paraboloide

Calcule la circulación de $\bar f(x,y,z) = (x^3 - 5 + z,\ xy + \mathop{\mathrm{sen}}(y^2),\ z^5 + 3z - 1)$, a lo largo del borde de la superficie S , definida por $z = 7 - x^2 - y^2$ , 3≤ z. Indicar la orientación elegida para la superficie.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Borde.** $z = 3 \Rightarrow x^2 + y^2 = 4$: circunferencia de radio 2 en el plano $z = 3$.

**Paso 2 — Rotor.**

$$\nabla\times\bar f = (R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y) = (0 - 0,\ 1 - 0,\ y - 0) = (0, 1, y)$$

**Paso 3 — Stokes con otra superficie.** Como el resultado solo depende del borde, se usa el disco $S_1$: $z = 3$, $x^2 + y^2 \le 4$, con normal $(0,0,1)$ (la misma orientación que el paraboloide con normal hacia arriba, que induce el recorrido antihorario visto desde arriba):

$$\oint\bar f\cdot d\bar s = \iint_{S_1}(0,1,y)\cdot(0,0,1)\thinspace dA = \iint_{x^2 + y^2 \le 4} y\thinspace dA = 0$$

por simetría del disco respecto del eje $x$.

</details>

**Respuesta:** Con normal hacia arriba (borde antihorario visto desde $z > 0$), la circulación vale $0$; con la orientación opuesta también es $0$.

</details>

---

### P4) Área de un trozo de paraboloide

Calcule el área de la porción de superficie descripta por $6 - x^2 - y^2 = z$, $2 \le z \le 5$, $x \ge 0, y \ge 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Región.** $r^2 = 6 - z$, así que $2 \le z \le 5 \iff 1 \le r \le 2$, y el primer cuadrante es $0 \le \theta \le \frac{\pi}{2}$.

**Paso 2 — Elemento de área.** $f = 6 - x^2 - y^2$: $dS = \sqrt{1 + 4x^2 + 4y^2}\thinspace dA = \sqrt{1 + 4r^2}\thinspace r\thinspace dr\thinspace d\theta$.

**Paso 3 — Calcular** (sustitución $u = 1 + 4r^2$, $du = 8r\thinspace dr$):

$$A = \frac{\pi}{2}\int_1^2\sqrt{1 + 4r^2}\thinspace r\thinspace dr = \frac{\pi}{2}\cdot\frac{1}{12}\left[(1 + 4r^2)^{3/2}\right]_1^2 = \frac{\pi}{24}\left(17\sqrt{17} - 5\sqrt5\right)$$

</details>

**Respuesta:** $A = \dfrac{\pi}{24}\left(17\sqrt{17} - 5\sqrt5\right) \approx 7{,}71$.

</details>

---

[Volver al menú principal](../README.md)
