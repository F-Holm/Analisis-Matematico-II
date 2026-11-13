# Unidad 6 — Práctica: Funciones compuestas e implícitas

Ejercicios del **T.P. N.º 6 de la Guía de Trabajos Prácticos** ([TP06-Compuestas-Implicitas.pdf](../aula-virtual/06-Compuestas-Implicitas/TP06-Compuestas-Implicitas.pdf)). Las respuestas se controlaron con las [respuestas oficiales de la guía](../aula-virtual/00-Guia-TP/Guia-TP-2016-Respuestas.pdf) y con la [fe de erratas](../aula-virtual/00-Guia-TP/Guia-TP-2016-Fe-de-Erratas-2018-07-31.pdf).

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

### 01) Composiciones y matrices jacobianas

Dadas $f$ y $g$, analice en cada caso si quedan definidas $f\circ g$ y $g\circ f$. Además, para cada función generada mediante la composición, determine su dominio natural y obtenga su matriz jacobiana en algún punto interior al mismo.

- a) $\vec f(x,y) = (xy,\ x - y)$, $\ \vec g(u,v) = (u^2,\ v - u)$.
- b) $f(x,y) = x\sqrt{y}$, $\ \vec g(u) = (u,\ 2 - u)$.
- c) $\vec f(x,y) = (x - y,\ \sqrt{x + y})$, $\ \vec g(t) = (2 - t,\ t - 3)$.
- d) $\vec f(x,y) = (xy^2,\ y - x,\ x)$, $\ \vec g(u,v,w) = (u - v,\ w\sqrt{1 - u})$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Recordatorio:** $D(f\circ g)(\vec A) = Df(g(\vec A))\cdot Dg(\vec A)$. Primero se evalúa $g(\vec A)$, después cada jacobiana, y al final se multiplican.

**a)** $\vec f, \vec g: \Re^2\to\Re^2$ ⇒ las dos composiciones tienen sentido y ambas tienen dominio $\Re^2$.

*Jacobianas genéricas:*

$$D\vec f(x,y) = \begin{pmatrix} y & x \cr 1 & -1 \end{pmatrix}, \qquad D\vec g(u,v) = \begin{pmatrix} 2u & 0 \cr -1 & 1 \end{pmatrix}$$

*Composición* $f\circ g$ en $(1,1)$:

- $\vec g(1,1) = (1, 0)$.
- $D\vec f(1,0) = \begin{pmatrix} 0 & 1 \cr 1 & -1 \end{pmatrix}$ y $D\vec g(1,1) = \begin{pmatrix} 2 & 0 \cr -1 & 1 \end{pmatrix}$.

$$D(\vec f\circ\vec g)(1,1) = \begin{pmatrix} 0\cdot2 + 1\cdot(-1) & 0\cdot0 + 1\cdot1 \cr 1\cdot2 + (-1)(-1) & 1\cdot0 + (-1)\cdot1 \end{pmatrix} = \begin{pmatrix} -1 & 1 \cr 3 & -1 \end{pmatrix}$$

*Composición* $g\circ f$ en $(1,1)$:

- $\vec f(1,1) = (1, 0)$.
- $D\vec g(1,0) = \begin{pmatrix} 2 & 0 \cr -1 & 1 \end{pmatrix}$ y $D\vec f(1,1) = \begin{pmatrix} 1 & 1 \cr 1 & -1 \end{pmatrix}$.

$$D(\vec g\circ\vec f)(1,1) = \begin{pmatrix} 2 & 2 \cr -1 + 1 & -1 - 1 \end{pmatrix} = \begin{pmatrix} 2 & 2 \cr 0 & -2 \end{pmatrix}$$

**b)** $f: \Re^2\to\Re$ (dominio $y \ge 0$) y $\vec g: \Re\to\Re^2$.

*Composición* $f\circ g$: $f(u, 2 - u) = u\sqrt{2 - u}$, con dominio $u \le 2$.

$$(f\circ g)'(u) = \sqrt{2-u} - \frac{u}{2\sqrt{2-u}} \ \Rightarrow\ (f\circ g)'(1) = 1 - \frac12 = 0{,}5$$

*Composición* $g\circ f$: $\vec g(x\sqrt y) = (x\sqrt y,\ 2 - x\sqrt y)$, con dominio $y \ge 0$. Interior: $y > 0$.

- $D\vec g = \begin{pmatrix} 1 \cr -1 \end{pmatrix}$ (constante).
- $Df(1,1) = \left(\sqrt y,\ \dfrac{x}{2\sqrt y}\right)\Big|_{(1,1)} = \left(1,\ \tfrac12\right)$.

$$D(\vec g\circ f)(1,1) = \begin{pmatrix} 1 \cr -1 \end{pmatrix}\left(1\ \ \tfrac12\right) = \begin{pmatrix} 1 & \tfrac12 \cr -1 & -\tfrac12 \end{pmatrix}$$

**c)**

- *Composición* $f\circ g$: $\vec f(2 - t,\ t - 3) = (5 - 2t,\ \sqrt{(2-t)+(t-3)}) = (5 - 2t,\ \sqrt{-1})$. La raíz nunca está definida ⇒ dominio vacío ⇒ no queda definida.
- *Composición* $g\circ f$: $\vec g$ tiene **una** variable, pero $\vec f$ da vectores de $\Re^2$ ⇒ dimensiones incompatibles ⇒ no queda definida.

**d)** $\vec f: \Re^2\to\Re^3$ y $\vec g: \Re^3\to\Re^2$ ⇒ las dos composiciones son posibles.

*Composición* $f\circ g$: el dominio es el de $\vec g$, $u \le 1$, porque $\vec f$ está definida en todo $\Re^2$. Calculamos en $(0,1,1)$:

- $\vec g(0,1,1) = (-1,\ 1\cdot\sqrt1) = (-1, 1)$.
- $D\vec f(x,y) = \begin{pmatrix} y^2 & 2xy \cr -1 & 1 \cr 1 & 0 \end{pmatrix}$, que en $(-1,1)$ es $\begin{pmatrix} 1 & -2 \cr -1 & 1 \cr 1 & 0 \end{pmatrix}$.
- $D\vec g(u,v,w) = \begin{pmatrix} 1 & -1 & 0 \cr \frac{-w}{2\sqrt{1-u}} & 0 & \sqrt{1-u} \end{pmatrix}$, que en $(0,1,1)$ es $\begin{pmatrix} 1 & -1 & 0 \cr -\frac12 & 0 & 1 \end{pmatrix}$.

$$D(\vec f\circ\vec g)(0,1,1) = \begin{pmatrix} 1 + 1 & -1 & -2 \cr -1 - \frac12 & 1 & 1 \cr 1 & -1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & -1 & -2 \cr -\frac32 & 1 & 1 \cr 1 & -1 & 0 \end{pmatrix}$$

*Composición* $g\circ f$: $\vec g(xy^2,\ y - x,\ x) = (xy^2 - y + x,\ x\sqrt{1 - xy^2})$, con dominio $xy^2 \le 1$. Calculamos en $(0,1)$:

- $\vec f(0,1) = (0, 1, 0)$.
- $D\vec g(0,1,0) = \begin{pmatrix} 1 & -1 & 0 \cr 0 & 0 & 1 \end{pmatrix}$ y $D\vec f(0,1) = \begin{pmatrix} 1 & 0 \cr -1 & 1 \cr 1 & 0 \end{pmatrix}$.

$$D(\vec g\circ\vec f)(0,1) = \begin{pmatrix} 1 + 1 & -1 \cr 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & -1 \cr 1 & 0 \end{pmatrix}$$

</details>

**Respuesta:**

- a) Ambas quedan definidas con dominio $\Re^2$. $D(\vec f\circ\vec g)(1,1) = \begin{pmatrix} -1 & 1 \cr 3 & -1 \end{pmatrix}$; $\ D(\vec g\circ\vec f)(1,1) = \begin{pmatrix} 2 & 2 \cr 0 & -2 \end{pmatrix}$.
- b) Dominio de $f\circ g = \lbrace u \in \Re / u \le 2\rbrace$; dominio de $g\circ f = \lbrace(x,y) \in \Re^2 / y \ge 0\rbrace$. $D(f\circ g)(1) = (0.5)$; $\ D(g\circ f)(1,1) = \begin{pmatrix} 1 & 1/2 \cr -1 & -1/2 \end{pmatrix}$.
- c) Ninguna queda definida; tampoco sus matrices jacobianas.
- d) Dominio de $\vec f\circ\vec g = \lbrace(u,v,w) \in \Re^3 / u \le 1\rbrace$; dominio de $\vec g\circ\vec f = \lbrace(x,y) \in \Re^2 / xy^2 \le 1\rbrace$. $D(\vec f\circ\vec g)(0,1,1) = \begin{pmatrix} 2 & -1 & -2 \cr -3/2 & 1 & 1 \cr 1 & -1 & 0 \end{pmatrix}$; $\ D(\vec g\circ\vec f)(0,1) = \begin{pmatrix} 2 & -1 \cr 1 & 0 \end{pmatrix}$.

</details>

---

### 02) Descomponer una función

Dada $h : D \subset \Re^2 \to \Re \ /\ h(x,y) = x\ln(1 - xy)$ siendo $D$ su dominio natural, defina dos funciones cuya composición genere $h$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Idea:** la estructura de $h$ es "primera variable · ln(segunda)". Tomamos:

- de afuera, $f(u,v) = u\ln v$, que necesita $v > 0$;
- de adentro, $\vec g(x,y) = (x,\ 1 - xy)$.

**Dominio:** para que $\vec g(x,y) \in D_f$ hace falta $1 - xy > 0 \iff xy < 1$, que es justamente el dominio natural de $h$.

</details>

**Respuesta:** Por ejemplo, $h = f\circ\vec g$ si $f : D_f \subset \Re^2 \to \Re \ /\ f(u,v) = u\ln(v)$ con $D_f = \lbrace(u,v) \in \Re^2 / v > 0\rbrace$ y $\vec g : D_g \subset \Re^2 \to \Re^2 \ /\ \vec g(x,y) = (x,\ 1 - xy)$ con $D_g = \lbrace(x,y) \in \Re^2 / xy < 1\rbrace$.

</details>

---

### 03) Composición, derivada direccional y recta normal

Si $z = 2uv - 2\sqrt{v - u}$ con $\begin{cases} u = x - y^2 \cr v = x + 2xy - 1 \end{cases}$, resulta $z = h(x,y)$.

- a) Reconozca las funciones $f$ y $g$ que generan $h$ como $h = f\circ g$.
- b) Calcule la derivada direccional de $h$ en $(2,1)$, en la dirección que va hacia el $(5,5)$.
- c) Sea $n_0$ la recta normal a la gráfica de $h$ en $(2,1,z_0)$, exprese $n_0$ como la intersección de dos superficies.
- d) Analice si la recta $n_0$ mencionada en "c)" tiene algún punto en común con el eje $z$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** $f(u,v) = 2uv - 2\sqrt{v - u}$ y $\vec g(x,y) = (x - y^2,\ x + 2xy - 1)$.

**b)**

*Paso 1 — Variables intermedias en $(2,1)$:* $u = 2 - 1 = 1$, $v = 2 + 4 - 1 = 5$, $v - u = 4$.

*Paso 2 — Derivadas de $f$* (en $(u,v) = (1,5)$):

$$f'_u = 2v + \frac{1}{\sqrt{v-u}} = 10 + \frac12 = \frac{21}{2}, \qquad f'_v = 2u - \frac{1}{\sqrt{v-u}} = 2 - \frac12 = \frac32$$

*Paso 3 — Derivadas de $\vec g$* (en $(2,1)$):

- $u'_x = 1$ y $u'_y = -2y = -2$.
- $v'_x = 1 + 2y = 3$ y $v'_y = 2x = 4$.

*Paso 4 — Regla de la cadena:*

$$h'_x = f'_u u'_x + f'_v v'_x = \frac{21}{2} + \frac32\cdot3 = 15, \qquad h'_y = f'_u u'_y + f'_v v'_y = -21 + 6 = -15$$

*Paso 5 — Versor:* de $(2,1)$ a $(5,5)$ es $(3,4)$, con norma 5 ⇒ $\breve r = \left(\frac35, \frac45\right)$.

*Paso 6 — Derivada direccional:* $h$ es diferenciable porque es composición de $C^1$ (con $v - u > 0$):

$$h'((2,1), \breve r) = \nabla h\cdot\breve r = \frac{15\cdot3 - 15\cdot4}{5} = -3$$

**c)**

- $z_0 = h(2,1) = f(1,5) = 2\cdot1\cdot5 - 2\sqrt4 = 6$.
- Normal a la gráfica: $(h'_x, h'_y, -1) = (15, -15, -1)$.
- $n_0: (x, y, z) = (2 + 15t,\ 1 - 15t,\ 6 - t)$.

Eliminamos $t$:

- Sumando $x$ e $y$: $x + y = 3$.
- De $z$: $t = 6 - z$, y entonces $x = 2 + 15(6 - z) \Rightarrow x + 15z = 92$.

**d)** En el eje $z$ es $x = y = 0$, pero entonces $x + y = 0 \ne 3$ ⇒ no hay puntos en común.

</details>

**Respuesta:**

- a) $f(u,v) = 2uv - 2\sqrt{v - u}$, $\ g(x,y) = (x - y^2,\ x + 2xy - 1)$.
- b) $-3$.
- c) $\begin{cases} x + y = 3 \cr x + 15z = 92 \end{cases}$.
- d) No.

</details>

---

### 04) Regla de la cadena sin componer

Dada $w = u^3 - xv^2$ con $u = x\sqrt{y - x} \ \wedge\ v = 2x + y^2$, resulta $w = f(x,y)$. Aplicando la regla de derivación de funciones compuestas (sin realizar la composición), calcule $f'_x(0,1)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Árbol.** $w$ depende de $u$, de $v$ y **también directamente de $x$**, por el término $-xv^2$. Entonces:

$$f'_x = w'_u\thinspace u'_x + w'_v\thinspace v'_x + w'_x\big|_{\text{directa}}$$

**Paso 2 — Valores en $(0,1)$:** $u = 0\cdot\sqrt1 = 0$ y $v = 0 + 1 = 1$.

**Paso 3 — Derivadas:**

- $w'_u = 3u^2 = 0$.
- $w'_v = -2xv = 0$.
- $w'_ x|_ {\text{directa}} = -v^2 = -1$.
- $u'_x = \sqrt{y - x} - \dfrac{x}{2\sqrt{y-x}}$, que en $(0,1)$ vale 1.
- $v'_x = 2$.

**Paso 4 — Total:** $f'_x(0,1) = 0\cdot1 + 0\cdot2 - 1 = -1$.

</details>

**Respuesta:** $f'_x(0,1) = -1$.

</details>

---

### 05) ¿Se puede aplicar la regla de la cadena?

Dadas $f(u,v) = |u - 1| - v$, $\ \vec g(x,y) = (1 + x^2,\ 2y - 1)$, demuestre que $h = f\circ\vec g$ es derivable en $(0,0)$. ¿Se puede aplicar la regla de la cadena?.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Componer.** Como $1 + x^2 - 1 = x^2 \ge 0$, el valor absoluto desaparece:

$$h(x,y) = |x^2| - (2y - 1) = x^2 - 2y + 1$$

Es un polinomio ⇒ derivable (y diferenciable) en todo punto. $\nabla h = (2x, -2)$, así que $\nabla h(0,0) = (0, -2)$.

**Paso 2 — ¿Regla de la cadena?** Para aplicarla hace falta que $f$ sea diferenciable en $\vec g(0,0) = (1, -1)$. Pero $f'_u(1,-1) = \lim\dfrac{|h|}{h}$ no existe ⇒ $f$ **no es diferenciable** en $(1,-1)$ ⇒ **no se puede** aplicar.

La composición resulta "mejor" que $f$ porque $\vec g$ sólo toma valores $u = 1 + x^2 \ge 1$, es decir, de un solo lado del "pico" del valor absoluto.

</details>

**Respuesta:** $\nabla h(0,0) = (0,-2)$. No se puede pues $\nexists f'_u(1,-1)$ ⇒ $f$ no es diferenciable en $(1,-1)$. Observe que en este caso $h$ resulta infinitamente diferenciable en $\mathbb{R}^2$, aun con $f$ no diferenciable.

</details>

---

### 06) Función de una expresión homogénea

Sea $z = f\negthinspace\left(\dfrac{x^2 - y^2}{x^2 + y^2}\right)$ con $f$ diferenciable, calcule $x\dfrac{\partial z}{\partial x} + y\dfrac{\partial z}{\partial y}$ para todo $(x,y) \ne (0,0)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Variable intermedia.** $t = \dfrac{x^2 - y^2}{x^2 + y^2}$, así que $z = f(t)$ y:

$$z'_x = f'(t)\thinspace t'_x, \qquad z'_y = f'(t)\thinspace t'_y$$

**Paso 2 — Derivadas de $t$** (regla del cociente):

$$t'_x = \frac{2x(x^2+y^2) - (x^2-y^2)2x}{(x^2+y^2)^2} = \frac{4xy^2}{(x^2+y^2)^2}, \qquad t'_y = \frac{-2y(x^2+y^2) - (x^2-y^2)2y}{(x^2+y^2)^2} = \frac{-4x^2y}{(x^2+y^2)^2}$$

**Paso 3 — Combinación:**

$$x\thinspace z'_x + y\thinspace z'_y = f'(t)\thinspace\frac{4x^2y^2 - 4x^2y^2}{(x^2+y^2)^2} = 0$$

**Interpretación:** $t$ es homogénea de grado 0 ($t(\lambda x, \lambda y) = t(x,y)$), así que es constante sobre las rectas por el origen. La combinación $xz'_x + yz'_y$ es la derivada en la dirección radial, y por eso es 0.

</details>

**Respuesta:** $0$.

</details>

---

### 07) Verificación de una identidad

Dada $h(x,y) = f(2x/y) - f(y/x)$ con $f \in C^1$, verifique que $x\thinspace h'_x + y\thinspace h'_y = 0$ para todo punto $(x,y)$ tal que $xy \ne 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Derivadas.** Llamamos $s = 2x/y$ y $t = y/x$:

$$h'_x = f'(s)\cdot\frac{2}{y} - f'(t)\cdot\left(-\frac{y}{x^2}\right), \qquad h'_y = f'(s)\cdot\left(-\frac{2x}{y^2}\right) - f'(t)\cdot\frac{1}{x}$$

**Paso 2 — Combinación.**

$$x\thinspace h'_x + y\thinspace h'_y = f'(s)\left(\frac{2x}{y} - \frac{2x}{y}\right) + f'(t)\left(\frac{y}{x} - \frac{y}{x}\right) = 0 \ ✓$$

Como en el ejercicio 06, $s$ y $t$ son homogéneas de grado 0.

</details>

**Respuesta:** Se verifica.

</details>

---

### 08) Máximo crecimiento en una dirección dada

Sean $f(x,y) = x^2 + y^2 + 1$ y $\vec g(x,y) = (x + y,\ ay)$, determine el valor de $a$ para que $h = f\circ\vec g$ en $(1,1)$ tenga máximo crecimiento en la dirección del vector $\vec v = (5,7)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Componer.** $h(x,y) = (x + y)^2 + a^2y^2 + 1$.

**Paso 2 — Gradiente en $(1,1)$.**

$$\nabla h = \big(2(x+y),\ 2(x+y) + 2a^2y\big) \ \Rightarrow\ \nabla h(1,1) = (4,\ 4 + 2a^2)$$

**Paso 3 — Condición.** El máximo crecimiento es en la dirección de $\nabla h$. Tiene que ser $\nabla h = \lambda(5, 7)$ con $\lambda > 0$:

$$\frac{4}{5} = \frac{4 + 2a^2}{7} \ \Rightarrow\ 28 = 20 + 10a^2 \ \Rightarrow\ a^2 = \frac45 \ \Rightarrow\ a = \pm\frac{2}{\sqrt5}$$

Con $\lambda = \frac45 > 0$, el sentido es el correcto.

</details>

**Respuesta:** $a = 2/\sqrt5$ o bien $a = -2/\sqrt5$.

</details>

---

### 09) Temperatura en una lámina

La temperatura en cada punto $(x,y)$ de una lámina metálica plana es $T = 3x/(x^2 + y^2)$.

- a) Halle la línea de nivel (isoterma) que pasa por el punto $\bar A = (2,-1)$.
- b) Halle la dirección de máximo crecimiento de la temperatura en $\bar A = (2,-1)$.
- c) Halle el coeficiente de variación de temperatura, $f'(\bar A, \breve r)$ con $\bar A = (2,-1)$, en la dirección de la bisectriz del 1º cuadrante con componente positiva según $x$.
- d) Halle el coeficiente de variación de temperatura a lo largo de la curva $C$ de ecuación $\bar X = (2\mathop{\mathrm{sen}}(t),\ \cos(t))$ con $t \in [0, 2\pi]$. Esto es $dT/dt$ con $T = f(\bar X)$ y $\bar X \in C$.<sup>(\*)</sup>
- e) Halle la cota de error relativo porcentual en el cálculo de $T$ si se midieron $x = 2$ e $y = -1$ con cotas de errores relativos de 1% y 2% respectivamente.

<sup>(\*)</sup> Observe que esta derivada, para funciones diferenciables, coincide con $f'(\bar X, \breve r)$ para $\bar X \in C$ y $\breve r$ versor tangente a la curva orientado según lo impone la parametrización de la misma.

> **Fe de erratas (31/07/18):** en la nota a pie de página del ítem 09-d dice "…coincide con $f'(\bar X, \breve r)$ para…", **debe decir** "…es proporcional a $f'(\bar X, \breve r)$ para…".

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** $T(2,-1) = \dfrac{6}{5}$. La isoterma es:

$$\frac{3x}{x^2+y^2} = \frac65 \iff x^2 + y^2 = \frac{5x}{2} \iff \left(x - \frac54\right)^2 + y^2 = \left(\frac54\right)^2$$

Es una circunferencia de centro $(5/4, 0)$ y radio $5/4$, **sin el origen**, porque $T$ no está definida ahí.

**b)** Gradiente (regla del cociente):

$$\nabla T = \left(\frac{3(x^2+y^2) - 6x^2}{(x^2+y^2)^2},\ \frac{-6xy}{(x^2+y^2)^2}\right) = \frac{\big(3(y^2 - x^2),\ -6xy\big)}{(x^2+y^2)^2}$$

En $(2,-1)$:

$$\nabla T(2,-1) = \frac{(3(1-4),\ 12)}{25} = \left(-\frac{9}{25}, \frac{12}{25}\right)$$

Su norma es $\dfrac{15}{25}$, así que el versor es $\left(-\frac35, \frac45\right)$.

**c)** Versor de la bisectriz del 1.er cuadrante con $x > 0$: $\breve r = \left(\frac{1}{\sqrt2}, \frac{1}{\sqrt2}\right)$.

$$T'(\bar A, \breve r) = \frac{-9 + 12}{25\sqrt2} = \frac{3}{25\sqrt2} = \frac{3\sqrt2}{50}$$

**d)** Sobre la curva, $x = 2\mathop{\mathrm{sen}}t$ e $y = \cos t$, así que $x^2 + y^2 = 4\mathop{\mathrm{sen}}\nolimits^2t + \cos^2t = 3\mathop{\mathrm{sen}}\nolimits^2t + 1$:

$$T(t) = \frac{6\mathop{\mathrm{sen}}t}{3\mathop{\mathrm{sen}}\nolimits^2t + 1}$$

Derivando como cociente:

$$\frac{dT}{dt} = \frac{6\cos t\thinspace(3\mathop{\mathrm{sen}}\nolimits^2t + 1) - 6\mathop{\mathrm{sen}}t\cdot6\mathop{\mathrm{sen}}t\cos t}{(3\mathop{\mathrm{sen}}\nolimits^2t + 1)^2} = \frac{6\cos t\thinspace(1 - 3\mathop{\mathrm{sen}}\nolimits^2t)}{(3\mathop{\mathrm{sen}}\nolimits^2t + 1)^2}$$

Sobre la nota: $\dfrac{dT}{dt} = \nabla T\cdot\bar X'(t) = \lVert\bar X'(t)\rVert\thinspace T'(\bar X, \breve r)$. Es **proporcional** a la derivada direccional, con factor $\lVert\bar X'\rVert$; coincide sólo si la curva está parametrizada por longitud de arco. Por eso la fe de erratas.

**e)** **Fórmula:**

$$\varepsilon_{\text{rel}\thinspace T} = \left|\frac{x\thinspace T'_x}{T}\right|\varepsilon_{\text{rel}\thinspace x} + \left|\frac{y\thinspace T'_y}{T}\right|\varepsilon_{\text{rel}\thinspace y}$$

Sale de dividir $\varepsilon_T = |T'_ x|\varepsilon_x + |T'_ y|\varepsilon_y$ por $|T|$ y escribir $\varepsilon_x = |x|\thinspace\varepsilon_{\text{rel}\thinspace x}$.

**Cálculo:** $T = \dfrac{30}{25}$, $T'_x = -\dfrac{9}{25}$ y $T'_y = \dfrac{12}{25}$:

- $\left|\dfrac{2\cdot(-9)}{30}\right| = 0{,}6$.
- $\left|\dfrac{(-1)\cdot12}{30}\right| = 0{,}4$.

$$\varepsilon_{\text{rel}\thinspace T} = 0{,}6\cdot0{,}01 + 0{,}4\cdot0{,}02 = 0{,}014 \quad (1{,}4\text{ por ciento})$$

</details>

**Respuesta:**

- a) $\lbrace(x,y) \in \Re^2 - \lbrace\bar 0\rbrace / x^2 + y^2 = 5x/2\rbrace$. Es decir: puntos de la circunferencia con centro en $(5/4, 0)$ y radio $5/4$, salvo el origen de coordenadas.
- b) $\breve r_{\text{máx}} = (-3/5,\ 4/5)$.
- c) $3\sqrt2/50$.
- d) $\dfrac{6\cos(t)\thinspace(1 - 3\mathop{\mathrm{sen}}\nolimits^2(t))}{(3\mathop{\mathrm{sen}}\nolimits^2(t) + 1)^2}$.
- e) 1,4 %.

</details>

---

### 10) Aproximación lineal de una función implícita

La ecuación $xy - e^{z - x} = \ln(z)$ define implícitamente $z = f(x,y)$, halle una expresión lineal que permita aproximar los valores de $f$ en un entorno del punto $(1,1)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Valor de $z$ en $(1,1)$.** $1 - e^{z-1} = \ln z$. Probando $z = 1$: $1 - 1 = 0 = \ln 1$ ✓. Entonces $z_0 = 1$.

**Paso 2 — Derivadas de $F = xy - e^{z-x} - \ln z$** en $(1,1,1)$:

- $F'_x = y + e^{z-x} = 2$.
- $F'_y = x = 1$.
- $F'_z = -e^{z-x} - \frac1z = -2 \ne 0$, así que vale Cauchy-Dini.

**Paso 3 — Derivadas de $f$.**

$$f'_x = -\frac{F'_x}{F'_z} = 1, \qquad f'_y = -\frac{F'_y}{F'_z} = \frac12$$

**Paso 4 — Aproximación lineal.**

$$f(x,y) \approx 1 + 1\cdot(x - 1) + \frac12(y - 1)$$

</details>

**Respuesta:** $f(x,y) \cong 1 + (x - 1) + \frac12(y - 1)$.

</details>

---

### 11) Gradiente, plano tangente y direccionales de una implícita

La ecuación $z^3 + 2xz + yz - x = 0$ define $z = f(x,y)$ en un entorno del punto $(1,-2)$.

- a) Determine $\nabla f(1,-2)$.
- b) Halle ecuaciones del plano tangente y la recta normal a la gráfica de $f$ en $(1,-2,z_0)$.
- c) Calcule las derivadas direccionales de $f$ en $(1,-2)$, en las direcciones que forman ángulos de $\pi/3$ y de $-\pi/3$ medidos en sentido trigonométrico respecto de $x^+$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — $z_0$.** $z^3 + 2z - 2z - 1 = 0 \Rightarrow z^3 = 1 \Rightarrow z_0 = 1$.

**Paso 2 — Derivadas de $F$** en $(1,-2,1)$:

- $F'_x = 2z - 1 = 1$.
- $F'_y = z = 1$.
- $F'_z = 3z^2 + 2x + y = 3 + 2 - 2 = 3 \ne 0$.

**a)** $\nabla f = \left(-\dfrac{F'_x}{F'_z},\ -\dfrac{F'_y}{F'_z}\right) = \left(-\dfrac13, -\dfrac13\right)$.

**b)** Como $\nabla F = (1, 1, 3)$ es normal a la superficie $F = 0$:

- Plano tangente: $1(x - 1) + 1(y + 2) + 3(z - 1) = 0 \Rightarrow x + y + 3z = 2$.
- Recta normal: $\vec X = (1 + t,\ -2 + t,\ 1 + 3t)$.

**c)**

- Con ángulo $\pi/3$: $\breve r_1 = \left(\frac12, \frac{\sqrt3}{2}\right)$ ⇒ $f' = -\frac13\left(\frac12 + \frac{\sqrt3}{2}\right) = -\dfrac{1 + \sqrt3}{6}$.
- Con ángulo $-\pi/3$: $\breve r_2 = \left(\frac12, -\frac{\sqrt3}{2}\right)$ ⇒ $f' = -\frac13\left(\frac12 - \frac{\sqrt3}{2}\right) = \dfrac{-1 + \sqrt3}{6}$.

</details>

**Respuesta:**

- a) $\nabla f(1,-2) = (-1/3,\ -1/3)$.
- b) Plano tangente: $x + y + 3z = 2$. Recta normal: $\bar X = (1 + t,\ -2 + t,\ 1 + 3t)$, $t \in \Re$.
- c) Para $\pi/3$: $f'((1,-2), \breve r_1) = -(1 + \sqrt3)/6$. Para $-\pi/3$: $f'((1,-2), \breve r_2) = (-1 + \sqrt3)/6$.

</details>

---

### 12) Plano tangente paralelo a un plano dado

Halle los puntos del hiperboloide de una hoja de ecuación $2x^2 - 2y^2 + z^2 = 1$ donde el plano tangente es paralelo al plano de ecuación $z = x - y$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Normales.**

- Del hiperboloide: $\nabla F = (4x, -4y, 2z)$.
- Del plano $x - y - z = 0$: $(1, -1, -1)$.

**Paso 2 — Paralelismo.** $(4x, -4y, 2z) = \lambda(1, -1, -1)$ ⇒ $x = \dfrac\lambda4$, $y = \dfrac\lambda4$, $z = -\dfrac\lambda2$.

**Paso 3 — Reemplazar en la superficie.**

$$2\frac{\lambda^2}{16} - 2\frac{\lambda^2}{16} + \frac{\lambda^2}{4} = 1 \ \Rightarrow\ \lambda^2 = 4 \ \Rightarrow\ \lambda = \pm2$$

**Paso 4 — Puntos.**

- $\lambda = 2$: $\left(\frac12, \frac12, -1\right)$.
- $\lambda = -2$: $\left(-\frac12, -\frac12, 1\right)$.

</details>

**Respuesta:** $(-1/2,\ -1/2,\ 1)$ y $(1/2,\ 1/2,\ -1)$.

</details>

---

### 13) Derivada en la dirección normal interior

Dada $f(x,y,z) = 8x^2 - 2xy$, calcule la derivada de $f$ en $(3,1,2)$, en la dirección a la normal "interior" a $x^2 + y^2 + z^2 = 14$ en dicho punto.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Normal interior.** Para la esfera $x^2 + y^2 + z^2 = 14$, la normal exterior en $(3,1,2)$ tiene la dirección de $\nabla(x^2+y^2+z^2) = (6, 2, 4) \parallel (3,1,2)$. La **interior** es la opuesta:

$$\breve r = -\frac{(3,1,2)}{\sqrt{14}}$$

**Paso 2 — Gradiente de $f$.** $\nabla f = (16x - 2y,\ -2x,\ 0)$, que en $(3,1,2)$ vale $(46, -6, 0)$.

**Paso 3 — Derivada.**

$$f' = -\frac{46\cdot3 - 6\cdot1 + 0}{\sqrt{14}} = -\frac{132}{\sqrt{14}} = -66\cdot\frac{2}{\sqrt{14}} = -66\sqrt{\frac{2}{7}} \approx -35{,}28$$

</details>

**Respuesta:** $-66\sqrt{2/7}$.

</details>

---

### 14) Derivada en la dirección normal exterior a la línea de nivel

Dada $f : \Re^2 - \lbrace\bar 0\rbrace \to \Re \ /\ f(x,y) = \ln(x^2 + y^2)$, calcule la derivada direccional de $f$ en el punto $(x_0,y_0)$ de su dominio natural, en la dirección normal exterior<sup>(@)</sup> a la línea de nivel de $f$ que pasa por dicho punto.

<sup>(@)</sup> Hacia afuera de la región acotada que la línea encierra.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Líneas de nivel.** $\ln(x^2 + y^2) = k$ son circunferencias centradas en el origen. Su normal exterior es **radial hacia afuera**:

$$\breve r = \frac{(x_0, y_0)}{\sqrt{x_0^2 + y_0^2}}$$

**Paso 2 — Gradiente.**

$$\nabla f = \frac{(2x, 2y)}{x^2 + y^2}$$

Tiene la misma dirección y sentido que $\breve r$. Por eso la derivada es la máxima, $\lVert\nabla f\rVert$.

**Paso 3 — Derivada.** Con $\rho = \sqrt{x_0^2 + y_0^2}$:

$$f' = \nabla f\cdot\breve r = \frac{2x_0^2 + 2y_0^2}{(x_0^2 + y_0^2)\thinspace\rho} = \frac{2}{\rho}$$

</details>

**Respuesta:** $f'((x_0,y_0), \breve r) = 2/\sqrt{x_0^2 + y_0^2}$.

</details>

---

### 15) Derivada nula sobre el plano tangente

Sea $\bar A$ un punto de una superficie de nivel del campo escalar $f$ y $\pi_0$ el plano tangente a dicha superficie en $\bar A$. Demuestre que la derivada direccional de $f$ en $\bar A$ es siempre nula si se calcula en la dirección que va desde $\bar A$ hacia cualquier punto $\bar X \in \pi_0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Hipótesis implícitas:** $f$ es diferenciable en $\bar A$ y $\nabla f(\bar A) \ne \bar 0$, para que exista el plano tangente a la superficie de nivel. Tomamos $\bar X \ne \bar A$.

**Paso 1 — Plano tangente.** La superficie de nivel es $f = c$, con $c = f(\bar A)$. Su plano tangente es:

$$\pi_0:\ \nabla f(\bar A)\cdot(\bar X - \bar A) = 0$$

**Paso 2 — Derivada.** Para $\bar X \in \pi_0$, la dirección es $\breve r = \dfrac{\bar X - \bar A}{\lVert\bar X - \bar A\rVert}$, y como $f$ es diferenciable:

$$f'(\bar A, \breve r) = \nabla f(\bar A)\cdot\breve r = \frac{\nabla f(\bar A)\cdot(\bar X - \bar A)}{\lVert\bar X - \bar A\rVert} = \frac{0}{\lVert\bar X - \bar A\rVert} = 0 \quad\blacksquare$$

</details>

**Respuesta:** Se cumple: todo vector $\bar X - \bar A$ con $\bar X \in \pi_0$ es perpendicular a $\nabla f(\bar A)$, y entonces $f'(\bar A, \breve r) = \nabla f(\bar A)\cdot\breve r = 0$.

</details>

---

### 16) Recta tangente a una curva intersección

Siendo $C$ la curva intersección de las superficies: $x^2 - y^2 = 12$ y $z = x + y^2$, analice si la recta tangente a $C$ en $(4,2,z_0)$ corta a la superficie cilíndrica de ecuación $y = x^2$.<sup>(#)</sup>

<sup>(#)</sup> Nota: Si $F, G \in C^1$ en un entorno de $\bar A \in \Re^3$, $F(\bar A) = 0$, $G(\bar A) = 0$ y el vector $\bar d = \nabla F(\bar A) \times \nabla G(\bar A) \ne \bar 0$, la intersección de las superficies dadas implícitamente por $F(x,y,z) = 0$ y $G(x,y,z) = 0$ define una curva regular en un entorno de $\bar A$ cuya recta tangente en este punto está dirigida por $\bar d$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Punto.** $z_0 = 4 + 2^2 = 8$, así que $\bar A = (4, 2, 8)$. Se verifica $16 - 4 = 12$ ✓.

**Paso 2 — Gradientes.** Con $F = x^2 - y^2 - 12$ y $G = x + y^2 - z$:

- $\nabla F(\bar A) = (2x, -2y, 0) = (8, -4, 0)$.
- $\nabla G(\bar A) = (1, 2y, -1) = (1, 4, -1)$.

**Paso 3 — Dirección tangente.**

$$\bar d = \begin{vmatrix} \breve\imath & \breve\jmath & \breve k \cr 8 & -4 & 0 \cr 1 & 4 & -1 \end{vmatrix} = (4 - 0,\ -(-8 - 0),\ 32 + 4) = (4, 8, 36) \parallel (1, 2, 9)$$

**Paso 4 — Recta tangente.** $\vec X = (4 + t,\ 2 + 2t,\ 8 + 9t)$.

**Paso 5 — Intersección con $y = x^2$.**

$$2 + 2t = (4 + t)^2 = 16 + 8t + t^2 \ \Rightarrow\ t^2 + 6t + 14 = 0$$

El discriminante es $36 - 56 = -20 < 0$ ⇒ no hay soluciones reales ⇒ **no** la corta.

</details>

**Respuesta:** No.

</details>

---

### 17) Direcciones de derivada nula de una composición con implícita

Dada $z = u + v\thinspace e^{u - v}$ con $(u,v) = (f(x,y),\ y^2)$ resulta $z = h(x,y)$. Halle las direcciones $\breve r$ tales que $h'((2,1), \breve r) = 0$, si la función $f$ queda definida implícitamente mediante la ecuación $2y - ux - \ln(u) = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Valor de $u$ en $(2,1)$.** $2 - 2u - \ln u = 0$. Probando $u = 1$: $2 - 2 - 0 = 0$ ✓. Además $v = 1^2 = 1$.

**Paso 2 — Derivadas de $u = f(x,y)$** (Cauchy-Dini con $G = 2y - ux - \ln u$) en $(2,1,1)$:

- $G'_x = -u = -1$.
- $G'_y = 2$.
- $G'_u = -x - \frac1u = -3 \ne 0$.

Entonces:

$$u'_x = -\frac{G'_x}{G'_u} = -\frac13, \qquad u'_y = -\frac{G'_y}{G'_u} = \frac23$$

**Paso 3 — Derivadas de $v = y^2$:** $v'_x = 0$ y $v'_y = 2y = 2$.

**Paso 4 — Derivadas de $z$ respecto de $u$, $v$** (en $u = v = 1$, donde $e^{u-v} = 1$):

- $z'_u = 1 + v\thinspace e^{u-v} = 2$.
- $z'_v = e^{u-v} - v\thinspace e^{u-v} = 1 - 1 = 0$.

**Paso 5 — Regla de la cadena.**

$$h'_x = 2\cdot\left(-\frac13\right) + 0 = -\frac23, \qquad h'_y = 2\cdot\frac23 + 0\cdot2 = \frac43$$

Entonces $\nabla h(2,1) = \left(-\frac23, \frac43\right) \parallel (-1, 2)$.

**Paso 6 — Direcciones nulas:** son los versores perpendiculares a $(-1,2)$, es decir $\pm\dfrac{(2, 1)}{\sqrt5}$.

</details>

**Respuesta:** $\breve r_{\text{nula}_ 1} = (2/\sqrt5,\ 1/\sqrt5)$, $\ \breve r_{\text{nula}_ 2} = (-2/\sqrt5,\ -1/\sqrt5)$.

</details>

---

### 18) Plano normal a una curva sobre una superficie

Halle la ecuación cartesiana del plano normal a la curva $C$ en $\bar A = (2,1,-4)$ si se sabe que los puntos de $C$ pertenecen a la superficie de ecuación $z = xy - 3x$, y que la proyección de $C$ sobre el plano $xy$ es la parábola definida por $y = x^2 - 3$ con $z = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrizar $C$.** La proyección da $y = x^2 - 3$, y la superficie da $z = xy - 3x$. Con $x = t$:

$$\vec g(t) = \big(t,\ t^2 - 3,\ t(t^2 - 3) - 3t\big) = (t,\ t^2 - 3,\ t^3 - 6t)$$

**Paso 2 — Punto.** $t = 2$: $(2, 1, 8 - 12) = (2, 1, -4) = \bar A$ ✓.

**Paso 3 — Tangente.** $\vec g'(t) = (1,\ 2t,\ 3t^2 - 6)$, así que $\vec g'(2) = (1, 4, 6)$.

**Paso 4 — Plano normal.**

$$1(x - 2) + 4(y - 1) + 6(z + 4) = 0 \ \Rightarrow\ x + 4y + 6z + 18 = 0$$

</details>

**Respuesta:** $x + 4y + 6z + 18 = 0$.

</details>

---

### 19) Una EDO a partir de una implícita

Considere $h = f\circ\vec g$ con $\vec g(x) = (e^x,\ e^{x^2})$ y $f(u,v)$ definida por $y - 1 + \ln(yuv) = 0$. Demuestre que $y = h(x)$ con $h(0) = 1$ satisface la ecuación $(1 + y)\thinspace y' + (1 + 2x)\thinspace y = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Ecuación para $y = h(x)$.** Reemplazando $u = e^x$ y $v = e^{x^2}$ en la ecuación que define $f$:

$$y - 1 + \ln\negthinspace\left(y\thinspace e^x\thinspace e^{x^2}\right) = 0 \ \Rightarrow\ y - 1 + \ln y + x + x^2 = 0$$

En $x = 0$: $y - 1 + \ln y = 0$ se cumple con $y = 1$, que es consistente con $h(0) = 1$.

**Paso 2 — Derivar implícitamente respecto de $x$:**

$$y' + \frac{y'}{y} + 1 + 2x = 0$$

**Paso 3 — Multiplicar por $y$** ($y > 0$):

$$y\thinspace y' + y' + (1 + 2x)\thinspace y = 0 \ \Rightarrow\ (1 + y)\thinspace y' + (1 + 2x)\thinspace y = 0 \ ✓$$

</details>

**Respuesta:** Satisface la ecuación (ver la demostración en el paso a paso).

</details>

---

### 20) Identidad para una implícita

Verifique que $z = f(x,y)$ definida implícitamente por $x + yz - e^z = 0$ satisface la ecuación que $z\thinspace z'_x - z'_y = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Derivadas de $F = x + yz - e^z$:** $F'_x = 1$, $F'_y = z$ y $F'_z = y - e^z$. Suponemos $F'_z \ne 0$, que es la hipótesis de Cauchy-Dini.

**Paso 2 — Derivadas de $z$.**

$$z'_x = -\frac{1}{y - e^z}, \qquad z'_y = -\frac{z}{y - e^z}$$

**Paso 3 — Verificación.**

$$z\thinspace z'_x - z'_y = -\frac{z}{y - e^z} + \frac{z}{y - e^z} = 0 \ ✓$$

</details>

**Respuesta:** Se verifica (en los puntos donde $F'_z = y - e^z \ne 0$).

</details>

---

### 21) Derivada direccional máxima de una composición con implícita

Calcule la derivada direccional máxima de $h = f\circ\vec g$ en el punto $(1,1)$ cuando $f(u,v)$ queda definida por $z - u^2 + v^2 + \ln(v + z) = 0$, siendo $\vec g(x,y) = (xy^2,\ y - x^2)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Variables intermedias en $(1,1)$:** $u = 1$ y $v = 1 - 1 = 0$.

**Paso 2 — Valor de $z$.** $z - 1 + 0 + \ln(z) = 0$. Probando $z = 1$: $0 + 0 = 0$ ✓.

**Paso 3 — Derivadas de $f$** (Cauchy-Dini con $F = z - u^2 + v^2 + \ln(v + z)$) en $(1, 0, 1)$:

- $F'_u = -2u = -2$.
- $F'_v = 2v + \frac{1}{v+z} = 1$.
- $F'_z = 1 + \frac{1}{v+z} = 2$.

Entonces:

$$f'_u = -\frac{-2}{2} = 1, \qquad f'_v = -\frac{1}{2}$$

**Paso 4 — Derivadas de $\vec g$** en $(1,1)$:

- $u'_x = y^2 = 1$ y $u'_y = 2xy = 2$.
- $v'_x = -2x = -2$ y $v'_y = 1$.

**Paso 5 — Regla de la cadena.**

$$h'_x = 1\cdot1 + \left(-\frac12\right)(-2) = 2, \qquad h'_y = 1\cdot2 + \left(-\frac12\right)\cdot1 = \frac32$$

**Paso 6 — Máximo.**

$$\lVert\nabla h\rVert = \sqrt{4 + \frac94} = \sqrt{\frac{25}{4}} = \frac52$$

</details>

**Respuesta:** $h'((1,1), \breve r_{\text{máx}}) = 5/2$.

</details>

---

### 22) Aproximación con una variable implícita

Dada $w = u^2v + 3v^2$ con $\begin{cases} u = x + y^2 \cr v = g(x,y) \end{cases}$, resulta $w = h(x,y)$. Calcule aproximadamente $h(2.98,\ 2.01)$ sabiendo que $g$ queda definida por $xv + \ln(v + y - 2) - 3 = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Punto base** $(3, 2)$, cercano y cómodo:

- $u = 3 + 4 = 7$.
- $v$: $3v + \ln(v) - 3 = 0 \Rightarrow v = 1$, porque $3 + 0 - 3 = 0$.
- $h(3,2) = 49\cdot1 + 3 = 52$.

**Paso 2 — Derivadas de $v = g$** (con $G = xv + \ln(v + y - 2) - 3$) en $(3, 2, 1)$:

- $G'_x = v = 1$.
- $G'_y = \frac{1}{v + y - 2} = 1$.
- $G'_v = x + \frac{1}{v+y-2} = 4$.

Entonces $v'_x = -\frac14$ y $v'_y = -\frac14$.

**Paso 3 — Derivadas de $w$:**

- $w'_u = 2uv = 14$ y $w'_v = u^2 + 6v = 55$.
- $u'_x = 1$ y $u'_y = 2y = 4$.

**Paso 4 — Regla de la cadena.**

$$h'_x = 14\cdot1 + 55\cdot\left(-\frac14\right) = 0{,}25, \qquad h'_y = 14\cdot4 + 55\cdot\left(-\frac14\right) = 42{,}25$$

**Paso 5 — Aproximación** con $\vec h = (-0{,}02;\ 0{,}01)$:

$$h(2{,}98;\ 2{,}01) \approx 52 + 0{,}25(-0{,}02) + 42{,}25(0{,}01) = 52 - 0{,}005 + 0{,}4225 = 52{,}4175$$

</details>

**Respuesta:** $h(2.98,\ 2.01) \cong 52.4175$.

</details>

---

### 23) Función decreciente a lo largo de una curva

La ecuación $uy + x + e^{2u + y + x - 5} - 4 = 0$ define implícitamente $u = f(x,y)$, sabiendo que los puntos $(x,y)$ pertenecen a la curva de ecuación $\bar X = (t^2 - 3,\ 2 + \mathop{\mathrm{sen}}(t - 2))$ resulta que $u = h(t)$; verifique que $h$ es decreciente en $t_0 = 2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Punto.** $\bar X(2) = (4 - 3,\ 2 + 0) = (1, 2)$.

**Paso 2 — Valor de $u$.** $2u + 1 + e^{2u + 2 + 1 - 5} - 4 = 0 \Rightarrow 2u - 3 + e^{2u - 2} = 0$. Con $u = 1$: $2 - 3 + 1 = 0$ ✓.

**Paso 3 — Derivadas de $F$** en $(x, y, u) = (1, 2, 1)$, donde la exponencial vale $e^0 = 1$:

- $F'_x = 1 + e^{(\cdot)} = 2$.
- $F'_y = u + e^{(\cdot)} = 2$.
- $F'_u = y + 2e^{(\cdot)} = 4$.

Entonces $u'_x = -\frac24 = -\frac12$ y $u'_y = -\frac12$.

**Paso 4 — Derivada de la curva.** $\bar X'(t) = (2t,\ \cos(t - 2))$, así que $\bar X'(2) = (4, 1)$.

**Paso 5 — Regla de la cadena.**

$$h'(2) = \nabla f\cdot\bar X'(2) = -\frac12\cdot4 - \frac12\cdot1 = -\frac52 < 0$$

Por lo tanto $h$ es decreciente en $t_0 = 2$.

</details>

**Respuesta:** Se verifica pues $h'(2) = -5/2 < 0$.

</details>

---

### 24) Hallar $g$ para que la composición sea constante

Sea $f \in C^1$ con $\nabla f = (1,-1)$ constante, halle $g$ derivable tal que $h(x) = f(x\thinspace g(x),\ g(x))$ sea constante; suponga que la gráfica de $g$ pasa por $(3,1)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Derivada de $h$.** Con $u = x\thinspace g(x)$ y $v = g(x)$:

$$h'(x) = f'_u\thinspace u' + f'_v\thinspace v' = 1\cdot\big(g + x\thinspace g'\big) + (-1)\cdot g' = g + (x - 1)\thinspace g'$$

**Paso 2 — $h$ constante ⇔ $h' = 0$:**

$$g + (x - 1)\thinspace g' = 0 \ \Rightarrow\ \frac{g'}{g} = -\frac{1}{x - 1}$$

**Paso 3 — Resolver (separable).** $\ln|g| = -\ln|x - 1| + c \Rightarrow g = \dfrac{C}{x - 1}$.

**Paso 4 — Condición $g(3) = 1$.** $\dfrac{C}{2} = 1 \Rightarrow C = 2$.

</details>

**Respuesta:** $g(x) = 2/(x - 1)$.

</details>

---

### 25) Hallar $f$ para que sea solución de una EDO

Halle $f(u)$ tal que $y = x\thinspace f(x^2 - 1)$ sea solución de la ecuación diferencial $x\thinspace y' - y = 2x^3$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Derivar.** Con $u = x^2 - 1$ y $u' = 2x$:

$$y' = f(u) + x\thinspace f'(u)\cdot2x = f(u) + 2x^2f'(u)$$

**Paso 2 — Reemplazar en la EDO.**

$$x\thinspace y' - y = x\thinspace f(u) + 2x^3f'(u) - x\thinspace f(u) = 2x^3f'(u) = 2x^3$$

**Paso 3 — Despejar.** $f'(u) = 1$ (para $x \ne 0$) ⇒ $f(u) = u + C$.

</details>

**Respuesta:** $f(u) = u + C$ con $C$ constante arbitraria.

</details>

---

## Cuestionario

### Cuestionario a)

Indique condiciones para que $f(x,y) = 0$ defina una curva plana que pasa por $\bar A$, ¿puede asegurar que la curva es regular en dicho punto?.

<details>
<summary><b>Solución</b></summary>

**Respuesta:** por el teorema de Cauchy-Dini, alcanza con:

1. $f \in C^1$ en un entorno de $\bar A$;
2. $f(\bar A) = 0$;
3. $\nabla f(\bar A) \ne \bar 0$, es decir $f'_y(\bar A) \ne 0$ (se despeja $y = \varphi(x)$) o $f'_x(\bar A) \ne 0$ (se despeja $x = \psi(y)$).

En ese caso, cerca de $\bar A$ la ecuación define el gráfico de una función $C^1$. Por eso **sí** se puede asegurar que la curva es **regular** en $\bar A$: su vector tangente, $(1, \varphi')$ o $(\psi', 1)$, no se anula, y su normal es $\nabla f(\bar A) \ne \bar 0$.

</details>

---

### Cuestionario b)

Sea $\nabla\varphi$ continuo en un entorno de $\bar A$ y no nulo en $\bar A$; demuestre que $\nabla\varphi(\bar A)$ es normal al conjunto de nivel de $\varphi$ que pasa por $\bar A$, y está orientado localmente hacia los conjuntos de nivel creciente.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Normal.** Sea $\vec X(t)$ una curva derivable contenida en el conjunto de nivel $\varphi = c$, con $\vec X(t_0) = \bar A$. Entonces $\varphi(\vec X(t)) = c$ para todo $t$. Derivando con la regla de la cadena ($\varphi$ es $C^1$, y por lo tanto diferenciable):

$$\nabla\varphi(\bar A)\cdot\vec X'(t_0) = 0$$

El gradiente es perpendicular a todo vector tangente al conjunto de nivel ⇒ es **normal**.

**Orientación.** Con $\breve r = \dfrac{\nabla\varphi(\bar A)}{\lVert\nabla\varphi(\bar A)\rVert}$:

$$\varphi'(\bar A, \breve r) = \nabla\varphi\cdot\breve r = \lVert\nabla\varphi(\bar A)\rVert > 0$$

Moviéndose un poco desde $\bar A$ en el sentido del gradiente, $\varphi$ **crece**: se pasa a conjuntos de nivel mayor que $c$. $\blacksquare$

</details>

**Respuesta:** Derivando $\varphi(\vec X(t)) = c$ se obtiene $\nabla\varphi\cdot\vec X' = 0$ (normal), y la derivada en la dirección del gradiente es $\lVert\nabla\varphi\rVert > 0$ (crecimiento).

</details>

---

### Cuestionario c)

Sea $S$ una superficie regular en $\bar A$ y $\pi_0$ su plano tangente en $\bar A$. Demuestre que $\pi_0$ contiene a la recta tangente en $\bar A$ a cualquier curva regular $C \subset S$ que pase por dicho punto.

<details>
<summary><b>Solución</b></summary>

**Respuesta:** describimos $S$ localmente como $F = 0$, con $F \in C^1$ y $\nabla F(\bar A) \ne \bar 0$. El plano tangente es $\pi_0: \nabla F(\bar A)\cdot(\vec X - \bar A) = 0$.

Si $C \subset S$ es una curva regular, $\vec g(t)$, con $\vec g(t_0) = \bar A$, entonces $F(\vec g(t)) = 0$ para todo $t$. Derivando, $\nabla F(\bar A)\cdot\vec g'(t_0) = 0$, así que el vector tangente $\vec g'(t_0)$ es perpendicular a la normal del plano.

La recta tangente $\bar A + \lambda\vec g'(t_0)$ cumple entonces $\nabla F(\bar A)\cdot(\lambda\vec g'(t_0)) = 0$ para todo $\lambda$ ⇒ está contenida en $\pi_0$. $\blacksquare$

Con una parametrización $\vec X(u,v)$ se llega a lo mismo: el tangente a $\vec X(u(t), v(t))$ es $\vec X'_u u' + \vec X'_v v'$, que es una combinación de los vectores que generan $\pi_0$.

</details>

---

### Cuestionario d)

Proponga dos funciones discontinuas (no son continuas en todo punto) cuya composición genere una función continua y derivable en todo punto.

<details>
<summary><b>Solución</b></summary>

**Respuesta:** por ejemplo:

- $g(x) = \begin{cases} 1 & x \ge 0 \cr -1 & x < 0 \end{cases}$, discontinua en 0.
- $f(u) = \begin{cases} 0 & u = \pm1 \cr 1 & u \ne \pm1 \end{cases}$, discontinua en $\pm1$.

Como $g$ sólo toma los valores $\pm1$, $(f\circ g)(x) = 0$ para todo $x$: es **constante**, y por lo tanto continua y derivable en todo punto.

</details>

---

[← Volver al menú principal](../README.md)
