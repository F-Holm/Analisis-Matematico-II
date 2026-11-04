# 2.º Parcial de práctica 18

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Trabajo independiente del camino

Enuncie una condición suficiente para que un campo $\vec f = (P,Q) \in C^1$ sea conservativo. Verifique que $\vec f(x,y) = (2x\cos y,\ -x^2\mathop{\mathrm{sen}}y)$ la cumple y calcule el trabajo de $\vec f$ desde $(1,0)$ hasta $(2,\pi)$ a lo largo de cualquier curva.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Condición suficiente:** si $\vec f = (P,Q) \in C^1$ en un abierto **simplemente conexo** $D$ y $Q'_x = P'_y$ en $D$, entonces $\vec f$ es conservativo en $D$.

**Verificación.** $D = \mathbb{R}^2$ (simplemente conexo), $P'_y = -2x\mathop{\mathrm{sen}}y = Q'_x$ ✓.

**Potencial.** $\phi = \int 2x\cos y\thinspace dx = x^2\cos y + D(y)$; $\phi'_y = -x^2\mathop{\mathrm{sen}}y + D' = -x^2\mathop{\mathrm{sen}}y \Rightarrow D = k$.

**Trabajo.** $\phi(2,\pi) - \phi(1,0) = 4\cos\pi - \cos0 = -4 - 1 = -5$.

</details>

**Respuesta:** $W = -5$.

</details>

---

### T2) Gauss con divergencia constante

Enuncie el teorema de la divergencia. Sabiendo que $\vec f \in C^1(\mathbb{R}^3)$ tiene $\mathop{\mathrm{div}}\vec f = 2$ en todo punto, calcule el flujo saliente de $\vec f$ a través de la frontera de la caja $[0,1]\times[0,2]\times[0,3]$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** sea $V \subset \mathbb{R}^3$ un sólido acotado cuya frontera $\partial V$ es una superficie cerrada, suave a trozos y orientada con normal exterior. Si $\vec f \in C^1$ en un abierto que contiene a $V$:

$$\iint_{\partial V}\vec f\cdot\breve n\thinspace d\sigma = \iiint_V\mathop{\mathrm{div}}\vec f\thinspace dV$$

**Aplicación.** La frontera de la caja es cerrada y suave a trozos:

$$\Phi = \iiint_V 2\thinspace dV = 2\cdot(1\cdot2\cdot3) = 12$$

No hace falta conocer $\vec f$.

</details>

**Respuesta:** $12$.

</details>

---

## Ejercicios prácticos

### P1) Circulación sobre un paralelo de una esfera

Calcule la circulación de $\vec f(x,y,z) = (-y,\ x,\ z)$ a lo largo de la curva intersección de la esfera $x^2 + y^2 + z^2 = 25$ con el plano $z = 3$, recorrida en sentido antihorario vista desde arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Curva.** $z = 3 \Rightarrow x^2 + y^2 = 16$: circunferencia de radio 4.

**Paso 2 — Rotor.** $\mathop{\mathrm{rot}}\vec f = (0,\ 0,\ 2)$.

**Paso 3 — Stokes** sobre el disco $z = 3$, $x^2 + y^2 \le 16$, normal $\breve k$:

$$\oint\vec f\cdot d\vec s = 2\cdot16\pi = 32\pi$$

</details>

**Respuesta:** $32\pi$.

</details>

---

### P2) Masa de un cilindro macizo

Calcule la masa del cilindro $x^2 + y^2 \le 4$, $0 \le z \le 3$, si su densidad en cada punto es igual al cuadrado de la distancia del punto al eje $z$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Densidad.** $\delta = x^2 + y^2 = r^2$.

**Paso 2 — Cilíndricas.**

$$M = \int_0^{2\pi}\negthinspace\negthinspace\int_0^3\negthinspace\negthinspace\int_0^2 r^2\cdot r\thinspace dr\thinspace dz\thinspace d\theta = 2\pi\cdot3\cdot4 = 24\pi$$

</details>

**Respuesta:** $M = 24\pi$.

</details>

---

### P3) Flujo a través de un tronco de cono

Calcule el flujo de $\vec f(x,y,z) = (0,\ 0,\ z^2)$ a través de la superficie cónica $z = \sqrt{x^2 + y^2}$, $1 \le z \le 2$, orientada con normales de tercera componente negativa.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Normal.** Con $r = \sqrt{x^2 + y^2}$, $\vec N = \left(\dfrac{x}{r},\ \dfrac{y}{r},\ -1\right)$.

**Paso 2 — Integrando.** $\vec f\cdot\vec N = -z^2 = -r^2$.

**Paso 3 — Polares** sobre la corona $1 \le r \le 2$:

$$\Phi = -\int_0^{2\pi}\negthinspace\negthinspace\int_1^2 r^2\cdot r\thinspace dr\thinspace d\theta = -2\pi\cdot\frac{16 - 1}{4} = -\frac{15\pi}{2}$$

</details>

**Respuesta:** $-\dfrac{15\pi}{2}$.

</details>

---

### P4) Oscilador amortiguado forzado

Resuelva $y'' + 2y' + 2y = 4x$ con $y(0) = 0$ e $y'(0) = 1$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Homogénea.** $r^2 + 2r + 2 = 0 \Rightarrow r = -1 \pm i$ ⇒ $y_H = e^{-x}(C_1\cos x + C_2\mathop{\mathrm{sen}}x)$.

**Paso 2 — Particular.** $y_P = Ax + B$: $2A + 2Ax + 2B = 4x$ ⇒ $A = 2$, $B = -2$.

**Paso 3 — Constantes.**

- $y(0) = C_1 - 2 = 0 \Rightarrow C_1 = 2$.
- $y'(0) = -C_1 + C_2 + 2 = 1 \Rightarrow C_2 = 1$.

</details>

**Respuesta:** $y = e^{-x}(2\cos x + \mathop{\mathrm{sen}}x) + 2x - 2$.

</details>

---

[← Anterior](practica-segundo-parcial-17.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-19.md)
