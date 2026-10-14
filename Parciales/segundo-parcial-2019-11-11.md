# 2.º Parcial (11/11/2019) — Curso semipresencial

Análisis Matemático II — UTN-FRBA. Segundo cuatrimestre de 2019.

Enunciado y resolución de la cátedra: [Parcial2-2019-11-11-Resuelto.pdf](../aula-virtual/Parciales/Segundo-Parcial/Parcial2-2019-11-11-Resuelto.pdf).

> Para aprobar los TP, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Campo conservativo y función potencial

Defina campo vectorial conservativo y función potencial.

Determine si el campo $\vec f(x,y) = (2xy + \cos(x),\ x^2 + 3y^2)$ es conservativo y en caso afirmativo encuentre una función potencial.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Definiciones:**

- $\vec f$ es **conservativo** (campo de gradientes) en un abierto $D$ si existe $\varphi: D \to \mathbb{R}$ diferenciable con $\nabla\varphi = \vec f$ en $D$.
- $\varphi$ es una **función potencial** de $\vec f$.

**Paso 1 — Simetría.** $P'_y = 2x$ y $Q'_x = 2x$ ✓. Como el dominio es $\mathbb{R}^2$, simplemente conexo, $\vec f$ es conservativo.

**Paso 2 — Potencial.**

- $\varphi = \int(2xy + \cos x)\,dx = x^2y + \operatorname{sen}x + D(y)$.
- $\varphi'_y = x^2 + D'(y) = x^2 + 3y^2 \Rightarrow D' = 3y^2 \Rightarrow D = y^3 + k$.

</details>

**Respuesta:** Es conservativo; $\varphi(x,y) = x^2y + \operatorname{sen}(x) + y^3 + k$.

</details>

---

### T2) Teorema de Green y área

Enuncie el teorema de Green y utilícelo, con un campo vectorial conveniente, para calcular el área de la región encerrada por la curva simple cerrada parametrizada por $\vec\alpha(t) = (t^3 - 4t,\ 16 - t^4)$, $-2 \le t \le 2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** si $D$ es una región acotada cuya frontera $C$ es una curva cerrada, simple, suave a trozos y orientada positivamente, y $\vec f = (P,Q) \in C^1$ en un abierto que contiene a $D$, entonces:

$$\oint_C P\,dx + Q\,dy = \iint_D(Q'_x - P'_y)\,dx\,dy$$

**Paso 1 — Campo conveniente.** $\vec f = (0, x)$ ⇒ $Q'_x - P'_y = 1$ ⇒ $\oint_C\vec f\cdot d\vec s = \text{Área}(D)$.

**Paso 2 — Integral de línea.** $\vec\alpha'(t) = (3t^2 - 4,\ -4t^3)$:

$$\oint\vec f\cdot d\vec s = \int_{-2}^2(0,\ t^3 - 4t)\cdot(3t^2 - 4,\ -4t^3)\,dt = \int_{-2}^2(-4t^6 + 16t^4)\,dt$$

**Paso 3 — Calcular** (el integrando es par):

$$= 2\left[-\frac{4t^7}{7} + \frac{16t^5}{5}\right]_0^2 = 2\left(-\frac{512}{7} + \frac{512}{5}\right) = 1024\cdot\frac{2}{35} = \frac{2048}{35}$$

El resultado es positivo, así que la parametrización recorre $C$ en sentido positivo.

</details>

**Respuesta:** $\text{Área}(D) = \dfrac{2048}{35}$.

</details>

---

## Ejercicios prácticos

### P1) Masa de una chapa

Calcule la masa de una chapa con forma de la **superficie** definida por $S: z = x^2 + y^2$, $1 \le z \le 4$, sabiendo que la función densidad es $\delta(x,y,z) = \dfrac{z}{\sqrt{1 + 4x^2 + 4y^2}}$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $\vec T(u,v) = (u,\ v,\ u^2 + v^2)$, con $D: 1 \le u^2 + v^2 \le 4$ y $\vec T'_u\wedge\vec T'_v = (-2u, -2v, 1)$, cuya norma es $\sqrt{1 + 4u^2 + 4v^2}$.

**Paso 2 — Integrando.** La raíz de la densidad se cancela con la del elemento de área:

$$M = \iint_D\frac{u^2 + v^2}{\sqrt{1 + 4u^2 + 4v^2}}\sqrt{1 + 4u^2 + 4v^2}\,du\,dv = \iint_D(u^2 + v^2)\,du\,dv$$

**Paso 3 — Polares.**

$$M = \int_0^{2\pi}\!\!\int_1^2 r^2\cdot r\,dr\,d\theta = 2\pi\,\frac{16 - 1}{4} = \frac{15\pi}{2}$$

</details>

**Respuesta:** $M = \dfrac{15\pi}{2}$.

</details>

---

### P2) Circulación con Stokes

Sea $g: \mathbb{R} \to \mathbb{R}$ una función $C^1$. Calcule la circulación de

$$\vec f(x,y,z) = \left(y^2 + g(x),\ y + g(y),\ x + z\right)$$

a lo largo de la curva borde de la superficie $S: z = 4 - x^2$, $y \le 5$, $x \ge 0$, $y \ge 0$, $z \ge 0$ orientada en sentido $(2,0,0) \to (2,5,0) \to (0,5,4) \to (0,0,4) \to (2,0,0)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Rotor.**

$$\operatorname{rot}\vec f = (R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y) = (0,\ -1,\ -2y)$$

Las funciones $g(x)$ y $g(y)$ no aportan.

**Paso 2 — Parametrización.** $\vec T(u,v) = (u,\ v,\ 4 - u^2)$, con $D = [0,2]\times[0,5]$ y $\vec T'_u\wedge\vec T'_v = (2u, 0, 1)$ (hacia arriba).

**Paso 3 — Orientación.** En el plano $(u,v)$ el borde se recorre $(2,0)\to(2,5)\to(0,5)\to(0,0)$, en sentido antihorario ⇒ es compatible con $\vec T'_u\wedge\vec T'_v$.

**Paso 4 — Stokes.**

$$\oint_{\partial S}\vec f\cdot d\vec s = \iint_D(0, -1, -2v)\cdot(2u, 0, 1)\,du\,dv = \iint_D -2v\,du\,dv = -2\cdot2\cdot\frac{25}{2} = -50$$

</details>

**Respuesta:** $-50$.

</details>

---

### P3) Divergencia dada y flujo

Sea $g: \mathbb{R} \to \mathbb{R}$ una función $C^2$ y $\vec f(x,y,z) = (g'(x),\ 4yg(x),\ 8xz + 3)$.

- a) Halle $g$ tal que $\operatorname{div}\vec f(x,y,z) = 4$ y $\vec f(0,1,1) = (4,\ 4,\ 3)$.
- b) Con la función $g$ hallada en a), calcule el flujo de $\vec f$ a través de la superficie $S: z = 4 - x^2 - y^2$, $z \ge 0$ orientada con vectores normales con tercera componente positiva.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)**

*Ecuación:* $\operatorname{div}\vec f = g'' + 4g + 8x = 4$ ⇒ $g'' + 4g = 4 - 8x$.

*Condiciones:* $\vec f(0,1,1) = (g'(0),\ 4g(0),\ 3) = (4,4,3)$ ⇒ $g'(0) = 4$ y $g(0) = 1$.

*Homogénea:* $\lambda^2 + 4 = 0 \Rightarrow \lambda = \pm2i$ ⇒ $g_H = C_1\cos2x + C_2\operatorname{sen}2x$.

*Particular:* $g_P = Ax + B$ ⇒ $4Ax + 4B = 4 - 8x$ ⇒ $A = -2$, $B = 1$.

*Constantes:*

- $g(0) = C_1 + 1 = 1 \Rightarrow C_1 = 0$;
- $g'(0) = 2C_2 - 2 = 4 \Rightarrow C_2 = 3$.

**b)** *Cerrar con la tapa* $T$: $z = 0$, $x^2+y^2 \le 4$. Divergencia:

$$\iiint_V 4\,dV = 4\int_0^{2\pi}\!\!\int_0^2(4 - r^2)\,r\,dr\,d\theta = 4\cdot2\pi\cdot4 = 32\pi$$

*Tapa* (normal saliente $(0,0,-1)$): $\vec f\cdot\breve n = -(8xz + 3) = -3$ en $z = 0$ ⇒ $\Phi_T = -3\cdot4\pi = -12\pi$.

*Resultado:* $\Phi_S = 32\pi - (-12\pi) = 44\pi$.

</details>

**Respuesta:**

- a) $g(x) = 3\operatorname{sen}(2x) - 2x + 1$.
- b) $44\pi$.

</details>

---

### P4) Circulación sobre un arco

Calcule la circulación de $\vec f(x,y,z) = (-y,\ x,\ z)$ a lo largo de la curva $C$ definida por la intersección de las superficies $S_1: x^2 + z^2 = 9$ y $S_2: x + y = 3$ en el primer octante. Indique claramente la orientación elegida para el cálculo.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $x = 3\cos t$, $z = 3\operatorname{sen}t$ e $y = 3 - 3\cos t$, con $t\in[0, \pi/2]$. Recorre la curva desde $(3,0,0)$ hasta $(0,3,3)$.

**Paso 2 — Integrando.** $\vec\alpha' = (-3\operatorname{sen}t,\ 3\operatorname{sen}t,\ 3\cos t)$ y $\vec f(\vec\alpha) = (-3 + 3\cos t,\ 3\cos t,\ 3\operatorname{sen}t)$:

$$\vec f\cdot\vec\alpha' = 9\operatorname{sen}t - 9\operatorname{sen}t\cos t + 9\operatorname{sen}t\cos t + 9\operatorname{sen}t\cos t = 9\operatorname{sen}t + 9\operatorname{sen}t\cos t$$

**Paso 3 — Integral.**

$$\int_0^{\pi/2}(9\operatorname{sen}t + 9\operatorname{sen}t\cos t)\,dt = 9 + \frac92 = \frac{27}{2}$$

</details>

**Respuesta:** $\dfrac{27}{2}$, recorriendo $C$ desde $(3,0,0)$ hasta $(0,3,3)$ (en el sentido opuesto daría $-27/2$).

</details>

---

[← Volver al menú principal](../README.md)
