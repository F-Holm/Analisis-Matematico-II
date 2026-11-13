# 2.º Parcial de práctica 19

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) ¿Puede ser un rotor?

Defina divergencia y rotor de un campo vectorial. Demuestre que si $\vec g \in C^2(\mathbb{R}^3)$ entonces $\mathop{\mathrm{div}}(\mathop{\mathrm{rot}}\vec g) = 0$. ¿Existe $\vec g \in C^2(\mathbb{R}^3)$ tal que $\mathop{\mathrm{rot}}\vec g = (x,\ y,\ z)$?

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Definiciones:** para $\vec f = (P,Q,R) \in C^1$,

- $\mathop{\mathrm{div}}\vec f = \nabla\cdot\vec f = P'_x + Q'_y + R'_z$;
- $\mathop{\mathrm{rot}}\vec f = \nabla\times\vec f = (R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y)$.

**Demostración.** Con $\vec g = (P,Q,R)$:

```math
\mathop{\mathrm{div}}(\mathop{\mathrm{rot}}\vec g) = (R''_{yx} - Q''_{zx}) + (P''_{zy} - R''_{xy}) + (Q''_{xz} - P''_{yz}) = 0
```

por Schwarz, ya que $\vec g \in C^2$. $\blacksquare$

**Aplicación.** Si existiera, $\mathop{\mathrm{div}}(x,y,z) = 3$ debería ser $0$. Contradicción.

</details>

**Respuesta:** **No** existe: $\mathop{\mathrm{div}}(x,y,z) = 3 \ne 0$, y la divergencia de un rotor siempre es nula.

</details>

---

### T2) Ecuación a partir de su solución general

Halle la ecuación diferencial lineal de 2.º orden a coeficientes constantes, de la forma $y'' + ay' + by = f(x)$, cuya solución general es $y = C_1e^x + C_2e^{3x} + x$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Homogénea.** $e^x$ y $e^{3x}$ ⇒ raíces $1$ y $3$: $(r - 1)(r - 3) = r^2 - 4r + 3$ ⇒ $a = -4$, $b = 3$.

**Paso 2 — $f(x)$.** $y_P = x$ debe ser solución: $y_P'' - 4y_P' + 3y_P = 0 - 4 + 3x$.

</details>

**Respuesta:** $y'' - 4y' + 3y = 3x - 4$.

</details>

---

## Ejercicios prácticos

### P1) Área de una esfera dentro de un cilindro

Calcule el área de la porción de la esfera $x^2 + y^2 + z^2 = 4$ con $z \ge 0$ que es interior al cilindro $x^2 + y^2 = 1$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Elemento de área.** $z = \sqrt{4 - x^2 - y^2}$ ⇒ $d\sigma = \dfrac{2}{\sqrt{4 - x^2 - y^2}}\thinspace dA$.

**Paso 2 — Polares** sobre $r \le 1$:

$$A = \int_0^{2\pi}\negthinspace\negthinspace\int_0^1\frac{2r}{\sqrt{4 - r^2}}\thinspace dr\thinspace d\theta = 2\pi\left[-2\sqrt{4 - r^2}\right]_0^1 = 2\pi(4 - 2\sqrt3) = 4\pi(2 - \sqrt3)$$

*Control con Arquímedes:* el casquete va de $z = \sqrt3$ a $z = 2$, altura $h = 2 - \sqrt3$: $2\pi\cdot2\cdot h$ ✓.

</details>

**Respuesta:** $A = 4\pi(2 - \sqrt3)$.

</details>

---

### P2) Flujo saliente de una esfera

Calcule el flujo de $\vec f(x,y,z) = (xy^2,\ yz^2,\ zx^2)$ a través de la esfera $x^2 + y^2 + z^2 = 4$, orientada hacia afuera.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Gauss.** $\mathop{\mathrm{div}}\vec f = y^2 + z^2 + x^2 = \rho^2$.

**Paso 2 — Esféricas.**

$$\Phi = \int_0^{2\pi}\negthinspace\negthinspace\int_0^{\pi}\negthinspace\negthinspace\int_0^2\rho^4\mathop{\mathrm{sen}}\varphi\thinspace d\rho\thinspace d\varphi\thinspace d\theta = 2\pi\cdot2\cdot\frac{32}{5} = \frac{128\pi}{5}$$

</details>

**Respuesta:** $\dfrac{128\pi}{5}$.

</details>

---

### P3) Circulación sobre un tramo de hélice

Calcule la circulación de $\vec f(x,y,z) = (z,\ x,\ y)$ a lo largo de la hélice $\vec\alpha(t) = (\cos t,\ \mathop{\mathrm{sen}}t,\ t)$, desde $(1,0,0)$ hasta $\left(0,1,\tfrac{\pi}{2}\right)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parámetro.** $t\in[0, \pi/2]$, $\vec\alpha' = (-\mathop{\mathrm{sen}}t,\ \cos t,\ 1)$.

**Paso 2 — Integrando.** $\vec f(\vec\alpha) = (t,\ \cos t,\ \mathop{\mathrm{sen}}t)$:

$$\vec f\cdot\vec\alpha' = -t\mathop{\mathrm{sen}}t + \cos^2t + \mathop{\mathrm{sen}}t$$

**Paso 3 — Integrales.**

- $\displaystyle\int_0^{\pi/2}t\mathop{\mathrm{sen}}t\thinspace dt = \left[-t\cos t + \mathop{\mathrm{sen}}t\right]_0^{\pi/2} = 1$ (por partes).
- $\displaystyle\int_0^{\pi/2}\cos^2t\thinspace dt = \frac{\pi}{4}$.
- $\displaystyle\int_0^{\pi/2}\mathop{\mathrm{sen}}t\thinspace dt = 1$.

$$\int_C\vec f\cdot d\vec s = -1 + \frac{\pi}{4} + 1 = \frac{\pi}{4}$$

</details>

**Respuesta:** $\dfrac{\pi}{4}$.

</details>

---

### P4) Volumen dentro de un cilindro desplazado

Calcule el volumen del cuerpo limitado por el paraboloide $z = 4 - x^2 - y^2$, el plano $z = 0$ y el cilindro $x^2 + y^2 = 2y$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Proyección.** $x^2 + y^2 \le 2y$: en polares $r \le 2\mathop{\mathrm{sen}}\theta$, $\theta\in[0,\pi]$. Allí $r \le 2$, así que $4 - r^2 \ge 0$.

**Paso 2 — Integral.**

$$V = \int_0^{\pi}\negthinspace\int_0^{2\mathop{\mathrm{sen}}\theta}(4 - r^2)\thinspace r\thinspace dr\thinspace d\theta = \int_0^{\pi}\left(8\mathop{\mathrm{sen}}\nolimits^2\theta - 4\mathop{\mathrm{sen}}\nolimits^4\theta\right)d\theta$$

**Paso 3 — Calcular.** $\displaystyle\int_0^{\pi}\mathop{\mathrm{sen}}\nolimits^2\theta\thinspace d\theta = \frac{\pi}{2}$ y $\displaystyle\int_0^{\pi}\mathop{\mathrm{sen}}\nolimits^4\theta\thinspace d\theta = \frac{3\pi}{8}$:

$$V = 4\pi - \frac{3\pi}{2} = \frac{5\pi}{2}$$

</details>

**Respuesta:** $V = \dfrac{5\pi}{2}$.

</details>

---

[← Anterior](practica-segundo-parcial-18.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-20.md)
