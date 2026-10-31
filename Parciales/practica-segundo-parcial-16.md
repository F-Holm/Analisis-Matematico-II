# 2.º Parcial de práctica 16

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Campo conservativo con datos

Sea $\vec f(x,y) = (3x^2 + ay,\ bx + 2y)$ con $\vec f(1,1) = (5,\ 4)$.

- a) Halle $a$ y $b$ y demuestre que $\vec f$ es conservativo, enunciando la condición que utiliza.
- b) Calcule el trabajo de $\vec f$ desde $(0,0)$ hasta $(1,2)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)**

*Datos:* $\vec f(1,1) = (3 + a,\ b + 2) = (5,\ 4)$ ⇒ $a = 2$, $b = 2$.

*Condición:* si $\vec f = (P,Q) \in C^1$ en un abierto **simplemente conexo** y $Q'_x = P'_y$, entonces $\vec f$ es conservativo.

*Verificación:* $P'_y = 2 = Q'_x$ en $\mathbb{R}^2$ ✓.

*Potencial:* $\phi = \int(3x^2 + 2y)\thinspace dx = x^3 + 2xy + D(y)$; $\phi'_y = 2x + D' = 2x + 2y \Rightarrow D = y^2$.

**b)** $W = \phi(1,2) - \phi(0,0) = 1 + 4 + 4 = 9$.

</details>

**Respuesta:**

- a) $a = b = 2$; $\phi = x^3 + 2xy + y^2 + k$.
- b) $W = 9$.

</details>

---

### T2) Flujo de un rotor a través de un paraboloide

Enuncie el teorema de Stokes. Sea $\vec f(x,y,z) = (-y + z,\ x + xz,\ e^z)$. Calcule el flujo de $\mathop{\mathrm{rot}}\vec f$ a través de $S: z = 4 - x^2 - y^2$, $z \ge 0$, orientada hacia arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** sea $S$ una superficie suave a trozos, orientable, cuyo borde $\partial S$ es una curva cerrada, simple y suave a trozos, orientada en forma compatible con la normal de $S$. Si $\vec f \in C^1$ en un abierto que contiene a $S$:

$$\iint_S\mathop{\mathrm{rot}}\vec f\cdot\breve n\thinspace d\sigma = \oint_{\partial S}\vec f\cdot d\vec s$$

**Paso 1 — Borde.** $x^2 + y^2 = 4$, $z = 0$, en sentido antihorario visto desde arriba: $\vec\alpha(t) = (2\cos t,\ 2\mathop{\mathrm{sen}}t,\ 0)$.

**Paso 2 — Circulación.** Con $z = 0$: $\vec f = (-y,\ x,\ 1)$ y $dz = 0$:

$$\oint\vec f\cdot d\vec s = \int_0^{2\pi}(4\mathop{\mathrm{sen}}\nolimits^2t + 4\cos^2t)\thinspace dt = 8\pi$$

</details>

**Respuesta:** $8\pi$.

</details>

---

## Ejercicios prácticos

### P1) Volumen entre un cono y un paraboloide

Calcule el volumen del cuerpo limitado por el cono $z = \sqrt{x^2 + y^2}$ y el paraboloide $z = 6 - x^2 - y^2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Intersección.** $r = 6 - r^2 \Rightarrow r^2 + r - 6 = 0 \Rightarrow r = 2$.

**Paso 2 — Cilíndricas.** $r \le z \le 6 - r^2$, $0 \le r \le 2$:

$$V = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2(6 - r^2 - r)\thinspace r\thinspace dr\thinspace d\theta = 2\pi\left(12 - 4 - \frac83\right) = \frac{32\pi}{3}$$

</details>

**Respuesta:** $V = \dfrac{32\pi}{3}$.

</details>

---

### P2) Flujo a través de una semiesfera con Gauss

Calcule el flujo de $\vec f(x,y,z) = \left(x + e^{yz},\ y + \mathop{\mathrm{sen}}(xz),\ z\right)$ a través de la semiesfera $x^2 + y^2 + z^2 = 1$, $z \ge 0$, orientada hacia afuera.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Cerrar.** Tapa $T$: $z = 0$, $x^2 + y^2 \le 1$, normal $(0,0,-1)$. El cálculo directo sobre la semiesfera es difícil por $e^{yz}$ y $\mathop{\mathrm{sen}}(xz)$.

**Paso 2 — Divergencia.** $\mathop{\mathrm{div}}\vec f = 1 + 1 + 1 = 3$ ⇒ $\iiint 3\thinspace dV = 3\cdot\dfrac{2\pi}{3} = 2\pi$.

**Paso 3 — Tapa.** $\vec f\cdot(0,0,-1) = -z = 0$ en $z = 0$ ⇒ $\Phi_T = 0$.

**Paso 4 — Resultado.** $\Phi_S = 2\pi$.

</details>

**Respuesta:** $2\pi$.

</details>

---

### P3) Oscilador forzado

Resuelva $y'' + 9y = 18$ con $y(0) = 0$ e $y'(0) = 3$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Homogénea.** $r = \pm3i$ ⇒ $y_H = C_1\cos3x + C_2\mathop{\mathrm{sen}}3x$.

**Paso 2 — Particular.** $y_P = A$ ⇒ $9A = 18 \Rightarrow A = 2$.

**Paso 3 — Constantes.**

- $y(0) = C_1 + 2 = 0 \Rightarrow C_1 = -2$.
- $y'(0) = 3C_2 = 3 \Rightarrow C_2 = 1$.

</details>

**Respuesta:** $y = 2 - 2\cos3x + \mathop{\mathrm{sen}}3x$.

</details>

---

### P4) Trabajo a lo largo de una hélice

Calcule la circulación de $\vec f(x,y,z) = (y^2,\ 2xy,\ 3)$ a lo largo de la hélice $\vec\alpha(t) = (\cos t,\ \mathop{\mathrm{sen}}t,\ t)$, $t\in[0,2\pi]$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — ¿Es conservativo?** $\mathop{\mathrm{rot}}\vec f = (0 - 0,\ 0 - 0,\ 2y - 2y) = \vec 0$ en $\mathbb{R}^3$ ⇒ sí.

**Paso 2 — Potencial.** $\phi = xy^2 + 3z$ (verificación: $\nabla\phi = (y^2,\ 2xy,\ 3)$ ✓).

**Paso 3 — Extremos.** $\vec\alpha(0) = (1,0,0)$ y $\vec\alpha(2\pi) = (1,0,2\pi)$:

$$\int_C\vec f\cdot d\vec s = \phi(1,0,2\pi) - \phi(1,0,0) = 6\pi$$

</details>

**Respuesta:** $6\pi$.

</details>

---

[← Anterior](practica-segundo-parcial-15.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-17.md)
