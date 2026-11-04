# 2.º Parcial de práctica 05

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Flujo de un rotor que sólo depende del borde

Enuncie el teorema de Stokes. Sea $\vec f(x,y,z) = \left(-y^3,\ x^3,\ e^{xyz}\right)$. Calcule el flujo de $\mathop{\mathrm{rot}}\vec f$ a través de la semiesfera $x^2 + y^2 + z^2 = 1$, $z \ge 0$, orientada hacia arriba, **sin** calcular el rotor.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** sea $S$ una superficie suave a trozos, orientable, cuyo borde $\partial S$ es una curva cerrada, simple y suave a trozos, orientada en forma compatible con la normal de $S$. Si $\vec f \in C^1$ en un abierto que contiene a $S$:

$$\iint_S\mathop{\mathrm{rot}}\vec f\cdot\breve n\thinspace d\sigma = \oint_{\partial S}\vec f\cdot d\vec s$$

**Paso 1 — Borde.** El borde de la semiesfera es la circunferencia $x^2 + y^2 = 1$, $z = 0$. Con normal hacia arriba, la orientación compatible es antihoraria vista desde arriba: $\vec\alpha(t) = (\cos t,\ \mathop{\mathrm{sen}}t,\ 0)$.

**Paso 2 — Circulación.** Como $z = 0$, $dz = 0$ y la tercera componente no aporta:

$$\oint\vec f\cdot d\vec s = \int_0^{2\pi}(-\mathop{\mathrm{sen}}\nolimits^3t)(-\mathop{\mathrm{sen}}t) + \cos^3t\cos t\thinspace dt = \int_0^{2\pi}(\mathop{\mathrm{sen}}\nolimits^4t + \cos^4t)\thinspace dt$$

**Paso 3 — Calcular.** $\displaystyle\int_0^{2\pi}\mathop{\mathrm{sen}}\nolimits^4t\thinspace dt = \int_0^{2\pi}\cos^4t\thinspace dt = \frac{3\pi}{4}$, así que el flujo vale $\dfrac{3\pi}{2}$.

</details>

**Respuesta:** $\dfrac{3\pi}{2}$.

</details>

---

### T2) Ecuación diferencial a partir de su solución general

- a) Halle la ecuación diferencial lineal homogénea de 2.º orden a coeficientes constantes cuya solución general es $y = C_1e^{2x} + C_2xe^{2x}$.
- b) Halle la solución particular que cumple $y(0) = 1$ e $y'(0) = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** $e^{2x}$ y $xe^{2x}$ corresponden a la raíz doble $r = 2$ de la ecuación característica:

$$(r - 2)^2 = r^2 - 4r + 4 = 0 \Rightarrow y'' - 4y' + 4y = 0$$

**b)**

- $y(0) = C_1 = 1$.
- $y' = (2C_1 + C_2 + 2C_2x)e^{2x}$ ⇒ $y'(0) = 2C_1 + C_2 = 0 \Rightarrow C_2 = -2$.

</details>

**Respuesta:**

- a) $y'' - 4y' + 4y = 0$.
- b) $y = (1 - 2x)e^{2x}$.

</details>

---

## Ejercicios prácticos

### P1) Green sobre un triángulo

Calcule la circulación de $\vec f(x,y) = (-y^2,\ x^2)$ a lo largo de la frontera del triángulo de vértices $(0,0)$, $(1,0)$ y $(0,1)$, orientada positivamente.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Green.** $\vec f$ es polinómico ⇒ $C^1$. $Q'_x - P'_y = 2x + 2y$.

**Paso 2 — Región.** $D: 0 \le x \le 1$, $0 \le y \le 1 - x$.

**Paso 3 — Integral.**

$$\oint\vec f\cdot d\vec s = \int_0^1\negthinspace\int_0^{1-x}(2x + 2y)\thinspace dy\thinspace dx = \int_0^1\left[2x(1 - x) + (1 - x)^2\right]dx = \frac13 + \frac13 = \frac23$$

*Control directo:* sobre el lado $y = 0$ el integrando es $0$; sobre el lado $x + y = 1$, recorrido desde $(1,0)$ hasta $(0,1)$, da $\tfrac23$; sobre $x = 0$, $0$. Total $\tfrac23$ ✓.

</details>

**Respuesta:** $\dfrac23$.

</details>

---

### P2) Flujo a través de un triángulo

Calcule el flujo de $\vec f(x,y,z) = (y,\ x,\ z^2)$ a través del trozo del plano $x + y + z = 1$ ubicado en el primer octante, orientado con el versor normal que se aleja del origen.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $\vec T(x,y) = (x,\ y,\ 1 - x - y)$ con $D: x \ge 0$, $y \ge 0$, $x + y \le 1$. $\vec N = (1,1,1)$ se aleja del origen ✓.

**Paso 2 — Integrando.**

$$\vec f\cdot\vec N = y + x + (1 - x - y)^2$$

**Paso 3 — Integral.** Llamando $u = x + y$, el integrando es $u + (1 - u)^2$:

$$\Phi = \int_0^1\negthinspace\int_0^{1-x}\left[(x + y) + (1 - x - y)^2\right]dy\thinspace dx = \frac13 + \frac{1}{12} = \frac{5}{12}$$

</details>

**Respuesta:** $\dfrac{5}{12}$.

</details>

---

### P3) Volumen bajo un plano inclinado

Calcule el volumen del cuerpo limitado por el cilindro $x^2 + y^2 = 4$ y los planos $z = 0$ y $z = x + 3$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Planteo.** Sobre el disco $x^2 + y^2 \le 4$ se tiene $x \ge -2$, así que $x + 3 \ge 1 > 0$: el techo siempre está por encima del piso.

$$V = \iint_D(x + 3)\thinspace dA$$

**Paso 2 — Simetría.** $\iint_D x\thinspace dA = 0$ (el disco es simétrico respecto del eje $y$). Queda:

$$V = 3\cdot\text{Área}(D) = 3\cdot4\pi = 12\pi$$

</details>

**Respuesta:** $V = 12\pi$.

</details>

---

### P4) Masa de un alambre helicoidal

Calcule la masa de un alambre con forma de la hélice $\vec\alpha(t) = (\cos t,\ \mathop{\mathrm{sen}}t,\ t)$, $t\in[0, 2\pi]$, si su densidad lineal en cada punto es igual a la distancia del punto al plano $xy$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Densidad.** $\delta = |z| = t$ (en el intervalo, $t \ge 0$).

**Paso 2 — Diferencial de arco.** $\vec\alpha' = (-\mathop{\mathrm{sen}}t,\ \cos t,\ 1)$ ⇒ $\Vert\vec\alpha'\Vert = \sqrt2$.

**Paso 3 — Integral.**

$$M = \int_0^{2\pi}t\sqrt2\thinspace dt = \sqrt2\cdot\frac{(2\pi)^2}{2} = 2\sqrt2\thinspace\pi^2$$

</details>

**Respuesta:** $M = 2\sqrt2\thinspace\pi^2$.

</details>

---

[← Anterior](practica-segundo-parcial-04.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-06.md)
