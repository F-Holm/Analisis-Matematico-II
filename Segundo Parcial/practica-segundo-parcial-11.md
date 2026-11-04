# 2.º Parcial de práctica 11

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Una integral de línea que mide áreas

Enuncie el teorema de Green. Muestre que para toda curva $C$ cerrada, simple, suave a trozos y orientada positivamente,

$$\oint_C x^2y\thinspace dx + \left(\frac{x^3}{3} + x\right)dy$$

es igual al área encerrada por $C$, y calcúlela para la circunferencia $(x - 2)^2 + y^2 = 1$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** si $D$ es una región acotada cuya frontera $C$ es una curva cerrada, simple, suave a trozos y orientada positivamente, y $\vec f = (P,Q) \in C^1$ en un abierto que contiene a $D$:

$$\oint_C P\thinspace dx + Q\thinspace dy = \iint_D(Q'_x - P'_y)\thinspace dx\thinspace dy$$

**Paso 1 — Hipótesis.** $P = x^2y$ y $Q = \tfrac{x^3}{3} + x$ son polinomios ⇒ $C^1$ en $\mathbb{R}^2$.

**Paso 2 — Integrando.** $Q'_x - P'_y = (x^2 + 1) - x^2 = 1$ ⇒ la integral vale $\iint_D 1\thinspace dA = \text{Área}(D)$.

**Paso 3 — Aplicación.** La circunferencia tiene radio 1 ⇒ área $\pi$.

</details>

**Respuesta:** $\pi$.

</details>

---

### T2) Gauss con divergencia constante

Enuncie el teorema de la divergencia. Sea $\vec f \in C^1(\mathbb{R}^3)$ con $\mathop{\mathrm{div}}\vec f = 2$ en todo punto. Halle el radio $R$ de la esfera centrada en el origen a través de la cual el flujo saliente de $\vec f$ vale $72\pi$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** sea $V \subset \mathbb{R}^3$ un sólido acotado cuya frontera $\partial V$ es una superficie cerrada, suave a trozos y orientada con normal exterior. Si $\vec f \in C^1$ en un abierto que contiene a $V$:

$$\iint_{\partial V}\vec f\cdot\breve n\thinspace d\sigma = \iiint_V\mathop{\mathrm{div}}\vec f\thinspace dV$$

**Aplicación.** Para la bola de radio $R$:

$$\Phi = \iiint_V 2\thinspace dV = 2\cdot\frac43\pi R^3 = \frac83\pi R^3 = 72\pi \Rightarrow R^3 = 27 \Rightarrow R = 3$$

</details>

**Respuesta:** $R = 3$.

</details>

---

## Ejercicios prácticos

### P1) Potencial con un parámetro

Sea $\vec f(x,y,z) = \left(y\cos(xy),\ x\cos(xy) + az,\ 2y + z\right)$.

- a) Halle $a$ para que $\vec f$ sea un campo de gradientes y obtenga una función potencial.
- b) Calcule el trabajo de $\vec f$ desde $(0,0,0)$ hasta $\left(1, \tfrac{\pi}{2}, 1\right)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** Dominio $\mathbb{R}^3$, simplemente conexo:

- $P'_y = \cos(xy) - xy\mathop{\mathrm{sen}}(xy) = Q'_x$ ✓ (para cualquier $a$).
- $P'_z = 0 = R'_x$ ✓.
- $Q'_z = a$ y $R'_y = 2$ ⇒ $a = 2$.

*Potencial:*

- $\phi = \int y\cos(xy)\thinspace dx = \mathop{\mathrm{sen}}(xy) + D(y,z)$.
- $\phi'_y = x\cos(xy) + D'_y = x\cos(xy) + 2z \Rightarrow D = 2yz + E(z)$.
- $\phi'_z = 2y + E' = 2y + z \Rightarrow E = \tfrac{z^2}{2}$.

**b)**

$$W = \phi\left(1, \tfrac{\pi}{2}, 1\right) - \phi(0,0,0) = \mathop{\mathrm{sen}}\tfrac{\pi}{2} + \pi + \tfrac12 = \tfrac32 + \pi$$

</details>

**Respuesta:**

- a) $a = 2$; $\phi = \mathop{\mathrm{sen}}(xy) + 2yz + \tfrac{z^2}{2} + k$.
- b) $W = \tfrac32 + \pi$.

</details>

---

### P2) Flujo a través de medio cilindro

Calcule el flujo de $\vec f(x,y,z) = (x,\ y,\ z)$ a través de la superficie $x^2 + y^2 = 4$ con $x \ge 0$ y $0 \le z \le 3$, orientada hacia afuera del cilindro.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Normal.** Sobre el cilindro de radio 2, $\breve n = \left(\tfrac{x}{2},\ \tfrac{y}{2},\ 0\right)$.

**Paso 2 — Integrando.** $\vec f\cdot\breve n = \dfrac{x^2 + y^2}{2} = 2$, constante.

**Paso 3 — Área.** Medio cilindro de radio 2 y altura 3: $\pi\cdot2\cdot3 = 6\pi$.

$$\Phi = 2\cdot6\pi = 12\pi$$

</details>

**Respuesta:** $12\pi$.

</details>

---

### P3) Volumen bajo un cilindro parabólico

Calcule el volumen del cuerpo limitado por $z = 4 - y^2$, $z = 0$, $x = 0$ y $x = 3$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Región.** $z = 4 - y^2 \ge 0 \Rightarrow -2 \le y \le 2$; $0 \le x \le 3$.

**Paso 2 — Integral.**

$$V = \int_0^3\negthinspace\int_{-2}^2(4 - y^2)\thinspace dy\thinspace dx = 3\left(16 - \frac{16}{3}\right) = 3\cdot\frac{32}{3} = 32$$

</details>

**Respuesta:** $V = 32$.

</details>

---

### P4) Ecuación diferencial y circulación nula

Sea $g: \mathbb{R} \to \mathbb{R}$ una función $C^2$ y $\vec f(x,y) = \left(y\thinspace(x - g(x)),\ g'(x)\right)$.

- a) Halle $g$ para que la circulación de $\vec f$ sobre toda curva cerrada sea nula, con $g(0) = 1$ y $g'(0) = 2$.
- b) Con esa $g$, calcule el trabajo de $\vec f$ desde $(0,0)$ hasta $\left(\tfrac{\pi}{4}, 4\right)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)**

*Ecuación:* en $\mathbb{R}^2$ la circulación es nula sobre toda curva cerrada si y sólo si $Q'_x = P'_y$:

$$g''(x) = x - g(x) \iff g'' + g = x$$

*Homogénea:* $g_H = C_1\cos x + C_2\mathop{\mathrm{sen}}x$. *Particular:* $g_P = x$.

*Constantes:* $g(0) = C_1 = 1$; $g'(0) = C_2 + 1 = 2 \Rightarrow C_2 = 1$.

**b)** *Potencial:* $\phi'_y = g'(x) \Rightarrow \phi = y\thinspace g'(x) + h(x)$; $\phi'_x = y\thinspace g'' + h' = y(x - g)$ ⇒ $h' = 0$. Entonces $\phi = y\thinspace g'(x) = y(\cos x - \mathop{\mathrm{sen}}x + 1)$.

*Trabajo:*

$$W = \phi\left(\tfrac{\pi}{4}, 4\right) - \phi(0,0) = 4\left(\tfrac{\sqrt2}{2} - \tfrac{\sqrt2}{2} + 1\right) = 4$$

</details>

**Respuesta:**

- a) $g(x) = \cos x + \mathop{\mathrm{sen}}x + x$.
- b) $W = 4$.

</details>

---

[← Anterior](practica-segundo-parcial-10.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-12.md)
