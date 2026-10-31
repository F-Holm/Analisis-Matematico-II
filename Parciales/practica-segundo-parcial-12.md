# 2.º Parcial de práctica 12

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Green y una singularidad

Sea $\vec f(x,y) = \left(\dfrac{-y}{x^2 + y^2},\ \dfrac{x}{x^2 + y^2}\right)$. Calcule su circulación en sentido antihorario sobre:

- a) la circunferencia $(x - 3)^2 + y^2 = 1$;
- b) la circunferencia $x^2 + y^2 = 1$.

Justifique por qué en un caso se puede aplicar el teorema de Green y en el otro no.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Integrando de Green.** Fuera del origen:

$$Q'_x = \frac{y^2 - x^2}{(x^2 + y^2)^2} = P'_y \Rightarrow Q'_x - P'_y = 0$$

**a)** El disco $(x - 3)^2 + y^2 \le 1$ no contiene al origen, así que $\vec f \in C^1$ en un abierto que contiene al disco. Por Green:

$$\oint\vec f\cdot d\vec s = \iint_D 0\thinspace dA = 0$$

**b)** El disco $x^2 + y^2 \le 1$ contiene al origen, donde $\vec f$ no está definido: **no** se cumplen las hipótesis de Green. Se calcula directamente con $\vec\alpha(t) = (\cos t,\ \mathop{\mathrm{sen}}t)$:

$$\oint\vec f\cdot d\vec s = \int_0^{2\pi}\left(\mathop{\mathrm{sen}}\nolimits^2t + \cos^2t\right)dt = 2\pi$$

</details>

**Respuesta:**

- a) $0$ (Green aplica: el disco no contiene al origen).
- b) $2\pi$ (Green no aplica: $\vec f$ no está definido en el origen).

</details>

---

### T2) Raíces complejas

Halle la solución de $y'' - 2y' + 5y = 0$ que cumple $y(0) = 1$ e $y'(0) = 3$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Ecuación característica.** $r^2 - 2r + 5 = 0 \Rightarrow r = 1 \pm 2i$.

**Paso 2 — S.G.** $y = e^x(C_1\cos2x + C_2\mathop{\mathrm{sen}}2x)$.

**Paso 3 — Constantes.**

- $y(0) = C_1 = 1$.
- $y' = e^x\left[(C_1 + 2C_2)\cos2x + (C_2 - 2C_1)\mathop{\mathrm{sen}}2x\right]$ ⇒ $y'(0) = C_1 + 2C_2 = 3 \Rightarrow C_2 = 1$.

</details>

**Respuesta:** $y = e^x(\cos2x + \mathop{\mathrm{sen}}2x)$.

</details>

---

## Ejercicios prácticos

### P1) Flujo a través de una semiesfera con Gauss

Calcule el flujo de $\vec f(x,y,z) = (xz,\ yz,\ z^2)$ a través de la semiesfera $x^2 + y^2 + z^2 = 4$, $z \ge 0$, orientada hacia afuera.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Cerrar.** Tapa $T$: $z = 0$, $x^2 + y^2 \le 4$, normal $(0,0,-1)$. Allí $\vec f = \vec 0$ ⇒ $\Phi_T = 0$.

**Paso 2 — Divergencia.** $\mathop{\mathrm{div}}\vec f = z + z + 2z = 4z$. En esféricas:

$$\iiint_V 4z\thinspace dV = \int_0^{2\pi}\negthinspace\negthinspace\int_0^{\pi/2}\negthinspace\negthinspace\int_0^2 4\rho\cos\varphi\cdot\rho^2\mathop{\mathrm{sen}}\varphi\thinspace d\rho\thinspace d\varphi\thinspace d\theta = 2\pi\cdot4\cdot\frac{16}{4}\cdot\frac12 = 16\pi$$

**Paso 3 — Resultado.** $\Phi_S = 16\pi - 0 = 16\pi$.

</details>

**Respuesta:** $16\pi$.

</details>

---

### P2) Green sobre una región parabólica

Calcule la circulación de $\vec f(x,y) = (-y^2,\ xy)$ a lo largo de la frontera de la región limitada por $y = x^2$ e $y = 1$, orientada positivamente.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Green.** $Q'_x - P'_y = y - (-2y) = 3y$.

**Paso 2 — Región.** $-1 \le x \le 1$, $x^2 \le y \le 1$.

**Paso 3 — Integral.**

$$\oint\vec f\cdot d\vec s = \int_{-1}^1\negthinspace\int_{x^2}^1 3y\thinspace dy\thinspace dx = \int_{-1}^1\frac32(1 - x^4)\thinspace dx = \frac32\left(2 - \frac25\right) = \frac{12}{5}$$

</details>

**Respuesta:** $\dfrac{12}{5}$.

</details>

---

### P3) Masa de un triángulo en el espacio

Calcule la masa del trozo del plano $x + y + z = 2$ ubicado en el primer octante, si su densidad en cada punto es igual a la distancia del punto al plano $yz$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Densidad.** Distancia al plano $yz$: $\delta = x$.

**Paso 2 — Elemento de área.** $z = 2 - x - y$ ⇒ $d\sigma = \sqrt{1 + 1 + 1}\thinspace dA = \sqrt3\thinspace dA$, sobre el triángulo $D: x, y \ge 0$, $x + y \le 2$.

**Paso 3 — Integral.**

$$M = \sqrt3\int_0^2\negthinspace\int_0^{2-x}x\thinspace dy\thinspace dx = \sqrt3\int_0^2 x(2 - x)\thinspace dx = \sqrt3\left(4 - \frac83\right) = \frac{4\sqrt3}{3}$$

</details>

**Respuesta:** $M = \dfrac{4\sqrt3}{3}$.

</details>

---

### P4) Circulación sobre un arco de parábola

Calcule la circulación de $\vec f(x,y,z) = (y,\ -x,\ z)$ a lo largo de la curva intersección de $z = 4 - x^2$ con $y = x$, desde $(0,0,4)$ hasta $(2,2,0)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $\vec\alpha(t) = (t,\ t,\ 4 - t^2)$, $t\in[0,2]$, $\vec\alpha' = (1,\ 1,\ -2t)$.

**Paso 2 — Integrando.** $\vec f(\vec\alpha) = (t,\ -t,\ 4 - t^2)$:

$$\vec f\cdot\vec\alpha' = t - t - 2t(4 - t^2) = 2t^3 - 8t$$

**Paso 3 — Integral.**

$$\int_0^2(2t^3 - 8t)\thinspace dt = 8 - 16 = -8$$

</details>

**Respuesta:** $-8$.

</details>

---

[← Anterior](practica-segundo-parcial-11.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-13.md)
