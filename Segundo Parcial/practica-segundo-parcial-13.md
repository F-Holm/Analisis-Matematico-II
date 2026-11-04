# 2.º Parcial de práctica 13

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Stokes con rotor constante

Enuncie el teorema de Stokes. Utilícelo para calcular la circulación de

$$\vec f(x,y,z) = \left(-y + e^x,\ x + z,\ \ln(1 + z^2) + y\right)$$

a lo largo de la circunferencia $x^2 + y^2 = 4$, $z = 3$, recorrida en sentido antihorario vista desde arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** sea $S$ una superficie suave a trozos, orientable, cuyo borde $\partial S$ es una curva cerrada, simple y suave a trozos, orientada en forma compatible con la normal de $S$. Si $\vec f \in C^1$ en un abierto que contiene a $S$:

$$\oint_{\partial S}\vec f\cdot d\vec s = \iint_S\mathop{\mathrm{rot}}\vec f\cdot\breve n\thinspace d\sigma$$

**Paso 1 — Rotor.**

$$\mathop{\mathrm{rot}}\vec f = (R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y) = (1 - 1,\ 0 - 0,\ 1 + 1) = (0,\ 0,\ 2)$$

**Paso 2 — Superficie.** El disco $z = 3$, $x^2 + y^2 \le 4$, con normal $\breve k$ (compatible con el sentido antihorario visto desde arriba).

**Paso 3 — Flujo del rotor.** $\iint 2\thinspace d\sigma = 2\cdot4\pi = 8\pi$.

</details>

**Respuesta:** $8\pi$.

</details>

---

### T2) Líneas de campo hiperbólicas

Halle la línea de campo de $\vec f(x,y) = (x,\ -y)$ que pasa por el punto $(2,1)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Ecuación.** Las líneas de campo cumplen $\dfrac{dx}{x} = \dfrac{dy}{-y}$.

**Paso 2 — Integrar.** $\ln|x| = -\ln|y| + c$ ⇒ $xy = C$.

**Paso 3 — Punto.** $(2,1)$: $C = 2$. La línea es la rama de la hipérbola $xy = 2$ en el primer cuadrante.

</details>

**Respuesta:** $xy = 2$, con $x > 0$.

</details>

---

## Ejercicios prácticos

### P1) Volumen en esféricas

Calcule el volumen del sólido interior a la esfera $x^2 + y^2 + z^2 = 4z$ y por encima del cono $z = \sqrt{x^2 + y^2}$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Esfera en esféricas.** $\rho^2 = 4\rho\cos\varphi \Rightarrow \rho = 4\cos\varphi$ (esfera de radio 2 centrada en $(0,0,2)$, que pasa por el origen).

**Paso 2 — Cono.** $\varphi = \pi/4$. La región es $0 \le \rho \le 4\cos\varphi$, $0 \le \varphi \le \pi/4$.

**Paso 3 — Integral.**

$$V = \int_0^{2\pi}\negthinspace\negthinspace\int_0^{\pi/4}\negthinspace\negthinspace\int_0^{4\cos\varphi}\rho^2\mathop{\mathrm{sen}}\varphi\thinspace d\rho\thinspace d\varphi\thinspace d\theta = 2\pi\cdot\frac{64}{3}\int_0^{\pi/4}\cos^3\varphi\mathop{\mathrm{sen}}\varphi\thinspace d\varphi$$

$$= 2\pi\cdot\frac{64}{3}\cdot\frac14\left(1 - \frac14\right) = 8\pi$$

</details>

**Respuesta:** $V = 8\pi$.

</details>

---

### P2) Flujo a través de un paraboloide hacia abajo

Calcule el flujo de $\vec f(x,y,z) = (y,\ -x,\ z)$ a través de $S: z = x^2 + y^2$, $z \le 1$, orientada con normales de tercera componente negativa.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Normal.** Con $\vec T(x,y) = (x,\ y,\ x^2 + y^2)$, la normal hacia arriba es $(-2x, -2y, 1)$; la pedida es $\vec N = (2x,\ 2y,\ -1)$.

**Paso 2 — Integrando.**

$$\vec f\cdot\vec N = 2xy - 2xy - z = -(x^2 + y^2)$$

**Paso 3 — Polares** sobre $r \le 1$:

$$\Phi = -\int_0^{2\pi}\negthinspace\negthinspace\int_0^1 r^2\cdot r\thinspace dr\thinspace d\theta = -\frac{\pi}{2}$$

</details>

**Respuesta:** $-\dfrac{\pi}{2}$.

</details>

---

### P3) Ecuación sin término en $y$

Resuelva $y'' + 3y' = 6$ con $y(0) = 1$ e $y'(0) = -1$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Homogénea.** $r^2 + 3r = 0 \Rightarrow r = 0,\ r = -3$ ⇒ $y_H = C_1 + C_2e^{-3x}$.

**Paso 2 — Particular.** El término independiente es constante y $0$ **es** raíz ⇒ $y_P = Ax$: $3A = 6 \Rightarrow A = 2$.

**Paso 3 — Constantes.** $y = C_1 + C_2e^{-3x} + 2x$:

- $y(0) = C_1 + C_2 = 1$.
- $y'(0) = -3C_2 + 2 = -1 \Rightarrow C_2 = 1$, y $C_1 = 0$.

</details>

**Respuesta:** $y = e^{-3x} + 2x$.

</details>

---

### P4) Masa de un alambre parabólico

Calcule la masa de un alambre con forma del arco de parábola $y = x^2$, $0 \le x \le 1$ (en el plano $xy$), si su densidad lineal es $\delta(x,y) = x$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $\vec\alpha(t) = (t,\ t^2)$, $t\in[0,1]$, $\Vert\vec\alpha'\Vert = \sqrt{1 + 4t^2}$.

**Paso 2 — Integral.**

$$M = \int_0^1 t\sqrt{1 + 4t^2}\thinspace dt = \left[\frac{(1 + 4t^2)^{3/2}}{12}\right]_0^1 = \frac{5\sqrt5 - 1}{12}$$

</details>

**Respuesta:** $M = \dfrac{5\sqrt5 - 1}{12}$.

</details>

---

[← Anterior](practica-segundo-parcial-12.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-14.md)
