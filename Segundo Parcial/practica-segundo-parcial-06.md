# 2.º Parcial de práctica 06

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Líneas de campo

Defina línea de campo de un campo vectorial. Halle la línea de campo de $\vec f(x,y) = (2x,\ y)$ que pasa por el punto $(1,2)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Definición:** una **línea de campo** de $\vec f$ es una curva tal que en cada uno de sus puntos el vector $\vec f$ es tangente a ella. Si $\vec\alpha$ la parametriza, $\vec\alpha'(t) \parallel \vec f(\vec\alpha(t))$; en el plano esto da la ecuación $\dfrac{dx}{P} = \dfrac{dy}{Q}$.

**Paso 1 — Ecuación diferencial.**

$$\frac{dx}{2x} = \frac{dy}{y}$$

**Paso 2 — Variables separables.** $\tfrac12\ln|x| = \ln|y| + c$ ⇒ $y^2 = Cx$.

**Paso 3 — Punto.** $(1,2)$: $4 = C$ ⇒ $y^2 = 4x$. Como $y = 2 > 0$, la rama que pasa por el punto es $y = 2\sqrt x$, $x > 0$.

</details>

**Respuesta:** $y = 2\sqrt x$, $x > 0$ (rama superior de la parábola $y^2 = 4x$).

</details>

---

### T2) Teorema de Gauss y volumen

Enuncie el teorema de la divergencia. Demuestre que si $V$ cumple sus hipótesis y $\vec f(x,y,z) = (x,\ y,\ z)$, el flujo saliente de $\vec f$ a través de $\partial V$ es $3\cdot\text{Vol}(V)$. Utilícelo para calcular el flujo saliente de $\vec f$ a través de la frontera del cubo $[0,2]^3$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** sea $V \subset \mathbb{R}^3$ un sólido acotado cuya frontera $\partial V$ es una superficie cerrada, suave a trozos y orientada con normal exterior. Si $\vec f \in C^1$ en un abierto que contiene a $V$:

$$\iint_{\partial V}\vec f\cdot\breve n\thinspace d\sigma = \iiint_V\mathop{\mathrm{div}}\vec f\thinspace dV$$

**Demostración.** $\vec f = (x,y,z)$ es $C^1$ y $\mathop{\mathrm{div}}\vec f = 1 + 1 + 1 = 3$:

$$\iint_{\partial V}\vec f\cdot\breve n\thinspace d\sigma = \iiint_V 3\thinspace dV = 3\cdot\text{Vol}(V) \quad\blacksquare$$

**Aplicación.** $\text{Vol}([0,2]^3) = 8$ ⇒ flujo $= 24$.

*Control:* sólo aportan las tres caras $x = 2$, $y = 2$, $z = 2$ (en las otras, $\vec f\cdot\breve n = 0$). En cada una $\vec f\cdot\breve n = 2$ y el área es $4$: $3\cdot8 = 24$ ✓.

</details>

**Respuesta:** $24$.

</details>

---

## Ejercicios prácticos

### P1) Circulación sobre una elipse inclinada

Calcule la circulación de $\vec f(x,y,z) = (z,\ x,\ y)$ a lo largo de la curva intersección del cilindro $x^2 + y^2 = 9$ con el plano $x + z = 5$, recorrida en sentido antihorario vista desde arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Rotor.** $\mathop{\mathrm{rot}}\vec f = (1,\ 1,\ 1)$.

**Paso 2 — Superficie.** El trozo de plano $z = 5 - x$ sobre $D: x^2 + y^2 \le 9$, con $\vec N = (-z'_x,\ -z'_y,\ 1) = (1,\ 0,\ 1)$, hacia arriba ✓.

**Paso 3 — Stokes.**

$$\oint_C\vec f\cdot d\vec s = \iint_D(1,1,1)\cdot(1,0,1)\thinspace dA = 2\cdot9\pi = 18\pi$$

</details>

**Respuesta:** $18\pi$.

</details>

---

### P2) Campo solenoidal y flujo

Sea $g: \mathbb{R} \to \mathbb{R}$ una función $C^2$ y $\vec f(x,y,z) = \left(g'(x),\ y\thinspace g(x),\ z + 2\right)$.

- a) Halle $g$ tal que $\mathop{\mathrm{div}}\vec f = 0$ y $\vec f(0,1,0) = (1,\ 0,\ 2)$.
- b) Con esa $g$, calcule el flujo de $\vec f$ a través de la semiesfera $x^2 + y^2 + z^2 = 1$, $z \ge 0$, orientada hacia arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)**

*Ecuación:* $\mathop{\mathrm{div}}\vec f = g'' + g + 1 = 0 \iff g'' + g = -1$.

*Condiciones:* $\vec f(0,1,0) = (g'(0),\ g(0),\ 2) = (1, 0, 2)$ ⇒ $g'(0) = 1$, $g(0) = 0$.

*Homogénea:* $r = \pm i$ ⇒ $g_H = C_1\cos x + C_2\mathop{\mathrm{sen}}x$. *Particular:* $g_P = -1$.

*Constantes:* $g(0) = C_1 - 1 = 0 \Rightarrow C_1 = 1$; $g'(0) = C_2 = 1$.

**b)** *Cerrar con la tapa* $T$: $z = 0$, $x^2 + y^2 \le 1$, normal saliente $(0,0,-1)$. Como $\mathop{\mathrm{div}}\vec f = 0$, por Gauss:

$$\Phi_S + \Phi_T = 0$$

*Tapa:* $\vec f\cdot(0,0,-1) = -(z + 2) = -2$ en $z = 0$ ⇒ $\Phi_T = -2\pi$.

*Resultado:* $\Phi_S = 2\pi$.

</details>

**Respuesta:**

- a) $g(x) = \cos x + \mathop{\mathrm{sen}}x - 1$.
- b) $2\pi$.

</details>

---

### P3) Área con cambio de variables

Calcule el área de la región del primer cuadrante limitada por las curvas $xy = 1$, $xy = 4$, $y = x$ e $y = 4x$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Cambio de variables.** $u = xy$, $v = \dfrac{y}{x}$. La región se transforma en el rectángulo $1 \le u \le 4$, $1 \le v \le 4$.

**Paso 2 — Jacobiano.**

```math
\frac{\partial(u,v)}{\partial(x,y)} = \begin{vmatrix} y & x \cr -\frac{y}{x^2} & \frac1x \end{vmatrix} = \frac{y}{x} + \frac{y}{x} = 2v \Rightarrow \left|\frac{\partial(x,y)}{\partial(u,v)}\right| = \frac{1}{2v}
```

**Paso 3 — Integral.**

$$A = \int_1^4\negthinspace\int_1^4\frac{1}{2v}\thinspace du\thinspace dv = 3\cdot\frac{\ln4}{2} = 3\ln2$$

</details>

**Respuesta:** $A = 3\ln2$.

</details>

---

### P4) Masa de un casquete esférico

Calcule la masa del casquete $S: x^2 + y^2 + z^2 = 4$, $z \ge 1$, si su densidad en cada punto es $\delta(x,y,z) = z$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización esférica.** $\rho = 2$: $\vec T(\varphi,\theta) = (2\mathop{\mathrm{sen}}\varphi\cos\theta,\ 2\mathop{\mathrm{sen}}\varphi\mathop{\mathrm{sen}}\theta,\ 2\cos\varphi)$ con $d\sigma = 4\mathop{\mathrm{sen}}\varphi\thinspace d\varphi\thinspace d\theta$.

**Paso 2 — Límites.** $z = 2\cos\varphi \ge 1 \Rightarrow \varphi\in[0, \pi/3]$.

**Paso 3 — Integral.**

$$M = \int_0^{2\pi}\negthinspace\negthinspace\int_0^{\pi/3}2\cos\varphi\cdot4\mathop{\mathrm{sen}}\varphi\thinspace d\varphi\thinspace d\theta = 2\pi\cdot4\left[\mathop{\mathrm{sen}}\nolimits^2\varphi\right]_0^{\pi/3} = 8\pi\cdot\frac34 = 6\pi$$

</details>

**Respuesta:** $M = 6\pi$.

</details>

---

[← Anterior](practica-segundo-parcial-05.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-07.md)
