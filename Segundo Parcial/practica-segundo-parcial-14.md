# 2.º Parcial de práctica 14

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Campo de gradientes exponencial

Defina campo de gradientes. Muestre que $\vec f(x,y,z) = \left(yz\thinspace e^{xyz},\ xz\thinspace e^{xyz},\ xy\thinspace e^{xyz}\right)$ lo es y calcule su circulación desde $(0,0,0)$ hasta $(1,1,\ln2)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Definición:** $\vec f$ es un **campo de gradientes** (conservativo) en un abierto $D$ si existe $\phi: D \to \mathbb{R}$ diferenciable tal que $\nabla\phi = \vec f$ en $D$.

**Paso 1 — Potencial.** Con $\phi = e^{xyz}$, por la regla de la cadena:

$$\nabla\phi = \left(yz\thinspace e^{xyz},\ xz\thinspace e^{xyz},\ xy\thinspace e^{xyz}\right) = \vec f$$

**Paso 2 — Circulación.** Por cualquier camino:

$$\phi(1,1,\ln2) - \phi(0,0,0) = e^{\ln2} - e^0 = 2 - 1 = 1$$

</details>

**Respuesta:** $\phi = e^{xyz}$; la circulación vale $1$.

</details>

---

### T2) Gauss en un cilindro

Enuncie el teorema de la divergencia y utilícelo para calcular el flujo saliente de $\vec f(x,y,z) = (x + yz,\ y - xz,\ z)$ a través de la frontera del cilindro $x^2 + y^2 \le 1$, $0 \le z \le 1$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** sea $V \subset \mathbb{R}^3$ un sólido acotado cuya frontera $\partial V$ es una superficie cerrada, suave a trozos y orientada con normal exterior. Si $\vec f \in C^1$ en un abierto que contiene a $V$:

$$\iint_{\partial V}\vec f\cdot\breve n\thinspace d\sigma = \iiint_V\mathop{\mathrm{div}}\vec f\thinspace dV$$

**Paso 1 — Divergencia.** $\mathop{\mathrm{div}}\vec f = 1 + 1 + 1 = 3$ (los términos $yz$ y $-xz$ no dependen de la variable que se deriva).

**Paso 2 — Volumen.** $\pi\cdot1^2\cdot1 = \pi$.

**Paso 3 — Resultado.** $\Phi = 3\pi$.

</details>

**Respuesta:** $3\pi$.

</details>

---

## Ejercicios prácticos

### P1) Circulación sobre una elipse inclinada

Calcule la circulación de $\vec f(x,y,z) = (z,\ x,\ y)$ a lo largo de la curva intersección del cilindro $x^2 + y^2 = 1$ con el plano $z = x + y + 2$, recorrida en sentido antihorario vista desde arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Rotor.** $\mathop{\mathrm{rot}}\vec f = (1,\ 1,\ 1)$.

**Paso 2 — Superficie.** $z = x + y + 2$ sobre el disco $x^2 + y^2 \le 1$, con normal hacia arriba $\vec N = (-z'_x,\ -z'_y,\ 1) = (-1,\ -1,\ 1)$.

**Paso 3 — Stokes.**

$$\oint_C\vec f\cdot d\vec s = \iint_D(1,1,1)\cdot(-1,-1,1)\thinspace dA = \iint_D(-1)\thinspace dA = -\pi$$

</details>

**Respuesta:** $-\pi$.

</details>

---

### P2) Área de un helicoide

Calcule el área de la superficie $\vec X(u,v) = (u\cos v,\ u\mathop{\mathrm{sen}}v,\ v)$, con $0 \le u \le 1$ y $0 \le v \le 2\pi$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Vector normal.**

$$\vec X'_u = (\cos v,\ \mathop{\mathrm{sen}}v,\ 0),\qquad \vec X'_v = (-u\mathop{\mathrm{sen}}v,\ u\cos v,\ 1)$$

$$\vec X'_u\times\vec X'_v = (\mathop{\mathrm{sen}}v,\ -\cos v,\ u) \Rightarrow \Vert\vec X'_u\times\vec X'_v\Vert = \sqrt{1 + u^2}$$

**Paso 2 — Integral.**

$$A = \int_0^{2\pi}\negthinspace\negthinspace\int_0^1\sqrt{1 + u^2}\thinspace du\thinspace dv = 2\pi\left[\frac{u\sqrt{1 + u^2}}{2} + \frac{\ln\left(u + \sqrt{1 + u^2}\right)}{2}\right]_0^1$$

$$= \pi\left(\sqrt2 + \ln(1 + \sqrt2)\right)$$

</details>

**Respuesta:** $A = \pi\left(\sqrt2 + \ln(1 + \sqrt2)\right) \approx 7{,}21$.

</details>

---

### P3) Masa con cambio en el orden de integración

Calcule la masa de la chapa triangular $D: 0 \le x \le y \le 1$ cuya densidad es $\delta(x,y) = e^{y^2}$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Elegir el orden.** $e^{y^2}$ no tiene primitiva elemental en $y$, así que conviene integrar primero en $x$: para cada $y\in[0,1]$, $0 \le x \le y$.

**Paso 2 — Integral.**

$$M = \int_0^1\negthinspace\int_0^y e^{y^2}\thinspace dx\thinspace dy = \int_0^1 y\thinspace e^{y^2}\thinspace dy = \left[\frac{e^{y^2}}{2}\right]_0^1 = \frac{e - 1}{2}$$

</details>

**Respuesta:** $M = \dfrac{e - 1}{2}$.

</details>

---

### P4) Divergencia nula y flujo

Sea $g: \mathbb{R} \to \mathbb{R}$ una función $C^2$ y $\vec f(x,y,z) = \left(g'(x),\ y\thinspace g(x),\ 5 - 2xz\right)$.

- a) Halle $g$ tal que $\mathop{\mathrm{div}}\vec f = 0$ y $\vec f(0,1,0) = (3,\ 1,\ 5)$.
- b) Calcule el flujo de $\vec f$ a través de la semiesfera $x^2 + y^2 + z^2 = 1$, $z \ge 0$, orientada hacia arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)**

*Ecuación:* $\mathop{\mathrm{div}}\vec f = g'' + g - 2x = 0 \iff g'' + g = 2x$.

*Condiciones:* $g'(0) = 3$, $g(0) = 1$.

*Solución:* $g_H = C_1\cos x + C_2\mathop{\mathrm{sen}}x$, $g_P = 2x$.

- $g(0) = C_1 = 1$.
- $g'(0) = C_2 + 2 = 3 \Rightarrow C_2 = 1$.

**b)** *Cerrar con la tapa* $T$: $z = 0$, $x^2 + y^2 \le 1$, normal $(0,0,-1)$. Como $\mathop{\mathrm{div}}\vec f = 0$, $\Phi_S + \Phi_T = 0$.

*Tapa:* $\vec f\cdot(0,0,-1) = -(5 - 2xz) = -5$ en $z = 0$ ⇒ $\Phi_T = -5\pi$.

*Resultado:* $\Phi_S = 5\pi$.

</details>

**Respuesta:**

- a) $g(x) = \cos x + \mathop{\mathrm{sen}}x + 2x$.
- b) $5\pi$.

</details>

---

[← Anterior](practica-segundo-parcial-13.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-15.md)
