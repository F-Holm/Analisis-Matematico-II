# 2.º Parcial de práctica 15

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Área de una cardioide

Enuncie el teorema de Green y deduzca una fórmula para el área de una región plana como integral de línea. Utilícela para calcular el área encerrada por la cardioide $\vec\alpha(t) = \left((1 + \cos t)\cos t,\ (1 + \cos t)\mathop{\mathrm{sen}}t\right)$, $t\in[0,2\pi]$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** si $D$ es una región acotada cuya frontera $C$ es una curva cerrada, simple, suave a trozos y orientada positivamente, y $\vec f = (P,Q) \in C^1$ en un abierto que contiene a $D$:

$$\oint_C P\thinspace dx + Q\thinspace dy = \iint_D(Q'_x - P'_y)\thinspace dx\thinspace dy$$

**Fórmula del área.** Con $\vec f = \left(-\tfrac{y}{2}, \tfrac{x}{2}\right)$, $Q'_x - P'_y = 1$:

$$\text{Área}(D) = \frac12\oint_C x\thinspace dy - y\thinspace dx$$

**Paso 1 — Polares.** La curva es $r(t) = 1 + \cos t$ en polares. Para $x = r\cos t$, $y = r\mathop{\mathrm{sen}}t$ se cumple $xy' - yx' = r^2$ (los términos con $r'$ se cancelan).

**Paso 2 — Integral.**

$$\text{Área} = \frac12\int_0^{2\pi}(1 + \cos t)^2\thinspace dt = \frac12\left(2\pi + 0 + \pi\right) = \frac{3\pi}{2}$$

</details>

**Respuesta:** $\text{Área} = \dfrac{3\pi}{2}$.

</details>

---

### T2) Raíz doble

- a) Sabiendo que $y = xe^{-x}$ es solución de $y'' + ay' + by = 0$ (con $a, b$ constantes), halle $a$ y $b$.
- b) Resuelva $y'' + ay' + by = 3$ con $y(0) = 0$ e $y'(0) = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** Para que $xe^{-x}$ sea solución, $-1$ debe ser raíz **doble** de la ecuación característica:

$$(r + 1)^2 = r^2 + 2r + 1 \Rightarrow a = 2,\ b = 1$$

**b)**

- *Homogénea:* $y_H = (C_1 + C_2x)e^{-x}$.
- *Particular:* $y_P = A$ ⇒ $A = 3$.

*Condiciones* con $y = (C_1 + C_2x)e^{-x} + 3$:

- $y(0) = C_1 + 3 = 0 \Rightarrow C_1 = -3$.
- $y'(0) = C_2 - C_1 = 0 \Rightarrow C_2 = -3$.

</details>

**Respuesta:**

- a) $a = 2$, $b = 1$.
- b) $y = 3 - 3(1 + x)e^{-x}$.

</details>

---

## Ejercicios prácticos

### P1) Green sobre un triángulo

Calcule la circulación de $\vec f(x,y) = (xy,\ x^2 + y)$ a lo largo de la frontera del triángulo de vértices $(0,0)$, $(1,0)$ y $(1,1)$, orientada positivamente.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Green.** $Q'_x - P'_y = 2x - x = x$.

**Paso 2 — Región.** $0 \le x \le 1$, $0 \le y \le x$.

**Paso 3 — Integral.**

$$\oint\vec f\cdot d\vec s = \int_0^1\negthinspace\int_0^x x\thinspace dy\thinspace dx = \int_0^1 x^2\thinspace dx = \frac13$$

</details>

**Respuesta:** $\dfrac13$.

</details>

---

### P2) Flujo radial a través de un casquete

Calcule el flujo de $\vec f(x,y,z) = (x,\ y,\ z)$ a través del casquete $x^2 + y^2 + z^2 = 4$, $z \ge 1$, orientado hacia afuera de la esfera.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Integrando.** Sobre la esfera de radio 2, $\breve n = \tfrac{(x,y,z)}{2}$ ⇒ $\vec f\cdot\breve n = \dfrac{x^2 + y^2 + z^2}{2} = 2$.

**Paso 2 — Área del casquete.** En esféricas, $z = 2\cos\varphi \ge 1 \Rightarrow \varphi \le \pi/3$:

$$A = \int_0^{2\pi}\negthinspace\negthinspace\int_0^{\pi/3}4\mathop{\mathrm{sen}}\varphi\thinspace d\varphi\thinspace d\theta = 8\pi\left(1 - \frac12\right) = 4\pi$$

**Paso 3 — Resultado.** $\Phi = 2\cdot4\pi = 8\pi$.

</details>

**Respuesta:** $8\pi$.

</details>

---

### P3) Masa de una esfera de densidad variable

Calcule la masa de la bola $x^2 + y^2 + z^2 \le 1$ si su densidad en cada punto es igual a la distancia del punto al origen.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Esféricas.** $\delta = \rho$, $dV = \rho^2\mathop{\mathrm{sen}}\varphi\thinspace d\rho\thinspace d\varphi\thinspace d\theta$.

**Paso 2 — Integral.**

$$M = \int_0^{2\pi}\negthinspace\negthinspace\int_0^{\pi}\negthinspace\negthinspace\int_0^1\rho^3\mathop{\mathrm{sen}}\varphi\thinspace d\rho\thinspace d\varphi\thinspace d\theta = 2\pi\cdot2\cdot\frac14 = \pi$$

</details>

**Respuesta:** $M = \pi$.

</details>

---

### P4) Stokes sobre un paraboloide

Sea $S$ el paraboloide $z = 4 - x^2 - y^2$, $z \ge 0$, orientado hacia arriba. Calcule el flujo de $\mathop{\mathrm{rot}}\vec f$ a través de $S$, con $\vec f(x,y,z) = (y,\ z,\ x)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Borde.** $\partial S$: la circunferencia $x^2 + y^2 = 4$, $z = 0$, en sentido antihorario visto desde arriba (compatible con la normal hacia arriba).

**Paso 2 — Stokes.** Con $\vec\alpha(t) = (2\cos t,\ 2\mathop{\mathrm{sen}}t,\ 0)$, $\vec\alpha' = (-2\mathop{\mathrm{sen}}t,\ 2\cos t,\ 0)$ y $\vec f(\vec\alpha) = (2\mathop{\mathrm{sen}}t,\ 0,\ 2\cos t)$:

$$\iint_S\mathop{\mathrm{rot}}\vec f\cdot\breve n\thinspace d\sigma = \oint\vec f\cdot d\vec s = \int_0^{2\pi}-4\mathop{\mathrm{sen}}\nolimits^2t\thinspace dt = -4\pi$$

*Control:* $\mathop{\mathrm{rot}}\vec f = (-1,-1,-1)$ y sobre el paraboloide $\vec N = (2x, 2y, 1)$: $\iint(-2x - 2y - 1)\thinspace dA = -4\pi$ ✓.

</details>

**Respuesta:** $-4\pi$.

</details>

---

[← Anterior](practica-segundo-parcial-14.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-16.md)
