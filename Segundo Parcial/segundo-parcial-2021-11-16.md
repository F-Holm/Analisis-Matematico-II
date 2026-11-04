# 2.º Parcial (16/11/2021) — Curso Z2004, temas 1 y 3

Análisis Matemático II — UTN-FRBA.

Enunciados (fotos, sin resolución oficial): [Tema 1](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-2021-11-16-Z2004-Tema1.jpeg) y [Tema 3](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-2021-11-16-Z2004-Tema3.jpeg).

- [Tema 1](#tema-1)
- [Tema 3](#tema-3)

> Para aprobar los TP, deben estar bien al menos dos ejercicios prácticos (los teóricos no son tenidos en cuenta) esto equivale a una calificación de 6. Para aspirar a aprobación directa es necesario tener al menos cuatro ejercicios bien, uno de ellos un teórico. Esto equivale a una calificación de 8D.

Las resoluciones son propias (no hay solución de la cátedra). Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Tema 1

### Ejercicios Prácticos

#### P1) Masa de medio cono macizo

Calcular la maza del macizo H definido por $\sqrt{x^2 + z^2} \le y \le 3;\ z \ge 0,$ si la densidad en cada punto del mismo está dada por $\delta(x,y,z) = x^2 + z^2$. Graficar el macizo.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Gráfico.** $y = \sqrt{x^2 + z^2}$ es un cono con vértice en el origen y eje $y$, que se abre hacia $y > 0$. El macizo es lo que queda dentro del cono hasta el plano $y = 3$ (la "tapa" es un disco de radio 3), cortado a la mitad por $z \ge 0$.

**Paso 2 — Cilíndricas con eje $y$.** $x = r\cos\theta$, $z = r\mathop{\mathrm{sen}}\theta$, $y = y$, jacobiano $r$. Entonces $r \le y \le 3$, $0 \le r \le 3$, y $z \ge 0 \iff 0 \le \theta \le \pi$. La densidad es $\delta = r^2$.

**Paso 3 — Calcular.**

$$M = \int_0^{\pi}\negthinspace\negthinspace\int_0^3\negthinspace\negthinspace\int_r^3 r^2\cdot r\thinspace dy\thinspace dr\thinspace d\theta = \pi\int_0^3 r^3(3 - r)\thinspace dr = \pi\left(\frac{3\cdot 81}{4} - \frac{243}{5}\right) = \frac{243\pi}{20}$$

</details>

**Respuesta:** $M = \dfrac{243\pi}{20}$.

</details>

---

#### P2) Flujo a través de un paraboloide cortado por un plano

Calcule el flujo de $\bar f(x,y,z) = (2y - 6;\ -2x;\ -z + 2y)$ a través de la porción de superficie $z = 9 - x^2 - (y - 3)^2$ con $z \ge 2y$ . Indique la orientación elegida para la superficie.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Proyección.** $9 - x^2 - (y - 3)^2 \ge 2y \iff x^2 + y^2 - 4y \le 0 \iff x^2 + (y - 2)^2 \le 4$: disco $D$ de centro $(0,2)$ y radio 2.

**Paso 2 — Normal.** $\vec T(x,y) = (x,\ y,\ 9 - x^2 - (y - 3)^2)$, con normal hacia arriba $\vec n = (-z'_x, -z'_y, 1) = (2x,\ 2(y - 3),\ 1)$.

**Paso 3 — Producto escalar.**

$$\bar f\cdot\vec n = (2y - 6)\thinspace 2x - 2x\cdot 2(y - 3) + (-z + 2y) = -z + 2y$$

Reemplazando $z$: $-9 + x^2 + (y - 3)^2 + 2y = x^2 + y^2 - 4y = x^2 + (y - 2)^2 - 4$.

**Paso 4 — Polares centradas en $(0,2)$.** $x = \rho\cos\theta$, $y = 2 + \rho\mathop{\mathrm{sen}}\theta$:

$$\Phi = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2(\rho^2 - 4)\thinspace\rho\thinspace d\rho\thinspace d\theta = 2\pi(4 - 8) = -8\pi$$

</details>

**Respuesta:** Con normal hacia arriba ($z$ positiva), $\Phi = -8\pi$ (con la normal opuesta, $8\pi$).

</details>

---

#### P3) Integral de línea de un campo exacto

Calcular $\int_C(y - 4xe^{y^2})dx + (x - 4yx^2e^{y^2})dy$ si C es el arco de curva de ecuación $\bar\gamma(t) = (e^{t^2 - t} - 2t;\ t - t^2)$ con $0 \le t \le 1$. Justifique el procedimiento utilizado.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Simetría.** $P = y - 4xe^{y^2}$, $Q = x - 4yx^2e^{y^2}$:

$$P'_y = 1 - 8xye^{y^2} = Q'_x$$

El campo es $C^1$ en $\mathbb{R}^2$ (simplemente conexo) ⇒ es conservativo y la integral no depende del camino.

**Paso 2 — Potencial.**

- $\varphi = \int(y - 4xe^{y^2})\thinspace dx = xy - 2x^2e^{y^2} + D(y)$.
- $\varphi'_y = x - 4x^2ye^{y^2} + D'(y) = Q \Rightarrow D = \text{cte}$.

**Paso 3 — Extremos.** $\bar\gamma(0) = (1, 0)$, $\bar\gamma(1) = (e^0 - 2,\ 0) = (-1, 0)$.

**Paso 4 — Integral.**

$$\int_C = \varphi(-1,0) - \varphi(1,0) = (0 - 2) - (0 - 2) = 0$$

</details>

**Respuesta:** $0$ (el campo es conservativo, con potencial $\varphi = xy - 2x^2e^{y^2}$).

</details>

---

#### P4) Circulación sobre una semicircunferencia con Green

Siendo $\bar f(x,y) = (y + x;\ 5x + \varphi(y))$ con $\bar f \in C^1(R^2)$, calcule la circulación de $\bar f$ desde el punto (0,0) hasta (2,0) a lo largo de la curva C de ecuación $x^2 + y^2 = 2x$ con $y \ge 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Curva.** $(x - 1)^2 + y^2 = 1$ con $y \ge 0$: semicircunferencia superior de centro $(1,0)$, recorrida de $(0,0)$ a $(2,0)$, es decir, en sentido **horario**.

**Paso 2 — Cerrar.** Se agrega el segmento $C_1$ de $(2,0)$ a $(0,0)$. $C \cup C_1$ encierra el semidisco $D$ (área $\frac{\pi}{2}$) en sentido horario.

**Paso 3 — Green** (con signo menos por ser horario):

$$\oint_{C\cup C_1}\bar f\cdot d\bar s = -\iint_D(Q'_x - P'_y)\thinspace dA = -\iint_D(5 - 1)\thinspace dA = -4\cdot\frac{\pi}{2} = -2\pi$$

**Paso 4 — Segmento.** En $C_1$: $y = 0$, $dy = 0$, $x$ de 2 a 0:

$$\int_{C_1}\bar f\cdot d\bar s = \int_2^0 x\thinspace dx = -2$$

**Paso 5 — Despejar.**

$$\int_C\bar f\cdot d\bar s = -2\pi - (-2) = 2 - 2\pi$$

</details>

**Respuesta:** $\displaystyle\int_C\bar f\cdot d\bar s = 2 - 2\pi$.

</details>

---

### Ejercicios teóricos

#### T1) EDO con raíz doble y recta tangente

Dada la ecuación diferencial $y'' + ay' + by = 3e^x$

a. hallar los valores de $a$ y $b$ si se sabe que $y_1(x) = xe^{2x}$ es una solución de la ecuación diferencial $y'' + ay' + by = 0$

b. Hallar la solución de la ecuación diferencial $y'' + ay' + by = 3e^x$ con recta tangente de ecuación $y = 2x + 3$ en $(0, y_0)$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** $xe^{2x}$ es solución de la homogénea solo si $r = 2$ es raíz **doble** de la ecuación característica:

$$(r - 2)^2 = r^2 - 4r + 4 \quad\Longrightarrow\quad a = -4,\ b = 4$$

**b) Paso 1 — Homogénea.** $y_h = (C_1 + C_2x)e^{2x}$.

**Paso 2 — Particular.** $e^x$ no es solución de la homogénea: $y_p = Ae^x$. $A(1 - 4 + 4)e^x = 3e^x \Rightarrow A = 3$.

**Paso 3 — Condiciones.** La recta tangente en $x = 0$ da $y(0) = 3$ (ordenada al origen) e $y'(0) = 2$ (pendiente).

- $y(0) = C_1 + 3 = 3 \Rightarrow C_1 = 0$.
- $y' = C_2e^{2x} + 2C_2xe^{2x} + 3e^x \Rightarrow y'(0) = C_2 + 3 = 2 \Rightarrow C_2 = -1$.

</details>

**Respuesta:** a) $a = -4$, $b = 4$. b) $y = -xe^{2x} + 3e^x$.

</details>

---

#### T2) Campo con singularidad en el origen

Dado el campo vectorial $\bar f(x,y) = \left(-\dfrac{y}{4x^2 + y^2};\ \dfrac{x}{4x^2 + y^2}\right)$

a) Determinar si el mismo admite función potencial en su dominio.

b) ¿Es posible conocer el valor $\int_C\bar f\thinspace\overline{ds}$ siendo C cualquier curva cerrada que encierra al origen? Justifique.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a) Paso 1 — Dominio.** $D = \mathbb{R}^2 - \{(0,0)\}$, que no es simplemente conexo.

**Paso 2 — Simetría.**

$$P'_y = -\frac{(4x^2 + y^2) - 2y^2}{(4x^2 + y^2)^2} = \frac{y^2 - 4x^2}{(4x^2 + y^2)^2}, \qquad Q'_x = \frac{(4x^2 + y^2) - 8x^2}{(4x^2 + y^2)^2} = \frac{y^2 - 4x^2}{(4x^2 + y^2)^2}$$

La jacobiana es simétrica, pero como $D$ no es simplemente conexo eso no alcanza.

**Paso 3 — Circulación sobre la elipse $4x^2 + y^2 = 1$.** $\vec\alpha(t) = \left(\frac{\cos t}{2},\ \mathop{\mathrm{sen}}t\right)$, $0 \le t \le 2\pi$. Sobre ella el denominador vale 1:

$$\oint\bar f\cdot d\bar s = \int_0^{2\pi}\left(-\mathop{\mathrm{sen}}t\cdot\left(-\frac{\mathop{\mathrm{sen}}t}{2}\right) + \frac{\cos t}{2}\cos t\right)dt = \int_0^{2\pi}\frac12\thinspace dt = \pi \ne 0$$

Hay una curva cerrada en $D$ con circulación no nula ⇒ **no** admite función potencial en su dominio.

**b)** Sí. Si $C$ es cerrada, simple, encierra al origen y está orientada positivamente, se aplica Green a la región entre $C$ y una elipse chica $E$: $4x^2 + y^2 = \varepsilon^2$ (contenida dentro de $C$). Como $Q'_x - P'_y = 0$ allí, $\oint_C = \oint_E = \pi$ (el mismo cálculo del paso 3 escalado da $\pi$ para todo $\varepsilon$).

</details>

**Respuesta:** a) No admite potencial en $\mathbb{R}^2 - \{0\}$: la circulación sobre $4x^2 + y^2 = 1$ vale $\pi$. b) Sí: para toda curva cerrada simple que encierre al origen vale $\pi$ en sentido positivo ($-\pi$ en sentido negativo).

</details>

---

## Tema 3

### Ejercicios Prácticos

#### P1) Masa de medio cono macizo

Calcular la maza del macizo H definido por $\sqrt{x^2 + z^2} \le y \le 2;\ z \ge 0,$ si la densidad en cada punto del mismo está dada por $\delta(x,y,z) = 2x^2 + 2z^2$. Graficar el macizo.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Gráfico.** Mitad superior ($z \ge 0$) del cono macizo de eje $y$, vértice en el origen, cerrado por el plano $y = 2$ (tapa: semidisco de radio 2).

**Paso 2 — Cilíndricas con eje $y$.** $x = r\cos\theta$, $z = r\mathop{\mathrm{sen}}\theta$: $r \le y \le 2$, $0 \le r \le 2$, $0 \le \theta \le \pi$, $\delta = 2r^2$.

**Paso 3 — Calcular.**

$$M = \int_0^{\pi}\negthinspace\negthinspace\int_0^2\negthinspace\negthinspace\int_r^2 2r^2\cdot r\thinspace dy\thinspace dr\thinspace d\theta = 2\pi\int_0^2 r^3(2 - r)\thinspace dr = 2\pi\left(8 - \frac{32}{5}\right) = \frac{16\pi}{5}$$

</details>

**Respuesta:** $M = \dfrac{16\pi}{5}$.

</details>

---

#### P2) Flujo a través de un paraboloide cortado por un plano

Calcule el flujo de $\bar f(x,y,z) = (2y - 8;\ -2x;\ z - 4y)$ a través de la porción de superficie $z = 16 - x^2 - (y - 4)^2$ con $z \ge 4y$ . Indique la orientación elegida para la superficie.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Proyección.** $16 - x^2 - (y - 4)^2 \ge 4y \iff x^2 + y^2 - 4y \le 0 \iff x^2 + (y - 2)^2 \le 4$.

**Paso 2 — Normal hacia arriba.** $\vec n = (2x,\ 2(y - 4),\ 1)$.

**Paso 3 — Producto escalar.**

$$\bar f\cdot\vec n = (2y - 8)\thinspace 2x - 2x\cdot 2(y - 4) + z - 4y = z - 4y = -\left(x^2 + y^2 - 4y\right) = -\left(x^2 + (y - 2)^2 - 4\right)$$

**Paso 4 — Polares centradas en $(0,2)$.**

$$\Phi = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2(4 - \rho^2)\thinspace\rho\thinspace d\rho\thinspace d\theta = 2\pi(8 - 4) = 8\pi$$

</details>

**Respuesta:** Con normal hacia arriba, $\Phi = 8\pi$ (con la normal opuesta, $-8\pi$).

</details>

---

#### P3) Integral de línea (¿campo exacto?)

Calcular $\int_C(y - 4xy^2e^{x^2})dx + (x - 2y\thinspace e^{x^2})dy$ si C es el arco de curva de ecuación $\bar\gamma(t) = (t - t^2;\ e^{t^2 - t} - 2t)$ con $0 \le t \le 1$. Justifique el procedimiento utilizado.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Simetría.** $P = y - 4xy^2e^{x^2}$, $Q = x - 2ye^{x^2}$:

$$P'_y = 1 - 8xye^{x^2}, \qquad Q'_x = 1 - 4xye^{x^2}$$

**Con el enunciado tal como está, el campo no es conservativo.** Lo más probable es una errata: con $2xy^2e^{x^2}$ en lugar de $4xy^2e^{x^2}$ queda $P'_y = Q'_x$ (es la versión "espejada" del P3 del Tema 1). Se resuelven las dos lecturas.

**Paso 2 — Extremos.** $\bar\gamma(0) = (0, 1)$, $\bar\gamma(1) = (0,\ e^0 - 2) = (0, -1)$.

**Paso 3 — Versión corregida ($2xy^2e^{x^2}$).** Potencial $\varphi = xy - y^2e^{x^2}$ ($\varphi'_x = y - 2xy^2e^{x^2}$, $\varphi'_y = x - 2ye^{x^2}$):

$$\int_C = \varphi(0,-1) - \varphi(0,1) = (-1) - (-1) = 0$$

**Paso 4 — Versión literal.** Se escribe $\bar f = \nabla\varphi + (-2xy^2e^{x^2},\ 0)$. La parte gradiente aporta 0 (paso 3) y queda

$$\int_C -2xy^2e^{x^2}\thinspace dx = \int_0^1 -2x(t)\thinspace y(t)^2e^{x(t)^2}x'(t)\thinspace dt, \qquad x = t - t^2,\ y = e^{t^2 - t} - 2t$$

que no tiene primitiva elemental; numéricamente vale $\approx 0{,}0181$.

</details>

**Respuesta:** Con la errata corregida ($2xy^2e^{x^2}$), el campo es conservativo y la integral vale $0$. Con el enunciado literal el campo no es conservativo y la integral vale $\approx 0{,}0181$ (solo numéricamente).

</details>

---

#### P4) Circulación sobre una semicircunferencia con Green

Siendo $\bar f(x,y) = (y + \omega(x);\ 5x + y)$ con $\bar f \in C^1(R^2)$, calcule la circulación de $\bar f$ desde el punto (0,4) hasta (0,0) a lo largo de la curva C de ecuación $x^2 + y^2 = 4y$ con $x \ge 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Curva.** $x^2 + (y - 2)^2 = 4$ con $x \ge 0$: semicircunferencia derecha de centro $(0,2)$ y radio 2, recorrida de $(0,4)$ a $(0,0)$ pasando por $(2,2)$: sentido **horario**.

**Paso 2 — Cerrar** con el segmento $C_1$ sobre el eje $y$ de $(0,0)$ a $(0,4)$. Se encierra el semidisco $D$ de área $2\pi$, en sentido horario.

**Paso 3 — Green.**

$$\oint_{C\cup C_1}\bar f\cdot d\bar s = -\iint_D(5 - 1)\thinspace dA = -4\cdot 2\pi = -8\pi$$

**Paso 4 — Segmento.** En $C_1$: $x = 0$, $dx = 0$: $\int_0^4 y\thinspace dy = 8$.

**Paso 5 — Despejar.** $\int_C = -8\pi - 8$.

</details>

**Respuesta:** $\displaystyle\int_C\bar f\cdot d\bar s = -8\pi - 8$.

</details>

---

### Ejercicios teóricos

#### T1) EDO con raíz doble y recta tangente

Dada la ecuación diferencial $y'' + ay' + by = e^x$

a. hallar los valores de $a$ y $b$ si se sabe que $y_1(x) = xe^{4x}$ es una solución de la ecuación diferencial $y'' + ay' + by = 0$

b. Hallar la solución de la ecuación diferencial $y'' + ay' + by = e^x$ con recta tangente de ecuación $y = -3x + \frac19$ en el punto $(0, y_0)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** $r = 4$ debe ser raíz doble: $(r - 4)^2 = r^2 - 8r + 16 \Rightarrow a = -8$, $b = 16$.

**b) Paso 1 — Homogénea.** $y_h = (C_1 + C_2x)e^{4x}$.

**Paso 2 — Particular.** $y_p = Ae^x$: $A(1 - 8 + 16) = 1 \Rightarrow A = \frac19$.

**Paso 3 — Condiciones.** $y(0) = \frac19$ e $y'(0) = -3$.

- $y(0) = C_1 + \frac19 = \frac19 \Rightarrow C_1 = 0$.
- $y'(0) = C_2 + \frac19 = -3 \Rightarrow C_2 = -\frac{28}{9}$.

</details>

**Respuesta:** a) $a = -8$, $b = 16$. b) $y = -\dfrac{28}{9}xe^{4x} + \dfrac19 e^x$.

</details>

---

#### T2) Campo con singularidad en el origen

Dado el campo vectorial $\bar f(x,y) = \left(-\dfrac{y}{x^2 + 9y^2};\ \dfrac{x}{x^2 + 9y^2}\right)$

a. Determinar si el mismo admite función potencial en su dominio.

b. ¿Es posible conocer el valor $\int_C\bar f\thinspace\overline{ds}$ siendo C cualquier curva cerrada que encierra al origen? Justifique.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a) Paso 1 — Simetría.** En $D = \mathbb{R}^2 - \{0\}$:

$$P'_y = \frac{9y^2 - x^2}{(x^2 + 9y^2)^2} = Q'_x$$

Pero $D$ no es simplemente conexo.

**Paso 2 — Circulación sobre $x^2 + 9y^2 = 1$.** $\vec\alpha(t) = \left(\cos t,\ \frac{\mathop{\mathrm{sen}}t}{3}\right)$:

$$\oint\bar f\cdot d\bar s = \int_0^{2\pi}\left(\frac{\mathop{\mathrm{sen}}^2t}{3} + \frac{\cos^2t}{3}\right)dt = \frac{2\pi}{3} \ne 0$$

⇒ **no** admite función potencial en su dominio.

**b)** Sí: por Green en la región entre $C$ y una elipse chica $x^2 + 9y^2 = \varepsilon^2$ (donde $Q'_x - P'_y = 0$), la circulación sobre toda curva cerrada simple que encierra al origen es la misma que sobre la elipse: $\frac{2\pi}{3}$ en sentido positivo.

</details>

**Respuesta:** a) No: la circulación sobre $x^2 + 9y^2 = 1$ vale $\dfrac{2\pi}{3}$. b) Sí: vale $\dfrac{2\pi}{3}$ en sentido positivo ($-\dfrac{2\pi}{3}$ en sentido negativo).

</details>

---

[Volver al menú principal](../README.md)
