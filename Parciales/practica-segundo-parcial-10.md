# 2.º Parcial de práctica 10

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Circulación proporcional al área

Sea $\vec f = (P,Q) \in C^1(\mathbb{R}^2)$ tal que $Q'_x - P'_y = 2$ en todo el plano. Demuestre que la circulación de $\vec f$ a lo largo de cualquier curva cerrada simple $C$, suave a trozos y orientada positivamente, es igual al doble del área que encierra. Enuncie el teorema que utiliza.

Verifíquelo calculando directamente la circulación de $\vec f(x,y) = (-y,\ x)$ sobre la circunferencia $x^2 + y^2 = 9$ en sentido antihorario.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Teorema de Green:** si $D$ es una región acotada cuya frontera $C$ es una curva cerrada, simple, suave a trozos y orientada positivamente, y $\vec f = (P,Q) \in C^1$ en un abierto que contiene a $D$:

$$\oint_C P\thinspace dx + Q\thinspace dy = \iint_D(Q'_x - P'_y)\thinspace dx\thinspace dy$$

**Demostración.** Con $Q'_x - P'_y = 2$: $\oint_C\vec f\cdot d\vec s = \iint_D 2\thinspace dA = 2\cdot\text{Área}(D)$. $\blacksquare$

**Verificación.** Para $\vec f = (-y, x)$, $Q'_x - P'_y = 1 + 1 = 2$ ✓. Con $\vec\alpha(t) = (3\cos t,\ 3\mathop{\mathrm{sen}}t)$:

$$\oint\vec f\cdot d\vec s = \int_0^{2\pi}(9\mathop{\mathrm{sen}}\nolimits^2t + 9\cos^2t)\thinspace dt = 18\pi = 2\cdot9\pi \ \checkmark$$

</details>

**Respuesta:** La circulación vale $2\cdot\text{Área}(D)$; para la circunferencia de radio 3, $18\pi$.

</details>

---

### T2) Forma de la solución particular

Para la ecuación $y'' - 4y' + 4y = f(x)$:

- a) Indique la forma de la solución particular (sin calcular los coeficientes) cuando $f(x) = e^{2x}$, $f(x) = x$ y $f(x) = \mathop{\mathrm{sen}}x$.
- b) Resuelva la ecuación con $f(x) = e^{2x}$, $y(0) = 0$ e $y'(0) = 1$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Ecuación característica:** $r^2 - 4r + 4 = (r - 2)^2$ ⇒ $r = 2$ doble, $y_H = (C_1 + C_2x)e^{2x}$.

**a)**

- $f = e^{2x}$: $2$ es raíz **doble** ⇒ se multiplica por $x^2$: $y_P = Ax^2e^{2x}$.
- $f = x$: $0$ no es raíz ⇒ $y_P = Ax + B$.
- $f = \mathop{\mathrm{sen}}x$: $\pm i$ no son raíces ⇒ $y_P = A\cos x + B\mathop{\mathrm{sen}}x$.

**b)** Con $y_P = Ax^2e^{2x}$: $y_P'' - 4y_P' + 4y_P = 2Ae^{2x}$ (los términos con $x$ y $x^2$ se cancelan) ⇒ $A = \tfrac12$.

*Condiciones* con $y = (C_1 + C_2x)e^{2x} + \tfrac12x^2e^{2x}$:

- $y(0) = C_1 = 0$.
- $y'(0) = 2C_1 + C_2 = 1 \Rightarrow C_2 = 1$.

</details>

**Respuesta:**

- a) $Ax^2e^{2x}$; $Ax + B$; $A\cos x + B\mathop{\mathrm{sen}}x$.
- b) $y = \left(x + \tfrac{x^2}{2}\right)e^{2x}$.

</details>

---

## Ejercicios prácticos

### P1) Circulación sobre una circunferencia horizontal

Calcule la circulación de $\vec f(x,y,z) = (x + y,\ y - x,\ z)$ a lo largo de la curva intersección de $z = x^2 + y^2$ con $z = 1$, recorrida en sentido antihorario vista desde arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $\vec\alpha(t) = (\cos t,\ \mathop{\mathrm{sen}}t,\ 1)$, $t\in[0,2\pi]$, $\vec\alpha' = (-\mathop{\mathrm{sen}}t,\ \cos t,\ 0)$.

**Paso 2 — Integrando.**

$$\vec f\cdot\vec\alpha' = -(\cos t + \mathop{\mathrm{sen}}t)\mathop{\mathrm{sen}}t + (\mathop{\mathrm{sen}}t - \cos t)\cos t = -\mathop{\mathrm{sen}}\nolimits^2t - \cos^2t = -1$$

**Paso 3 — Integral.** $\displaystyle\int_0^{2\pi}(-1)\thinspace dt = -2\pi$.

*Control con Stokes:* $\mathop{\mathrm{rot}}\vec f = (0,\ 0,\ -2)$, por el disco de radio 1 con normal $\breve k$: $-2\pi$ ✓.

</details>

**Respuesta:** $-2\pi$.

</details>

---

### P2) Flujo a través de un paraboloide con Gauss

Calcule el flujo de $\vec f(x,y,z) = (x,\ y,\ z^2)$ a través de $S: z = 1 - x^2 - y^2$, $z \ge 0$, orientada hacia arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Cerrar.** Tapa $T$: $z = 0$, $x^2 + y^2 \le 1$, normal saliente $(0,0,-1)$.

**Paso 2 — Divergencia.** $\mathop{\mathrm{div}}\vec f = 2 + 2z$:

$$\iiint_V(2 + 2z)\thinspace dV = \int_0^{2\pi}\negthinspace\negthinspace\int_0^1\negthinspace\int_0^{1-r^2}(2 + 2z)\thinspace dz\thinspace r\thinspace dr\thinspace d\theta = 2\pi\int_0^1\left[2(1 - r^2) + (1 - r^2)^2\right]r\thinspace dr$$

$$= 2\pi\left(\frac12 + \frac16\right) = \frac{4\pi}{3}$$

**Paso 3 — Tapa.** $\vec f\cdot(0,0,-1) = -z^2 = 0$ en $z = 0$ ⇒ $\Phi_T = 0$.

**Paso 4 — Resultado.** $\Phi_S = \dfrac{4\pi}{3}$.

</details>

**Respuesta:** $\dfrac{4\pi}{3}$.

</details>

---

### P3) Área de un casquete esférico

Calcule el área de la porción de la esfera $x^2 + y^2 + z^2 = 9$ que se encuentra por encima del plano $z = 2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Esféricas.** $\rho = 3$, $d\sigma = 9\mathop{\mathrm{sen}}\varphi\thinspace d\varphi\thinspace d\theta$. $z = 3\cos\varphi \ge 2 \Rightarrow \cos\varphi \ge \tfrac23$.

**Paso 2 — Integral.**

$$A = \int_0^{2\pi}\negthinspace\negthinspace\int_0^{\arccos(2/3)}9\mathop{\mathrm{sen}}\varphi\thinspace d\varphi\thinspace d\theta = 2\pi\cdot9\left(1 - \frac23\right) = 6\pi$$

Coincide con la fórmula de Arquímedes $A = 2\pi Rh$, con $R = 3$ y altura $h = 1$.

</details>

**Respuesta:** $A = 6\pi$.

</details>

---

### P4) Masa de una chapa cuadrada girada

Calcule la masa de la chapa $D: |x| + |y| \le 1$ si su densidad es $\delta(x,y) = (x + y)^2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Cambio de variables.** $u = x + y$, $v = x - y$. La región pasa a ser el cuadrado $-1 \le u \le 1$, $-1 \le v \le 1$.

**Paso 2 — Jacobiano.**

```math
\left|\frac{\partial(u,v)}{\partial(x,y)}\right| = \left|\begin{vmatrix} 1 & 1 \cr 1 & -1 \end{vmatrix}\right| = 2 \Rightarrow dx\thinspace dy = \tfrac12\thinspace du\thinspace dv
```

**Paso 3 — Integral.**

$$M = \int_{-1}^1\negthinspace\int_{-1}^1 u^2\cdot\frac12\thinspace du\thinspace dv = \frac12\cdot\frac23\cdot2 = \frac23$$

</details>

**Respuesta:** $M = \dfrac23$.

</details>

---

[← Anterior](practica-segundo-parcial-09.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-11.md)
