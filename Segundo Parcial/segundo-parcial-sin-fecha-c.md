# 2.º Parcial (sin fecha) — C

Análisis Matemático II — UTN-FRBA. Son recortes de un mismo examen, sin fecha ni curso. El ejercicio del trabajo no muestra número; por el orden de los recortes es el 3. El T1 coincide con el del [recuperatorio del 01/12/2023](recuperatorio-segundo-parcial-2023-12-01.md).

Enunciados (fotos, sin resolución oficial): [1](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-sin-fecha-C-E1.jpeg), [2](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-sin-fecha-C-E2.jpeg), [3](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-sin-fecha-C-E3.jpeg), [4](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-sin-fecha-C-E4.jpeg), [T1](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-sin-fecha-C-T1.jpeg) y [T2](../aula-virtual/Parciales/Segundo-Parcial/fotos/Parcial2-sin-fecha-C-T2.jpeg).

Las resoluciones son propias (no hay solución de la cátedra). Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Parte práctica

### 1) Flujo saliente con Gauss

Calcular el flujo del campo vectorial $\bar f: R^3 \to R^3$ tal que $\bar f(x,y,z) = (6x\ ,3z^2, -2y)$ a través de la frontera del sólido del primer octante definido por: $2y + z \le 4, x + y \le 2$ , Indicar la orientación elegida para la superficie.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Divergencia.** $\operatorname{div}\bar f = 6 + 0 + 0 = 6$.

**Paso 2 — Volumen.** En el primer octante, para cada $y \in [0,2]$: $0 \le x \le 2 - y$ y $0 \le z \le 4 - 2y$:

$$V = \int_0^2(2 - y)(4 - 2y)\thinspace dy = 2\int_0^2(2 - y)^2\thinspace dy = 2\cdot\frac83 = \frac{16}{3}$$

**Paso 3 — Gauss** (normal exterior): $\Phi = 6V = 32$.

</details>

**Respuesta:** Con normal exterior, $\Phi = 32$.

</details>

---

### 2) Circulación sobre la intersección de un elipsoide y un plano

Calcular la circulación del campo vectorial $\bar f: R^3 \to R^3$ tal que $\bar f(x,y,z) = (3x^2y^2z^4 - y;\ 2x^3yz^4;\ 4x^3y^2z^3)$ a lo largo de la curva intersección de las superficies $x^2 + z^2 + 2y^2 = 4z$; $x + z = 2$, Indicar la orientación elegida para la curva.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Separar la parte conservativa.** $\bar f = \nabla(x^3y^2z^4) + (-y, 0, 0)$. Sobre la curva cerrada solo aporta $(-y, 0, 0)$, cuyo rotor es $(0, 0, 1)$.

**Paso 2 — Superficie.** Se toma la porción del plano $z = 2 - x$ encerrada por la curva. Reemplazando en el elipsoide: $x^2 + (2 - x)^2 + 2y^2 = 4(2 - x) \iff 2x^2 + 2y^2 = 4 \iff x^2 + y^2 = 2$. La proyección sobre $xy$ es el disco $D$ de radio $\sqrt2$.

**Paso 3 — Normal.** $\vec T(x,y) = (x,\ y,\ 2 - x)$: $\vec T'_x\times\vec T'_y = (1,0,-1)\times(0,1,0) = (1, 0, 1)$ (hacia arriba).

**Paso 4 — Stokes.**

$$\oint_C\bar f\cdot d\bar s = \iint_D(0,0,1)\cdot(1,0,1)\thinspace dx\thinspace dy = \text{Área}(D) = 2\pi$$

**Paso 5 — Sentido.** La normal $(1,0,1)$ induce el recorrido antihorario visto desde arriba ($z > 0$), por ejemplo $\vec\alpha(t) = (\sqrt2\cos t,\ \sqrt2\mathop{\mathrm{sen}}t,\ 2 - \sqrt2\cos t)$, $0 \le t \le 2\pi$.

</details>

**Respuesta:** Recorrida en sentido antihorario visto desde arriba, la circulación vale $2\pi$; en sentido contrario, $-2\pi$.

</details>

---

### 3) Trabajo a lo largo de una línea de campo

Calcular el trabajo del campo vectorial $\bar f: R^2 \to R^2$ tal que $\bar f(x,y) = (x - 2y; x - 2)$ a lo largo de la línea de campo correspondiente a $\bar f(x,y) = (x - 2, 2y)$ que pasa por (0,2), entre los puntos (0,4) y (3,1)

> El enunciado es inconsistente: la línea de campo que pasa por $(0,2)$ es $y = \frac12(x - 2)^2$, que no contiene a $(0,4)$ ni a $(3,1)$; esos dos puntos están en la línea $y = (x - 2)^2$. (En la foto hay una corrección a mano sobre el $(0,4)$.) Como se ve abajo, el trabajo entre $x = 0$ y $x = 3$ da lo mismo sobre cualquier línea de la familia.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Familia de líneas de campo de $\vec g = (x - 2, 2y)$.**

$$\frac{dy}{dx} = \frac{2y}{x - 2} \Rightarrow \ln|y| = 2\ln|x - 2| + c \Rightarrow y = C(x - 2)^2$$

Por $(0,2)$: $C = \frac12$. Por $(0,4)$ y $(3,1)$: $C = 1$.

**Paso 2 — El campo del trabajo no es conservativo.** $Q'_x - P'_y = 1 + 2 = 3 \ne 0$, así que hay que integrar sobre la curva.

**Paso 3 — Parametrización.** $\vec\alpha(x) = (x,\ C(x - 2)^2)$, $0 \le x \le 3$, $\vec\alpha' = (1,\ 2C(x - 2))$:

$$\bar f\cdot\vec\alpha' = x - 2C(x - 2)^2 + (x - 2)\cdot 2C(x - 2) = x$$

Los términos con $C$ se cancelan.

**Paso 4 — Integrar.**

$$W = \int_0^3 x\thinspace dx = \frac92$$

</details>

**Respuesta:** $W = \dfrac92$, sobre $y = (x - 2)^2$ de $(0,4)$ a $(3,1)$; sobre $y = \frac12(x - 2)^2$ entre $x = 0$ y $x = 3$ da lo mismo.

</details>

---

### 4) Área del dominio de un campo escalar

Determinar el área de la región que constituye el dominio del campo escalar

$$f(x,y) = \sqrt{-x^2 + 2x - y^2}.\ln(x - y)$$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Dominio.**

- Raíz: $-x^2 + 2x - y^2 \ge 0 \iff (x - 1)^2 + y^2 \le 1$ (disco de centro $(1,0)$ y radio 1).
- Logaritmo: $x - y > 0 \iff y < x$.

**Paso 2 — Geometría.** La recta $y = x$ está a distancia $d = \frac{|1 - 0|}{\sqrt2} = \frac{1}{\sqrt2}$ del centro, y el centro cumple $y < x$. El dominio es el disco menos el segmento circular que queda sobre la recta.

**Paso 3 — Segmento circular** (radio 1, distancia $d$ al centro, ángulo central $2\alpha$ con $\cos\alpha = d$, $\alpha = \frac{\pi}{4}$):

$$A_{seg} = \alpha - d\sqrt{1 - d^2} = \frac{\pi}{4} - \frac12$$

**Paso 4 — Área.**

$$A = \pi - \left(\frac{\pi}{4} - \frac12\right) = \frac{3\pi}{4} + \frac12$$

**Con integral doble:** $A = \displaystyle\int_0^2\negthinspace\negthinspace\int_{-\sqrt{1 - (x - 1)^2}}^{\min\left(x,\ \sqrt{1 - (x - 1)^2}\right)}dy\thinspace dx$ da el mismo valor.

</details>

**Respuesta:** $A = \dfrac{3\pi}{4} + \dfrac12 \approx 2{,}86$.

</details>

---

## Parte teórica

### T1) Áreas planas con integrales de línea

a) Indique cómo pueden usarse las integrales de línea para calcular áreas planas.

b) Calcular el área de la región definida por $x^2 + (y - 1)^2 \le 4, x \le 0$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** Por el teorema de Green, si $D$ es una región acotada con frontera $C$ cerrada, simple, suave a trozos y orientada positivamente, y $(P,Q) \in C^1$ cumple $Q'_x - P'_y = 1$, entonces

$$\text{Área}(D) = \iint_D 1\thinspace dA = \oint_C P\thinspace dx + Q\thinspace dy$$

Campos usuales: $(0, x)$, $(-y, 0)$ o $\frac12(-y, x)$:

$$\text{Área}(D) = \oint_C x\thinspace dy = -\oint_C y\thinspace dx = \frac12\oint_C(x\thinspace dy - y\thinspace dx)$$

**b) Paso 1 — Frontera positiva.** Arco $C_1$: $(2\cos t,\ 1 + 2\mathop{\mathrm{sen}}t)$, $\frac{\pi}{2} \le t \le \frac{3\pi}{2}$; segmento $C_2$ sobre $x = 0$ de $(0,-1)$ a $(0,3)$.

**Paso 2 — Con $\oint x\thinspace dy$.** En $C_2$, $x = 0$: no aporta. En $C_1$:

$$\int_{\pi/2}^{3\pi/2}2\cos t\cdot 2\cos t\thinspace dt = 4\cdot\frac{\pi}{2} = 2\pi$$

</details>

**Respuesta:** b) $\text{Área} = 2\pi$ (medio círculo de radio 2).

</details>

---

### T2) Condición para la existencia de potencial

a) Enuncie la condición necesaria y suficiente para la existencia de función potencial

b) Calcule la circulación del campo $\bar f(x,y) = \left(\frac{2x}{x^2 + y^2};\ \frac{2y}{x^2 + y^2}\right)$ a lo largo de la curva $\frac{x^2}{4} + y^2 = 1$ con $x \ge 1$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** $\vec f$ continuo en un abierto conexo $D$ admite función potencial **si y solo si** $\oint_C\vec f\cdot d\vec s = 0$ para toda curva cerrada suave a trozos $C \subset D$. Si $\vec f \in C^1$, una condición necesaria es que la jacobiana sea simétrica, y en un $D$ simplemente conexo también es suficiente.

**b) Paso 1 — Potencial.** $\varphi = \ln(x^2 + y^2)$ cumple $\nabla\varphi = \bar f$ en $\mathbb{R}^2 - \{0\}$, que contiene a la curva.

**Paso 2 — Extremos.** Con $x = 1$: $y^2 = \frac34$, extremos $\left(1, \pm\frac{\sqrt3}{2}\right)$, ambos con $x^2 + y^2 = \frac74$.

**Paso 3 — Circulación.** $\varphi(\text{fin}) - \varphi(\text{inicio}) = \ln\frac74 - \ln\frac74 = 0$.

</details>

**Respuesta:** b) $0$, porque $\bar f = \nabla\ln(x^2 + y^2)$ y los extremos están a la misma distancia del origen.

</details>

---

[Volver al menú principal](../README.md)
