# 2.º Parcial de práctica 17

Análisis Matemático II — UTN-FRBA. Parcial **de práctica** armado con el formato de los segundos parciales de la cátedra (unidades 8 a 12): dos ejercicios teóricos y cuatro prácticos. No es un examen oficial; los enunciados y las resoluciones son propios.

> Para aprobar, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta); esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios teóricos

### T1) Flujo del rotor a través de una superficie cerrada

Enuncie el teorema de Stokes. Utilícelo para demostrar que si $\vec f \in C^1(\mathbb{R}^3)$, el flujo de $\mathop{\mathrm{rot}}\vec f$ a través de una esfera es nulo. Calcule el flujo saliente de $\mathop{\mathrm{rot}}\vec f$ a través de $x^2 + y^2 + z^2 = 9$ para $\vec f(x,y,z) = (xy,\ yz,\ zx)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Enunciado:** sea $S$ una superficie suave a trozos, orientable, cuyo borde $\partial S$ es una curva cerrada, simple y suave a trozos, orientada en forma compatible con la normal de $S$. Si $\vec f \in C^1$ en un abierto que contiene a $S$:

$$\iint_S\mathop{\mathrm{rot}}\vec f\cdot\breve n\thinspace d\sigma = \oint_{\partial S}\vec f\cdot d\vec s$$

**Demostración.** Se corta la esfera por el ecuador $E$ en dos semiesferas $S_1$ (superior) y $S_2$ (inferior), ambas con la normal exterior.

- Para $S_1$ (normal hacia arriba), el borde compatible es $E$ recorrido en sentido antihorario visto desde arriba.
- Para $S_2$ (normal hacia abajo), el borde compatible es $E$ en sentido **horario**.

Las dos circulaciones son opuestas:

$$\iint_{S}\mathop{\mathrm{rot}}\vec f\cdot\breve n\thinspace d\sigma = \oint_{E^+}\vec f\cdot d\vec s + \oint_{E^-}\vec f\cdot d\vec s = 0 \quad\blacksquare$$

**Aplicación.** $\vec f$ es polinómico ($C^1$ en $\mathbb{R}^3$) ⇒ el flujo es $0$. (También sale por Gauss: $\mathop{\mathrm{div}}(\mathop{\mathrm{rot}}\vec f) = 0$.)

</details>

**Respuesta:** $0$.

</details>

---

### T2) Línea de campo y su longitud

Halle la línea de campo de $\vec f(x,y) = (y,\ -x)$ que pasa por el punto $(3,4)$ y calcule su longitud.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Ecuación.** $\dfrac{dx}{y} = \dfrac{dy}{-x} \Rightarrow x\thinspace dx + y\thinspace dy = 0$.

**Paso 2 — Integrar.** $x^2 + y^2 = C$; por $(3,4)$, $C = 25$: es la circunferencia de radio 5.

**Paso 3 — Longitud.** $2\pi\cdot5 = 10\pi$.

</details>

**Respuesta:** $x^2 + y^2 = 25$; longitud $10\pi$.

</details>

---

## Ejercicios prácticos

### P1) Circulación alrededor de una singularidad

Calcule la circulación de

$$\vec f(x,y) = \left(\frac{-y}{x^2 + y^2} + x^2,\ \frac{x}{x^2 + y^2} + y\right)$$

a lo largo de la elipse $\dfrac{x^2}{4} + y^2 = 1$ en sentido antihorario.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Separar.** $\vec f = \vec g + \vec h$ con $\vec g = \left(\dfrac{-y}{x^2 + y^2},\ \dfrac{x}{x^2 + y^2}\right)$ y $\vec h = (x^2,\ y)$.

**Paso 2 — Parte $\vec h$.** $\vec h = \nabla\left(\tfrac{x^3}{3} + \tfrac{y^2}{2}\right)$ es conservativo en $\mathbb{R}^2$ ⇒ circulación $0$.

**Paso 3 — Parte $\vec g$.** No es $C^1$ en el origen, que está dentro de la elipse. Se aplica Green en la región $D$ entre la elipse y una circunferencia chica $C_\varepsilon$ de radio $\varepsilon$:

- En $D$ el integrando de Green es nulo ($Q'_x = P'_y$), así que la circulación de $\vec g$ sobre la elipse es igual a la circulación sobre la circunferencia chica (ambas antihorarias).
- Sobre $C_\varepsilon$: $\vec\alpha = (\varepsilon\cos t,\ \varepsilon\mathop{\mathrm{sen}}t)$ ⇒ $\vec g\cdot\vec\alpha' = \mathop{\mathrm{sen}}\nolimits^2t + \cos^2t = 1$, integral $2\pi$.

**Paso 4 — Resultado.** $2\pi + 0 = 2\pi$.

</details>

**Respuesta:** $2\pi$.

</details>

---

### P2) Área de un trozo de plano

Calcule el área de la porción del plano $z = 2x + 2y$ interior al cilindro $x^2 + y^2 = 1$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Elemento de área.** $d\sigma = \sqrt{1 + 2^2 + 2^2}\thinspace dA = 3\thinspace dA$.

**Paso 2 — Resultado.** La proyección es el disco unitario (área $\pi$) ⇒ $A = 3\pi$.

</details>

**Respuesta:** $A = 3\pi$.

</details>

---

### P3) Flujo a través de un paraboloide

Calcule el flujo de $\vec f(x,y,z) = (x,\ y,\ 3)$ a través de $S: z = 1 - x^2 - y^2$, $z \ge 0$, orientada hacia arriba.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Normal.** $\vec T(x,y) = (x,\ y,\ 1 - x^2 - y^2)$ ⇒ $\vec N = (2x,\ 2y,\ 1)$, hacia arriba ✓.

**Paso 2 — Integrando.** $\vec f\cdot\vec N = 2x^2 + 2y^2 + 3$.

**Paso 3 — Polares.**

$$\Phi = \int_0^{2\pi}\negthinspace\negthinspace\int_0^1(2r^2 + 3)\thinspace r\thinspace dr\thinspace d\theta = 2\pi\left(\frac12 + \frac32\right) = 4\pi$$

</details>

**Respuesta:** $4\pi$.

</details>

---

### P4) Resonancia

Resuelva $y'' - 4y = 8e^{2x}$ con $y(0) = 0$ e $y'(0) = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Homogénea.** $r = \pm2$ ⇒ $y_H = C_1e^{2x} + C_2e^{-2x}$.

**Paso 2 — Particular.** $2$ es raíz simple ⇒ $y_P = Axe^{2x}$. Con $y_P' = A(1 + 2x)e^{2x}$ e $y_P'' = A(4 + 4x)e^{2x}$:

$$y_P'' - 4y_P = 4Ae^{2x} = 8e^{2x} \Rightarrow A = 2$$

**Paso 3 — Constantes.**

- $y(0) = C_1 + C_2 = 0$.
- $y'(0) = 2C_1 - 2C_2 + 2 = 0 \Rightarrow C_1 - C_2 = -1$.

Entonces $C_1 = -\tfrac12$, $C_2 = \tfrac12$.

</details>

**Respuesta:** $y = -\dfrac12e^{2x} + \dfrac12e^{-2x} + 2xe^{2x}$.

</details>

---

[← Anterior](practica-segundo-parcial-16.md) · [Volver al menú principal](../README.md) · [Siguiente →](practica-segundo-parcial-18.md)
