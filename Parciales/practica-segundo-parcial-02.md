# 2.º Parcial de práctica 02

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Teorema de Green y área

Enuncie el teorema de Green y utilícelo para calcular el área de la región encerrada por la astroide $\vec\alpha(t) = (\cos^3t,\ \mathop{\mathrm{sen}}\nolimits^3t)$, $t\in[0,2\pi]$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** si $D$ es una región acotada cuya frontera $C$ es una curva cerrada, simple, suave a trozos y orientada positivamente, y $\vec f = (P,Q) \in C^1$ en un abierto que contiene a $D$, entonces:

$$\oint_C P\thinspace dx + Q\thinspace dy = \iint_D(Q'_x - P'_y)\thinspace dx\thinspace dy$$

**Paso 1 — Campo conveniente.** Con $\vec f = \left(-\tfrac{y}{2},\ \tfrac{x}{2}\right)$ resulta $Q'_x - P'_y = 1$, así que:

$$\text{Área}(D) = \frac12\oint_C x\thinspace dy - y\thinspace dx$$

**Paso 2 — Integrando.** $x' = -3\cos^2t\mathop{\mathrm{sen}}t$ e $y' = 3\mathop{\mathrm{sen}}\nolimits^2t\cos t$:

$$xy' - yx' = 3\cos^4t\mathop{\mathrm{sen}}\nolimits^2t + 3\mathop{\mathrm{sen}}\nolimits^4t\cos^2t = 3\mathop{\mathrm{sen}}\nolimits^2t\cos^2t = \frac34\mathop{\mathrm{sen}}\nolimits^2(2t)$$

**Paso 3 — Integral.**

$$\text{Área} = \frac12\int_0^{2\pi}\frac34\mathop{\mathrm{sen}}\nolimits^2(2t)\thinspace dt = \frac38\cdot\pi = \frac{3\pi}{8}$$

El resultado es positivo: la parametrización recorre la curva en sentido positivo.

</details>

**Respuesta:** $\text{Área} = \dfrac{3\pi}{8}$.

</details>

---

### T2) Teorema de Stokes: verdadero o falso

Enuncie el teorema de Stokes. Determine la veracidad de la siguiente afirmación y justifique:

> Si $\vec f \in C^1(\mathbb{R}^3)$ y la circulación de $\vec f$ sobre la circunferencia $x^2 + y^2 = 1$, $z = 0$, es nula, entonces $\mathop{\mathrm{rot}}\vec f = \vec 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** sea $S$ una superficie suave a trozos, orientable, cuyo borde $\partial S$ es una curva cerrada, simple y suave a trozos, orientada en forma compatible con la normal de $S$ (regla de la mano derecha). Si $\vec f \in C^1$ en un abierto que contiene a $S$:

$$\oint_{\partial S}\vec f\cdot d\vec s = \iint_S\mathop{\mathrm{rot}}\vec f\cdot\breve n\thinspace d\sigma$$

**Análisis.** Stokes sólo dice que el **flujo** de $\mathop{\mathrm{rot}}\vec f$ a través del disco es nulo, no que el rotor lo sea.

**Contraejemplo.** $\vec f = (0,\ 0,\ x)$:

- $\mathop{\mathrm{rot}}\vec f = (0,\ -1,\ 0) \ne \vec 0$.
- Sobre la circunferencia, $z = 0$ constante ⇒ $dz = 0$ y $\oint\vec f\cdot d\vec s = \oint x\thinspace dz = 0$.

Es coherente con Stokes: $(0,-1,0)\cdot\breve k = 0$ en el disco.

</details>

**Respuesta:** **Falsa**. Contraejemplo: $\vec f = (0,0,x)$ tiene circulación nula sobre la circunferencia y $\mathop{\mathrm{rot}}\vec f = (0,-1,0)$.

</details>

---

## Ejercicios prácticos

### P1) Circulación sobre una corona circular

Calcule la circulación de $\vec f(x,y) = (x^2 - y^3,\ x^3 + y^2)$ a lo largo de la frontera de la región $D: 1 \le x^2 + y^2 \le 4$, orientada positivamente.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Orientación.** La frontera positiva de la corona es la circunferencia exterior en sentido antihorario y la interior en sentido horario (la región queda siempre a la izquierda).

**Paso 2 — Green.** $Q'_x - P'_y = 3x^2 - (-3y^2) = 3(x^2 + y^2)$, polinomio ⇒ $C^1$ en $\mathbb{R}^2$.

**Paso 3 — Polares.**

$$\oint_{\partial D}\vec f\cdot d\vec s = \int_0^{2\pi}\negthinspace\negthinspace\int_1^2 3r^2\cdot r\thinspace dr\thinspace d\theta = 2\pi\cdot\frac34(16 - 1) = \frac{45\pi}{2}$$

</details>

**Respuesta:** $\dfrac{45\pi}{2}$.

</details>

---

### P2) Campo conservativo con parámetros

Sea $\vec f(x,y,z) = (axy + z,\ x^2 + bz,\ x + 3y)$.

- a) Halle $a$ y $b$ para que $\vec f$ sea un campo de gradientes y obtenga su función potencial.
- b) Calcule la circulación de $\vec f$ a lo largo de la hélice $\vec\alpha(t) = (\cos t,\ \mathop{\mathrm{sen}}t,\ t)$, $t\in[0,\pi]$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** El dominio es $\mathbb{R}^3$ (simplemente conexo), así que basta la simetría de la jacobiana:

- $P'_y = ax$ y $Q'_x = 2x$ ⇒ $a = 2$.
- $Q'_z = b$ y $R'_y = 3$ ⇒ $b = 3$.
- $P'_z = 1 = R'_x$ ✓.

*Potencial:*

- $\phi = \int(2xy + z)\thinspace dx = x^2y + xz + D(y,z)$.
- $\phi'_y = x^2 + D'_y = x^2 + 3z \Rightarrow D = 3yz + E(z)$.
- $\phi'_z = x + 3y + E' = x + 3y \Rightarrow E = k$.

**b)** La hélice va de $\vec\alpha(0) = (1,0,0)$ a $\vec\alpha(\pi) = (-1,0,\pi)$:

$$\int_C\vec f\cdot d\vec s = \phi(-1,0,\pi) - \phi(1,0,0) = (0 - \pi + 0) - 0 = -\pi$$

</details>

**Respuesta:**

- a) $a = 2$, $b = 3$; $\phi(x,y,z) = x^2y + xz + 3yz + k$.
- b) $-\pi$.

</details>

---

### P3) Flujo a través de un paraboloide

Calcule el flujo de $\vec f(x,y,z) = (x,\ y,\ z)$ a través de la superficie $S: z = 4 - x^2 - y^2$, $z \ge 0$, orientada hacia arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $\vec T(x,y) = (x,\ y,\ 4 - x^2 - y^2)$ con $D: x^2 + y^2 \le 4$. La normal $\vec N = (2x,\ 2y,\ 1)$ apunta hacia arriba ✓.

**Paso 2 — Integrando.**

$$\vec f\cdot\vec N = 2x^2 + 2y^2 + (4 - x^2 - y^2) = x^2 + y^2 + 4$$

**Paso 3 — Polares.**

$$\Phi = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2(r^2 + 4)\thinspace r\thinspace dr\thinspace d\theta = 2\pi(4 + 8) = 24\pi$$

*Control con Gauss:* $\mathop{\mathrm{div}}\vec f = 3$ y el volumen bajo el paraboloide es $8\pi$, así que el flujo total saliente es $24\pi$. Sobre la tapa $z = 0$ el flujo es $\iint -z\thinspace dA = 0$, así que todo el flujo pasa por $S$ ✓.

</details>

**Respuesta:** $24\pi$.

</details>

---

### P4) Ecuación diferencial y campo conservativo

Sea $g: \mathbb{R} \to \mathbb{R}$ una función $C^2$ y $\vec f(x,y) = \left(y\thinspace(6x - 4g(x)),\ g'(x)\right)$.

- a) Halle $g$ para que $\vec f$ sea conservativo y $\vec f(0,1) = \left(0,\ \tfrac72\right)$.
- b) Con la $g$ hallada, calcule el trabajo de $\vec f$ desde $(0,0)$ hasta $\left(\tfrac{\pi}{4},\ 2\right)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)**

*Ecuación:* en $\mathbb{R}^2$, $\vec f$ es conservativo si y sólo si $Q'_x = P'_y$:

$$g''(x) = 6x - 4g(x) \iff g'' + 4g = 6x$$

*Condiciones:* $\vec f(0,1) = (-4g(0),\ g'(0)) = \left(0, \tfrac72\right)$ ⇒ $g(0) = 0$ y $g'(0) = \tfrac72$.

*Homogénea:* $r^2 + 4 = 0 \Rightarrow r = \pm2i$ ⇒ $g_H = C_1\cos2x + C_2\mathop{\mathrm{sen}}2x$.

*Particular:* $g_P = Ax + B$ ⇒ $4Ax + 4B = 6x$ ⇒ $A = \tfrac32$, $B = 0$.

*Constantes:*

- $g(0) = C_1 = 0$.
- $g'(0) = 2C_2 + \tfrac32 = \tfrac72 \Rightarrow C_2 = 1$.

**b)** *Potencial:* $\phi'_y = g'(x) \Rightarrow \phi = y\thinspace g'(x) + h(x)$. Entonces $\phi'_x = y\thinspace g''(x) + h'(x) = y(6x - 4g)$, y como $g'' = 6x - 4g$, queda $h' = 0$. Así $\phi = y\thinspace g'(x) = y\left(2\cos2x + \tfrac32\right)$.

*Trabajo:*

$$W = \phi\left(\tfrac{\pi}{4}, 2\right) - \phi(0,0) = 2\left(0 + \tfrac32\right) - 0 = 3$$

</details>

**Respuesta:**

- a) $g(x) = \mathop{\mathrm{sen}}(2x) + \tfrac32x$.
- b) $W = 3$.

</details>

---

[← Anterior](practica-segundo-parcial-01.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-03.md)
