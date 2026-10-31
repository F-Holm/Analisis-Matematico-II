# 2.º Parcial de práctica 04

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Rotor de un gradiente

Defina rotor de un campo vectorial. Demuestre que si $\phi \in C^2(\mathbb{R}^3)$ entonces $\mathop{\mathrm{rot}}(\nabla\phi) = \vec 0$.

Determine si $\vec f(x,y,z) = (yz,\ xz,\ xy + 2z)$ es un campo de gradientes y, en caso afirmativo, calcule su circulación desde $(1,1,1)$ hasta $(2,1,3)$ a lo largo de cualquier curva.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Definición:** para $\vec f = (P,Q,R) \in C^1$,

$$\mathop{\mathrm{rot}}\vec f = \nabla\wedge\vec f = (R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y)$$

**Demostración.** Con $P = \phi'_x$, $Q = \phi'_y$, $R = \phi'_z$:

```math
\mathop{\mathrm{rot}}(\nabla\phi) = (\phi''_{zy} - \phi''_{yz},\ \phi''_{xz} - \phi''_{zx},\ \phi''_{yx} - \phi''_{xy}) = \vec 0
```

por el teorema de Schwarz ($\phi \in C^2$). $\blacksquare$

**Aplicación.**

*Rotor:* $\mathop{\mathrm{rot}}\vec f = (x - x,\ y - y,\ z - z) = \vec 0$ en $\mathbb{R}^3$, simplemente conexo ⇒ $\vec f$ es un campo de gradientes.

*Potencial:*

- $\phi = \int yz\thinspace dx = xyz + D(y,z)$.
- $\phi'_y = xz + D'_y = xz \Rightarrow D = E(z)$.
- $\phi'_z = xy + E' = xy + 2z \Rightarrow E = z^2$.

*Circulación:* $\phi(2,1,3) - \phi(1,1,1) = (6 + 9) - (1 + 1) = 13$.

</details>

**Respuesta:** Sí: $\phi = xyz + z^2 + k$, y la circulación vale $13$ por cualquier camino.

</details>

---

### T2) Área de un lazo con Green

Justifique, mediante el teorema de Green, que el área de una región $D$ cuya frontera $C$ está orientada positivamente es $\oint_C x\thinspace dy$. Utilícelo para calcular el área encerrada por el lazo $\vec\alpha(t) = (t^2,\ t^3 - t)$, $t\in[-1,1]$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Justificación.** Con $\vec f = (P,Q) = (0,\ x)$, $C^1$ en $\mathbb{R}^2$, $Q'_x - P'_y = 1$. Por Green:

$$\oint_C x\thinspace dy = \iint_D 1\thinspace dx\thinspace dy = \text{Área}(D)$$

**Paso 1 — El lazo.** $\vec\alpha(-1) = \vec\alpha(1) = (1, 0)$ y la curva no se corta en otros puntos ($t^2$ determina $|t|$ y $t^3 - t$ el signo): es cerrada y simple.

**Paso 2 — Integral.** $y' = 3t^2 - 1$:

$$\oint x\thinspace dy = \int_{-1}^1 t^2(3t^2 - 1)\thinspace dt = 2\left(\frac35 - \frac13\right) = \frac{8}{15}$$

El valor es positivo, así que la parametrización recorre el lazo en sentido positivo.

</details>

**Respuesta:** $\text{Área} = \dfrac{8}{15}$.

</details>

---

## Ejercicios prácticos

### P1) Volumen de un cono de helado

Calcule el volumen del cuerpo limitado por la esfera $x^2 + y^2 + z^2 = 4$ y el cono $z = \sqrt{x^2 + y^2}$ (región interior a la esfera y por encima del cono).

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Esféricas.** La esfera es $\rho = 2$. El cono $z = \sqrt{x^2 + y^2}$ forma un ángulo de $45°$ con el eje $z$: $\varphi = \pi/4$. La región es $0 \le \rho \le 2$, $0 \le \varphi \le \pi/4$, $0 \le \theta \le 2\pi$.

**Paso 2 — Integral.**

$$V = \int_0^{2\pi}\negthinspace\negthinspace\int_0^{\pi/4}\negthinspace\negthinspace\int_0^2\rho^2\mathop{\mathrm{sen}}\varphi\thinspace d\rho\thinspace d\varphi\thinspace d\theta = 2\pi\cdot\left(1 - \frac{\sqrt2}{2}\right)\cdot\frac83 = \frac{8\pi(2 - \sqrt2)}{3}$$

</details>

**Respuesta:** $V = \dfrac{8\pi(2 - \sqrt2)}{3}$.

</details>

---

### P2) Área de un trozo de paraboloide

Calcule el área de la porción del paraboloide $z = x^2 + y^2$ que se encuentra por debajo del plano $z = 2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Proyección.** $x^2 + y^2 \le 2$: disco de radio $\sqrt2$.

**Paso 2 — Elemento de área.** $d\sigma = \sqrt{1 + (z'_x)^2 + (z'_y)^2}\thinspace dA = \sqrt{1 + 4x^2 + 4y^2}\thinspace dA$.

**Paso 3 — Polares.**

$$A = \int_0^{2\pi}\negthinspace\negthinspace\int_0^{\sqrt2}\sqrt{1 + 4r^2}\thinspace r\thinspace dr\thinspace d\theta = 2\pi\left[\frac{(1 + 4r^2)^{3/2}}{12}\right]_0^{\sqrt2} = 2\pi\cdot\frac{27 - 1}{12} = \frac{13\pi}{3}$$

</details>

**Respuesta:** $A = \dfrac{13\pi}{3}$.

</details>

---

### P3) Flujo saliente de un cilindro con Gauss

Calcule el flujo de $\vec f(x,y,z) = \left(\tfrac{x^3}{3} + e^{yz},\ \tfrac{y^3}{3},\ \tfrac{z^3}{3} + \mathop{\mathrm{sen}}(xy)\right)$ a través de la frontera del sólido $V: x^2 + y^2 \le 4$, $0 \le z \le 3$, orientada hacia afuera.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Gauss.** $\vec f \in C^1(\mathbb{R}^3)$ y $\partial V$ es cerrada, con normal exterior. Los términos $e^{yz}$ y $\mathop{\mathrm{sen}}(xy)$ no aportan a la divergencia:

$$\mathop{\mathrm{div}}\vec f = x^2 + y^2 + z^2$$

**Paso 2 — Cilíndricas.**

$$\Phi = \int_0^{2\pi}\negthinspace\negthinspace\int_0^3\negthinspace\negthinspace\int_0^2(r^2 + z^2)\thinspace r\thinspace dr\thinspace dz\thinspace d\theta$$

**Paso 3 — Calcular.**

- $\displaystyle\int_0^3\negthinspace\int_0^2 r^3\thinspace dr\thinspace dz = 3\cdot4 = 12$.
- $\displaystyle\int_0^3\negthinspace\int_0^2 z^2r\thinspace dr\thinspace dz = 9\cdot2 = 18$.

$$\Phi = 2\pi(12 + 18) = 60\pi$$

</details>

**Respuesta:** $60\pi$.

</details>

---

### P4) Circulación sobre una curva alabeada

Calcule la circulación de $\vec f(x,y,z) = (-y,\ x,\ z)$ a lo largo de la curva intersección del cilindro $x^2 + y^2 = 1$ con la superficie $z = xy$, recorrida en sentido antihorario vista desde el semieje $z$ positivo.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $\vec\alpha(t) = (\cos t,\ \mathop{\mathrm{sen}}t,\ \mathop{\mathrm{sen}}t\cos t)$, $t\in[0,2\pi]$ (antihoraria vista desde arriba).

**Paso 2 — Integrando.** $\vec\alpha' = (-\mathop{\mathrm{sen}}t,\ \cos t,\ z')$ con $z = \tfrac12\mathop{\mathrm{sen}}2t$:

$$\vec f(\vec\alpha)\cdot\vec\alpha' = \mathop{\mathrm{sen}}\nolimits^2t + \cos^2t + z\thinspace z' = 1 + \frac{d}{dt}\left(\frac{z^2}{2}\right)$$

**Paso 3 — Integral.** El segundo término es una derivada exacta de una función periódica: integra $0$ en $[0,2\pi]$.

$$\oint_C\vec f\cdot d\vec s = \int_0^{2\pi}1\thinspace dt = 2\pi$$

</details>

**Respuesta:** $2\pi$.

</details>

---

[← Anterior](practica-segundo-parcial-03.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-05.md)
