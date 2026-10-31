# 2.º Parcial de práctica 01

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Función potencial y trabajo

Defina función potencial de un campo vectorial. Demuestre que si $\vec f = \nabla\phi$ con $\phi \in C^1$, la circulación de $\vec f$ desde $\bar A$ hasta $\bar B$ a lo largo de cualquier curva suave $C$ vale $\phi(\bar B) - \phi(\bar A)$.

Utilice este resultado para calcular el trabajo de $\vec f(x,y,z) = (y^2 + 2xz,\ 2xy + z^2,\ x^2 + 2yz)$ desde $(0,0,0)$ hasta $(1,2,1)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Definición:** $\phi: D \to \mathbb{R}$ diferenciable es **función potencial** de $\vec f$ en el abierto $D$ si $\nabla\phi = \vec f$ en todo $D$.

**Demostración.** Sea $\vec g: [a,b] \to D$ una parametrización de $C$ con $\vec g(a) = \bar A$ y $\vec g(b) = \bar B$. Por la regla de la cadena, $\dfrac{d}{dt}\phi(\vec g(t)) = \nabla\phi(\vec g(t))\cdot\vec g'(t) = \vec f(\vec g(t))\cdot\vec g'(t)$. Entonces:

$$\int_C\vec f\cdot d\vec s = \int_a^b\frac{d}{dt}\phi(\vec g(t))\thinspace dt = \phi(\vec g(b)) - \phi(\vec g(a)) = \phi(\bar B) - \phi(\bar A) \quad\blacksquare$$

**Aplicación.**

*Simetría de la jacobiana* (dominio $\mathbb{R}^3$, simplemente conexo):

- $P'_y = 2y = Q'_x$;
- $P'_z = 2x = R'_x$;
- $Q'_z = 2z = R'_y$.

*Potencial:*

- $\phi = \int(y^2 + 2xz)\thinspace dx = xy^2 + x^2z + D(y,z)$.
- $\phi'_y = 2xy + D'_y = 2xy + z^2 \Rightarrow D = yz^2 + E(z)$.
- $\phi'_z = x^2 + 2yz + E'(z) = x^2 + 2yz \Rightarrow E = k$.

*Trabajo:* con $\phi = xy^2 + x^2z + yz^2$, $W = \phi(1,2,1) - \phi(0,0,0) = 4 + 1 + 2 = 7$.

</details>

**Respuesta:** $\phi(x,y,z) = xy^2 + x^2z + yz^2 + k$ y $W = 7$.

</details>

---

### T2) Ecuación diferencial lineal de 2.º orden

Dada la ecuación diferencial $y'' - 3y' + 2y = f(x)$:

- a) Halle $f(x)$ para que $y = 2x + 1$ resulte solución de la ecuación.
- b) Con la $f$ hallada, obtenga la solución particular que cumple $y(0) = 1$ e $y'(0) = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** Con $y = 2x + 1$, $y' = 2$ e $y'' = 0$:

$$f(x) = 0 - 3\cdot2 + 2(2x + 1) = 4x - 4$$

**b)**

- *Homogénea:* $r^2 - 3r + 2 = 0 \Rightarrow r = 1,\ r = 2$ ⇒ $y_H = C_1e^x + C_2e^{2x}$.
- *Particular:* por a), $y_P = 2x + 1$.
- *S.G.:* $y = C_1e^x + C_2e^{2x} + 2x + 1$.

*Condiciones:*

- $y(0) = C_1 + C_2 + 1 = 1 \Rightarrow C_1 + C_2 = 0$.
- $y'(0) = C_1 + 2C_2 + 2 = 0 \Rightarrow C_1 + 2C_2 = -2$.

Restando: $C_2 = -2$ y $C_1 = 2$.

</details>

**Respuesta:**

- a) $f(x) = 4x - 4$.
- b) $y = 2e^x - 2e^{2x} + 2x + 1$.

</details>

---

## Ejercicios prácticos

### P1) Circulación con Stokes

Calcule la circulación de $\vec f(x,y,z) = (z,\ x,\ y)$ a lo largo de la curva intersección del cilindro $x^2 + y^2 = 4$ con el plano $y + z = 3$, recorrida en sentido antihorario vista desde arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Rotor.**

$$\mathop{\mathrm{rot}}\vec f = (R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y) = (1,\ 1,\ 1)$$

**Paso 2 — Superficie.** Se toma el trozo de plano $z = 3 - y$ encerrado por la curva: $\vec T(x,y) = (x,\ y,\ 3 - y)$ con $D: x^2 + y^2 \le 4$. La normal $\vec N = (-z'_x,\ -z'_y,\ 1) = (0,\ 1,\ 1)$ apunta hacia arriba, compatible con el sentido antihorario visto desde arriba.

**Paso 3 — Stokes.**

$$\oint_C\vec f\cdot d\vec s = \iint_D(1,1,1)\cdot(0,1,1)\thinspace dx\thinspace dy = \iint_D 2\thinspace dx\thinspace dy = 2\cdot4\pi = 8\pi$$

*Control directo:* con $\vec\alpha(t) = (2\cos t,\ 2\mathop{\mathrm{sen}}t,\ 3 - 2\mathop{\mathrm{sen}}t)$, $t\in[0,2\pi]$, la integral de línea también da $8\pi$.

</details>

**Respuesta:** $8\pi$.

</details>

---

### P2) Volumen entre dos paraboloides

Calcule el volumen del cuerpo limitado por las superficies $z = x^2 + y^2$ y $z = 8 - x^2 - y^2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Intersección.** $x^2 + y^2 = 8 - x^2 - y^2 \Rightarrow x^2 + y^2 = 4$: la proyección sobre el plano $xy$ es el disco de radio 2.

**Paso 2 — Planteo en cilíndricas.** Para cada $(r,\theta)$, $z$ va de $r^2$ a $8 - r^2$:

$$V = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2(8 - 2r^2)\thinspace r\thinspace dr\thinspace d\theta$$

**Paso 3 — Calcular.**

$$V = 2\pi\left[4r^2 - \frac{r^4}{2}\right]_0^2 = 2\pi(16 - 8) = 16\pi$$

</details>

**Respuesta:** $V = 16\pi$.

</details>

---

### P3) Flujo a través de una semiesfera

Calcule el flujo de $\vec f(x,y,z) = (x^3,\ y^3,\ z^3)$ a través de la semiesfera $x^2 + y^2 + z^2 = 1$, $z \ge 0$, orientada con normal de tercera componente positiva.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Cerrar la superficie.** Se agrega la tapa $T$: $z = 0$, $x^2 + y^2 \le 1$, con normal saliente $(0,0,-1)$. La semiesfera junto con $T$ encierran la media bola $V$.

**Paso 2 — Divergencia.** $\mathop{\mathrm{div}}\vec f = 3x^2 + 3y^2 + 3z^2 = 3\rho^2$. En esféricas:

$$\iiint_V 3\rho^2\thinspace dV = \int_0^{2\pi}\negthinspace\negthinspace\int_0^{\pi/2}\negthinspace\negthinspace\int_0^1 3\rho^4\mathop{\mathrm{sen}}\varphi\thinspace d\rho\thinspace d\varphi\thinspace d\theta = 2\pi\cdot1\cdot\frac35 = \frac{6\pi}{5}$$

**Paso 3 — Tapa.** Sobre $z = 0$: $\vec f\cdot(0,0,-1) = -z^3 = 0$ ⇒ $\Phi_T = 0$.

**Paso 4 — Resultado.** $\Phi_S = \dfrac{6\pi}{5} - 0 = \dfrac{6\pi}{5}$.

</details>

**Respuesta:** $\dfrac{6\pi}{5}$.

</details>

---

### P4) Masa de una superficie cónica

Calcule la masa de la superficie $S: z = \sqrt{x^2 + y^2}$, $z \le 2$, si su densidad en cada punto es igual a la distancia del punto al plano $xy$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Densidad.** La distancia al plano $xy$ es $\delta = z = \sqrt{x^2 + y^2}$.

**Paso 2 — Elemento de área.** Para $z = \sqrt{x^2 + y^2}$: $z'_x = x/z$, $z'_y = y/z$ ⇒ $d\sigma = \sqrt{1 + \dfrac{x^2 + y^2}{z^2}}\thinspace dA = \sqrt2\thinspace dA$. La proyección es el disco $x^2 + y^2 \le 4$.

**Paso 3 — Polares.**

$$M = \iint_D\sqrt{x^2 + y^2}\cdot\sqrt2\thinspace dA = \sqrt2\int_0^{2\pi}\negthinspace\negthinspace\int_0^2 r\cdot r\thinspace dr\thinspace d\theta = \sqrt2\cdot2\pi\cdot\frac83 = \frac{16\sqrt2\thinspace\pi}{3}$$

</details>

**Respuesta:** $M = \dfrac{16\sqrt2\thinspace\pi}{3}$.

</details>

---

[← Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-02.md)
