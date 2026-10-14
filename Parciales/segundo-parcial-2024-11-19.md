# 2.º Parcial (19/11/2024) — Cuatro temas

Análisis Matemático II — UTN-FRBA.

Enunciados (sin resolución oficial): [Parcial2-2024-11-19-Cuatro-Temas.pdf](../aula-virtual/Parciales/Segundo-Parcial/Parcial2-2024-11-19-Cuatro-Temas.pdf). El PDF trae cuatro versiones:

- [Comisión z2051 — Tema 1](#comisión-z2051--tema-1)
- [Comisión z2004 — Tema II](#comisión-z2004--tema-ii)
- [Comisión Z2004 — Tema 1](#comisión-z2004--tema-1-segunda-versión)
- [Comisión Z2004 — Tema II](#comisión-z2004--tema-ii-segunda-versión)

Las resoluciones son propias (no hay solución de la cátedra). Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Comisión z2051 — Tema 1

### Parte teórica

#### T1) Integral sobre el borde de un rectángulo

Sea C el borde de un rectángulo de altura h y base b. Mostrar que la integral $\int_C xy^2\,dx + (x^2y + 2x)\,dy$, no depende de la ubicación del rectángulo en el plano. Enunciar los teoremas y propiedades que utilice para justificar.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Teorema de Green:** si $D$ es una región acotada cuya frontera $C$ es una curva cerrada, simple, suave a trozos y orientada positivamente, y $\vec f = (P,Q) \in C^1$ en un abierto que contiene a $D$:

$$\oint_C P\,dx + Q\,dy = \iint_D(Q'_x - P'_y)\,dA$$

**Paso 1 — Hipótesis.** $P = xy^2$ y $Q = x^2y + 2x$ son polinomios ⇒ $C^1$ en $\mathbb{R}^2$. El borde de un rectángulo es una curva cerrada, simple y suave a trozos.

**Paso 2 — Integrando.** $Q'_x - P'_y = (2xy + 2) - 2xy = 2$, constante.

**Paso 3 — Resultado.** Recorriendo el borde en sentido positivo:

$$\oint_C\vec f\cdot d\vec s = \iint_D 2\,dA = 2\cdot\text{Área}(D) = 2bh$$

Sólo depende del área del rectángulo, no de dónde esté ubicado (ni de cómo esté rotado). En sentido horario vale $-2bh$.

</details>

**Respuesta:** Por Green, $\oint_C = \iint_D 2\,dA = 2bh$ (sentido positivo), que sólo depende de $b$ y $h$.

</details>

---

#### T2) Ecuación diferencial de 2.º orden

Dada la ecuación diferencial $y'' + 4y' + 5y = f(x)$

- a) Hallar $f(x)$ para que $y = x^2$ resulte solución de la ecuación.
- b) Hallar la solución de la ED que en el punto $(0, y_0)$ posee recta tangente de ecuación $y = 2x$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** Con $y = x^2$, $y' = 2x$ e $y'' = 2$:

$$f(x) = 2 + 8x + 5x^2$$

**b)** La recta tangente $y = 2x$ en $x = 0$ da $y(0) = 0$ e $y'(0) = 2$.

- *Homogénea:* $r^2 + 4r + 5 = 0 \Rightarrow r = -2 \pm i$ ⇒ $y_H = e^{-2x}(C_1\cos x + C_2\operatorname{sen}x)$.
- *Particular:* por a), $y_P = x^2$.
- *S.G.:* $y = e^{-2x}(C_1\cos x + C_2\operatorname{sen}x) + x^2$.

*Condiciones:*

- $y(0) = C_1 = 0$.
- $y'(0) = -2C_1 + C_2 + 0 = 2 \Rightarrow C_2 = 2$.

</details>

**Respuesta:**

- a) $f(x) = 5x^2 + 8x + 2$.
- b) $y = 2e^{-2x}\operatorname{sen}(x) + x^2$.

</details>

---

### Parte práctica

#### P1) Circulación sobre una circunferencia

Calcular $\int_C\vec G\cdot d\vec s$ donde $\vec G(x,y,z) = (yz + \operatorname{actan}(z),\ e^zy + \operatorname{sen}(z),\ z^3)$ y C es la curva intersección del cono $z = \sqrt{x^2 + y^2}$ con el cilindro $x^2 + y^2 = 1$ recorrida en sentido antihorario

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Curva.** En el cilindro, $z = \sqrt1 = 1$: es la circunferencia de radio 1 a altura $z = 1$, $\vec\alpha(t) = (\cos t,\ \operatorname{sen}t,\ 1)$, $t\in[0,2\pi]$ (antihoraria vista desde arriba).

**Paso 2 — Integrando.** $\vec\alpha' = (-\operatorname{sen}t,\ \cos t,\ 0)$ y $\vec G(\vec\alpha) = (\operatorname{sen}t + \arctan1,\ e\operatorname{sen}t + \operatorname{sen}1,\ 1)$:

$$\vec G\cdot\vec\alpha' = -\operatorname{sen}^2t - \arctan(1)\operatorname{sen}t + e\operatorname{sen}t\cos t + \operatorname{sen}(1)\cos t$$

**Paso 3 — Integrar en $[0,2\pi]$.** Todos los términos se anulan salvo el primero:

$$\oint_C\vec G\cdot d\vec s = -\int_0^{2\pi}\operatorname{sen}^2t\,dt = -\pi$$

*Control con Stokes:* la tercera componente del rotor es $Q'_x - P'_y = 0 - z = -1$ sobre el disco $z = 1$ (normal $\breve k$), de área $\pi$ ⇒ $-\pi$ ✓.

</details>

**Respuesta:** $-\pi$.

</details>

---

#### P2) Área de un trozo de cilindro

Calcular el área de la porción de superficie $x^2 + y^2 = 2y$ que se encuentra limitado por $z = 0$ y $z + y = 2$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Superficie.** $x^2 + (y - 1)^2 = 1$: cilindro de radio 1 y eje paralelo al eje $z$ por $(0,1)$. Sobre él, $y\in[0,2]$, así que el techo $z = 2 - y \ge 0$.

**Paso 2 — Parametrización.** $(\cos t,\ 1 + \operatorname{sen}t,\ z)$, con $z\in[0,\ 2 - y] = [0,\ 1 - \operatorname{sen}t]$ y $d\sigma = 1\cdot dt\,dz$ (radio 1).

**Paso 3 — Área.**

$$A = \int_0^{2\pi}(1 - \operatorname{sen}t)\,dt = 2\pi$$

</details>

**Respuesta:** $2\pi$.

</details>

---

#### P3) Trabajo de una fuerza conservativa

Determinar el trabajo ejercido por la fuerza $\vec f(x,y) = (y\cos(xy);\ x\cos(xy))$ al mover una partícula a lo largo de la curva dada por $y = \tan(x)$, con $x \in [0, \pi/4]$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Potencial.** $\vec f = \nabla\operatorname{sen}(xy)$: en efecto, $(\operatorname{sen}(xy))'_x = y\cos(xy)$ y $(\operatorname{sen}(xy))'_y = x\cos(xy)$.

**Paso 2 — Extremos.** De $(0, 0)$ a $(\pi/4,\ \tan(\pi/4)) = (\pi/4,\ 1)$.

**Paso 3 — Trabajo.**

$$W = \operatorname{sen}\!\left(\frac\pi4\cdot1\right) - \operatorname{sen}(0) = \frac{\sqrt2}{2}$$

</details>

**Respuesta:** $W = \dfrac{\sqrt2}{2}$.

</details>

---

#### P4) Volumen de un sólido

Calcular el volumen del sólido definido por: $y - x^2 \le 0$; $y \ge 0$; $z + x \le 4$; $z \ge 0$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

> **Observación sobre el enunciado:** tal como está escrito, para $x < 0$ el sólido no es acotado ($0 \le y \le x^2$ y $0 \le z \le 4 - x$ crecen sin límite cuando $x \to -\infty$). En la otra versión de la comisión Z2004 se aclara "primer octante"; asumimos lo mismo, $x \ge 0$.

**Paso 1 — Límites.** $0 \le z \le 4 - x$ (requiere $x \le 4$), $0 \le y \le x^2$ y $0 \le x \le 4$.

**Paso 2 — Integral.**

$$V = \int_0^4dx\int_0^{x^2}dy\int_0^{4 - x}dz = \int_0^4 x^2(4 - x)\,dx = \frac{4\cdot64}{3} - \frac{256}{4} = \frac{256}{3} - 64 = \frac{64}{3}$$

</details>

**Respuesta:** $V = \dfrac{64}{3}$ (en el primer octante).

</details>

---

## Comisión z2004 — Tema II

Los teóricos T1 y T2 son **iguales** a los del Tema 1 de la comisión z2051 (ver arriba).

### Parte práctica

#### P1) Área de un trozo de cilindro

Calcular el área de la porción de superficie $x^2 + y^2 = 4y$ que se encuentra limitado por $z = 0$ y $z + y = 5$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Superficie.** $x^2 + (y - 2)^2 = 4$: cilindro de radio 2 por $(0,2)$, con $y\in[0,4]$ ⇒ $z = 5 - y \ge 1 > 0$.

**Paso 2 — Parametrización.** $(2\cos t,\ 2 + 2\operatorname{sen}t,\ z)$, con $z\in[0,\ 3 - 2\operatorname{sen}t]$ y $d\sigma = 2\,dt\,dz$.

**Paso 3 — Área.**

$$A = \int_0^{2\pi}2(3 - 2\operatorname{sen}t)\,dt = 12\pi$$

</details>

**Respuesta:** $12\pi$.

</details>

---

#### P2) Circulación sobre una circunferencia

Calcular $\int_C\vec G\cdot d\vec s$ donde $\vec G(x,y,z) = (yz + \operatorname{sen}(z),\ e^zy + \operatorname{actan}(z),\ z^3)$ y C es la curva intersección del cono $z = \sqrt{x^2 + y^2}$ con el cilindro $x^2 + y^2 = 4$ recorrida en sentido antihorario

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Curva.** $z = 2$: $\vec\alpha = (2\cos t,\ 2\operatorname{sen}t,\ 2)$, con $\vec\alpha' = (-2\operatorname{sen}t,\ 2\cos t,\ 0)$.

**Paso 2 — Integrando.**

$$\vec G\cdot\vec\alpha' = (4\operatorname{sen}t + \operatorname{sen}2)(-2\operatorname{sen}t) + (2e^2\operatorname{sen}t + \arctan2)(2\cos t)$$

**Paso 3 — Integrar.** Sólo sobrevive $-8\displaystyle\int_0^{2\pi}\operatorname{sen}^2t\,dt = -8\pi$.

*Control con Stokes:* $(\operatorname{rot}\vec G)_z = -z = -2$ sobre el disco de área $4\pi$ ⇒ $-8\pi$ ✓.

</details>

**Respuesta:** $-8\pi$.

</details>

---

#### P3) Volumen de un sólido

Calcular el volumen del sólido definido por: $y - x^2 \le 0$; $y \ge 0$; $z + x \le 4$; $z \ge 0$

<details>
<summary><b>Solución</b></summary>

Es el mismo enunciado que el P4 del Tema 1 (ver arriba, con la misma observación sobre $x \ge 0$).

**Respuesta:** $V = \dfrac{64}{3}$.

</details>

---

#### P4) Trabajo de una fuerza conservativa

Determinar el trabajo ejercido por la fuerza $\vec f(x,y) = (y\operatorname{sen}(xy);\ x\operatorname{sen}(xy))$ al mover una partícula a lo largo de la curva dada por $y = \tan(x)$, con $x \in [-\frac\pi4, 0]$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Potencial.** $\vec f = \nabla(-\cos(xy))$.

**Paso 2 — Extremos.** De $(-\pi/4,\ -1)$ a $(0, 0)$.

**Paso 3 — Trabajo.**

$$W = -\cos(0) - \left(-\cos\frac\pi4\right) = -1 + \frac{\sqrt2}{2} \approx -0{,}293$$

</details>

**Respuesta:** $W = \dfrac{\sqrt2}{2} - 1$.

</details>

---

## Comisión Z2004 — Tema 1 (segunda versión)

### Parte teórica

#### T1) Volumen con el teorema de la divergencia

Mostrar que el volumen de un sólido V puede calcularse con: $\frac13\iint_{\partial V}\vec F\cdot\breve n\,d\sigma$, siendo $\vec F(x,y,z) = (x,y,z)$. Enunciar los teoremas y propiedades que utilice para justificar.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Teorema de la divergencia:** si $V$ es un sólido cuya frontera $\partial V$ es una superficie cerrada, suave a trozos, orientada con normal saliente, y $\vec F \in C^1$ en un abierto que contiene a $V$:

$$\oint\!\!\!\oint_{\partial V}\vec F\cdot\breve n\,d\sigma = \iiint_V\operatorname{div}\vec F\,dV$$

**Aplicación.** $\vec F = (x,y,z)$ es $C^1$ en $\mathbb{R}^3$ y $\operatorname{div}\vec F = 1 + 1 + 1 = 3$:

$$\frac13\oint\!\!\!\oint_{\partial V}\vec F\cdot\breve n\,d\sigma = \frac13\iiint_V 3\,dV = \text{Vol}(V) \quad\blacksquare$$

</details>

**Respuesta:** Por el teorema de la divergencia, con $\operatorname{div}\vec F = 3$, se obtiene $\frac13\cdot3\,\text{Vol}(V)$.

</details>

---

#### T2) ¿Es conservativo?

Determinar si el campo $\vec F(x,y) = \left(\dfrac{1 - y}{x^2 + (y - 1)^2};\ \dfrac{x}{x^2 + (y - 1)^2}\right)$ es conservativo. Enunciar los teoremas y propiedades que utilice para justificar.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Cambio de variable.** Con $u = x$, $w = y - 1$ y $r^2 = u^2 + w^2$: $\vec F = \dfrac{(-w,\ u)}{r^2}$, el "vórtice" centrado en $(0,1)$. El dominio es $\mathbb{R}^2 - \{(0,1)\}$, que **no** es simplemente conexo.

**Paso 2 — Jacobiana simétrica.**

$$P'_y = \frac{w^2 - u^2}{r^4} = Q'_x$$

Es **condición necesaria** para ser conservativo, pero en un dominio con un agujero no es suficiente.

**Paso 3 — Circulación alrededor del agujero.** Sobre la circunferencia $u = R\cos t$, $w = R\operatorname{sen}t$ (antihoraria):

$$\vec F\cdot d\vec s = \frac{(-R\operatorname{sen}t)(-R\operatorname{sen}t) + (R\cos t)(R\cos t)}{R^2}\,dt = dt \ \Rightarrow\ \oint = 2\pi \ne 0$$

**Paso 4 — Conclusión.** Un campo conservativo tiene circulación nula sobre toda curva cerrada (teorema de independencia del camino) ⇒ $\vec F$ **no** es conservativo en su dominio.

</details>

**Respuesta:** No es conservativo: su jacobiana es simétrica, pero la circulación alrededor de $(0,1)$ vale $2\pi \ne 0$.

</details>

---

### Parte práctica

#### P1) Flujo a través de un tronco de cono

Sea S la porción de superficie $z^2 = x^2 + y^2$ con $-2 \le z \le -1$ calcular el flujo de $\vec F(x,y,z) = (-zx,\ -zy,\ z^2)$ a través de S, indicar la orientación elegida para S.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** Es la hoja inferior del cono, $z = -\rho$, con $\rho\in[1,2]$: $\vec X = (\rho\cos\theta,\ \rho\operatorname{sen}\theta,\ -\rho)$.

**Paso 2 — Normal.**

$$\vec X'_\rho\wedge\vec X'_\theta = (\cos\theta,\ \operatorname{sen}\theta,\ -1)\wedge(-\rho\operatorname{sen}\theta,\ \rho\cos\theta,\ 0) = (\rho\cos\theta,\ \rho\operatorname{sen}\theta,\ \rho)$$

Tiene tercera componente positiva: elegimos la orientación con $\breve n\cdot\breve k > 0$.

**Paso 3 — Integrando.** $\vec F = (\rho^2\cos\theta,\ \rho^2\operatorname{sen}\theta,\ \rho^2)$:

$$\vec F\cdot\vec N = \rho^3 + \rho^3 = 2\rho^3$$

**Paso 4 — Integral.**

$$\Phi = \int_0^{2\pi}\!\!\int_1^2 2\rho^3\,d\rho\,d\theta = 2\pi\cdot\frac{16 - 1}{2} = 15\pi$$

</details>

**Respuesta:** $15\pi$ con $\breve n$ tal que $\breve n\cdot(0,0,1) > 0$ (con la orientación opuesta, $-15\pi$).

</details>

---

#### P2) Volumen en el primer octante

Calcular el volumen del sólido ubicado en el primer octante definido por: $z \le 4 - y^2$; $y \ge x$; $y - 2x \le 0$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Límites.**

- $y \ge x$ e $y \le 2x$ ⇒ $\frac y2 \le x \le y$.
- $0 \le z \le 4 - y^2$ requiere $y \le 2$.

**Paso 2 — Integral.**

$$V = \int_0^2dy\int_{y/2}^{y}(4 - y^2)\,dx = \int_0^2(4 - y^2)\frac y2\,dy = \frac12\left[2y^2 - \frac{y^4}{4}\right]_0^2 = \frac12(8 - 4) = 2$$

</details>

**Respuesta:** $V = 2$.

</details>

---

#### P3) Integral de línea sobre una curva intersección

Calcular la integral de línea del campo $\vec F(x,y,z) = (2xy;\ 8x^2 + 2xy;\ 2xz)$, si C es la curva ubicada en el primer octante resultado de la intersección entre las superficies $x + y = 2$; $z = 4 - x^2$ orientada del punto (2,0,0) al (0,2,4)

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — ¿Conservativo?** $P'_y = 2x$ y $Q'_x = 16x + 2y$: no son iguales ⇒ hay que parametrizar.

**Paso 2 — Parametrización.** $x = t$, $y = 2 - t$, $z = 4 - t^2$, con $t$ de 2 a 0. Diferenciales: $dx = dt$, $dy = -dt$, $dz = -2t\,dt$.

**Paso 3 — Integrando.**

$$2t(2 - t) - \big(8t^2 + 2t(2 - t)\big) + 2t(4 - t^2)(-2t) = -24t^2 + 4t^4$$

**Paso 4 — Integral** (de $t = 2$ a $t = 0$):

$$\int_2^0(-24t^2 + 4t^4)\,dt = -\left[-8t^3 + \frac45t^5\right]_0^2 = -\left(-64 + \frac{128}{5}\right) = \frac{192}{5}$$

</details>

**Respuesta:** $\dfrac{192}{5} = 38.4$.

</details>

---

#### P4) Circulación sobre una elipse

Calcular $\int_C\vec G\cdot d\vec s$ donde $\vec G(x,y) = (x - y^2,\ 3x + y)$ a lo largo de la porción de curva $x^2 + \frac{(y-1)^2}{4} = 1$, orientada en sentido horario

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

> El enunciado dice "porción de curva" pero no indica cuál; se interpreta como la elipse completa (curva cerrada).

**Paso 1 — Green.** $Q'_x - P'_y = 3 + 2y$.

**Paso 2 — Región.** Elipse de centro $(0,1)$ y semiejes 1 y 2: área $2\pi$ y centroide $\bar y = 1$.

$$\iint_D(3 + 2y)\,dA = 3\cdot2\pi + 2\cdot1\cdot2\pi = 10\pi$$

**Paso 3 — Orientación horaria** ⇒ signo opuesto: $-10\pi$.

</details>

**Respuesta:** $-10\pi$ (recorriendo la elipse completa en sentido horario).

</details>

---

## Comisión Z2004 — Tema II (segunda versión)

Los teóricos T1 y T2 son **iguales** a los del Tema 1 de esta comisión (ver arriba).

### Parte práctica

#### P1) Circulación sobre una elipse

Calcular $\int_C\vec G\cdot d\vec s$ donde $\vec G(x,y) = (x - 2y^2,\ 4x + y)$ a lo largo de la porción de curva $x^2 + \frac{(y+1)^2}{9} = 1$, orientada en sentido horario

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

Se interpreta como la elipse completa.

**Paso 1 — Green.** $Q'_x - P'_y = 4 + 4y$.

**Paso 2 — Región.** Elipse de centro $(0,-1)$ y semiejes 1 y 3: área $3\pi$ y centroide $\bar y = -1$.

$$\iint_D(4 + 4y)\,dA = 4\cdot3\pi + 4(-1)(3\pi) = 0$$

**Paso 3 — Orientación horaria:** $-0 = 0$.

</details>

**Respuesta:** $0$.

</details>

---

#### P2) Flujo a través de un tronco de cono

Sea S la porción de superficie $z^2 = x^2 + y^2$ con $-3 \le z \le -2$ calcular el flujo de $\vec F(x,y,z) = (zx,\ zy,\ 2z^2)$ a través de S.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización** (como en el Tema 1): $\vec X = (\rho\cos\theta,\ \rho\operatorname{sen}\theta,\ -\rho)$, $\rho\in[2,3]$, con $\vec N = (\rho\cos\theta,\ \rho\operatorname{sen}\theta,\ \rho)$ ($\breve n\cdot\breve k > 0$).

**Paso 2 — Integrando.** $\vec F = (-\rho^2\cos\theta,\ -\rho^2\operatorname{sen}\theta,\ 2\rho^2)$:

$$\vec F\cdot\vec N = -\rho^3 + 2\rho^3 = \rho^3$$

**Paso 3 — Integral.**

$$\Phi = 2\pi\int_2^3\rho^3\,d\rho = 2\pi\cdot\frac{81 - 16}{4} = \frac{65\pi}{2}$$

</details>

**Respuesta:** $\dfrac{65\pi}{2}$ con $\breve n \cdot (0,0,1) > 0$ (el enunciado no fija orientación; con la opuesta, $-65\pi/2$).

</details>

---

#### P3) Volumen en el primer octante

Calcular el volumen del sólido ubicado en el primer octante definido por: $z \le 9 - y^2$; $y \ge \frac12x$; $y - x \le 0$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Límites.**

- $\frac x2 \le y \le x$ ⇒ $y \le x \le 2y$.
- $z \ge 0$ requiere $y \le 3$.

**Paso 2 — Integral.**

$$V = \int_0^3(9 - y^2)(2y - y)\,dy = \int_0^3(9y - y^3)\,dy = \frac{81}{2} - \frac{81}{4} = \frac{81}{4}$$

</details>

**Respuesta:** $V = \dfrac{81}{4}$.

</details>

---

#### P4) Integral de línea sobre una curva intersección

Calcular la integral de línea del campo $\vec F(x,y,z) = (2xy;\ 8x^2 + 2xy;\ 2xz)$, si C es la curva ubicada en el primer octante resultado de la intersección entre las superficies $x + y = 3$; $z = 9 - x^2$ orientada del punto (3,0,0) al (0,3,9)

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $x = t$, $y = 3 - t$, $z = 9 - t^2$, con $t$ de 3 a 0. Diferenciales: $dy = -dt$, $dz = -2t\,dt$.

**Paso 2 — Integrando.**

$$2t(3 - t) - \big(8t^2 + 2t(3 - t)\big) - 4t^2(9 - t^2) = -44t^2 + 4t^4$$

**Paso 3 — Integral.**

$$\int_3^0(-44t^2 + 4t^4)\,dt = -\left[-\frac{44}{3}t^3 + \frac45t^5\right]_0^3 = -\left(-396 + \frac{972}{5}\right) = \frac{1008}{5}$$

</details>

**Respuesta:** $\dfrac{1008}{5} = 201.6$.

</details>

---

[← Volver al menú principal](../README.md)
