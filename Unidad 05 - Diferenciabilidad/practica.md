# Unidad 5 — Práctica: Diferenciabilidad, plano tangente y recta normal

Ejercicios del **T.P. N.º 5 de la Guía de Trabajos Prácticos** ([TP05-Diferenciabilidad.pdf](../aula-virtual/05-Diferenciabilidad/TP05-Diferenciabilidad.pdf)). Las respuestas se controlaron con las [respuestas oficiales de la guía](../aula-virtual/00-Guia-TP/Guia-TP-2016-Respuestas.pdf).

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

> **Nomenclatura y consideraciones básicas:**
>
> - Dada $f : \Re^n \to \Re^m \ /\ f(X) = (f_1(x), \cdots, f_m(x))$, cuando $f$ es derivable<sup>(\*)</sup> en $A$, queda definida la matriz jacobiana de $f$ en $A$ que denotamos como $Df(A)$:
>
> $$Df(A) = \begin{pmatrix} \frac{\partial f_1}{\partial x_1}(A) & \cdots & \frac{\partial f_1}{\partial x_n}(A) \\ \vdots & & \vdots \\ \frac{\partial f_m}{\partial x_1}(A) & \cdots & \frac{\partial f_m}{\partial x_n}(A) \end{pmatrix}.$$
>
> - Siendo $f$ un campo escalar derivable en $\bar A$, el vector cuyas componentes son los elementos de $Df(\bar A)$ se denomina gradiente de $f$ en $\bar A$ y lo denotamos $\nabla f(\bar A) \equiv \operatorname{grad} f(\bar A)$:
>
> $$\nabla f(\bar A) = \left(\frac{\partial f}{\partial x_1}(\bar A), \cdots, \frac{\partial f}{\partial x_n}(\bar A)\right).$$
>
> - La expresión "$f$ con matriz jacobiana continua en $W$" es equivalente a "$f \in C^1(W)$". Para funciones de una variable significa que la función $f'$ es continua en $W$; para las de varias variables significa que todas las derivadas parciales de 1° orden son funciones continuas en $W$.
>
> <sup>(\*)</sup> Derivadas parciales existentes para el caso de función de varias variables.

---

### 01) Matriz jacobiana y conjunto de continuidad

Exprese $Df(X)$ y halle el conjunto $W$ tal que $Df$ sea continua en $W$.

- a) $\vec f(t) = \left(t^3 - 2,\ \dfrac{t^2 - 1}{t + 1},\ \dfrac{\cos(t)}{2t - \pi}\right)$
- b) $f(x,y) = \dfrac{xy}{x^2 + y^2}$
- c) $\vec f(x,y,z) = (x^2 + y,\ z\ln(x^2 + z^2))$
- d) $\vec f(\bar X) = \dfrac{k\,\breve r}{r^2}$ con $\begin{cases} \bar r = \bar X = (x,y,z) \\ r = \|\bar r\| \end{cases}$, $k = $ cte.
- e) $f(x,y) = \dfrac{xy^2}{x^2 + y^4}$ si $(x,y) \ne (0,0)$, $f(0,0) = 0$.
- f) $f(x,y) = (x^2y^3,\ (y - x)^2)$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Recordatorio:** la jacobiana tiene **una fila por componente** y **una columna por variable**.

**a)** Una variable ($t$) y tres componentes ⇒ matriz $3\times1$ (columna). El dominio es $t \ne -1$ y $t \ne \pi/2$.

- $f_1' = 3t^2$.
- $f_2 = \dfrac{(t-1)(t+1)}{t+1} = t - 1$ (para $t \ne -1$) ⇒ $f_2' = 1$.
- $f_3 = \dfrac{\cos t}{2t - \pi}$, por la regla del cociente:

$$f_3' = \frac{-\operatorname{sen}t\,(2t - \pi) - 2\cos t}{(2t - \pi)^2} = -\frac{2\cos t}{(2t-\pi)^2} - \frac{\operatorname{sen}t}{2t - \pi}$$

Todas son continuas donde están definidas ⇒ $W = \{t \ne -1 \wedge t \ne \pi/2\}$.

**b)** Por la regla del cociente:

$$f'_x = \frac{y(x^2+y^2) - xy\cdot 2x}{(x^2+y^2)^2} = \frac{y^3 - x^2y}{(x^2+y^2)^2}, \qquad f'_y = \frac{x^3 - xy^2}{(x^2+y^2)^2}$$

Como la función no está definida en el origen: $W = \Re^2 - \{\bar 0\}$.

**c)** Dos componentes y tres variables ⇒ matriz $2\times3$.

- Fila 1, $f_1 = x^2 + y$: $(2x,\ 1,\ 0)$.
- Fila 2, $f_2 = z\ln(x^2+z^2)$: $\left(\dfrac{2xz}{x^2+z^2},\ 0,\ \ln(x^2+z^2) + \dfrac{2z^2}{x^2+z^2}\right)$.

Están definidas y son continuas donde $x^2 + z^2 \ne 0$.

**d)** Como $\breve r = \bar r/r$, el campo es $\vec f = \dfrac{k\,\bar r}{r^3} = k\left(\dfrac{x}{r^3}, \dfrac{y}{r^3}, \dfrac{z}{r^3}\right)$. Usando $r'_x = x/r$:

$$\frac{\partial}{\partial x}\left(\frac{kx}{r^3}\right) = k\,\frac{r^3 - x\cdot 3r^2\frac{x}{r}}{r^6} = k\,r^{-3}\left(1 - \frac{3x^2}{r^2}\right), \qquad \frac{\partial}{\partial y}\left(\frac{kx}{r^3}\right) = kx\cdot(-3)r^{-4}\frac{y}{r} = -\frac{3kxy}{r^5}$$

Las demás entradas son análogas (la matriz es simétrica). $W = \Re^3 - \{\bar 0\}$.

**e)** **Fuera del origen**, por la regla del cociente:

$$f'_x = \frac{y^2(x^2+y^4) - xy^2\cdot 2x}{(x^2+y^4)^2} = \frac{y^6 - x^2y^2}{(x^2+y^4)^2}, \qquad f'_y = \frac{2xy(x^2+y^4) - xy^2\cdot 4y^3}{(x^2+y^4)^2} = \frac{2x^3y - 2xy^5}{(x^2+y^4)^2}$$

**En el origen** (por definición): $f(h,0) = 0$ y $f(0,k) = 0$ ⇒ $Df(0,0) = (0\ \ 0)$.

**Continuidad de $f'_y$ en el origen:** sobre $y = mx$,

$$f'_y(x, mx) = \frac{2mx^4(1 - m^4x^2)}{x^4(1 + m^4x^2)^2} \to 2m$$

Depende de $m$ ⇒ $f'_y$ no es continua en el origen ⇒ $W = \Re^2 - \{\bar 0\}$.

**f)** Dos componentes y dos variables:

- Fila 1, $x^2y^3$: $(2xy^3,\ 3x^2y^2)$.
- Fila 2, $(y-x)^2$: $(-2(y - x),\ 2(y - x)) = (2(x - y),\ 2(y - x))$.

Son polinomios ⇒ $W = \Re^2$.

</details>

**Respuesta:**

- a) $D\vec f(t) = \begin{pmatrix} 3t^2 \\ 1 \\ -\dfrac{2\cos(t)}{(2t-\pi)^2} - \dfrac{\operatorname{sen}(t)}{2t - \pi} \end{pmatrix}$, $\ W = \{t \in \Re / t \ne -1 \wedge t \ne \pi/2\}$.
- b) $Df(x,y) = \left(\dfrac{y^3 - x^2y}{(x^2+y^2)^2}\ \ \dfrac{x^3 - xy^2}{(x^2+y^2)^2}\right)$, $\ W = \Re^2 - \{\bar 0\}$.
- c) $D\vec f(x,y,z) = \begin{pmatrix} 2x & 1 & 0 \\ \dfrac{2xz}{x^2+z^2} & 0 & \dfrac{2z^2}{x^2+z^2} + \ln(x^2+z^2) \end{pmatrix}$, $\ W = \{(x,y,z) \in \Re^3 / x^2 + z^2 \ne 0\}$.
- d) $D\vec f(x,y,z) = \begin{pmatrix} kr^{-3}(1 - 3x^2/r^2) & -3kxy/r^5 & -3kxz/r^5 \\ -3kxy/r^5 & kr^{-3}(1 - 3y^2/r^2) & -3kyz/r^5 \\ -3kxz/r^5 & -3kyz/r^5 & kr^{-3}(1 - 3z^2/r^2) \end{pmatrix}$, $\ W = \Re^3 - \{\bar 0\}$.
- e) $Df(x,y) = \begin{cases} \left(\dfrac{y^6 - x^2y^2}{(x^2+y^4)^2}\ \ \dfrac{2x^3y - 2xy^5}{(x^2+y^4)^2}\right) & \text{si } (x,y) \ne (0,0) \\ (0\ \ 0) & \text{si } (x,y) = (0,0) \end{cases}$, $\ W = \Re^2 - \{\bar 0\}$ (acercándose por rectas es sencillo probar que $f'_y$ no es continua en el origen).
- f) $D\vec f(x,y) = \begin{pmatrix} 2xy^3 & 3x^2y^2 \\ 2(x - y) & 2(y - x) \end{pmatrix}$, $\ W = \Re^2$.

</details>

---

### 02) Derivada direccional que no es $\nabla f\cdot\breve r$

Siendo $f(x,y) = \sqrt{xy}$ si $xy \ge 0$ y $f(x,y) = x$ si $xy < 0$, calcule $f'((0,0),(2,-1))$ aplicando la definición. Observe que en este caso $f'((0,0),(2,-1)) \ne \nabla f(0,0)\cdot(2,-1)$. ¿Existe la derivada pedida?; si existe, ¿cuál es su valor?.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Definición** (derivada respecto del vector $\vec r = (2, -1)$):

$$f'((0,0), (2,-1)) = \lim_{h\to0}\frac{f(2h, -h) - f(0,0)}{h}$$

**Paso 2 — Qué rama usar.** En $(2h, -h)$ es $xy = -2h^2 < 0$ (para $h \ne 0$) ⇒ $f(2h, -h) = x = 2h$. Además $f(0,0) = \sqrt0 = 0$.

**Paso 3 — Límite.** $\dfrac{2h - 0}{h} = 2 \to 2$. **Existe y vale 2.**

**Paso 4 — Comparación con el gradiente.**

- Sobre los ejes $xy = 0$, así que $f = \sqrt{0} = 0$. Entonces $f(h, 0) = 0$ y $f(0, k) = 0$ ⇒ $\nabla f(0,0) = (0, 0)$.
- $\nabla f(0,0)\cdot(2,-1) = 0 \ne 2$.

La regla "derivada = gradiente · vector" **no se cumple**, lo que prueba que $f$ **no es diferenciable** en el origen.

</details>

**Respuesta:** Sí existe, $f'((0,0),(2,-1)) = 2$.

</details>

---

### 03) Derivable en toda dirección pero no diferenciable

Sea $f(x,y) = x^2/y$ si $(x,y) \ne (x,0)$ con $f(x,0) = 0$. Demuestre que $f$ es derivable en toda dirección en $(0,0)$ pero no es diferenciable en dicho punto.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Direccionales.** Sea $\breve r = (u, v)$, con $u^2 + v^2 = 1$.

- **Si $v \ne 0$:** el punto $(hu, hv)$ no está en el eje $x$, así que:

$$\frac{f(hu, hv) - 0}{h} = \frac{1}{h}\cdot\frac{h^2u^2}{hv} = \frac{u^2}{v}$$

  Es constante ⇒ el límite vale $u^2/v$.
- **Si $v = 0$:** $f(hu, 0) = 0$ ⇒ la derivada vale 0.

Existe en **toda** dirección.

**Paso 2 — No es diferenciable.** Basta ver que **no es continua** en el origen. Sobre la parábola $y = x^2$, $f = \dfrac{x^2}{x^2} = 1 \ne 0 = f(0,0)$. Como diferenciable ⇒ continua, $f$ no es diferenciable.

También se ve con el gradiente: $\nabla f(0,0) = (0, 0)$ (las direccionales según $(1,0)$ y $(0,1)$ valen 0), pero $f'(\vec 0, (u,v)) = u^2/v \ne 0 = \nabla f\cdot(u,v)$.

</details>

**Respuesta:** $f'(\bar 0, (u,v)) = \begin{cases} u^2/v & \text{si } v \ne 0 \\ 0 & \text{si } v = 0 \end{cases}$ con $u^2 + v^2 = 1$; no es continua en $\bar 0$ ⇒ no es diferenciable en $\bar 0$.

</details>

---

### 04) Derivabilidad y diferenciabilidad en el origen

En los siguientes casos analice la derivabilidad en distintas direcciones y la diferenciabilidad de la función en el origen de coordenadas.

- a) $f(x,y) = \begin{cases} \dfrac{x^4}{x + y} & \text{si } x + y \ne 0 \\ 0 & \text{si } x + y = 0 \end{cases}$, observe que $f$ no es continua en $(0,0)$.
- b) $f(x,y) = \begin{cases} \dfrac{x^2y}{x^2 + y^2} & \text{si } (x,y) \ne (0,0) \\ 0 & \text{si } (x,y) = (0,0) \end{cases}$. Verifique que en $(0,0)$ la función tiene dos direcciones de derivada direccional máxima y cuatro direcciones para las cuales la derivada resulta nula (cada dirección se especifica mediante el versor correspondiente).

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)**

*Direccionales.* Sea $\breve r = (a, b)$ unitario.

- Si $a + b \ne 0$:

$$\frac{f(ha, hb)}{h} = \frac{1}{h}\cdot\frac{h^4a^4}{h(a + b)} = \frac{h^2a^4}{a+b} \to 0$$

- Si $a + b = 0$: $f = 0$ sobre esa recta ⇒ la derivada es 0.

Todas las direccionales valen 0.

*No es continua.* La curva de nivel $k$: $x^4 = k(x + y) \iff y = \dfrac{x^4}{k} - x$ pasa por el origen y, para $x \ne 0$ chico, cumple $x + y = x^4/k \ne 0$. Sobre ella $f = k$ ⇒ no existe el límite ⇒ no es continua ⇒ **no es diferenciable**.

**b)**

*Direccionales.* Con $\breve r = (u, v)$ unitario:

$$f'(\bar 0, (u,v)) = \lim_{h\to0}\frac{1}{h}\cdot\frac{h^3u^2v}{h^2(u^2 + v^2)} = u^2v$$

*Máximos.* Maximizamos $g = u^2v$ con $u^2 = 1 - v^2$, es decir $g(v) = v - v^3$:

- $g'(v) = 1 - 3v^2 = 0 \Rightarrow v = \pm\dfrac{1}{\sqrt3}$.
- El máximo es en $v = \dfrac{1}{\sqrt3}$, con $u^2 = \dfrac23 \Rightarrow u = \pm\sqrt{2/3}$. Valor máximo: $\dfrac23\cdot\dfrac{1}{\sqrt3} = \dfrac{2}{3\sqrt3}$.
- Hay **dos** direcciones de máximo: $\left(\pm\sqrt{2/3},\ 1/\sqrt3\right)$.

*Nulas.* $u^2v = 0 \iff u = 0$ o $v = 0$ ⇒ $(1,0)$, $(-1,0)$, $(0,1)$, $(0,-1)$: **cuatro** direcciones.

*No es diferenciable.* $\nabla f(\bar 0) = (f'(\bar 0,(1,0)),\ f'(\bar 0,(0,1))) = (0, 0)$. Si fuera diferenciable, todas las direccionales serían $\nabla f\cdot\breve r = 0$, pero por ejemplo la de máximo vale $\dfrac{2}{3\sqrt3} \ne 0$.

</details>

**Respuesta:**

- a) $f'(\bar 0, \breve r) = 0 \ \forall\breve r \in \Re^2$. No es diferenciable en $\bar 0$, por no ser continua en el origen.
- b) $f'(\bar 0, (u,v)) = u^2v$ con $u^2 + v^2 = 1$.
  - Direcciones de derivada máxima: $(\sqrt{2/3},\ 1/\sqrt3)$ y $(-\sqrt{2/3},\ 1/\sqrt3)$.
  - Direcciones de derivada nula: $(1,0)$, $(-1,0)$, $(0,1)$, $(0,-1)$.
  - No es diferenciable en el origen. Si lo fuera, $f'(\bar 0, \breve r) = \nabla f(\bar 0)\cdot\breve r \ \forall\breve r \in \Re^2$; como en este caso resulta $\nabla f(\bar 0) = \bar 0$, las derivadas deberían ser nulas en toda dirección.

</details>

---

### 05) ¿Plano tangente?

Analice si la gráfica de $f$ del ítem "01e" admite plano tangente en $(0,0,0)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

$f(x,y) = \dfrac{xy^2}{x^2 + y^4}$, con $f(0,0) = 0$.

**Paso 1 — ¿Es continua en el origen?** Sobre $x = y^2$, que iguala los órdenes de $x^2$ e $y^4$:

$$f(y^2, y) = \frac{y^4}{y^4 + y^4} = \frac12 \ne 0$$

⇒ no es continua en $(0,0)$.

**Paso 2 — Conclusión.** No continua ⇒ no diferenciable ⇒ la gráfica **no admite plano tangente** en $(0,0,0)$. Esto pasa aunque existan $f'_x(0,0) = f'_y(0,0) = 0$: el "candidato" sería el plano $z = 0$, pero no es un plano tangente.

</details>

**Respuesta:** La función no es continua en $(0,0)$ ⇒ no es diferenciable en $(0,0)$, por lo tanto la gráfica de $f$ no admite plano tangente en $(0,0,0)$.

</details>

---

### 06) Plano tangente horizontal

Dada la superficie de ecuación $z = e^{(x-1)^2 + y^2}$, determine en qué puntos tiene plano tangente horizontal y obtenga la ecuación de esos planos.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Condición.** El plano tangente $z = z_0 + f'_x(x - x_0) + f'_y(y - y_0)$ es horizontal si y sólo si $f'_x = f'_y = 0$. La función es $C^1$, así que el plano tangente existe en todo punto.

**Paso 2 — Derivadas.**

$$f'_x = 2(x - 1)\,e^{(x-1)^2+y^2}, \qquad f'_y = 2y\,e^{(x-1)^2+y^2}$$

La exponencial nunca se anula ⇒ $x = 1$, $y = 0$.

**Paso 3 — Punto y plano.** $z = e^0 = 1$. El punto es $(1, 0, 1)$ y el plano es $z = 1$.

</details>

**Respuesta:** Únicamente en el punto $(1,0,1)$; ecuación del plano: $z = 1$.

</details>

---

### 07) *Optativo*

*Optativo*: Siendo $f(x,y) = (x^3 - xy^2)/(x^2 + y^2)$ si $(x,y) \ne (0,0)$ y $f(0,0) = 0$, demuestre que $f$ es continua y derivable en toda dirección en $(0,0)$ pero no es diferenciable en $(0,0)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Continuidad.** Separamos la fracción en dos términos de la forma infinitésimo × acotada:

$$\frac{x^3 - xy^2}{x^2+y^2} = \underbrace{x}_{\to0}\cdot\underbrace{\frac{x^2}{x^2+y^2}}_{\in[0,1]} - \underbrace{x}_{\to0}\cdot\underbrace{\frac{y^2}{x^2+y^2}}_{\in[0,1]} \to 0 = f(0,0) \ ✓$$

**Direccionales.** Con $\vec r = (u, v)$:

$$f'(\bar 0, (u,v)) = \lim_{h\to0}\frac{1}{h}\cdot\frac{h^3(u^3 - uv^2)}{h^2(u^2+v^2)} = \frac{u^3 - uv^2}{u^2 + v^2}$$

Para un versor ($u^2 + v^2 = 1$) queda $u^3 - uv^2$. Existe en toda dirección ✓.

**No diferenciable.**

- $f'_x(0,0)$: con $(u,v) = (1,0)$ vale $1$. $f'_y(0,0)$: con $(0,1)$ vale $0$. Entonces $\nabla f(0,0) = (1, 0)$.
- Si fuera diferenciable, sería $f'(\bar 0, (u,v)) = \nabla f\cdot(u,v) = u$.
- Pero, por ejemplo, con $\breve r = \left(\frac{1}{\sqrt2}, \frac{1}{\sqrt2}\right)$: $u^3 - uv^2 = 0$, mientras que $\nabla f\cdot\breve r = \frac{1}{\sqrt2}$.

No coinciden ⇒ **no es diferenciable**.

</details>

**Respuesta:**

- Para el límite observe que: $\dfrac{x^3 - xy^2}{x^2+y^2} = x\,\dfrac{x^2}{x^2+y^2} - x\,\dfrac{y^2}{x^2+y^2}$.
- Derivada direccional: $f'(\bar 0, (u,v)) = u^3 - uv^2 \ \forall\breve r = (u,v) \in \Re^2$.
- Por otra parte, $f'((0,0),(u,v)) \ne \nabla f(0,0)\cdot(u,v)$ ⇒ $f$ no es diferenciable en $(0,0)$.

</details>

---

### 08) Aproximación lineal

Calcule mediante aproximación lineal y compare el resultado con el obtenido con calculadora.

- a) $f(1.96,\ 0.96)$ cuando $f(x,y) = \sqrt{25 - 2x^2 - y^2}$.
- b) $f(0.99,\ 1.98,\ 1.02)$ cuando $f(x,y,z) = xy + \operatorname{sen}(\operatorname{Exp}(2x - y + 3z - 3) - 1)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Fórmula:** $f(\vec A + \vec h) \approx f(\vec A) + \nabla f(\vec A)\cdot\vec h$, eligiendo un $\vec A$ cercano donde $f$ sea fácil de calcular.

**a)**

*Punto cómodo:* $\vec A = (2, 1)$, con $\vec h = (-0{,}04;\ -0{,}04)$.

*Fórmulas:*

$$f(2,1) = \sqrt{25 - 8 - 1} = 4, \qquad f'_x = \frac{-2x}{\sqrt{25 - 2x^2 - y^2}}, \qquad f'_y = \frac{-y}{\sqrt{25 - 2x^2 - y^2}}$$

*Gradiente en $\vec A$:* $f'_x = -\frac44 = -1$ y $f'_y = -\frac14$.

*Cálculo:*

$$f(1{,}96;\ 0{,}96) \approx 4 + (-1)(-0{,}04) + \left(-\tfrac14\right)(-0{,}04) = 4 + 0{,}04 + 0{,}01 = 4{,}05$$

*Calculadora:* $\sqrt{25 - 7{,}6832 - 0{,}9216} = \sqrt{16{,}3952} \approx 4{,}0491$.

**b)**

*Punto cómodo:* $\vec A = (1, 2, 1)$, donde el argumento $2x - y + 3z - 3 = 0$. Entonces $\operatorname{Exp}(0) - 1 = 0$, $\operatorname{sen}0 = 0$ y $f(\vec A) = 2$. El incremento es $\vec h = (-0{,}01;\ -0{,}02;\ 0{,}02)$.

*Derivadas:* llamamos $u = 2x - y + 3z - 3$ y $g = \operatorname{sen}(e^u - 1)$, con $g'_u = \cos(e^u - 1)\,e^u$, que en $\vec A$ vale 1.

- $f'_x = y + 2\,g'_u \to 2 + 2 = 4$.
- $f'_y = x - g'_u \to 1 - 1 = 0$.
- $f'_z = 3\,g'_u \to 3$.

*Cálculo:*

$$f \approx 2 + 4(-0{,}01) + 0(-0{,}02) + 3(0{,}02) = 2 - 0{,}04 + 0{,}06 = 2{,}02$$

*Calculadora:* $xy = 1{,}9602$, $u = 0{,}06$, $e^{0{,}06} - 1 \approx 0{,}06184$ y $\operatorname{sen}(0{,}06184) \approx 0{,}06180$. Total $\approx 2{,}0220$.

</details>

**Respuesta:**

- a) $4.05$ (con calculadora $\approx 4.0491$).
- b) $2.02$ (con calculadora $\approx 2.0220$).

</details>

---

### 09) Aproximación cerca del origen

Demuestre que en un entorno del origen $e^{x/(y+1)} + \ln(y + 1) \cong x + y + 1$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Fórmula.** $f(\vec X) \approx f(\vec 0) + \nabla f(\vec 0)\cdot\vec X$, porque cerca del origen el incremento es $\vec h = (x, y)$. $f$ es $C^1$ cerca del origen ($y > -1$), así que es diferenciable.

**Paso 2 — Valor.** $f(0,0) = e^0 + \ln 1 = 1$.

**Paso 3 — Gradiente.**

$$f'_x = \frac{e^{x/(y+1)}}{y + 1} \to 1, \qquad f'_y = e^{x/(y+1)}\cdot\left(-\frac{x}{(y+1)^2}\right) + \frac{1}{y+1} \to 0 + 1 = 1$$

**Paso 4 — Aproximación.** $f(x,y) \approx 1 + 1\cdot x + 1\cdot y = x + y + 1$ ✓.

</details>

**Respuesta:** Aplicar $f(\bar X) \cong f(\bar A) + \nabla f(\bar A)\cdot(\bar X - \bar A)$ (aproximación mediante diferencial primero), con $\bar A = \bar 0$, $f(\bar 0) = 1$ y $\nabla f(\bar 0) = (1,1)$.

</details>

---

### 10) Superficie paramétrica: punto regular, plano tangente y recta normal

Sea $S$ la superficie de ecuación $\bar X = (u - v^2,\ v^2/u,\ u/v)$ con $(u,v) \in \Re^2 / uv \ne 0$, verifique que $\bar A = (-2,2,1)$ es un punto regular de $S$. Determine y exprese en forma cartesiana el plano tangente y la recta normal a $S$ en $\bar A$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parámetros del punto.**

- $\dfrac{u}{v} = 1 \Rightarrow u = v$.
- $\dfrac{v^2}{u} = v = 2 \Rightarrow u = v = 2$.
- Control: $u - v^2 = 2 - 4 = -2$ ✓.

**Paso 2 — Derivadas parciales del vector posición.**

$$\bar X'_u = \left(1,\ -\frac{v^2}{u^2},\ \frac1v\right) \to (1,\ -1,\ \tfrac12), \qquad \bar X'_v = \left(-2v,\ \frac{2v}{u},\ -\frac{u}{v^2}\right) \to (-4,\ 2,\ -\tfrac12)$$

**Paso 3 — Vector normal** $\vec n = \bar X'_u \times \bar X'_v$:

$$\vec n = \begin{vmatrix} \breve\imath & \breve\jmath & \breve k \\ 1 & -1 & \tfrac12 \\ -4 & 2 & -\tfrac12 \end{vmatrix} = \left(\tfrac12 - 1,\ -\left(-\tfrac12 + 2\right),\ 2 - 4\right) = \left(-\tfrac12,\ -\tfrac32,\ -2\right)$$

Es $\ne \vec 0$ y las derivadas son continuas cerca de $(2,2)$ ⇒ **$\bar A$ es regular**. Multiplicando por $-2$ se obtiene un normal más cómodo: $(1, 3, 4)$.

**Paso 4 — Plano tangente.**

$$1(x + 2) + 3(y - 2) + 4(z - 1) = 0 \ \Rightarrow\ x + 3y + 4z = 8$$

**Paso 5 — Recta normal.** $\vec X = (-2, 2, 1) + t\,(1, 3, 4)$. En forma cartesiana, eliminando $t = x + 2$:

- $y - 2 = 3(x + 2) \Rightarrow y - 3x = 8$.
- $z - 1 = 4(x + 2) \Rightarrow z - 4x = 9$.

</details>

**Respuesta:** Plano tangente: $x + 3y + 4z = 8$. Recta normal: $r_0 = \begin{cases} y - 3x = 8 \\ z - 4x = 9 \end{cases}$.

</details>

---

### 11) Puntos regulares y plano tangente horizontal

Dada la superficie de ecuación $z = x^2 - xy^3 + x$, demuestre que todos sus puntos son regulares y halle aquellos puntos en los que el plano tangente es "horizontal" (paralelo al $xy$).

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Regularidad.** Escribimos la superficie como $F(x,y,z) = x^2 - xy^3 + x - z = 0$:

$$\nabla F = (2x - y^3 + 1,\ -3xy^2,\ -1)$$

La tercera componente es $-1 \ne 0$ ⇒ $\nabla F \ne \vec 0$ en todo punto, y $F$ es $C^1$ ⇒ **todos los puntos son regulares**.

**Plano horizontal.** La normal tiene que ser paralela a $\breve k$, o sea $z'_x = z'_y = 0$:

$$\begin{cases} 2x - y^3 + 1 = 0 \\ -3xy^2 = 0 \end{cases}$$

De la segunda, $x = 0$ o $y = 0$:

- $x = 0$: $-y^3 + 1 = 0 \Rightarrow y = 1$, y $z = 0$ ⇒ punto $(0, 1, 0)$.
- $y = 0$: $2x + 1 = 0 \Rightarrow x = -\frac12$, y $z = \frac14 + 0 - \frac12 = -\frac14$ ⇒ punto $\left(-\frac12, 0, -\frac14\right)$.

</details>

**Respuesta:** $(-1/2,\ 0,\ -1/4)$ y $(0,1,0)$.

</details>

---

### 12) Recta normal a una semiesfera

Sea $r_0$ la recta normal a la superficie de ecuación $z = \sqrt{9 - x^2 - y^2}$ en $(1, 2, z_0)$, analice si existe algún punto en el que $r_0$ interseca a la superficie cilíndrica de ecuación $z = x^2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Punto.** $z_0 = \sqrt{9 - 1 - 4} = 2$, así que el punto es $(1, 2, 2)$.

**Paso 2 — Normal.** La superficie es la semiesfera $x^2 + y^2 + z^2 = 9$ con $z \ge 0$. Con $F = x^2 + y^2 + z^2$, $\nabla F = (2x, 2y, 2z) = (2, 4, 4) \parallel (1, 2, 2)$. Es radial, como en toda esfera.

**Paso 3 — Recta normal.** $r_0: \vec X = (1,2,2) + t(1,2,2) = s\,(1, 2, 2)$, con $s = 1 + t$. Pasa por el origen.

**Paso 4 — Intersección con $z = x^2$.** $2s = s^2 \Rightarrow s(s - 2) = 0 \Rightarrow s = 0$ o $s = 2$:

- $s = 0$: $(0, 0, 0)$.
- $s = 2$: $(2, 4, 4)$.

</details>

**Respuesta:** Sí, en $(0,0,0)$ y en $(2,4,4)$.

</details>

---

### 13) Direcciones de derivada máxima, mínima y nula

Halle las direcciones de derivada direccional máxima, mínima y nula de las siguientes funciones en el punto $\bar A$:

- a) $f(x,y) = x^2 - xy^2$, $\bar A = (1,3)$.
- b) $f(x,y,z) = x^2 - yz^3$, $\bar A = (5,2,0)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Fórmulas** (para $f$ diferenciable, que vale porque son polinomios):

- máxima: $\breve r = \dfrac{\nabla f}{\lVert\nabla f\rVert}$;
- mínima: $\breve r = -\dfrac{\nabla f}{\lVert\nabla f\rVert}$;
- nula: $\breve r \perp \nabla f$.

**a)** $\nabla f = (2x - y^2,\ -2xy)$ ⇒ $\nabla f(1,3) = (2 - 9,\ -6) = (-7, -6)$, con $\lVert\nabla f\rVert = \sqrt{49 + 36} = \sqrt{85}$.

- Máxima: $\left(-\dfrac{7}{\sqrt{85}}, -\dfrac{6}{\sqrt{85}}\right)$.
- Mínima: $\left(\dfrac{7}{\sqrt{85}}, \dfrac{6}{\sqrt{85}}\right)$.
- Nulas: en $\Re^2$, un vector perpendicular a $(a,b)$ es $(-b, a)$ ⇒ $\pm\dfrac{(6, -7)}{\sqrt{85}}$.

**b)** $\nabla f = (2x,\ -z^3,\ -3yz^2)$ ⇒ $\nabla f(5,2,0) = (10, 0, 0)$.

- Máxima: $(1, 0, 0)$.
- Mínima: $(-1, 0, 0)$.
- Nulas: todos los versores perpendiculares a $(1,0,0)$, es decir $(0, u, v)$ con $u^2 + v^2 = 1$.

</details>

**Respuesta:**

- a) $\breve r_{\text{máx}} = (-7/\sqrt{85},\ -6/\sqrt{85})$, $\breve r_{\text{mín}} = (7/\sqrt{85},\ 6/\sqrt{85})$, $\breve r_{\text{nula}_1} = (-6/\sqrt{85},\ 7/\sqrt{85})$, $\breve r_{\text{nula}_2} = (6/\sqrt{85},\ -7/\sqrt{85})$.
- b) $\breve r_{\text{máx}} = (1,0,0)$, $\breve r_{\text{mín}} = (-1,0,0)$, $\breve r_{\text{nula}} = (0,u,v)\ \forall(u,v) \in \Re^2 / u^2 + v^2 = 1$.

</details>

---

### 14) Derivada direccional según un ángulo

Siendo $g(x,y) = 3x^4 - xy + y^3$, calcule la derivada direccional de $g$ en el punto $(1,2)$ según la dirección que forma con $x^+$ un ángulo –en sentido trigonométrico– de $\pi/3$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Versor.** $\breve r = (\cos\frac\pi3,\ \operatorname{sen}\frac\pi3) = \left(\frac12, \frac{\sqrt3}{2}\right)$.

**Paso 2 — Gradiente** ($g$ es un polinomio, así que es diferenciable):

$$\nabla g = (12x^3 - y,\ -x + 3y^2) \ \Rightarrow\ \nabla g(1,2) = (12 - 2,\ -1 + 12) = (10, 11)$$

**Paso 3 — Derivada.**

$$g'((1,2), \breve r) = \nabla g\cdot\breve r = 10\cdot\frac12 + 11\cdot\frac{\sqrt3}{2} = 5 + \frac{11\sqrt3}{2} \approx 14{,}53$$

</details>

**Respuesta:** $5 + 11\sqrt3/2$.

</details>

---

### 15) Máximo en una dirección dada

Sea $f(x,y) = ax^2y^3 + bx^4 + 4xy$, determine $a$ y $b$ de manera que la derivada direccional de $f$ en el punto $(1,-2)$ tenga el valor máximo en una dirección paralela al eje $y$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Condición.** La derivada máxima está en la dirección del gradiente. Para que sea paralela al eje $y$, el gradiente debe ser **no nulo** y de la forma $(0, c)$:

$$f'_x(1,-2) = 0, \qquad f'_y(1,-2) \ne 0$$

**Paso 2 — Derivadas parciales.**

$$f'_x = 2axy^3 + 4bx^3 + 4y, \qquad f'_y = 3ax^2y^2 + 4x$$

**Paso 3 — Evaluar en $(1,-2)$.**

- $f'_x(1,-2) = 2a(-8) + 4b - 8 = -16a + 4b - 8$.
- $f'_y(1,-2) = 3a\cdot4 + 4 = 12a + 4$.

**Paso 4 — Resolver.**

- $-16a + 4b - 8 = 0 \Rightarrow a = \dfrac{b - 2}{4}$.
- $12a + 4 \ne 0 \Rightarrow a \ne -\dfrac13 \Rightarrow \dfrac{b-2}{4} \ne -\dfrac13 \Rightarrow b \ne \dfrac23$.

</details>

**Respuesta:** $a, b \in \Re$ tal que $a = (b - 2)/4$ y $b \ne 2/3$.

</details>

---

### 16) Mayor incremento de temperatura

La temperatura en ºC en cada punto $(x,y,z)$ de un cuerpo es $T(x,y,z) = e^{2x + y + 3z}$, ¿en qué dirección desde el origen se produce el mayor incremento de temperatura?.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

El mayor incremento está en la dirección del gradiente:

$$\nabla T = e^{2x+y+3z}\,(2, 1, 3) \ \Rightarrow\ \nabla T(\bar 0) = (2, 1, 3), \qquad \lVert\nabla T\rVert = \sqrt{4 + 1 + 9} = \sqrt{14}$$

El versor es $\breve r = \dfrac{(2,1,3)}{\sqrt{14}}$.

</details>

**Respuesta:** $\breve r_{\text{máx}} = (2/\sqrt{14},\ 1/\sqrt{14},\ 3/\sqrt{14})$.

</details>

---

### 17) Gradiente a partir de dos derivadas

Sea $f \in C^1$, si $f'(\bar A,(3,4)) = 4$ y $f'(\bar A,(2,7)) = -6$.

- a) Calcule $f'(\bar A,(5,9))$.
- b) Determine el valor de la derivada direccional máxima de $f$ en $\bar A$.
- c) Sabiendo que $f(\bar A) = 3$, calcule en forma aproximada $f(\bar A + (0.01, -0.02))$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Planteo.** Como $f \in C^1$, es diferenciable y $f'(\bar A, \vec r) = \nabla f(\bar A)\cdot\vec r$ para **cualquier** vector $\vec r$. Llamamos $\nabla f(\bar A) = (a, b)$:

$$\begin{cases} 3a + 4b = 4 \\ 2a + 7b = -6 \end{cases}$$

**Paso 2 — Resolver.** Multiplicamos la primera por 2 y la segunda por 3, y restamos:

$$(6a + 21b) - (6a + 8b) = -18 - 8 \Rightarrow 13b = -26 \Rightarrow b = -2$$

Entonces $3a - 8 = 4 \Rightarrow a = 4$, y $\nabla f(\bar A) = (4, -2)$.

**a)** $f'(\bar A, (5,9)) = 4\cdot5 + (-2)\cdot9 = 20 - 18 = 2$.

**b)** $\lVert\nabla f(\bar A)\rVert = \sqrt{16 + 4} = \sqrt{20} = 2\sqrt5$.

**c)** $f(\bar A + \vec h) \approx f(\bar A) + \nabla f\cdot\vec h = 3 + 4(0{,}01) + (-2)(-0{,}02) = 3 + 0{,}04 + 0{,}04 = 3{,}08$.

</details>

**Respuesta:**

- a) $f'(\bar A, (5,9)) = 2$.
- b) $f'(\bar A, \breve r_{\text{máx}}) = 2\sqrt5$.
- c) $f(\bar A + (0.01, -0.02)) \cong 3.08$.

</details>

---

### 18) Recta normal dada por intersección

La recta determinada por la intersección de las superficies de ecuaciones $y^2 = x^2 - z^2$ y $z = x$ es normal a la superficie de ecuación $z = f(x,y)$ en $(1,0,1)$, calcule aproximadamente $f(0.98,\ 0.01)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — La recta.** Con $z = x$: $y^2 = x^2 - x^2 = 0 \Rightarrow y = 0$. La intersección es la recta $(t, 0, t)$, de dirección $(1, 0, 1)$, que pasa por $(1,0,1)$ ✓.

**Paso 2 — Normal a la gráfica.** Para $z = f(x,y)$, un vector normal es $(f'_x, f'_y, -1)$. Tiene que ser paralelo a $(1, 0, 1)$:

$$(f'_x, f'_y, -1) = \lambda(1, 0, 1) \ \Rightarrow\ \lambda = -1 \ \Rightarrow\ f'_x(1,0) = -1, \quad f'_y(1,0) = 0$$

**Paso 3 — Aproximación.** $f(1,0) = 1$ (el punto está en la superficie) y $\vec h = (-0{,}02;\ 0{,}01)$:

$$f(0{,}98;\ 0{,}01) \approx 1 + (-1)(-0{,}02) + 0\cdot(0{,}01) = 1{,}02$$

</details>

**Respuesta:** $f(0.98,\ 0.01) \cong 1.02$.

</details>

---

### 19) Plano tangente a una superficie implícita

Dada la superficie $\Sigma$ de ecuación $z\,e^{y - 2x} - 5 = 0$, halle una ecuación cartesiana para el plano tangente a $\Sigma$ en $(1,2,z_0)$; con esta última calcule aproximadamente $z_1$ sabiendo que $(1.01,\ 1.97,\ z_1) \in \Sigma$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — $z_0$.** $z_0\,e^{2 - 2} - 5 = 0 \Rightarrow z_0 = 5$.

**Paso 2 — Despejar $z$.** $z = 5\,e^{2x - y}$, una función $C^1$.

**Paso 3 — Derivadas en $(1,2)$.**

$$z'_x = 10\,e^{2x-y} \to 10, \qquad z'_y = -5\,e^{2x-y} \to -5$$

**Paso 4 — Plano tangente.**

$$z = 5 + 10(x - 1) - 5(y - 2) = 10x - 5y + 5$$

**Paso 5 — Aproximar $z_1$** usando el plano:

$$z_1 \approx 10(1{,}01) - 5(1{,}97) + 5 = 10{,}1 - 9{,}85 + 5 = 5{,}25$$

El valor exacto es $5e^{0{,}05} \approx 5{,}256$.

</details>

**Respuesta:** $z = 10x - 5y + 5$, $\ f(1.01,\ 1.97) \cong 5.25$.

</details>

---

### 20) Derivada direccional a partir del plano tangente

Se sabe que el plano tangente a la superficie de ecuación $z = f(x,y)$ en el punto $(1,2,z_0)$ es $2x + 3y + 4z = 1$. Con esta información, ¿es posible calcular la derivada direccional de $f$ en el punto $(1,2)$ en la dirección que va hacia el punto $(3,4)$?.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — ¿Se puede?** Sí. Si la superficie admite plano tangente, $f$ es diferenciable en $(1,2)$, y entonces la derivada direccional es $\nabla f\cdot\breve r$.

**Paso 2 — Gradiente a partir del plano.** Despejamos $z$: $z = \dfrac14 - \dfrac12x - \dfrac34y$. Los coeficientes de $x$ e $y$ son las derivadas parciales:

$$f'_x(1,2) = -\frac12, \qquad f'_y(1,2) = -\frac34$$

**Paso 3 — Versor.** Desde $(1,2)$ hacia $(3,4)$: $\vec v = (2, 2)$ ⇒ $\breve r = \left(\frac{1}{\sqrt2}, \frac{1}{\sqrt2}\right)$.

**Paso 4 — Derivada.**

$$f'((1,2), \breve r) = \left(-\frac12 - \frac34\right)\frac{1}{\sqrt2} = -\frac{5}{4\sqrt2} = -\frac{5\sqrt2}{8} \approx -0{,}884$$

</details>

**Respuesta:** Sí. Dado que la superficie admite plano tangente, $f$ es diferenciable en $(1,2)$; entonces se puede usar el gradiente para calcular la derivada direccional. Resulta: $f'((1,2), \breve r) = -5\sqrt2/8$.

</details>

---

### 21) Propagación de errores

El resultado de la medición de una magnitud escalar $w$ es del tipo $w_0 \pm \varepsilon_w$, donde $w_0$ es el valor medido y $\varepsilon_w = |\Delta w|_{\text{máx}}$ es la ***cota de error absoluto*** de la medición. Cuando $w = f(x_1, \cdots, x_n)$ y se miden los $x_i$ para calcular $w$ a través de $f$, una forma acostumbrada de evaluar $\varepsilon_w$ es:

$$\varepsilon_w = \sum_{i=1}^n |f'_{x_i}(A)|\,\varepsilon_{x_i}, \quad \text{donde } A = (a_1, \cdots, a_n), \ a_i \text{ es el valor medido para cada } x_i.$$

- a) Sea $I = 0.50$ mA la intensidad de corriente eléctrica a través de un resistor y $V = 0.44$ Volt la diferencia de potencial entre sus terminales. Sabiendo que $R = V / I$ es la resistencia eléctrica del resistor, determine $R \pm \varepsilon_R$ considerando que Volt/mA = kΩ<sup>(\*)</sup> y que ambos instrumentos tienen un error máximo de $\pm1$ en el dígito menos significativo (típico en instrumentos digitales).
- b) Un recipiente tiene forma de cilindro circular recto, sus dimensiones internas son: diámetro $3.1 \pm 0.05$ cm y altura $5.2 \pm 0.05$ cm. Calcule su capacidad $V \pm \varepsilon_V$.
- c) Determine la cota de error relativo de $z$ en función de los errores relativos de $x$ e $y$ en los siguientes casos: $z = xy$, $z = x/y$, $z = x^2y^3$. Nota: para $w \ne 0$, $\varepsilon_{\text{rel}_w} \doteq \varepsilon_w / |w|$.
- d) Dados dos resistores con resistencia nominal $R_1 = R_2 = 39$ kΩ al 5% ($\varepsilon_{\text{relativo}}$ en % o *tolerancia*), calcule $R_{EQ} = \dfrac{R_1R_2}{R_1 + R_2}$ (resistencia equivalente de dos resistores en paralelo); no olvide indicar la cota de error relativo de $R_{EQ}$ en %.

<sup>(\*)</sup> kΩ "se lee" kiloOhm, 1 kΩ = 1000 Ω. mA "se lee" miliAmpere, 1 mA = 0.001 Ampere.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)**

*Fórmula:* $R = \dfrac{V}{I}$, $R'_V = \dfrac1I$, $R'_I = -\dfrac{V}{I^2}$:

$$\varepsilon_R = \frac{1}{I}\,\varepsilon_V + \frac{V}{I^2}\,\varepsilon_I$$

*Datos:* $V = 0{,}44$ V e $I = 0{,}50$ mA. Un error de $\pm1$ en el último dígito da $\varepsilon_V = 0{,}01$ V y $\varepsilon_I = 0{,}01$ mA.

*Cálculo:*

- $R = \dfrac{0{,}44}{0{,}50} = 0{,}88$ kΩ.
- $\varepsilon_R = \dfrac{0{,}01}{0{,}5} + \dfrac{0{,}44}{0{,}25}\cdot0{,}01 = 0{,}02 + 0{,}0176 = 0{,}0376 \approx 0{,}04$ kΩ.

**b)**

*Fórmula:* $V = \pi\left(\dfrac d2\right)^2h = \dfrac{\pi d^2h}{4}$, con $V'_d = \dfrac{\pi dh}{2}$ y $V'_h = \dfrac{\pi d^2}{4}$:

$$\varepsilon_V = \frac{\pi d h}{2}\,\varepsilon_d + \frac{\pi d^2}{4}\,\varepsilon_h$$

*Cálculo* con $d = 3{,}1$, $h = 5{,}2$ y $\varepsilon_d = \varepsilon_h = 0{,}05$:

- $V = \dfrac{\pi\cdot 9{,}61\cdot 5{,}2}{4} \approx 39{,}25$ cm³.
- $\varepsilon_V = \dfrac{\pi\cdot3{,}1\cdot5{,}2}{2}(0{,}05) + \dfrac{\pi\cdot9{,}61}{4}(0{,}05) \approx 1{,}266 + 0{,}377 \approx 1{,}6$ cm³.

**c)** Se divide $\varepsilon_z$ por $|z|$ en cada caso.

- **$z = xy$:** $\varepsilon_z = |y|\varepsilon_x + |x|\varepsilon_y$ ⇒ $\dfrac{\varepsilon_z}{|xy|} = \dfrac{\varepsilon_x}{|x|} + \dfrac{\varepsilon_y}{|y|}$.
- **$z = x/y$:** $\varepsilon_z = \dfrac{\varepsilon_x}{|y|} + \dfrac{|x|}{y^2}\varepsilon_y$ ⇒ dividiendo por $\dfrac{|x|}{|y|}$: $\dfrac{\varepsilon_x}{|x|} + \dfrac{\varepsilon_y}{|y|}$.
- **$z = x^2y^3$:** $\varepsilon_z = 2|xy^3|\varepsilon_x + 3|x^2y^2|\varepsilon_y$ ⇒ dividiendo por $|x^2y^3|$: $2\dfrac{\varepsilon_x}{|x|} + 3\dfrac{\varepsilon_y}{|y|}$.

**d)**

*Fórmula:*

$$\frac{\partial R_{EQ}}{\partial R_1} = \frac{R_2(R_1 + R_2) - R_1R_2}{(R_1+R_2)^2} = \frac{R_2^2}{(R_1+R_2)^2}, \qquad \frac{\partial R_{EQ}}{\partial R_2} = \frac{R_1^2}{(R_1+R_2)^2}$$

*Cálculo* con $R_1 = R_2 = 39$:

- $R_{EQ} = \dfrac{39\cdot39}{78} = 19{,}5$ kΩ.
- Ambas derivadas valen $\dfrac{39^2}{78^2} = \dfrac14$.
- $\varepsilon_{R_1} = \varepsilon_{R_2} = 5\%\cdot39 = 1{,}95$ kΩ.
- $\varepsilon_{R_{EQ}} = \dfrac14(1{,}95) + \dfrac14(1{,}95) = 0{,}975$ kΩ.
- Error relativo: $\dfrac{0{,}975}{19{,}5} = 5\%$.

</details>

**Respuesta:**

- a) $0.88 \pm 0.04$ kΩ.
- b) $39.2 \pm 1.6$ cm³.
- c) Para $z = xy$ y $z = x/y$: $\varepsilon_{\text{rel}_z} = \varepsilon_{\text{rel}_x} + \varepsilon_{\text{rel}_y}$. Para $z = x^2y^3$: $\varepsilon_{\text{rel}_z} = 2\varepsilon_{\text{rel}_x} + 3\varepsilon_{\text{rel}_y}$.
- d) $19.5 \pm 0.975$ kΩ. Es decir, 19.5 kΩ al 5%.

</details>

---

## Cuestionario

### Cuestionario a)

Demuestre que todo campo diferenciable es continuo y derivable en toda dirección.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

Por hipótesis, $f(\vec A + \vec h) - f(\vec A) = T(\vec h) + \lVert\vec h\rVert\,\varphi(\vec h)$, con $T$ lineal y $\varphi \to 0$.

**Continuidad.** Cuando $\vec h \to \vec 0$, $T(\vec h) \to 0$ (una transformación lineal es continua) y $\lVert\vec h\rVert\,\varphi(\vec h) \to 0$. Entonces $f(\vec A + \vec h) \to f(\vec A)$ ✓.

**Derivabilidad.** Tomamos $\vec h = t\vec r$:

$$\frac{f(\vec A + t\vec r) - f(\vec A)}{t} = \frac{t\,T(\vec r) + |t|\,\lVert\vec r\rVert\,\varphi(t\vec r)}{t} = T(\vec r) \pm \lVert\vec r\rVert\,\varphi(t\vec r) \xrightarrow[t\to0]{} T(\vec r)$$

Por lo tanto $f'(\vec A, \vec r) = T(\vec r)$ existe para todo $\vec r$. $\blacksquare$

</details>

**Respuesta:** De la definición, el incremento es $T(\vec h)$ más un término que tiende a 0 más rápido que $\lVert\vec h\rVert$: eso da la continuidad, y con $\vec h = t\vec r$ da $f'(\vec A, \vec r) = T(\vec r)$.

</details>

---

### Cuestionario b)

Demuestre que $Df(A)$ es la matriz asociada a la transformación lineal que figura en la definición de diferenciabilidad de $f$ en $A$.

<details>
<summary><b>Solución</b></summary>

**Respuesta:** por el ítem a), $f'(A, \vec r) = T(\vec r)$. En particular, con los versores canónicos:

$$T(\breve e_j) = f'(A, \breve e_j) = \frac{\partial f}{\partial x_j}(A)$$

La columna $j$ de la matriz asociada a $T$ es justamente $T(\breve e_j)$. Entonces esa matriz tiene por columnas las derivadas parciales, que es la definición de $Df(A)$. Para un campo vectorial se aplica lo mismo a cada componente (cada fila). $\blacksquare$

</details>

---

### Cuestionario c)

Proponga un ejemplo de función de varias variables que resulte derivable pero no sea diferenciable en un punto interior a su dominio.

<details>
<summary><b>Solución</b></summary>

**Respuesta:** $f(x,y) = \dfrac{x^2y}{x^2+y^2}$ con $f(0,0) = 0$ (ejercicio 04 b). Es derivable en toda dirección en el origen, con $f' = u^2v$, pero no es diferenciable, porque $\nabla f(\bar 0) = \bar 0$ y las direccionales no son todas nulas.

</details>

---

### Cuestionario d)

Determine los casos en los que $\Delta w = dw$.

<details>
<summary><b>Solución</b></summary>

**Respuesta:** $\Delta w - dw = \lVert\vec h\rVert\,\varphi(\vec h)$ es el "resto" de la aproximación lineal. Es nulo para **todo** incremento si y sólo si $f$ es **afín**: $f(\vec x) = \vec c\cdot\vec x + d$ (un polinomio de grado $\le 1$). En ese caso $f(\vec A + \vec h) - f(\vec A) = \vec c\cdot\vec h = df$ exactamente. Para otras funciones puede coincidir sólo para algunos incrementos particulares.

</details>

---

### Cuestionario e)

*Optativo*: Sea $f(x,y) = x^{1/3}\sqrt{x^2 + y^2}$, demuestre que $f$ es diferenciable en $(0,0)$ pero $f'_x$ no es continua en $(0,0)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Gradiente en el origen** (por definición):

- $f'_x(0,0) = \lim\dfrac{h^{1/3}|h|}{h}$. Como $\left|\dfrac{h^{1/3}|h|}{h}\right| = |h|^{1/3} \to 0$, vale 0.
- $f'_y(0,0) = \lim\dfrac{0}{k} = 0$.

Entonces $\nabla f(\bar 0) = (0,0)$.

**Paso 2 — Diferenciabilidad.** Tenemos que verificar:

$$\lim_{(x,y)\to\bar0}\frac{f(x,y) - 0 - 0}{\sqrt{x^2+y^2}} = \lim x^{1/3} = 0 \ ✓$$

⇒ $f$ es diferenciable en $(0,0)$.

**Paso 3 — $f'_x$ fuera del eje $y$.** Para $x \ne 0$, por la regla del producto:

$$f'_x = \frac13x^{-2/3}\sqrt{x^2+y^2} + x^{1/3}\frac{x}{\sqrt{x^2+y^2}} = \frac{4x^2 + y^2}{3x^{2/3}\sqrt{x^2+y^2}}$$

**Paso 4 — No es continua en el origen.** Sobre $x = y^2$:

$$f'_x(y^2, y) = \frac{4y^4 + y^2}{3y^{4/3}\sqrt{y^4 + y^2}} \approx \frac{y^2}{3y^{4/3}|y|} = \frac{1}{3|y|^{1/3}} \to \infty$$

Además, sobre $x = y^{3/2}$ con $y \ge 0$ el límite da $1/3$. En ningún caso da $0 = f'_x(0,0)$ ⇒ $f'_x$ **no es continua** en el origen.

**Conclusión:** la condición $C^1$ es suficiente pero **no necesaria** para la diferenciabilidad.

</details>

**Respuesta:** Verifique que la $f$ propuesta cumple con la definición de diferenciabilidad en $(0,0)$. Por otra parte,

$$f'_x(x,y) = \begin{cases} \dfrac{4x^2 + y^2}{3x^{2/3}\sqrt{x^2+y^2}} & \text{si } (x,y) \ne (0,y) \\ 0 & \text{si } (x,y) = (0,0) \end{cases}$$

con lo cual $f'_x$ no es continua en $(0,0)$. Esto puede demostrarse analizando límites por curvas: por ejemplo, acercándose por $x = y^2$, $\lim\limits_{y\to0} f'_x(y^2, y) = \infty$. También puede analizarse por $x = y^{3/2}$ con $y \ge 0$, que resulta $\lim\limits_{y\to0^+} f'_x(y^{3/2}, y) = 1/3$.

</details>

---

[← Volver al menú principal](../README.md)
