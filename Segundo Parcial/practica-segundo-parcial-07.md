# 2.º Parcial de práctica 07

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Independencia del camino

Defina campo conservativo. Demuestre que la circulación de un campo conservativo $C^1$ a lo largo de una curva cerrada suave a trozos es nula.

Calcule el trabajo de $\vec f(x,y) = (e^y,\ xe^y + 2y)$ desde $(0,0)$ hasta $(2, \ln3)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Definición:** $\vec f$ es **conservativo** en un abierto $D$ si existe $\phi$ diferenciable con $\nabla\phi = \vec f$ en $D$.

**Demostración.** Si $\vec\alpha: [a,b] \to D$ parametriza la curva, por la regla de la cadena $\vec f(\vec\alpha)\cdot\vec\alpha' = (\phi\circ\vec\alpha)'$, entonces:

$$\oint_C\vec f\cdot d\vec s = \phi(\vec\alpha(b)) - \phi(\vec\alpha(a)) = 0$$

porque la curva es cerrada: $\vec\alpha(b) = \vec\alpha(a)$. Si es suave a trozos, se suman los tramos y las contribuciones intermedias se cancelan. $\blacksquare$

**Aplicación.**

*Simetría:* $P'_y = e^y = Q'_x$ en $\mathbb{R}^2$ ⇒ conservativo.

*Potencial:* $\phi = \int e^y\thinspace dx = xe^y + D(y)$; $\phi'_y = xe^y + D' = xe^y + 2y \Rightarrow D = y^2$.

*Trabajo:* $\phi(2,\ln3) - \phi(0,0) = 2\cdot3 + \ln^2 3 = 6 + \ln^2 3$.

</details>

**Respuesta:** $W = 6 + \ln^2 3$.

</details>

---

### T2) Flujo a través de superficies con el mismo borde

Determine la veracidad de la siguiente afirmación y justifique:

> Si $S_1$ y $S_2$ son dos superficies con el mismo borde, orientadas en forma compatible con el mismo sentido de recorrido del borde, entonces el flujo de cualquier campo $\vec f \in C^1(\mathbb{R}^3)$ a través de $S_1$ es igual al flujo a través de $S_2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Análisis.** Por Stokes, la igualdad vale si $\vec f$ es un **rotor** ($\vec f = \mathop{\mathrm{rot}}\vec g$): ambos flujos valen la circulación de $\vec g$ sobre el borde. Para un campo cualquiera no tiene por qué valer.

**Contraejemplo.** $\vec f = (0,0,z)$, borde: la circunferencia $x^2 + y^2 = 1$, $z = 0$, recorrida en sentido antihorario visto desde arriba.

- $S_1$: el disco $z = 0$, normal $\breve k$. Allí $\vec f = \vec 0$ ⇒ $\Phi_1 = 0$.
- $S_2$: la semiesfera superior, normal hacia arriba. Con Gauss sobre la media bola ($\mathop{\mathrm{div}}\vec f = 1$): $\Phi_2 - \Phi_1 = \text{Vol} = \tfrac{2\pi}{3}$ ⇒ $\Phi_2 = \tfrac{2\pi}{3}$.

Los flujos son distintos.

</details>

**Respuesta:** **Falsa**. Sólo vale para campos que son rotores (o, más en general, con divergencia nula). Contraejemplo: $\vec f = (0,0,z)$ da flujo $0$ por el disco y $\tfrac{2\pi}{3}$ por la semiesfera.

</details>

---

## Ejercicios prácticos

### P1) Circulación con Green

Calcule la circulación de $\vec f(x,y) = (x - y^3,\ x^3 + y)$ a lo largo de la circunferencia $x^2 + y^2 = 4$ recorrida en sentido antihorario.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Green.** $\vec f$ es polinómico ⇒ $C^1$. $Q'_x - P'_y = 3x^2 + 3y^2$.

**Paso 2 — Polares.**

$$\oint_C\vec f\cdot d\vec s = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2 3r^2\cdot r\thinspace dr\thinspace d\theta = 2\pi\cdot\frac{3\cdot16}{4} = 24\pi$$

</details>

**Respuesta:** $24\pi$.

</details>

---

### P2) Flujo saliente con Gauss

Calcule el flujo saliente de $\vec f(x,y,z) = (x,\ y,\ 2z)$ a través de la frontera del sólido limitado por $z = x^2 + y^2$ y $z = 4$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Gauss.** $\mathop{\mathrm{div}}\vec f = 1 + 1 + 2 = 4$ ⇒ $\Phi = 4\cdot\text{Vol}(V)$.

**Paso 2 — Volumen.** En cilíndricas, $r^2 \le z \le 4$ con $r\in[0,2]$:

$$\text{Vol} = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2(4 - r^2)\thinspace r\thinspace dr\thinspace d\theta = 2\pi(8 - 4) = 8\pi$$

**Paso 3 — Resultado.** $\Phi = 32\pi$.

</details>

**Respuesta:** $32\pi$.

</details>

---

### P3) Ecuación diferencial no homogénea

Resuelva $y'' - y' - 2y = 4x$ con $y(0) = 0$ e $y'(0) = 1$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Homogénea.** $r^2 - r - 2 = 0 \Rightarrow r = 2,\ r = -1$ ⇒ $y_H = C_1e^{2x} + C_2e^{-x}$.

**Paso 2 — Particular.** $y_P = Ax + B$: $-A - 2(Ax + B) = 4x$ ⇒ $A = -2$ y $-A - 2B = 0 \Rightarrow B = 1$. Así $y_P = 1 - 2x$.

**Paso 3 — Constantes.** $y = C_1e^{2x} + C_2e^{-x} + 1 - 2x$:

- $y(0) = C_1 + C_2 + 1 = 0$.
- $y'(0) = 2C_1 - C_2 - 2 = 1$.

Sumando: $3C_1 - 1 = 1 \Rightarrow C_1 = \tfrac23$, y $C_2 = -\tfrac53$.

</details>

**Respuesta:** $y = \dfrac23e^{2x} - \dfrac53e^{-x} + 1 - 2x$.

</details>

---

### P4) Circulación sobre un arco

Calcule la circulación de $\vec f(x,y,z) = (2x,\ z,\ -y)$ a lo largo de la curva intersección de $y = x^2$ con $z = x$, desde $(0,0,0)$ hasta $(1,1,1)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $\vec\alpha(t) = (t,\ t^2,\ t)$, $t\in[0,1]$, con $\vec\alpha' = (1,\ 2t,\ 1)$.

**Paso 2 — Integrando.** $\vec f(\vec\alpha) = (2t,\ t,\ -t^2)$:

$$\vec f\cdot\vec\alpha' = 2t + 2t^2 - t^2 = 2t + t^2$$

**Paso 3 — Integral.**

$$\int_0^1(2t + t^2)\thinspace dt = 1 + \frac13 = \frac43$$

</details>

**Respuesta:** $\dfrac43$.

</details>

---

[← Anterior](practica-segundo-parcial-06.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-08.md)
