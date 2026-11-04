# 2.º Parcial (15/11/2022) — Curso Z2004, Tema 1

Análisis Matemático II — UTN-FRBA.

Enunciado (foto, sin resolución oficial): [Parcial2-2022-11-15-Z2004-Tema1.jpeg](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-2022-11-15-Z2004-Tema1.jpeg).

Las resoluciones son propias (no hay solución de la cátedra). Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Parte práctica

### P1) Área de un paraboloide por encima de otro

Calcular el área de la porción de superficie $z = 5 - x^2 - y^2$ con $z \ge 2 - \frac14(x^2 + y^2)$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Proyección.** $5 - r^2 \ge 2 - \frac{r^2}{4} \iff 3 \ge \frac34 r^2 \iff r \le 2$.

**Paso 2 — Elemento de área.** $dS = \sqrt{1 + 4x^2 + 4y^2}\thinspace dA = \sqrt{1 + 4r^2}\thinspace r\thinspace dr\thinspace d\theta$.

**Paso 3 — Calcular** ($u = 1 + 4r^2$):

$$A = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2\sqrt{1 + 4r^2}\thinspace r\thinspace dr\thinspace d\theta = 2\pi\cdot\frac{1}{12}\left[(1 + 4r^2)^{3/2}\right]_0^2 = \frac{\pi}{6}\left(17\sqrt{17} - 1\right)$$

</details>

**Respuesta:** $A = \dfrac{\pi}{6}\left(17\sqrt{17} - 1\right) \approx 36{,}18$.

</details>

---

### P2) Circulación con Green en un triángulo

Calcule la circulación de $\bar f(x,y) = (2xe^y - 1;\ x^2e^y + yx)$ a lo largo de la curva frontera de la región plana definida por $x + y \ge 4$; $x + 2y \le 8$ ; $y \ge 0$, recorrida en sentido positivo.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Región.** Para cada $y \ge 0$: $4 - y \le x \le 8 - 2y$, posible si $y \le 4$. Es el triángulo de vértices $(4,0)$, $(8,0)$ y $(0,4)$.

**Paso 2 — Green.**

$$Q'_x - P'_y = (2xe^y + y) - 2xe^y = y$$

**Paso 3 — Calcular.**

$$\oint_C\bar f\cdot d\bar s = \int_0^4\negthinspace\negthinspace\int_{4 - y}^{8 - 2y}y\thinspace dx\thinspace dy = \int_0^4 y(4 - y)\thinspace dy = 32 - \frac{64}{3} = \frac{32}{3}$$

</details>

**Respuesta:** $\dfrac{32}{3}$.

</details>

---

### P3) Circulación de un campo conservativo

Sea $\bar f(x,y) = (-3x^2\cos(y) + 2x;\ x^3\mathop{\mathrm{sen}}(y) - 4)$, calcule la circulación de $\bar f$ a lo largo de la curva $\bar\gamma(t) = (t\mathop{\mathrm{sen}}(\pi t);\ 1 - 2t^2)$ con $0 \le t \le 1$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Simetría.** $P'_y = 3x^2\mathop{\mathrm{sen}}y = Q'_x$ en $\mathbb{R}^2$ ⇒ conservativo.

**Paso 2 — Potencial.**

- $\varphi = \int(-3x^2\cos y + 2x)\thinspace dx = -x^3\cos y + x^2 + D(y)$.
- $\varphi'_y = x^3\mathop{\mathrm{sen}}y + D'(y) = x^3\mathop{\mathrm{sen}}y - 4 \Rightarrow D = -4y$.

**Paso 3 — Extremos.** $\bar\gamma(0) = (0, 1)$, $\bar\gamma(1) = (\mathop{\mathrm{sen}}\pi,\ -1) = (0, -1)$.

**Paso 4 — Circulación.** $\varphi(0,-1) - \varphi(0,1) = 4 - (-4) = 8$.

</details>

**Respuesta:** $8$ (potencial $\varphi = -x^3\cos y + x^2 - 4y$).

</details>

---

### P4) Flujo saliente de un sector de cono

Dado $\bar f(x,y,z) = (\varphi(z,y);\ y + 1;\ \varphi(y,x))$ con $\bar f \in C^1(R^3)$ calcule el flujo de $\bar f$ a través de la superficie frontera del sólido H definido por $z \ge \sqrt{x^2 + y^2}$; $0 \le y \le x$; $z \le 4$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Divergencia.** La primera componente no depende de $x$ y la tercera no depende de $z$:

$$\operatorname{div}\bar f = 0 + 1 + 0 = 1$$

**Paso 2 — Gauss.** La frontera es cerrada; con normal exterior el flujo es el volumen de $H$.

**Paso 3 — Región.** $0 \le y \le x$ es el sector $0 \le \theta \le \frac{\pi}{4}$. En cilíndricas: $r \le z \le 4$, $0 \le r \le 4$.

$$V = \int_0^{\pi/4}\negthinspace\negthinspace\int_0^4(4 - r)\thinspace r\thinspace dr\thinspace d\theta = \frac{\pi}{4}\left(32 - \frac{64}{3}\right) = \frac{8\pi}{3}$$

</details>

**Respuesta:** Con normal exterior, $\Phi = \dfrac{8\pi}{3}$.

</details>

---

## Parte teórica

### T1) Coordenadas polares

Defina coordenadas polares. Calcule $\iint_D\frac{x + 2y}{x^2 + y^2}\thinspace dA$ utilizando coordenadas polares, sabiendo que D es la región del plano xy definida por: $y \ge |x|,\ x + 2y \le 4$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Definición:** las coordenadas polares de un punto $(x,y) \ne (0,0)$ son $(r,\theta)$, con $r > 0$ la distancia al origen y $\theta$ el ángulo con el semieje $x$ positivo. La transformación es

$$x = r\cos\theta, \quad y = r\mathop{\mathrm{sen}}\theta, \qquad \left|\frac{\partial(x,y)}{\partial(r,\theta)}\right| = r$$

y $\iint_D f(x,y)\thinspace dx\thinspace dy = \iint_{D'} f(r\cos\theta, r\mathop{\mathrm{sen}}\theta)\thinspace r\thinspace dr\thinspace d\theta$.

**Paso 1 — Región.** $y \ge |x| \iff \frac{\pi}{4} \le \theta \le \frac{3\pi}{4}$. La recta $x + 2y = 4$ es $r(\cos\theta + 2\mathop{\mathrm{sen}}\theta) = 4$, así que $0 \le r \le \dfrac{4}{\cos\theta + 2\mathop{\mathrm{sen}}\theta}$ (el denominador es positivo en ese rango).

**Paso 2 — Integrando.**

$$\frac{x + 2y}{x^2 + y^2}\cdot r = \frac{r(\cos\theta + 2\mathop{\mathrm{sen}}\theta)}{r^2}\cdot r = \cos\theta + 2\mathop{\mathrm{sen}}\theta$$

**Paso 3 — Calcular.**

$$\int_{\pi/4}^{3\pi/4}\negthinspace\negthinspace\int_0^{4/(\cos\theta + 2\mathop{\mathrm{sen}}\theta)}(\cos\theta + 2\mathop{\mathrm{sen}}\theta)\thinspace dr\thinspace d\theta = \int_{\pi/4}^{3\pi/4}4\thinspace d\theta = 2\pi$$

</details>

**Respuesta:** $\displaystyle\iint_D\frac{x + 2y}{x^2 + y^2}\thinspace dA = 2\pi$.

</details>

---

### T2) EDO desde sus soluciones y recta tangente

a. Halle la ecuación diferencial homogénea $y^{(n)} + a_{n-1}y^{(n-1)} + \dots + a_1y' + a_0y = 0$ de menor orden posible que tenga como soluciones a $e^x$; $x$; $e^{-x}$

b. Halle la solución de $y'' - y' = xe^x$ que en (0,2) posee recta tangente de ecuación $y = x + 2$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a) Paso 1 — Raíces.** $e^x \to r = 1$; $e^{-x} \to r = -1$; $x = x\cdot e^{0x}$ exige que $r = 0$ sea raíz **doble** (también aparece la solución $1$).

**Paso 2 — Polinomio característico.**

$$(r - 1)(r + 1)\thinspace r^2 = r^4 - r^2$$

Orden mínimo 4: $y^{(4)} - y'' = 0$.

**b) Paso 1 — Homogénea.** $r^2 - r = 0 \Rightarrow r = 0, 1$: $y_h = C_1 + C_2e^x$.

**Paso 2 — Particular.** $r = 1$ es raíz simple ⇒ $y_p = x(Ax + B)e^x = (Ax^2 + Bx)e^x$.

- $y_p' = (Ax^2 + (2A + B)x + B)e^x$.
- $y_p'' = (Ax^2 + (4A + B)x + 2A + 2B)e^x$.
- $y_p'' - y_p' = (2Ax + 2A + B)e^x = xe^x \Rightarrow A = \frac12$, $B = -1$.

**Paso 3 — Condiciones.** $y(0) = 2$, $y'(0) = 1$ (pendiente de la tangente).

- $y = C_1 + C_2e^x + \left(\frac{x^2}{2} - x\right)e^x \Rightarrow y(0) = C_1 + C_2 = 2$.
- $y' = C_2e^x + \left(\frac{x^2}{2} - 1\right)e^x \Rightarrow y'(0) = C_2 - 1 = 1 \Rightarrow C_2 = 2$, $C_1 = 0$.

</details>

**Respuesta:** a) $y^{(4)} - y'' = 0$. b) $y = 2e^x + \left(\dfrac{x^2}{2} - x\right)e^x$.

</details>

---

[Volver al menú principal](../README.md)
