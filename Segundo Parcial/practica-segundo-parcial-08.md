# 2.º Parcial de práctica 08

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Campos de divergencia nula

Enuncie el teorema de la divergencia. Demuestre que si $\mathop{\mathrm{div}}\vec f = 0$ en $\mathbb{R}^3$, el flujo de $\vec f$ a través de una superficie abierta $S$ sólo depende de su borde (siempre que, junto con otra superficie del mismo borde, encierre un sólido).

Utilícelo para calcular el flujo de $\vec f(x,y,z) = (y - z,\ z - x,\ x - y + 1)$ a través de la semiesfera $x^2 + y^2 + z^2 = 4$, $z \ge 0$, orientada hacia arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** sea $V \subset \mathbb{R}^3$ un sólido acotado cuya frontera $\partial V$ es una superficie cerrada, suave a trozos y orientada con normal exterior. Si $\vec f \in C^1$ en un abierto que contiene a $V$:

$$\iint_{\partial V}\vec f\cdot\breve n\thinspace d\sigma = \iiint_V\mathop{\mathrm{div}}\vec f\thinspace dV$$

**Demostración.** Sean $S_1$ y $S_2$ con el mismo borde que encierran el sólido $V$, con $\partial V = S_1 \cup S_2$. Orientando $S_1$ con la normal exterior y $S_2$ con la interior (es decir, ambas "del mismo lado" respecto del borde), Gauss da:

$$\Phi_{S_1} - \Phi_{S_2} = \iiint_V 0\thinspace dV = 0 \Rightarrow \Phi_{S_1} = \Phi_{S_2} \quad\blacksquare$$

**Aplicación.**

*Divergencia:* $\mathop{\mathrm{div}}\vec f = 0 + 0 + 0 = 0$ ✓.

*Superficie alternativa:* el disco $D$: $z = 0$, $x^2 + y^2 \le 4$, con normal $\breve k$ (hacia arriba, como la semiesfera).

*Flujo por el disco:* $\vec f\cdot\breve k = x - y + 1$:

$$\Phi = \iint_D(x - y + 1)\thinspace dA = 0 - 0 + 4\pi = 4\pi$$

($x$ e $y$ integran $0$ por simetría).

</details>

**Respuesta:** $4\pi$.

</details>

---

### T2) Ecuación a partir de dos soluciones

- a) Sabiendo que $y_1 = e^x$ e $y_2 = e^{-3x}$ son soluciones de $y'' + ay' + by = 0$, halle $a$ y $b$.
- b) Resuelva $y'' + ay' + by = 6$ con $y(0) = 0$ e $y'(0) = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** Las raíces de la ecuación característica son $1$ y $-3$:

$$(r - 1)(r + 3) = r^2 + 2r - 3 \Rightarrow a = 2,\ b = -3$$

**b)**

- *Homogénea:* $y_H = C_1e^x + C_2e^{-3x}$.
- *Particular:* $y_P = A$ ⇒ $-3A = 6 \Rightarrow A = -2$.

*Condiciones* con $y = C_1e^x + C_2e^{-3x} - 2$:

- $y(0) = C_1 + C_2 - 2 = 0$.
- $y'(0) = C_1 - 3C_2 = 0$.

Entonces $C_1 = 3C_2$ y $4C_2 = 2$: $C_2 = \tfrac12$, $C_1 = \tfrac32$.

</details>

**Respuesta:**

- a) $a = 2$, $b = -3$.
- b) $y = \dfrac32e^x + \dfrac12e^{-3x} - 2$.

</details>

---

## Ejercicios prácticos

### P1) Masa de un sólido

Calcule la masa del sólido limitado por el paraboloide $z = 4 - x^2 - y^2$ y el plano $z = 0$, si su densidad en cada punto es igual a la distancia del punto al plano $xy$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Densidad.** $\delta = z$ (en el sólido, $z \ge 0$).

**Paso 2 — Cilíndricas.** $0 \le z \le 4 - r^2$, $0 \le r \le 2$:

$$M = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2\negthinspace\int_0^{4-r^2}z\thinspace r\thinspace dz\thinspace dr\thinspace d\theta = 2\pi\int_0^2\frac{(4 - r^2)^2}{2}\thinspace r\thinspace dr$$

**Paso 3 — Sustitución** $u = 4 - r^2$, $du = -2r\thinspace dr$:

$$M = 2\pi\cdot\frac14\int_0^4 u^2\thinspace du = \frac{\pi}{2}\cdot\frac{64}{3} = \frac{32\pi}{3}$$

</details>

**Respuesta:** $M = \dfrac{32\pi}{3}$.

</details>

---

### P2) Área de un trozo de cono

Calcule el área de la porción del cono $z = \sqrt{x^2 + y^2}$ interior al cilindro $x^2 + y^2 = 2x$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Elemento de área.** Para el cono, $d\sigma = \sqrt{1 + \dfrac{x^2}{z^2} + \dfrac{y^2}{z^2}}\thinspace dA = \sqrt2\thinspace dA$.

**Paso 2 — Proyección.** $x^2 + y^2 \le 2x \iff (x - 1)^2 + y^2 \le 1$: disco de radio 1, área $\pi$.

**Paso 3 — Resultado.** $A = \sqrt2\cdot\pi$.

</details>

**Respuesta:** $A = \sqrt2\thinspace\pi$.

</details>

---

### P3) Circulación sobre un triángulo con Stokes

Calcule la circulación de $\vec f(x,y,z) = (z^2,\ x^2,\ y^2)$ a lo largo del borde del triángulo de vértices $(2,0,0)$, $(0,2,0)$ y $(0,0,2)$, recorrido en ese orden.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Rotor.** $\mathop{\mathrm{rot}}\vec f = (2y,\ 2z,\ 2x)$.

**Paso 2 — Superficie y orientación.** El triángulo está en el plano $x + y + z = 2$. Con $\bar A = (2,0,0)$, $\bar B = (0,2,0)$, $\bar C = (0,0,2)$:

$$(\bar B - \bar A)\times(\bar C - \bar A) = (-2,2,0)\times(-2,0,2) = (4,\ 4,\ 4)$$

La normal compatible con el recorrido es $\vec N = (1,1,1)$, usando $\vec T(x,y) = (x,\ y,\ 2 - x - y)$ sobre el triángulo $D$ de catetos 2.

**Paso 3 — Stokes.**

$$\oint\vec f\cdot d\vec s = \iint_D(2y + 2z + 2x)\thinspace dA = \iint_D 2(x + y + z)\thinspace dA = \iint_D 4\thinspace dA = 4\cdot2 = 8$$

(sobre el plano, $x + y + z = 2$, y el área de $D$ es $2$).

</details>

**Respuesta:** $8$.

</details>

---

### P4) Masa de una chapa semicircular

Calcule la masa de la chapa $D: 1 \le x^2 + y^2 \le 4$, $y \ge 0$, si su densidad es $\delta(x,y) = \dfrac{y}{x^2 + y^2}$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Polares.** $1 \le r \le 2$, $0 \le \theta \le \pi$. $\delta = \dfrac{r\mathop{\mathrm{sen}}\theta}{r^2} = \dfrac{\mathop{\mathrm{sen}}\theta}{r}$.

**Paso 2 — Integral.**

$$M = \int_0^{\pi}\negthinspace\int_1^2\frac{\mathop{\mathrm{sen}}\theta}{r}\thinspace r\thinspace dr\thinspace d\theta = \int_0^{\pi}\mathop{\mathrm{sen}}\theta\thinspace d\theta\cdot\int_1^2 dr = 2\cdot1 = 2$$

</details>

**Respuesta:** $M = 2$.

</details>

---

[← Anterior](practica-segundo-parcial-07.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-09.md)
