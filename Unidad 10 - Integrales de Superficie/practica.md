# Unidad 10 — Práctica: Integrales de superficie y flujo

Ejercicios del **T.P. N.º 10 de la Guía de Trabajos Prácticos** ([TP10-Integrales-Superficie-Flujo.pdf](../aula-virtual/10-Integrales-Superficie/TP10-Integrales-Superficie-Flujo.pdf)) y de la [Guía de ejercicios adicionales de flujo](../aula-virtual/10-Integrales-Superficie/Ejercicios-Adicionales-Flujo.pdf). Las respuestas se controlaron con las [respuestas oficiales de la guía](../aula-virtual/00-Guia-TP/Guia-TP-2016-Respuestas.pdf).

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

> **Nomenclatura y consideraciones básicas:**
>
> - Una superficie $S$ de ecuación $\bar X = \bar F(u,v)$ con $(u,v) \in D$ es ***suave*** según esta representación, si $\bar F \in C^1(D)$ y el producto vectorial $\bar F'_u \wedge \bar F'_v \ne \bar 0\ \ \forall(u,v) \in D$.
>
>   En este caso queda definido el versor normal $\breve n \doteq \dfrac{\bar F'_u \wedge \bar F'_v}{\Vert\bar F'_u \wedge \bar F'_v\Vert}$ que varía con continuidad sobre $S$; a su vez, si la superficie es orientable queda orientada mediante este versor.
>
>   La superficie es ***suave a trozos*** cuando $D$ puede ser dividido en cantidad finita de partes en cada una de las cuales (o en abierto que las contenga) $\bar F \in C^1$ y $\bar F'_u \wedge \bar F'_v \ne \bar 0$.
> - $\iint_S f\thinspace d\sigma$ simboliza la integral de superficie del campo escalar $f$ sobre $S$, donde $d\sigma = \Vert\bar F'_u \wedge \bar F'_v\Vert\thinspace du\thinspace dv$ es el ***diferencial de área de superficie***.
> - $\iint_S\bar f\cdot d\bar\sigma \equiv \iint_S\bar f\cdot\breve n\thinspace d\sigma$ simboliza el ***flujo*** o integral de superficie del campo vectorial $\bar f$ a través de $S$, donde $d\bar\sigma \doteq \breve n\thinspace d\sigma$.
>
> **Observación**: Si $S$ es suave y simple según dos representaciones $\bar F_1$ y $\bar F_2$, la $\iint_S f\thinspace d\sigma$ tiene el mismo resultado usando cualquiera de ellas; mientras que se observará un cambio de signo en el resultado de $\iint_S\bar f\cdot\breve n\thinspace d\sigma$ cuando $\bar F_1$ y $\bar F_2$ orienten a $S$ en sentidos opuestos.

---

### 01) Superficies cilíndricas

Una ***superficie cilíndrica*** es aquella generada por rectas paralelas que pasan por puntos de una curva $C \subset \Re^3$, la curva es la ***directriz*** y la rectas las ***generatrices*** de la superficie. Determine ecuaciones paramétricas y cartesianas para las siguientes superficies cilíndricas:

- a) directriz $y = x^2$ con $z = 0$, generatrices paralelas al eje $z$.
- b) directriz $y = x^2$ con $z = 0$, generatrices dirigidas por el vector $(1,1,1)$.
- c) directriz $x^2 + y^2 = 4$ con $z = 0$, generatrices paralelas al eje $z$.
- d) directriz $\bar X = (u,\ 2u,\ u^2)$ con $u \in \Re$, generatrices dirigidas por $(2,1,0)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Fórmula:** $\bar X(u,v) = \bar c(u) + v\thinspace\vec w$, con $\bar c$ la directriz y $\vec w$ la dirección de las generatrices. Para la cartesiana se **eliminan** $u$ y $v$.

**a)** $\bar c(u) = (u, u^2, 0)$ y $\vec w = (0,0,1)$ ⇒ $\bar X = (u, u^2, v)$. Como $x = u$ e $y = u^2$: $y = x^2$ (sin restricción sobre $z$).

**b)** $\bar X = (u, u^2, 0) + v(1,1,1) = (u + v,\ u^2 + v,\ v)$. Eliminando: $v = z$ y $u = x - z$ ⇒ $y - z = (x - z)^2$.

**c)** $\bar X = (2\cos u,\ 2\mathop{\mathrm{sen}}u,\ v)$ ⇒ $x^2 + y^2 = 4$.

**d)** $\bar X = (u, 2u, u^2) + v(2,1,0) = (u + 2v,\ 2u + v,\ u^2)$. Eliminando:

- $2y - x = 4u + 2v - u - 2v = 3u$ ⇒ $u = \dfrac{2y - x}{3}$.
- $z = u^2$ ⇒ $(2y - x)^2 = 9z$.

</details>

**Respuesta:**

- a) param.: $\bar X = (u, u^2, v) \wedge (u,v) \in \Re^2$; cart.: $y = x^2$.
- b) param.: $\bar X = (u + v,\ u^2 + v,\ v) \wedge (u,v) \in \Re^2$; cart.: $y - z = (x - z)^2$.
- c) param.: $\bar X = (2\cos(u),\ 2\mathop{\mathrm{sen}}(u),\ v)$ con $u \in [0, 2\pi]$, $v \in \Re$; cart.: $x^2 + y^2 = 4$.
- d) param.: $\bar X = (u + 2v,\ 2u + v,\ u^2) \wedge (u,v) \in \Re^2$; cart.: $(2y - x)^2 = 9z$.

</details>

---

### 02) Superficies cónicas

Una ***superficie cónica*** es aquella generada por rectas determinadas por los puntos de una curva $C \subset \Re^3$ y un punto fijo $\bar V \notin C$, la curva es la ***directriz*** y el punto $\bar V$ el ***vértice*** de la superficie. Determine ecuaciones paramétricas y cartesianas para las siguientes superficies cónicas:

| | a) | b) | c) | d) |
|---|---|---|---|---|
| directriz: | $y = x^2,\ z = 0$ | $y = x^2,\ z = 0$ | $x^2 + y^2 = 4,\ z = 0$ | $\bar X = (u, 2u, u^2) \wedge u \in \Re$ |
| vértice: | $(0,0,1)$ | $(1,4,0)$ | $(0,0,2)$ | $(0,0,1)$ |

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Fórmula:** $\bar X(u,v) = \bar V + v\thinspace(\bar c(u) - \bar V)$.

**a)** $\bar X = (0,0,1) + v(u, u^2, -1) = (uv,\ u^2v,\ 1 - v)$. Eliminando:

- $v = 1 - z$ y $u = \dfrac{x}{v}$.
- $y = u^2v = \dfrac{x^2}{v}$ ⇒ $x^2 = y\thinspace v = y(1 - z)$.

**b)** El vértice $(1,4,0)$ está en el plano $z = 0$ de la directriz (aunque no sobre la parábola). Todas las rectas quedan en ese plano: la "superficie cónica" es el **plano** $z = 0$, que se parametriza como $(u, v, 0)$.

**c)** $\bar X = (0,0,2) + v(2\cos u,\ 2\mathop{\mathrm{sen}}u,\ -2) = (2v\cos u,\ 2v\mathop{\mathrm{sen}}u,\ 2 - 2v)$. Eliminando:

- $x^2 + y^2 = 4v^2$ y $v = \dfrac{2 - z}{2}$.
- $x^2 + y^2 = (z - 2)^2$.

**d)** $\bar X = (0,0,1) + v(u, 2u, u^2 - 1) = (uv,\ 2uv,\ 1 + v(u^2 - 1))$. Siempre $y = 2x$: el vértice y la directriz están en el plano $y = 2x$, así que la superficie es ese plano: $\bar X = (v,\ 2v,\ w)$.

</details>

**Respuesta:**

- a) param.: $\bar X = (uv,\ u^2v,\ 1 - v) \wedge (u,v) \in \Re^2$; cart.: $x^2 = y(1 - z)$.
- b) param.: $\bar X = (u, v, 0) \wedge (u,v) \in \Re^2$; cart.: $z = 0$.
- c) param.: $\bar X = (2v\cos(u),\ 2v\mathop{\mathrm{sen}}(u),\ 2 - 2v)$ con $u \in [0, 2\pi]$, $v \in \Re$; cart.: $x^2 + y^2 = (z - 2)^2$.
- d) param.: $\bar X = (v,\ 2v,\ w) \wedge (v,w) \in \Re^2$; cart.: $y = 2x$.

</details>

---

### 03) Parametrizaciones

Parametrice las siguientes superficies:

- a) $x^2 + y^2 + z^2 = 4$.
- b) $x^2 + 4y^2 = 4$.
- c) $x^2 + 4y^2 + 9z^2 = 36$.
- d) $z = x^2 + y^2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** Es una esfera de radio 2 ⇒ coordenadas esféricas con $r = 2$.

**b)** Es un cilindro elíptico ($\frac{x^2}{4} + y^2 = 1$, sin $z$) ⇒ $x = 2\cos u$, $y = \mathop{\mathrm{sen}}u$, $z = v$.

**c)** Dividiendo por 36: $\frac{x^2}{36} + \frac{y^2}{9} + \frac{z^2}{4} = 1$, un elipsoide de semiejes 6, 3 y 2 ⇒ esféricas "estiradas".

**d)** Es un gráfico ⇒ $(u, v, u^2 + v^2)$. También se puede usar $(\rho\cos\varphi, \rho\mathop{\mathrm{sen}}\varphi, \rho^2)$.

</details>

**Respuesta:**

- a) $\bar X = (2\mathop{\mathrm{sen}}(\theta)\cos(\varphi),\ 2\mathop{\mathrm{sen}}(\theta)\mathop{\mathrm{sen}}(\varphi),\ 2\cos(\theta))$ con $\theta \in [0,\pi]$, $\varphi \in [0,2\pi]$.
- b) $\bar X = (2\cos(u),\ \mathop{\mathrm{sen}}(u),\ v)$ con $u \in [0,2\pi]$, $v \in \Re$.
- c) $\bar X = (6\mathop{\mathrm{sen}}(\theta)\cos(\varphi),\ 3\mathop{\mathrm{sen}}(\theta)\mathop{\mathrm{sen}}(\varphi),\ 2\cos(\theta))$ con $\theta \in [0,\pi]$, $\varphi \in [0,2\pi]$.
- d) $\bar X = (u,\ v,\ u^2 + v^2) \wedge (u,v) \in \Re^2$.

</details>

---

### 04) Integrales sobre una superficie implícita

Sea $S$ una superficie uniforme respecto del plano $xy$, definida implícitamente mediante la ecuación $G(x,y,z) = 0$. Imponga hipótesis para $G$ de manera que $S$ sea suave; en ese caso, si la ecuación en forma explícita fuera $z = g(x,y)$ con $(x,y) \in D_{xy}$, demuestre que:

- Para campo escalar: $\displaystyle\iint_S f\thinspace d\sigma = \iint_{D_{xy}}\left[f\thinspace\frac{\Vert\nabla G\Vert}{|G'_z|}\right]_{z = g(x,y)}dx\thinspace dy$.
- Para campo vectorial: $\displaystyle\iint_S\bar f\cdot d\bar\sigma = \iint_{D_{xy}}\left[\frac{\bar f\cdot\nabla G}{|G'_z|}\right]_{z = g(x,y)}dx\thinspace dy$.

Donde, en ambos casos, $D_{xy}$ se obtiene proyectando $S$ sobre el plano $xy$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Hipótesis:** $G \in C^1$ en un abierto que contiene a $S$, y $G'_z \ne 0$ sobre $S$. Esto garantiza (Cauchy-Dini) que $S$ es localmente $z = g(x,y)$ con $g \in C^1$, y que $\nabla G \ne \vec 0$.

**Paso 1 — Parametrizar.** $\bar F(x,y) = (x,\ y,\ g(x,y))$, de modo que:

$$\bar F'_x\wedge\bar F'_y = (-g'_x,\ -g'_y,\ 1)$$

**Paso 2 — Derivadas implícitas.** $g'_x = -\dfrac{G'_x}{G'_z}$ y $g'_y = -\dfrac{G'_y}{G'_z}$. Entonces:

$$\bar F'_x\wedge\bar F'_y = \left(\frac{G'_x}{G'_z},\ \frac{G'_y}{G'_z},\ 1\right) = \frac{\nabla G}{G'_z}$$

**Paso 3 — Escalar.** $d\sigma = \left\lVert\dfrac{\nabla G}{G'_z}\right\rVert dx\thinspace dy = \dfrac{\lVert\nabla G\rVert}{|G'_z|}dx\thinspace dy$, y queda la primera fórmula.

**Paso 4 — Vectorial.** $\bar f\cdot\breve n\thinspace d\sigma = \pm\thinspace\bar f\cdot\dfrac{\nabla G}{G'_z}\thinspace dx\thinspace dy$. Orientando $S$ según $\nabla G$ (el signo se elige para que el factor sea $|G'_z|$), queda $\dfrac{\bar f\cdot\nabla G}{|G'_z|}\thinspace dx\thinspace dy$. $\blacksquare$

</details>

**Respuesta:** Hipótesis: $G \in C^1$ y $G'_z \ne 0$ sobre $S$. La demostración usa que la normal del gráfico es $(-g'_x, -g'_y, 1) = \nabla G/G'_z$.

</details>

---

### 05) Áreas de superficies

Calcule el área de las siguientes superficies:

- a) Trozo de superficie cilíndrica $z = 2x^2$ con $y \le x$, $z \le 6$, 1° octante.
- b) Trozo de superficie cónica $z = \sqrt{2x^2 + 2y^2}$ interior a la esfera de radio 12 con centro en el origen de coordenadas.
- c) Trozo de superficie cilíndrica $x^2 + z^2 = 4$ con $-x \le y \le x$, $z \ge 0$.
- d) Superficie esférica de radio $R$.
- e) Trozo de superficie cilíndrica $x^2 + y^2 = 2x$ con $x^2 + y^2 + z^2 \le 4$ en el 1° octante.
- f) Superficie frontera del cuerpo definido por $x^2 + y^2 \le 1$, $0 \le z \le \sqrt{x^2 + y^2}$.
- g) Superficie de ecuación $z = x^2 - y$ con $|y| < x$, $x < 1$.
- h) Trozo de plano tangente a $z = x + \ln(xy)$ en $(1,1,z_0)$ con $x^2 + y^2 \le 9$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Fórmula:** $A = \displaystyle\iint_D\lVert\vec N\rVert\thinspace du\thinspace dv$. Para un gráfico $z = f(x,y)$: $\lVert\vec N\rVert = \sqrt{1 + f_x'^2 + f_y'^2}$.

**a)** Gráfico $z = 2x^2$ ⇒ $\lVert\vec N\rVert = \sqrt{1 + 16x^2}$.

- Región: $0 \le y \le x$ y $2x^2 \le 6 \Rightarrow x \le \sqrt3$.

$$A = \int_0^{\sqrt3}dx\int_0^x\sqrt{1 + 16x^2}\thinspace dy = \int_0^{\sqrt3}x\sqrt{1 + 16x^2}\thinspace dx = \left[\frac{(1 + 16x^2)^{3/2}}{48}\right]_0^{\sqrt3} = \frac{343 - 1}{48} = \frac{57}{8}$$

**b)** Cono $z = \sqrt2\thinspace\rho$ ⇒ $\lVert\vec N\rVert = \sqrt{1 + 2} = \sqrt3$ (por unidad de área proyectada).

- Dentro de la esfera: $\rho^2 + z^2 = 3\rho^2 \le 144 \Rightarrow \rho \le 4\sqrt3$.

$$A = \sqrt3\cdot\pi\thinspace(4\sqrt3)^2 = 48\sqrt3\thinspace\pi$$

**c)** Parametrización: $(2\cos\theta,\ y,\ 2\mathop{\mathrm{sen}}\theta)$ ⇒ $\lVert\vec N\rVert = 2$.

- $z \ge 0 \Rightarrow \theta\in[0, \pi]$.
- $-x \le y \le x$ exige $x \ge 0 \Rightarrow \theta\in[0, \pi/2]$, e $y\in[-2\cos\theta,\ 2\cos\theta]$.

$$A = \int_0^{\pi/2}\negthinspace\negthinspace\int_{-2\cos\theta}^{2\cos\theta}2\thinspace dy\thinspace d\theta = \int_0^{\pi/2}8\cos\theta\thinspace d\theta = 8$$

**d)** $\lVert\vec N\rVert = R^2\mathop{\mathrm{sen}}\theta$ ⇒ $A = \displaystyle\int_0^{2\pi}\negthinspace\negthinspace\int_0^\pi R^2\mathop{\mathrm{sen}}\theta\thinspace d\theta\thinspace d\varphi = 4\pi R^2$.

**e)** Cilindro de centro $(1,0)$ y radio 1: $(1 + \cos t,\ \mathop{\mathrm{sen}}t,\ z)$ ⇒ $\lVert\vec N\rVert = 1$.

- 1.er octante: $y \ge 0 \Rightarrow t\in[0,\pi]$, y $z \ge 0$.
- Esfera: $z \le \sqrt{4 - (x^2 + y^2)} = \sqrt{4 - 2x} = \sqrt{2 - 2\cos t} = 2\mathop{\mathrm{sen}}(t/2)$.

$$A = \int_0^\pi2\mathop{\mathrm{sen}}\frac t2\thinspace dt = \left[-4\cos\frac t2\right]_0^\pi = 4$$

**f)** La frontera tiene tres caras:

- piso $z = 0$, $\rho \le 1$: área $\pi$;
- pared $\rho = 1$, $0 \le z \le 1$: área $2\pi\cdot1 = 2\pi$;
- techo cónico $z = \rho$, $\rho \le 1$: $\lVert\vec N\rVert = \sqrt2$, área $\sqrt2\thinspace\pi$.

$A = \pi(3 + \sqrt2)$.

**g)** Gráfico $z = x^2 - y$ ⇒ $\lVert\vec N\rVert = \sqrt{1 + 4x^2 + 1} = \sqrt{2 + 4x^2}$.

- Región: $0 < x < 1$, $-x < y < x$ (ancho $2x$).

$$A = \int_0^1 2x\sqrt{2 + 4x^2}\thinspace dx = \left[\frac{(2 + 4x^2)^{3/2}}{6}\right]_0^1 = \frac{6\sqrt6 - 2\sqrt2}{6} = \sqrt6 - \frac{\sqrt2}{3}$$

**h)**

- Punto: $z_0 = 1 + \ln1 = 1$.
- Derivadas: $z'_x = 1 + \frac1x \to 2$ y $z'_y = \frac1y \to 1$. Plano tangente: $z = 1 + 2(x - 1) + (y - 1)$.
- Es un plano con $\lVert\vec N\rVert = \sqrt{1 + 4 + 1} = \sqrt6$, sobre el disco de área $9\pi$.

$A = 9\sqrt6\thinspace\pi$.

</details>

**Respuesta:**

- a) $57/8$.
- b) $48\pi\sqrt3$.
- c) $8$.
- d) $4\pi R^2$.
- e) $4$.
- f) $\pi(3 + \sqrt2)$.
- g) $\sqrt6 - \sqrt2/3$.
- h) $9\pi\sqrt6$.

</details>

---

### 06) Momento de inercia de una chapa

Calcule el momento de inercia respecto del eje $z$ de una chapa con forma de paraboloide $z = x^2 + y^2$, con $x \ge 0 \wedge 1 \le z \le 4$, si la densidad superficial en cada punto de la chapa es $\delta(x,y,z) = \dfrac{k}{x^2 + y^2}$ con $k$ constante.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Integrando.** $I_z = \iint_S(x^2 + y^2)\thinspace\delta\thinspace d\sigma = \iint_S k\thinspace d\sigma = k\cdot A(S)$: la distancia al cuadrado se cancela con la densidad.

**Paso 2 — Área.** Parametrizamos $(\rho\cos\varphi,\ \rho\mathop{\mathrm{sen}}\varphi,\ \rho^2)$, con $\lVert\vec N\rVert = \rho\sqrt{1 + 4\rho^2}$.

- $1 \le z \le 4 \Rightarrow 1 \le \rho \le 2$.
- $x \ge 0 \Rightarrow \varphi\in[-\pi/2, \pi/2]$.

$$A = \int_{-\pi/2}^{\pi/2}\negthinspace\negthinspace\int_1^2\rho\sqrt{1 + 4\rho^2}\thinspace d\rho\thinspace d\varphi = \pi\left[\frac{(1 + 4\rho^2)^{3/2}}{12}\right]_1^2 = \frac{\pi}{12}\left(17^{3/2} - 5^{3/2}\right)$$

**Paso 3 — Resultado.** $I_z = \dfrac{k\pi}{12}\left(17^{3/2} - 5^{3/2}\right) \approx 13{,}47\thinspace k$.

</details>

**Respuesta:** $\dfrac{k\pi}{12}\left(17^{3/2} - 5^{3/2}\right)$.

</details>

---

### 07) Flujo de un campo normal de módulo constante

Sea $\bar F = k\thinspace\breve n$ con $k > 0$ constante, demuestre que $\displaystyle\iint_S\bar F\cdot\breve n\thinspace d\sigma = F\ \text{área}(S)$ con $F = \Vert\bar F\Vert$.<sup>(\*)</sup>

<sup>(\*)</sup> Flujo de campo con módulo constante, con igual orientación que la superficie en cada punto.

<details>
<summary><b>Solución</b></summary>

**Respuesta:** $\bar F\cdot\breve n = k\thinspace\breve n\cdot\breve n = k$, y además $F = \lVert k\breve n\rVert = k$. Entonces:

$$\iint_S\bar F\cdot\breve n\thinspace d\sigma = k\iint_S d\sigma = F\cdot\text{área}(S) \quad\blacksquare$$

Observe que en este caso $\bar F\cdot\breve n$ resulta constante.

</details>

---

### 08) Campo constante y superficie plana

Demuestre que el flujo de $\bar F$ constante a través de $S$ plana con normal $\breve n$ es $\bar F\cdot\breve n$ área($S$).

<details>
<summary><b>Solución</b></summary>

**Respuesta:** como $S$ es plana, $\breve n$ es constante; como $\bar F$ también lo es, el producto $\bar F\cdot\breve n$ es una constante que sale de la integral:

$$\iint_S\bar F\cdot\breve n\thinspace d\sigma = (\bar F\cdot\breve n)\iint_S d\sigma = \bar F\cdot\breve n\ \text{área}(S) \quad\blacksquare$$

</details>

---

### 09) Flujo a través de una equipotencial

Sea $\bar f \in C^1$ un campo de gradientes y $S$ un trozo de una de sus superficies equipotenciales (que se supone suave). Demuestre que cuando $S$ está orientada en el sentido de los potenciales crecientes, el flujo de $\bar f$ a través de $S$ es positivo.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

Sea $\bar f = \nabla\phi$. $S$ está contenida en un conjunto de nivel $\phi = c$, y el gradiente es normal a los conjuntos de nivel y apunta hacia donde $\phi$ crece (Unidad 6). Con $S$ suave, $\nabla\phi \ne \vec 0$ sobre $S$. Por lo tanto, orientada hacia los potenciales crecientes:

$$\breve n = \frac{\nabla\phi}{\lVert\nabla\phi\rVert} \ \Rightarrow\ \bar f\cdot\breve n = \nabla\phi\cdot\frac{\nabla\phi}{\lVert\nabla\phi\rVert} = \lVert\nabla\phi\rVert > 0$$

El flujo es la integral de una función positiva sobre $S$, que tiene área positiva:

$$\Phi = \iint_S\lVert\nabla\phi\rVert\thinspace d\sigma > 0 \quad\blacksquare$$

</details>

**Respuesta:** Sobre una equipotencial orientada hacia potenciales crecientes, $\breve n = \nabla\phi/\lVert\nabla\phi\rVert$ y $\bar f\cdot\breve n = \lVert\nabla\phi\rVert > 0$.

</details>

---

### 10) Cálculo de flujos

Calcule el flujo de $\bar f$ a través de $S$, indicando gráficamente la orientación del versor normal que ha elegido, o bien que se le solicite en cada caso.<sup>(&)</sup>

- a) $\bar f(x,y,z) = (x^2 + yz,\ xz,\ 2z^2 - 2xz)$ a través de la superficie frontera del cuerpo definido por $1 \le z \le 5 - x^2 - y^2$.
- b) $\bar f(x,y,z) = (x,\ y,\ z)$ a través de la superficie esférica de ecuación $x^2 + y^2 + z^2 = 4$.
- c) $\bar f(x,y,z) = (xy,\ zx,\ y - xz^2)$ a través del trozo de superficie cilíndrica de ecuación $y = x^3$ con $0 \le z \le x + y$, $x + y \le 10$.
- d) $\bar f(x,y,z) = (y,\ x,\ y) \wedge (x,\ z,\ y)$ a través del trozo de plano tangente a la superficie de ecuación $z = x^2 - yx^3$ en el punto $(1,2,-1)$ con $(x,y) \in [0,2]\times[1,3]$.
- e) $\bar f(x,y,z) = (xy,\ z,\ y)$ a través de la superficie frontera del cuerpo limitado por $x^2 + y^2 \le 4$, $x + y + z \le 18$, en el 1° octante. Nota: en este caso, como en muchos otros, el cálculo de flujo puede realizarse en forma más sencilla aplicando el teorema de la divergencia (ver T.P. siguiente).

<sup>(&)</sup> Cuando la superficie es cerrada (frontera de un cuerpo $H$), se la orienta (por convención) con versor normal saliente de $H$. Entonces, el flujo positivo es "saliente" de $H$ y el negativo es "entrante" a $H$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Recordatorio:** flujo $= \iint_D\bar f\cdot\vec N\thinspace du\thinspace dv$, con $\vec N$ en el sentido pedido. Para gráficos $z = g$, $\vec N_{\uparrow} = (-g'_x, -g'_y, 1)$.

**a)** El cuerpo está entre el disco $z = 1$ (piso) y el paraboloide $z = 5 - \rho^2$ (techo). Se cortan en $\rho = 2$. Normales salientes:

*Techo* ($z = 5 - x^2 - y^2$, normal hacia arriba $\vec N = (2x, 2y, 1)$):

$$\bar f\cdot\vec N = 2x(x^2 + yz) + 2y\cdot xz + 2z^2 - 2xz = 2x^3 + 4xyz - 2xz + 2z^2$$

Sobre el disco $\rho \le 2$, los términos impares en $x$ se anulan por simetría. Queda:

$$\iint 2(5 - \rho^2)^2\thinspace dA = 2\cdot2\pi\int_0^2(5 - \rho^2)^2\rho\thinspace d\rho = 2\pi\int_0^4(5 - w)^2dw = 2\pi\thinspace\frac{125 - 1}{3} = \frac{248\pi}{3}$$

*Piso* ($z = 1$, normal $(0,0,-1)$): $\bar f\cdot\breve n = -(2 - 2x)$ ⇒ $\displaystyle\iint_{\rho\le2}(-2 + 2x)\thinspace dA = -2\cdot4\pi + 0 = -8\pi$.

*Total:*

$$\frac{248\pi}{3} - 8\pi = \frac{224\pi}{3}$$

Control con divergencia: $\mathop{\mathrm{div}}\bar f = 4z$ y $\iiint 4z\thinspace dV = \frac{224\pi}{3}$ ✓.

**b)** Sobre la esfera de radio 2, la normal saliente es $\breve n = \frac{(x,y,z)}{2}$:

$$\bar f\cdot\breve n = \frac{x^2+y^2+z^2}{2} = \frac42 = 2$$

Es constante ⇒ $\Phi = 2\cdot A = 2\cdot4\pi\cdot4 = 32\pi$.

**c)**

*Parametrización:* $(x,\ x^3,\ z)$, con $\vec N = \bar X'_x\wedge\bar X'_z = (1, 3x^2, 0)\wedge(0,0,1) = (3x^2,\ -1,\ 0)$. Su componente $y$ es negativa: apunta **desde $S$ hacia el plano $xz$**, que es la orientación de la respuesta.

*Región:* $0 \le z \le x + x^3$, lo que exige $x \ge 0$, y $x + x^3 \le 10 \Rightarrow x \le 2$.

*Integrando:* $\bar f\cdot\vec N = xy\cdot3x^2 - zx = 3x^6 - xz$.

$$\Phi = \int_0^2dx\int_0^{x+x^3}(3x^6 - xz)\thinspace dz = \int_0^2\left[3x^6(x + x^3) - \frac{x(x + x^3)^2}{2}\right]dx = \int_0^2\left(\frac52x^7 + 3x^9 - \frac12x^3 - x^5\right)dx$$

$$= 80 + \frac{1536}{5} - 2 - \frac{32}{3} = \frac{5618}{15} \approx 374{,}53$$

**d)**

*Campo:*

$$\bar f = (y, x, y)\wedge(x, z, y) = (xy - yz,\ xy - y^2,\ yz - x^2)$$

*Plano tangente* a $z = x^2 - yx^3$ en $(1,2,-1)$: $z'_x = 2x - 3yx^2 = -4$ y $z'_y = -x^3 = -1$, así que:

$$z = -1 - 4(x - 1) - (y - 2) = 5 - 4x - y$$

*Normal hacia arriba* ($\breve n\cdot\breve k > 0$): $\vec N = (4, 1, 1)$.

*Integrando,* reemplazando $z = 5 - 4x - y$:

$$\bar f\cdot\vec N = 4(xy - yz) + (xy - y^2) + (yz - x^2) = 5xy - 3yz - y^2 - x^2 = 17xy - 15y + 2y^2 - x^2$$

*Integral sobre $[0,2]\times[1,3]$* (con $\int_0^2x = 2$, $\int_1^3y = 4$, $\int_1^3y^2 = \frac{26}{3}$ y $\int_0^2x^2 = \frac83$):

$$\Phi = 17\cdot2\cdot4 - 15\cdot2\cdot4 + 2\cdot2\cdot\frac{26}{3} - \frac83\cdot2 = 136 - 120 + \frac{104}{3} - \frac{16}{3} = \frac{136}{3}$$

**e)** Cuerpo: $x, y, z \ge 0$, $x^2 + y^2 \le 4$, $z \le 18 - x - y$. Tiene 5 caras, con normal saliente:

| Cara | Normal | $\bar f\cdot\breve n$ | Flujo |
|---|---|---|---|
| $z = 0$ (cuarto de disco) | $(0,0,-1)$ | $-y$ | $-\iint y\thinspace dA = -\frac83$ |
| $x = 0$ | $(-1,0,0)$ | $-xy = 0$ | $0$ |
| $y = 0$ ($0 \le x \le 2$, $0 \le z \le 18 - x$) | $(0,-1,0)$ | $-z$ | $-\int_0^2\frac{(18-x)^2}{2}dx = -\frac{868}{3}$ |
| Techo $z = 18 - x - y$ | $(1,1,1)$ | $xy + 18 - x$ | $2 + 18\pi - \frac83$ |
| Pared $\rho = 2$ | $(\cos\varphi, \mathop{\mathrm{sen}}\varphi, 0)$ | $4\mathop{\mathrm{sen}}\varphi\cos^2\varphi + z\mathop{\mathrm{sen}}\varphi$ | $\frac{1016}{3} - 19\pi$ |

Para la pared: $d\sigma = 2\thinspace d\varphi\thinspace dz$ con $z\in[0,\ 18 - 2\cos\varphi - 2\mathop{\mathrm{sen}}\varphi]$ y $\varphi\in[0,\pi/2]$. Su integral es $(44 - \pi) + \left(292 + \frac83 - 18\pi\right)$.

*Suma:*

$$-\frac83 - \frac{868}{3} + 2 + 18\pi - \frac83 + \frac{1016}{3} - 19\pi = 46 - \pi$$

*Con el teorema de la divergencia* (mucho más corto): $\mathop{\mathrm{div}}\bar f = y$, y

$$\iiint y\thinspace dV = \iint_{\text{cuarto de disco}}y(18 - x - y)\thinspace dA = 48 - 2 - \pi = 46 - \pi \ ✓$$

</details>

**Respuesta:**

- a) $224\pi/3$.
- b) $32\pi$.
- c) $\dfrac{5618}{15}$ con $\breve n$ orientado desde $S$ hacia el plano $xz$.
- d) $\dfrac{136}{3}$ con $\breve n \ /\ \breve n\cdot(0,0,1) > 0$.
- e) $46 - \pi$.

</details>

---

### 11) Flujo con una componente desconocida

Sea $\bar f$ continuo tal que $\bar f(x,y,z) = (x - y,\ x - z,\ g(x,y,z))$, calcule el flujo de $\bar f$ a través de la superficie de ecuación $x = y^2$ con $0 \le z \le 4$, $0 \le y \le 2 - x^2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $(y^2,\ y,\ z)$, con:

$$\vec N = \bar X'_y\wedge\bar X'_z = (2y, 1, 0)\wedge(0, 0, 1) = (1,\ -2y,\ 0)$$

Su componente $y$ es negativa: apunta desde $S$ hacia el plano $xz$.

**Paso 2 — Región.** Sobre la superficie, $0 \le y \le 2 - x^2 = 2 - y^4 \Rightarrow y^4 + y - 2 \le 0 \Rightarrow y \le 1$. Además $z\in[0,4]$.

**Paso 3 — Integrando.** $\vec N$ tiene tercera componente nula ⇒ **$g$ no interviene**:

$$\bar f\cdot\vec N = (x - y) - 2y(x - z) = y^2 - y - 2y^3 + 2yz$$

**Paso 4 — Integral.**

$$\int_0^4dz\int_0^1(y^2 - y - 2y^3 + 2yz)\thinspace dy = \int_0^4\left(\frac13 - \frac12 - \frac12 + z\right)dz = 4\left(-\frac23\right) + 8 = \frac{16}{3}$$

</details>

**Respuesta:** $16/3$ con $\breve n$ orientado desde $S$ hacia el plano $xz$.

</details>

---

### 12) Flujo de un gradiente a través de un plano

Calcule el flujo del gradiente de $f(x,y,z) = x + y + z\thinspace g(x - y)$ a través de $x + y = 4$ en el 1° octante, con $0 \le z \le 8$. Suponga $g \in C^1$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Gradiente.**

$$\nabla f = \big(1 + z\thinspace g'(x - y),\ 1 - z\thinspace g'(x - y),\ g(x - y)\big)$$

**Paso 2 — Normal del plano** con $\breve n\cdot\breve\imath > 0$: $\breve n = \dfrac{(1,1,0)}{\sqrt2}$.

**Paso 3 — Producto.** Los términos con $g'$ se cancelan:

$$\nabla f\cdot\breve n = \frac{1 + zg' + 1 - zg'}{\sqrt2} = \frac{2}{\sqrt2} = \sqrt2$$

**Paso 4 — Área del trozo de plano.** El segmento de $(4,0)$ a $(0,4)$ mide $4\sqrt2$, y la altura es 8 ⇒ área $= 32\sqrt2$.

**Paso 5 — Flujo** (integrando constante): $\sqrt2\cdot32\sqrt2 = 64$.

</details>

**Respuesta:** $64$ con $\breve n \ /\ \breve n\cdot(1,0,0) > 0$.

</details>

---

### 13) Flujo proporcional al área de la proyección

Sea $S$ un trozo de superficie de ecuación $z = y^2 - x^2$ cuya proyección sobre el plano $xy$ es la región $D$. Sea $g(x,y,z) = z + h(xy)$ con $h \in C^1$, demuestre que el flujo de $\nabla g$ a través de $S$ es proporcional al área de $D$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Gradiente.** $\nabla g = \big(y\thinspace h'(xy),\ x\thinspace h'(xy),\ 1\big)$.

**Paso 2 — Normal** (hacia arriba) de $z = y^2 - x^2$: $\vec N = (-z'_x, -z'_y, 1) = (2x,\ -2y,\ 1)$.

**Paso 3 — Producto.**

$$\nabla g\cdot\vec N = 2xy\thinspace h' - 2xy\thinspace h' + 1 = 1$$

**Paso 4 — Flujo.**

$$\Phi = \iint_D 1\thinspace dx\thinspace dy = \text{área}(D)$$

Con la orientación opuesta da $-\text{área}(D)$. En ambos casos es proporcional al área de $D$. $\blacksquare$

</details>

**Respuesta:** Con $\breve n$ hacia $z^+$, $\nabla g\cdot\vec N = 1$ y el flujo es igual al área de $D$.

</details>

---

### 14) Flujo a través de un cubo

Calcule el flujo de $\bar X = (x,y,z)$ a través de la frontera del cubo $[-1,1]\times[-1,1]\times[-1,1]$ orientada con normal saliente del cubo.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Cada cara**, por ejemplo $x = 1$ con $\breve n = (1,0,0)$: $\bar X\cdot\breve n = x = 1$. Sobre $x = -1$, con $\breve n = (-1,0,0)$: $\bar X\cdot\breve n = -x = 1$. Lo mismo vale en las 6 caras.

**Flujo por cara:** $1\cdot\text{área} = 1\cdot4 = 4$.

**Total:** $6\cdot4 = 24$.

*Control con divergencia:* $\mathop{\mathrm{div}}\bar X = 3$ y el volumen es 8 ⇒ $24$ ✓.

</details>

**Respuesta:** $24$.

</details>

---

### 15) Flujo a través de un triángulo

Dado $\bar f(x,y,z) = (x,\ 2y,\ z)$, calcule el flujo de $\bar f$ a través del triángulo con vértices en los puntos $(2,0,0)$, $(0,2,0)$ y $(0,0,1)$. Indique en un gráfico cómo ha decidido orientar la superficie.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Plano.** Por los cortes con los ejes: $\frac x2 + \frac y2 + z = 1$, es decir $z = \dfrac{2 - x - y}{2}$.

**Paso 2 — Orientación hacia $z^+$:** $\vec N = (-z'_x, -z'_y, 1) = \left(\frac12, \frac12, 1\right)$.

**Paso 3 — Integrando.** Reemplazando $z$:

$$\bar f\cdot\vec N = \frac x2 + y + z = \frac x2 + y + \frac{2 - x - y}{2} = 1 + \frac y2$$

**Paso 4 — Región:** el triángulo $x, y \ge 0$, $x + y \le 2$, de área 2.

$$\Phi = \iint\left(1 + \frac y2\right)dA = 2 + \frac12\int_0^2y\thinspace(2 - y)\thinspace dy = 2 + \frac12\cdot\frac43 = \frac83$$

</details>

**Respuesta:** $8/3$, superficie orientada hacia $z^+$.

</details>

---

### 16) Flujo a través de un disco

Dado $\bar f(x,y,z) = (x^2z,\ z^3,\ x^2z)$, calcule el flujo de $\bar f$ a través del trozo de plano $\Sigma$ de ecuación $z = 2$ con $x^2 + y^2 + z^2 \le 5$. Indique gráficamente cómo decidió orientar a $\Sigma$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Región.** Con $z = 2$: $x^2 + y^2 \le 1$, el disco unitario.

**Paso 2 — Orientación hacia $z^+$.** $\breve n = (0,0,1)$ ⇒ $\bar f\cdot\breve n = x^2z = 2x^2$.

**Paso 3 — Integral** en polares:

$$\Phi = \iint_{\rho\le1}2x^2\thinspace dA = 2\int_0^{2\pi}\cos^2\varphi\thinspace d\varphi\int_0^1\rho^3\thinspace d\rho = 2\cdot\pi\cdot\frac14 = \frac\pi2$$

</details>

**Respuesta:** $\pi/2$, $\Sigma$ orientado hacia $z^+$.

</details>

---

### 17) Flujo a partir del flujo total

Sea $\partial D$ la superficie frontera del cuerpo $D$ definido por: $1 \le z \le 5 - x^2 - y^2$. Sabiendo que $\displaystyle\oint\negthinspace\negthinspace\negthinspace\oint_{\partial D}\bar f\cdot\breve n\thinspace d\sigma = 0$ y que $\bar f(x,y,z) = (\mathop{\mathrm{sen}}(y\cos(z)) - 2x,\ \mathop{\mathrm{sen}}(x\cos(z)) - y,\ 3z)$, calcule el flujo de $\bar f$ a través del trozo de frontera de ecuación $z = 5 - x^2 - y^2$ orientado hacia $z^+$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Descomponer.** $\partial D$ = techo (paraboloide) + piso (disco $z = 1$, $\rho \le 2$). Con normal saliente, el techo apunta hacia $z^+$ (como se pide) y el piso hacia $z^-$:

$$0 = \Phi_{\text{techo}} + \Phi_{\text{piso}} \ \Rightarrow\ \Phi_{\text{techo}} = -\Phi_{\text{piso}}$$

**Paso 2 — Flujo por el piso.** $\breve n = (0,0,-1)$ ⇒ $\bar f\cdot\breve n = -3z = -3$ en $z = 1$. El disco tiene área $4\pi$:

$$\Phi_{\text{piso}} = -3\cdot4\pi = -12\pi$$

**Paso 3 — Resultado.** $\Phi_{\text{techo}} = 12\pi$. Se evitó integrar sobre el paraboloide, que con ese campo sería muy difícil.

</details>

**Respuesta:** $12\pi$.

</details>

---

## Ejercicios adicionales (Guía de ejercicios adicionales de flujo)

Calcule el flujo de $\bar F$ a través de $S$, indicando gráficamente la orientación del versor normal que ha elegido, o bien que se le solicite en cada caso.

> En el PDF original, los resultados de los ítems 4 y 5 están corregidos a mano: en el 4 el resultado es $32\pi/3$, y en el 5 la condición es $x + y + z \le 2$. Abajo se usan los valores corregidos.

### Adicional 1)

$\bar F(x,y,z) = x\thinspace i + y\thinspace j + z\thinspace k$ a través del plano $x + y + z = 1$ ubicado en el primer octante.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

- Gráfico $z = 1 - x - y$, con normal hacia $z^+$: $\vec N = (1, 1, 1)$.
- $\bar F\cdot\vec N = x + y + z = 1$ sobre el plano.
- La proyección es el triángulo $x, y \ge 0$, $x + y \le 1$, de área $\frac12$.

$$\Phi = \iint 1\thinspace dA = \frac12$$

</details>

**Respuesta:** $1/2$ con normal con componente $z$ positiva.

</details>

---

### Adicional 2)

$\bar F(x,y,z) = z\thinspace i + x\thinspace j + y\thinspace k$, a través de la porción de superficie $x^2 + y^2 = 1$ entre $z = 0$ y $z = 2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

- Parametrización: $(\cos t, \mathop{\mathrm{sen}}t, z)$, con normal saliente $\breve n = (\cos t, \mathop{\mathrm{sen}}t, 0)$ y $d\sigma = dt\thinspace dz$.
- $\bar F\cdot\breve n = z\cos t + \cos t\mathop{\mathrm{sen}}t$.

$$\Phi = \int_0^2\negthinspace\negthinspace\int_0^{2\pi}(z\cos t + \cos t\mathop{\mathrm{sen}}t)\thinspace dt\thinspace dz = 0$$

Las integrales de $\cos t$ y de $\cos t\mathop{\mathrm{sen}}t$ en un período son 0.

</details>

**Respuesta:** $0$.

</details>

---

### Adicional 3)

$F(x,y,z) = x\thinspace i + y\thinspace j + z\thinspace k$, a través de la porción de superficie $z = 4 - x^2 - y^2$ con $z \ge 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

- Normal hacia $z^+$: $\vec N = (2x, 2y, 1)$.
- $\bar F\cdot\vec N = 2x^2 + 2y^2 + z = 2\rho^2 + 4 - \rho^2 = \rho^2 + 4$.
- $z \ge 0 \Rightarrow \rho \le 2$.

$$\Phi = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2(\rho^2 + 4)\rho\thinspace d\rho\thinspace d\varphi = 2\pi(4 + 8) = 24\pi$$

</details>

**Respuesta:** $24\pi$ con normal con componente $z$ positiva.

</details>

---

### Adicional 4)

$\bar F(x,y,z) = x\thinspace i + y\thinspace j - z\thinspace k$, a través de la porción de superficie $z = \sqrt{x^2 + y^2}$ entre $z = 0$ y $z = 2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

- Cono $z = \rho$, con normal hacia $z^-$: $\vec N = (z'_x, z'_y, -1) = \left(\frac x\rho, \frac y\rho, -1\right)$.
- $\bar F\cdot\vec N = \dfrac{x^2 + y^2}{\rho} + z = \rho + \rho = 2\rho$.

$$\Phi = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2 2\rho\cdot\rho\thinspace d\rho\thinspace d\varphi = 2\pi\cdot\frac{16}{3} = \frac{32\pi}{3}$$

</details>

**Respuesta:** $32\pi/3$ (corregido a mano en el PDF), con normal con componente $z$ negativa.

</details>

---

### Adicional 5)

$\bar F(x,y,z) = y\thinspace i + x\thinspace j + 2z\thinspace k$, a través de la porción de superficie $y = x^2$ ubicada en el primer octante con $x + y + z \le 2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Normal.** Con la parametrización $(x, x^2, z)$: $\bar X'_x\wedge\bar X'_z = (2x, -1, 0)$. Su componente $y$ es negativa, así que para la orientación pedida usamos $\vec N = (-2x,\ 1,\ 0)$.

**Paso 2 — Integrando.** $\bar F\cdot\vec N = -2x\thinspace y + x = x - 2x^3$.

**Paso 3 — Región.** $z$ va de $0$ a $2 - x - x^2$, que exige $x^2 + x \le 2 \Rightarrow x\in[0,1]$.

**Paso 4 — Integral.**

$$\Phi = \int_0^1(x - 2x^3)(2 - x - x^2)\thinspace dx = \int_0^1(2x - x^2 - 5x^3 + 2x^4 + 2x^5)\thinspace dx = 1 - \frac13 - \frac54 + \frac25 + \frac13 = \frac{3}{20}$$

</details>

**Respuesta:** $3/20$, con normal con componente $y$ positiva.

</details>

---

### Adicional 6)

$\bar F(x,y,z) = (x + y;\ y;\ 2x^2 + 2y^2)$ a través de la porción de superficie $z = x^2 + y^2$ con $x^2 + y^2 \le 4;\ y \ge |x|$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

- Normal hacia $z^+$: $\vec N = (-2x, -2y, 1)$.
- $\bar F\cdot\vec N = -2x(x + y) - 2y^2 + 2x^2 + 2y^2 = -2xy$.
- La región ($\rho \le 2$, $y \ge |x|$) es simétrica respecto del eje $y$, y $-2xy$ es impar en $x$ ⇒ la integral es 0.

Con la orientación opuesta también da 0.

</details>

**Respuesta:** $0$.

</details>

---

[← Volver al menú principal](../README.md)
