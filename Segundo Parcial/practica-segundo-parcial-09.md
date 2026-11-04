# 2.º Parcial de práctica 09

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Área de una elipse con Green

Enuncie el teorema de Green y demuestre que, si $D$ cumple sus hipótesis, $\text{Área}(D) = \dfrac12\oint_{\partial D^+}x\thinspace dy - y\thinspace dx$. Utilícelo para calcular el área de la elipse $\dfrac{x^2}{9} + \dfrac{y^2}{4} \le 1$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** si $D$ es una región acotada cuya frontera $C$ es una curva cerrada, simple, suave a trozos y orientada positivamente, y $\vec f = (P,Q) \in C^1$ en un abierto que contiene a $D$, entonces:

$$\oint_C P\thinspace dx + Q\thinspace dy = \iint_D(Q'_x - P'_y)\thinspace dx\thinspace dy$$

**Demostración.** Con $P = -\tfrac{y}{2}$ y $Q = \tfrac{x}{2}$ (polinomios, $C^1$): $Q'_x - P'_y = \tfrac12 + \tfrac12 = 1$, así que el miembro derecho es $\iint_D 1\thinspace dA = \text{Área}(D)$. $\blacksquare$

**Aplicación.** $\vec\alpha(t) = (3\cos t,\ 2\mathop{\mathrm{sen}}t)$, $t\in[0,2\pi]$ (antihoraria):

$$x y' - y x' = 3\cos t\cdot2\cos t + 2\mathop{\mathrm{sen}}t\cdot3\mathop{\mathrm{sen}}t = 6$$

$$\text{Área} = \frac12\int_0^{2\pi}6\thinspace dt = 6\pi$$

</details>

**Respuesta:** $\text{Área} = 6\pi$ (en general, $\pi ab$).

</details>

---

### T2) Campo radial en el plano perforado

Sea $\vec f(x,y) = \left(\dfrac{x}{x^2 + y^2},\ \dfrac{y}{x^2 + y^2}\right)$ en $\mathbb{R}^2 - \lbrace\bar 0\rbrace$.

- a) Muestre que $\vec f$ es conservativo hallando una función potencial.
- b) Calcule la circulación de $\vec f$ sobre la circunferencia $x^2 + y^2 = 1$ y el trabajo desde $(1,0)$ hasta $(e,e)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** Se propone $\phi = \tfrac12\ln(x^2 + y^2)$, definida en todo $\mathbb{R}^2 - \lbrace\bar 0\rbrace$:

$$\phi'_x = \frac{x}{x^2 + y^2},\qquad \phi'_y = \frac{y}{x^2 + y^2}$$

Como el potencial existe en **todo** el dominio, $\vec f$ es conservativo aunque el dominio no sea simplemente conexo.

**b)**

- *Circulación:* la curva es cerrada y $\vec f = \nabla\phi$ ⇒ $\oint\vec f\cdot d\vec s = 0$.
- *Trabajo:* $\phi(e,e) - \phi(1,0) = \tfrac12\ln(2e^2) - \tfrac12\ln1 = \tfrac12\ln2 + 1$.

</details>

**Respuesta:**

- a) $\phi(x,y) = \tfrac12\ln(x^2 + y^2) + k$.
- b) Circulación $0$; trabajo $1 + \tfrac12\ln2$.

</details>

---

## Ejercicios prácticos

### P1) Flujo a través de un cono

Calcule el flujo de $\vec f(x,y,z) = (x,\ y,\ 1)$ a través de la superficie cónica $z = \sqrt{x^2 + y^2}$, $z \le 2$, orientada con normales de tercera componente negativa.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Normal.** Con $\vec T(x,y) = (x,\ y,\ \sqrt{x^2 + y^2})$, la normal hacia arriba es $(-z'_x, -z'_y, 1)$. La pedida es la opuesta:

$$\vec N = \left(\frac{x}{r},\ \frac{y}{r},\ -1\right),\qquad r = \sqrt{x^2 + y^2}$$

**Paso 2 — Integrando.** $\vec f\cdot\vec N = \dfrac{x^2 + y^2}{r} - 1 = r - 1$.

**Paso 3 — Polares** sobre $D: r \le 2$:

$$\Phi = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2(r - 1)\thinspace r\thinspace dr\thinspace d\theta = 2\pi\left(\frac83 - 2\right) = \frac{4\pi}{3}$$

</details>

**Respuesta:** $\dfrac{4\pi}{3}$.

</details>

---

### P2) Ecuación diferencial con término polinómico

Resuelva $y'' + 4y = 8x^2$ con $y(0) = 0$ e $y'(0) = 2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Homogénea.** $r^2 + 4 = 0 \Rightarrow r = \pm2i$ ⇒ $y_H = C_1\cos2x + C_2\mathop{\mathrm{sen}}2x$.

**Paso 2 — Particular.** $y_P = Ax^2 + Bx + C$: $2A + 4(Ax^2 + Bx + C) = 8x^2$ ⇒ $A = 2$, $B = 0$, $2A + 4C = 0 \Rightarrow C = -1$.

**Paso 3 — Constantes.** $y = C_1\cos2x + C_2\mathop{\mathrm{sen}}2x + 2x^2 - 1$:

- $y(0) = C_1 - 1 = 0 \Rightarrow C_1 = 1$.
- $y'(0) = 2C_2 = 2 \Rightarrow C_2 = 1$.

</details>

**Respuesta:** $y = \cos2x + \mathop{\mathrm{sen}}2x + 2x^2 - 1$.

</details>

---

### P3) Volumen entre un paraboloide y un plano

Calcule el volumen del cuerpo limitado por el paraboloide $z = x^2 + y^2$ y el plano $z = 2x$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Proyección.** $x^2 + y^2 = 2x \iff (x - 1)^2 + y^2 = 1$. Dentro de ese disco $D$, $2x \ge x^2 + y^2$.

**Paso 2 — Integrando.** $2x - x^2 - y^2 = 1 - (x - 1)^2 - y^2$.

**Paso 3 — Polares centradas en $(1,0)$.** $x - 1 = \rho\cos\theta$, $y = \rho\mathop{\mathrm{sen}}\theta$:

$$V = \int_0^{2\pi}\negthinspace\negthinspace\int_0^1(1 - \rho^2)\thinspace\rho\thinspace d\rho\thinspace d\theta = 2\pi\left(\frac12 - \frac14\right) = \frac{\pi}{2}$$

</details>

**Respuesta:** $V = \dfrac{\pi}{2}$.

</details>

---

### P4) Circulación sobre una circunferencia de una esfera

Calcule la circulación de $\vec f(x,y,z) = (y,\ z,\ x)$ a lo largo de la curva intersección de la esfera $x^2 + y^2 + z^2 = 4$ con el plano $z = 1$, recorrida en sentido antihorario vista desde arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Curva.** Con $z = 1$: $x^2 + y^2 = 3$, circunferencia de radio $\sqrt3$.

**Paso 2 — Rotor.** $\mathop{\mathrm{rot}}\vec f = (R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y) = (-1,\ -1,\ -1)$.

**Paso 3 — Stokes** sobre el disco $z = 1$, $x^2 + y^2 \le 3$, normal $\breve k$:

$$\oint_C\vec f\cdot d\vec s = \iint(-1)\thinspace dA = -3\pi$$

</details>

**Respuesta:** $-3\pi$.

</details>

---

[← Anterior](practica-segundo-parcial-08.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-10.md)
