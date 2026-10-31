# 2.º Parcial de práctica 03

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Condición necesaria para campos conservativos

Sea $\vec f: A \subset \mathbb{R}^2 \to \mathbb{R}^2$, $A$ abierto, $\vec f = (P,Q) \in C^1$. Demuestre que si $\vec f$ es conservativo, entonces $Q'_x = P'_y$ en $A$.

¿Es cierta la recíproca? Analícelo con $\vec f(x,y) = \left(\dfrac{-y}{x^2 + y^2},\ \dfrac{x}{x^2 + y^2}\right)$ en $A = \mathbb{R}^2 - \lbrace\bar 0\rbrace$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Demostración.** Si $\vec f$ es conservativo existe $\phi$ con $\phi'_x = P$ y $\phi'_y = Q$. Como $P, Q \in C^1$, $\phi \in C^2$ y por el teorema de Schwarz:

```math
P'_y = \phi''_{xy} = \phi''_{yx} = Q'_x \quad\blacksquare
```

**Recíproca.** Para el campo dado:

$$Q'_x = \frac{(x^2 + y^2) - 2x^2}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2} = P'_y$$

La jacobiana es simétrica en todo $A$. Sin embargo, sobre la circunferencia $\vec\alpha(t) = (\cos t,\ \mathop{\mathrm{sen}}t)$:

$$\oint\vec f\cdot d\vec s = \int_0^{2\pi}(\mathop{\mathrm{sen}}\nolimits^2t + \cos^2t)\thinspace dt = 2\pi \ne 0$$

Una circulación no nula sobre una curva cerrada impide que $\vec f$ sea conservativo. La recíproca falla porque $A$ no es simplemente conexo (tiene un "agujero" en el origen); sí vale en dominios simplemente conexos.

</details>

**Respuesta:** La recíproca **no** es cierta en general: el campo dado cumple $Q'_x = P'_y$ en $\mathbb{R}^2 - \lbrace\bar 0\rbrace$ pero su circulación sobre la circunferencia unitaria es $2\pi$. Vale si el dominio es simplemente conexo.

</details>

---

### T2) Teorema de Gauss y flujo de un rotor

Enuncie el teorema de la divergencia (Gauss). Demuestre que si $\vec g \in C^2(\mathbb{R}^3)$ entonces $\mathop{\mathrm{div}}(\mathop{\mathrm{rot}}\vec g) = 0$, y deduzca el flujo de $\mathop{\mathrm{rot}}\vec g$ a través de la frontera del cubo $[0,1]^3$ para $\vec g(x,y,z) = (xy^2,\ yz^2,\ zx^2)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** sea $V \subset \mathbb{R}^3$ un sólido acotado cuya frontera $\partial V$ es una superficie cerrada, suave a trozos y orientada con normal exterior. Si $\vec f \in C^1$ en un abierto que contiene a $V$:

$$\iint_{\partial V}\vec f\cdot\breve n\thinspace d\sigma = \iiint_V\mathop{\mathrm{div}}\vec f\thinspace dV$$

**Demostración.** Con $\vec g = (P,Q,R)$, $\mathop{\mathrm{rot}}\vec g = (R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y)$:

```math
\mathop{\mathrm{div}}(\mathop{\mathrm{rot}}\vec g) = R''_{yx} - Q''_{zx} + P''_{zy} - R''_{xy} + Q''_{xz} - P''_{yz} = 0
```

porque, por Schwarz ($\vec g \in C^2$), las derivadas cruzadas se cancelan de a pares. $\blacksquare$

**Aplicación.** $\mathop{\mathrm{rot}}\vec g \in C^1$ y el cubo cumple las hipótesis de Gauss:

$$\iint_{\partial V}\mathop{\mathrm{rot}}\vec g\cdot\breve n\thinspace d\sigma = \iiint_V 0\thinspace dV = 0$$

</details>

**Respuesta:** El flujo es $0$, para este $\vec g$ y para cualquier $\vec g \in C^2$.

</details>

---

## Ejercicios prácticos

### P1) Masa de una chapa plana

Calcule la masa de la chapa plana $D$ limitada por las curvas $y = x^2$ e $y = 2x$, si su densidad en cada punto es $\delta(x,y) = x$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Región.** $x^2 = 2x \Rightarrow x = 0$ o $x = 2$. Para $x\in[0,2]$, $x^2 \le y \le 2x$.

**Paso 2 — Integral.**

$$M = \int_0^2\negthinspace\int_{x^2}^{2x}x\thinspace dy\thinspace dx = \int_0^2(2x^2 - x^3)\thinspace dx = \frac{16}{3} - 4 = \frac43$$

</details>

**Respuesta:** $M = \dfrac43$.

</details>

---

### P2) Circulación con Stokes

Calcule la circulación de $\vec f(x,y,z) = \left(3y + e^{x^2},\ x + z,\ yz\right)$ a lo largo de la curva intersección de $z = x^2 + y^2$ con $z = 4$, recorrida en sentido horario vista desde arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Rotor.** El término $e^{x^2}$ no admite primitiva elemental, pero no aporta al rotor:

$$\mathop{\mathrm{rot}}\vec f = (R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y) = (z - 1,\ 0,\ 1 - 3) = (z - 1,\ 0,\ -2)$$

**Paso 2 — Superficie.** La curva es la circunferencia $x^2 + y^2 = 4$ en el plano $z = 4$. Se toma el disco $S$: $z = 4$, $x^2 + y^2 \le 4$. Para el sentido horario visto desde arriba, la normal compatible es $\breve n = (0,0,-1)$.

**Paso 3 — Stokes.**

$$\oint_C\vec f\cdot d\vec s = \iint_S(z - 1,\ 0,\ -2)\cdot(0,0,-1)\thinspace d\sigma = \iint_S 2\thinspace d\sigma = 2\cdot4\pi = 8\pi$$

</details>

**Respuesta:** $8\pi$.

</details>

---

### P3) Flujo a través de un cilindro

Calcule el flujo de $\vec f(x,y,z) = (xz^2,\ y,\ z)$ a través de la superficie lateral del cilindro $x^2 + y^2 = 1$, $0 \le z \le 2$, orientada hacia afuera.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $\vec T(\theta, z) = (\cos\theta,\ \mathop{\mathrm{sen}}\theta,\ z)$, $\theta\in[0,2\pi]$, $z\in[0,2]$. La normal exterior es $\breve n = (x,\ y,\ 0)$ y $d\sigma = 1\cdot d\theta\thinspace dz$ (radio 1).

**Paso 2 — Integrando.**

$$\vec f\cdot\breve n = x^2z^2 + y^2 = z^2\cos^2\theta + \mathop{\mathrm{sen}}\nolimits^2\theta$$

**Paso 3 — Integral.**

$$\Phi = \int_0^2\negthinspace\int_0^{2\pi}(z^2\cos^2\theta + \mathop{\mathrm{sen}}\nolimits^2\theta)\thinspace d\theta\thinspace dz = \pi\cdot\frac83 + \pi\cdot2 = \frac{14\pi}{3}$$

</details>

**Respuesta:** $\dfrac{14\pi}{3}$.

</details>

---

### P4) Ecuación diferencial con condiciones iniciales

Halle la solución de $y'' + 2y' + y = 4e^x$ cuya gráfica pasa por el punto $(0,1)$ con recta tangente horizontal.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Condiciones.** Pasa por $(0,1)$ ⇒ $y(0) = 1$; tangente horizontal ⇒ $y'(0) = 0$.

**Paso 2 — Homogénea.** $r^2 + 2r + 1 = 0 \Rightarrow r = -1$ (doble) ⇒ $y_H = (C_1 + C_2x)e^{-x}$.

**Paso 3 — Particular.** $1$ no es raíz ⇒ $y_P = Ae^x$: $A + 2A + A = 4 \Rightarrow A = 1$.

**Paso 4 — Constantes.** $y = (C_1 + C_2x)e^{-x} + e^x$:

- $y(0) = C_1 + 1 = 1 \Rightarrow C_1 = 0$.
- $y' = (C_2 - C_1 - C_2x)e^{-x} + e^x$ ⇒ $y'(0) = C_2 - C_1 + 1 = 0 \Rightarrow C_2 = -1$.

</details>

**Respuesta:** $y = e^x - xe^{-x}$.

</details>

---

[← Anterior](practica-segundo-parcial-02.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-04.md)
