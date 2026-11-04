# 2.º Parcial de práctica 20

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Stokes: verdadero o falso

Enuncie el teorema de Stokes. Determine la veracidad de la siguiente afirmación y justifique:

> Si $\vec f \in C^1(\mathbb{R}^3)$ cumple $\mathop{\mathrm{rot}}\vec f = (1,\ 1,\ 0)$ en todo punto, entonces su circulación a lo largo de cualquier curva cerrada simple, suave a trozos, contenida en el plano $z = 0$, es nula.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** sea $S$ una superficie suave a trozos, orientable, cuyo borde $\partial S$ es una curva cerrada, simple y suave a trozos, orientada en forma compatible con la normal de $S$. Si $\vec f \in C^1$ en un abierto que contiene a $S$:

$$\oint_{\partial S}\vec f\cdot d\vec s = \iint_S\mathop{\mathrm{rot}}\vec f\cdot\breve n\thinspace d\sigma$$

**Justificación.** Sea $C$ la curva y $S$ la región plana que encierra en $z = 0$. Su normal es $\breve n = \pm\breve k$ (según el sentido de recorrido). Entonces:

$$\oint_C\vec f\cdot d\vec s = \iint_S(1,1,0)\cdot(0,0,\pm1)\thinspace d\sigma = \iint_S 0\thinspace d\sigma = 0$$

</details>

**Respuesta:** **Verdadera**: el rotor no tiene componente normal al plano $z = 0$, así que su flujo a través de cualquier región de ese plano es nulo.

</details>

---

### T2) Ecuación con raíz nula

Resuelva $y'' - 2y' = 4$ con $y(0) = 1$ e $y'(0) = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Homogénea.** $r^2 - 2r = 0 \Rightarrow r = 0,\ r = 2$ ⇒ $y_H = C_1 + C_2e^{2x}$.

**Paso 2 — Particular.** El término es constante y $0$ es raíz simple ⇒ $y_P = Ax$: $-2A = 4 \Rightarrow A = -2$.

**Paso 3 — Constantes.** $y = C_1 + C_2e^{2x} - 2x$:

- $y'(0) = 2C_2 - 2 = 0 \Rightarrow C_2 = 1$.
- $y(0) = C_1 + C_2 = 1 \Rightarrow C_1 = 0$.

</details>

**Respuesta:** $y = e^{2x} - 2x$.

</details>

---

## Ejercicios prácticos

### P1) Green sobre un cuarto de corona

Calcule la circulación de $\vec f(x,y) = (x - y,\ x + y^2)$ a lo largo de la frontera de la región $D: 1 \le x^2 + y^2 \le 4$, $x \ge 0$, $y \ge 0$, orientada positivamente.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Green.** $Q'_x - P'_y = 1 - (-1) = 2$.

**Paso 2 — Área de $D$.** Un cuarto de la corona: $\dfrac{\pi(4 - 1)}{4} = \dfrac{3\pi}{4}$.

**Paso 3 — Resultado.** $\oint\vec f\cdot d\vec s = 2\cdot\dfrac{3\pi}{4} = \dfrac{3\pi}{2}$.

</details>

**Respuesta:** $\dfrac{3\pi}{2}$.

</details>

---

### P2) Flujo a través de un semicilindro horizontal

Calcule el flujo de $\vec f(x,y,z) = (x^2,\ 0,\ z)$ a través de la superficie $y^2 + z^2 = 4$, $z \ge 0$, $0 \le x \le 3$, orientada hacia afuera del cilindro.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** El eje del cilindro es el eje $x$: $\vec T(x,\theta) = (x,\ 2\cos\theta,\ 2\mathop{\mathrm{sen}}\theta)$, $x\in[0,3]$, $\theta\in[0,\pi]$ (para que $z \ge 0$). $d\sigma = 2\thinspace dx\thinspace d\theta$.

**Paso 2 — Normal exterior.** $\breve n = \left(0,\ \tfrac{y}{2},\ \tfrac{z}{2}\right)$.

**Paso 3 — Integrando.** $\vec f\cdot\breve n = \dfrac{z^2}{2} = 2\mathop{\mathrm{sen}}\nolimits^2\theta$ (la componente $x^2$ es tangente y no aporta).

**Paso 4 — Integral.**

$$\Phi = \int_0^3\negthinspace\int_0^{\pi}2\mathop{\mathrm{sen}}\nolimits^2\theta\cdot2\thinspace d\theta\thinspace dx = 3\cdot4\cdot\frac{\pi}{2} = 6\pi$$

</details>

**Respuesta:** $6\pi$.

</details>

---

### P3) Volumen bajo una campana

Calcule el volumen del cuerpo limitado por la superficie $z = e^{-(x^2 + y^2)}$, el plano $z = 0$ y el cilindro $x^2 + y^2 = 4$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Polares.** $e^{-(x^2 + y^2)}$ no tiene primitiva elemental en cartesianas, pero en polares aparece el factor $r$ del jacobiano.

**Paso 2 — Integral.**

$$V = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2 e^{-r^2}\thinspace r\thinspace dr\thinspace d\theta = 2\pi\left[-\frac{e^{-r^2}}{2}\right]_0^2 = \pi\left(1 - e^{-4}\right)$$

</details>

**Respuesta:** $V = \pi\left(1 - e^{-4}\right)$.

</details>

---

### P4) Masa de una superficie cilíndrica

Calcule la masa de la superficie lateral del cilindro $x^2 + y^2 = 4$, $0 \le z \le 2$, si su densidad es $\delta(x,y,z) = z + x^2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $\vec T(\theta, z) = (2\cos\theta,\ 2\mathop{\mathrm{sen}}\theta,\ z)$, $d\sigma = 2\thinspace d\theta\thinspace dz$.

**Paso 2 — Integral.**

$$M = \int_0^2\negthinspace\int_0^{2\pi}(z + 4\cos^2\theta)\cdot2\thinspace d\theta\thinspace dz$$

**Paso 3 — Calcular.**

- $\displaystyle\int_0^2\negthinspace\int_0^{2\pi}z\thinspace d\theta\thinspace dz = 2\pi\cdot2 = 4\pi$.
- $\displaystyle\int_0^2\negthinspace\int_0^{2\pi}4\cos^2\theta\thinspace d\theta\thinspace dz = 2\cdot4\pi = 8\pi$.

$$M = 2(4\pi + 8\pi) = 24\pi$$

</details>

**Respuesta:** $M = 24\pi$.

</details>

---

[← Anterior](practica-segundo-parcial-19.md) · [Volver al menú principal](../README.md)
