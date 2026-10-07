# Unidad 1 — Práctica: Ecuaciones diferenciales (1.ª parte)

Ejercicios del **T.P. N.º 1 de la Guía de Trabajos Prácticos** ([TP01-Ecuaciones-Diferenciales-1.pdf](../aula-virtual/01-Ecuaciones-Diferenciales-1/TP01-Ecuaciones-Diferenciales-1.pdf)). Las respuestas se controlaron con las [respuestas oficiales de la guía](../aula-virtual/00-Guia-TP/Guia-TP-2016-Respuestas.pdf) y con la [fe de erratas](../aula-virtual/00-Guia-TP/Guia-TP-2016-Fe-de-Erratas-2018-07-31.pdf).

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

> **Nomenclatura y consideraciones básicas:**
>
> - S.G. simboliza *solución general*, S.P. *solución particular*, S.S. *solución singular*.
> - Las soluciones de una ecuación diferencial ordinaria de **orden *n*** son relaciones entre las variables que satisfacen a la ecuación diferencial; en especial, la S.G. debe contener ***n*** constantes arbitrarias esenciales.

---

### 01) Orden, grado y linealidad

Determine el orden y, si existe, el grado de las siguientes ecuaciones diferenciales ordinarias. Reconozca aquellas que son del tipo lineal.

- a) $(y'')^2 - y''' = y - (y')^2$
- b) $y''' + x\,(y')^4 = 0$
- c) $(1+x)\,(y'')^4 + 3\,y''' + 5\,x^2\,y = 0$
- d) $y'' - 3\,\operatorname{sen}(y') + y = x^3$
- e) $3\,x\,dy - y\,dx = 0$
- f) $x\,y'' - 4\,y' + x - 1 = 0$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Criterios:**

- **Orden** = mayor orden de derivada que aparece.
- **Grado** = exponente de esa derivada de mayor orden, **sólo si** la ecuación es polinómica en $y, y', y'', \dots$
- **Lineal** = $y$ y todas sus derivadas aparecen a la primera potencia, sin productos entre ellas y sin estar dentro de funciones como $\operatorname{sen}$, $e^{(\cdot)}$, etc.

**a)** $(y'')^2 - y''' = y - (y')^2$

- La derivada de mayor orden es $y'''$ ⇒ **orden 3**.
- $y'''$ aparece a la potencia 1 ⇒ **grado 1**. Que $y''$ esté al cuadrado no importa para el grado, porque no es la derivada de mayor orden.
- **No es lineal**, porque aparecen $(y'')^2$ y $(y')^2$.

**b)** $y''' + x\,(y')^4 = 0$

- Mayor derivada: $y'''$ ⇒ **orden 3**, **grado 1**.
- **No es lineal** por $(y')^4$.

**c)** $(1+x)(y'')^4 + 3y''' + 5x^2y = 0$

- Mayor derivada: $y'''$, con potencia 1 ⇒ **orden 3**, **grado 1**.
- **No es lineal** por $(y'')^4$.

**d)** $y'' - 3\operatorname{sen}(y') + y = x^3$

- Mayor derivada: $y''$ ⇒ **orden 2**.
- Aparece $\operatorname{sen}(y')$, que no es polinómica en $y'$ ⇒ **no tiene grado**.
- **No es lineal**.

**e)** $3x\,dy - y\,dx = 0$. Dividiendo por $dx$ queda $3x\,y' - y = 0$.

- **Orden 1**, **grado 1**.
- **Es lineal**: tiene la forma $p(x)\,y' + q(x)\,y = f(x)$ con $p = 3x$, $q = -1$, $f = 0$.

**f)** $x\,y'' - 4y' + x - 1 = 0$, o sea, $x\,y'' - 4y' = 1 - x$.

- **Orden 2**, **grado 1**.
- **Es lineal**: los coeficientes dependen sólo de $x$ y $y''$, $y'$ aparecen a la primera potencia.

</details>

**Respuesta:**

| | a | b | c | d | e | f |
|---|---|---|---|---|---|---|
| orden | 3 | 3 | 3 | 2 | 1 | 2 |
| grado | 1 | 1 | 1 | — | 1 | 1 |
| lineal | no | no | no | no | **sí** | **sí** |

</details>

---

### 02) Verificación de soluciones

Verifique que:

- a) $y = e^{-x} + x - 1$ es una solución de $y' + y = x$ que cumple con $y(0) = 0$.
- b) $y = (2 - \ln(x))\,\sqrt{x}$ satisface la ecuación diferencial $4\,x^2\,y'' + y = 0 \ \forall x / x > 0$ y tiene recta tangente de ecuación $y = 2$ en el punto $(1, 2)$.
- c) $y^2 = C_1 x + C_2$ es S.G. de $y\,y'^2 + y^2\,y'' = 0$. Halle la S.P. que en $(1, y_0)$ tiene recta tangente de ecuación $y = 2x - 1$.
- d) $y = x$ es una solución de $y\,y'^2 + y^2\,y'' = x$.
- e) $y = C\,x + C^2$ es S.G., $y = -x^2/4$ es S.S. de $y' = x\,y' + (y')^2$. Halle las soluciones que pasan por $(2, -1)$.
- f) $x^2 + 4y^2 = C$ es S.G. de $4\,y\,y' = -x$. Halle la S.P. que pasa por $(-2, 1)$.

> **Fe de erratas (31/07/18):** en el ítem 02-e la EDO dice $y' = x\,y' + (y')^2$, **debe decir** $y = x\,y' + (y')^2$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Idea general:** verificar una solución consiste en derivar la función propuesta, reemplazarla junto con sus derivadas en la ecuación y comprobar que queda una **identidad** (algo que vale para todo $x$).

**a)** $y = e^{-x} + x - 1$.

- Derivada: $y' = -e^{-x} + 1$.
- Reemplazo: $y' + y = (-e^{-x} + 1) + (e^{-x} + x - 1) = x$ ✓.
- Condición: $y(0) = e^0 + 0 - 1 = 0$ ✓.

**b)** $y = (2 - \ln x)\,x^{1/2}$.

*Primera derivada* (regla del producto):

$$y' = -\frac{1}{x}\,x^{1/2} + (2 - \ln x)\,\frac{1}{2}x^{-1/2} = x^{-1/2}\left[-1 + \frac{2 - \ln x}{2}\right] = -\frac{\ln x}{2\sqrt{x}}$$

*Segunda derivada*: escribimos $y' = -\frac12 \ln x \cdot x^{-1/2}$ y derivamos con la regla del producto:

$$y'' = -\frac12\left[\frac1x\,x^{-1/2} - \frac12\ln x\; x^{-3/2}\right] = -\frac12\,x^{-3/2}\left[1 - \frac{\ln x}{2}\right] = \frac{\ln x - 2}{4\,x^{3/2}}$$

*Reemplazo en la ecuación:*

$$4x^2\,y'' = 4x^2\cdot\frac{\ln x - 2}{4x^{3/2}} = (\ln x - 2)\sqrt{x} = -(2 - \ln x)\sqrt{x} = -y$$

Por lo tanto $4x^2y'' + y = 0$ para todo $x > 0$ ✓. (Hace falta $x > 0$ por $\ln x$ y $\sqrt{x}$.)

*Recta tangente en $(1,2)$:* $y(1) = (2 - 0)\cdot 1 = 2$ ✓ y $y'(1) = -\dfrac{\ln 1}{2} = 0$. La tangente es $y - 2 = 0\,(x - 1)$, es decir, $y = 2$ ✓.

**c)** $y^2 = C_1x + C_2$.

*Verificación:* derivamos implícitamente respecto de $x$:

$$2y\,y' = C_1 \quad (1)$$

Derivamos otra vez:

$$2y'^2 + 2y\,y'' = 0 \ \Rightarrow\ y'^2 + y\,y'' = 0$$

Multiplicando por $y$: $y\,y'^2 + y^2\,y'' = 0$ ✓. Además $C_1$ y $C_2$ son **esenciales**: no se pueden reunir en una sola constante. Hay 2 constantes y la ecuación es de orden 2 ⇒ es S.G.

*S.P.:* que la recta tangente en $(1, y_0)$ sea $y = 2x - 1$ significa dos cosas:

- El punto está sobre la recta: $y_0 = 2\cdot 1 - 1 = 1$.
- La pendiente es la de la recta: $y'(1) = 2$.

Usamos (1) en $x = 1$: $C_1 = 2\,y(1)\,y'(1) = 2\cdot 1\cdot 2 = 4$.

Usamos la familia en $(1, 1)$: $1^2 = C_1\cdot 1 + C_2 \Rightarrow C_2 = 1 - 4 = -3$.

S.P.: $y^2 = 4x - 3$.

**d)** $y = x \Rightarrow y' = 1,\ y'' = 0$. Reemplazando: $y\,y'^2 + y^2\,y'' = x\cdot 1 + x^2\cdot 0 = x$ ✓.

**e)** Con la corrección de la fe de erratas, la EDO es $y = x\,y' + (y')^2$ (ecuación de **Clairaut**).

*S.G.:* $y = Cx + C^2 \Rightarrow y' = C$. Entonces $x\,y' + (y')^2 = xC + C^2 = y$ ✓.

*S.S.:* $y = -\dfrac{x^2}{4} \Rightarrow y' = -\dfrac{x}{2}$. Entonces $x\left(-\dfrac x2\right) + \dfrac{x^2}{4} = -\dfrac{x^2}{2} + \dfrac{x^2}{4} = -\dfrac{x^2}{4} = y$ ✓.

No se obtiene de $Cx + C^2$ para ningún $C$ constante (es una parábola y la S.G. son rectas): es **singular**, y de hecho es la envolvente de las rectas.

*Soluciones que pasan por $(2, -1)$:*

- De la S.G.: $-1 = 2C + C^2 \Rightarrow C^2 + 2C + 1 = 0 \Rightarrow (C+1)^2 = 0 \Rightarrow C = -1$. Queda $y = -x + 1$.
- De la S.S.: $-\dfrac{2^2}{4} = -1$ ✓, así que **también pasa**.

Por ese punto pasan dos soluciones: no hay unicidad. Además, la recta $y = 1 - x$ es tangente a la parábola en $(2,-1)$.

**f)** $x^2 + 4y^2 = C$.

*Verificación:* derivando, $2x + 8y\,y' = 0 \Rightarrow 4y\,y' = -x$ ✓. Hay 1 constante y la ecuación es de orden 1 ⇒ es S.G.

*S.P. por $(-2, 1)$:* $C = (-2)^2 + 4\cdot 1^2 = 8$.

</details>

**Respuesta:**

- a), b), d): se verifican.
- c) S.P.: $y^2 = 4x - 3$.
- e) Existen dos soluciones: $y = 1 - x$ (de la S.G., con $C = -1$) e $y = -x^2/4$ (la S.S.).
- f) S.P.: $x^2 + 4y^2 = 8$.

</details>

---

### 03) Ecuación diferencial de una familia de curvas

Halle la ecuación diferencial correspondiente a las siguientes familias de curvas:

- a) $y^2 = 4\,a\,x$
- b) $x^2 + y^2 = r^2$
- c) $y = \operatorname{sen}(a\,x + b)$
- d) $y = a\,e^x + b\,x\,e^x$
- e) $y = C_1\,x + C_2\,x^{-1} + C_3$
- f) $y = b\,a^x$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Método:** si la familia tiene $n$ parámetros, se deriva $n$ veces y se **eliminan los parámetros** entre las ecuaciones. La EDO resultante es de orden $n$ y no contiene constantes.

**a)** $y^2 = 4ax$ (1 parámetro: $a$).

- Derivamos: $2y\,y' = 4a \Rightarrow a = \dfrac{y\,y'}{2}$.
- Reemplazamos en la familia: $y^2 = 4x\cdot\dfrac{y\,y'}{2} = 2x\,y\,y'$.
- Dividiendo por $y$ (para $y \ne 0$): $y = 2x\,y'$.

**b)** $x^2 + y^2 = r^2$ (1 parámetro: $r$). Derivando, $2x + 2y\,y' = 0 \Rightarrow x + y\,y' = 0$. El parámetro desaparece solo.

**c)** $y = \operatorname{sen}(ax + b)$ (2 parámetros ⇒ orden 2).

Derivamos dos veces:

$$y' = a\cos(ax+b), \qquad y'' = -a^2\operatorname{sen}(ax+b) = -a^2\,y \ \Rightarrow\ a^2 = -\frac{y''}{y}$$

Para eliminar $b$ usamos $\operatorname{sen}^2 + \cos^2 = 1$: $\ y^2 + \left(\dfrac{y'}{a}\right)^2 = 1$, es decir, $y^2 + \dfrac{y'^2}{a^2} = 1$.

Reemplazamos $\dfrac{1}{a^2} = -\dfrac{y}{y''}$:

$$y^2 - \frac{y\,y'^2}{y''} = 1$$

Multiplicamos por $y''$ y reordenamos:

$$y^2\,y'' - y\,y'^2 = y'' \ \Rightarrow\ y''\,(1 - y^2) + y\,y'^2 = 0$$

**d)** $y = a\,e^x + b\,x\,e^x$ (2 parámetros).

- $y' = a e^x + b e^x + b x e^x = y + b\,e^x$ ⇒ $y' - y = b\,e^x$ (A).
- Derivando (A): $y'' - y' = b\,e^x$ (B).
- Igualando (A) y (B): $y'' - y' = y' - y$ ⇒ $y'' - 2y' + y = 0$.

**e)** $y = C_1x + C_2x^{-1} + C_3$ (3 parámetros ⇒ orden 3).

$$y' = C_1 - C_2x^{-2}, \qquad y'' = 2C_2x^{-3}, \qquad y''' = -6C_2x^{-4}$$

Dividimos $y'''$ por $y''$: $\dfrac{y'''}{y''} = \dfrac{-6C_2x^{-4}}{2C_2x^{-3}} = -\dfrac{3}{x}$ ⇒ $x\,y''' + 3y'' = 0$, con $x \ne 0$.

**f)** $y = b\,a^x$ (2 parámetros).

- $y' = b\,a^x\ln a = y\ln a$ ⇒ $\ln a = \dfrac{y'}{y}$.
- $y'' = y'\ln a = y\,(\ln a)^2$.
- Reemplazando: $y'' = y\cdot\dfrac{y'^2}{y^2} = \dfrac{y'^2}{y}$ ⇒ $y\,y'' = y'^2$.

</details>

**Respuesta:**

- a) $y = 2x\,y'$
- b) $x + y\,y' = 0$
- c) $y''(1 - y^2) + y\,y'^2 = 0$
- d) $y'' - 2y' + y = 0$
- e) $x\,y''' + 3y'' = 0 \ \wedge\ x \neq 0$
- f) $y\,y'' = y'^2$

</details>

---

### 04) Ecuación diferencial de familias descriptas geométricamente

Halle la ecuación diferencial de la familia de ...

- a) ... rectas que pasan por $(1, -1)$.
- b) ... hipérbolas con focos en el eje $x$, centro en el origen y semiejes $a$ variable y $b = 1$.
- c) ... circunferencias que pasan por el origen y tienen su centro en el eje $x$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Método:** primero se escribe la **ecuación de la familia** con su parámetro y después se elimina el parámetro derivando.

**a)** Las rectas por $(1, -1)$ con pendiente $m$ son $y + 1 = m\,(x - 1)$. Derivando, $y' = m$. Reemplazando $m$:

$$y + 1 = y'\,(x - 1) \ \Rightarrow\ (x - 1)\,y' = y + 1$$

**b)** Una hipérbola con centro en el origen y focos en el eje $x$ es $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$. Con $b = 1$: $\ \dfrac{x^2}{a^2} - y^2 = 1$.

- Derivamos: $\dfrac{2x}{a^2} - 2y\,y' = 0 \Rightarrow \dfrac{1}{a^2} = \dfrac{y\,y'}{x}$.
- Reemplazamos: $x^2\cdot\dfrac{y\,y'}{x} - y^2 = 1 \Rightarrow x\,y\,y' - y^2 = 1$.

**c)** Si el centro es $(c, 0)$ y la circunferencia pasa por el origen, el radio es $|c|$:

$$(x - c)^2 + y^2 = c^2 \ \Rightarrow\ x^2 - 2cx + y^2 = 0 \ \Rightarrow\ 2c = \frac{x^2 + y^2}{x} \quad (1)$$

Derivando la segunda forma: $2x - 2c + 2y\,y' = 0 \Rightarrow 2c = 2x + 2y\,y'$ (2).

Igualando (1) y (2):

$$\frac{x^2 + y^2}{x} = 2x + 2y\,y' \ \Rightarrow\ x^2 + y^2 = 2x^2 + 2x\,y\,y' \ \Rightarrow\ 2x\,y\,y' = y^2 - x^2$$

</details>

**Respuesta:**

- a) $(x - 1)\,y' = y + 1$
- b) $x\,y\,y' - y^2 = 1$
- c) $2\,x\,y\,y' = y^2 - x^2$

</details>

---

### 05) $(f\,g)' = f'\,g'$

Dadas las funciones $f, g$ derivables, se sabe que en general $(f\,g)' \neq f'\,g'$. Para el caso en que $f(x) = e^{x^3 + 2x}$, halle las funciones $g$ para las que se cumple que $(f\,g)' = f'\,g'$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Planteo.** Por la regla del producto, $(fg)' = f'g + fg'$. La condición pedida es:

$$f'\,g + f\,g' = f'\,g'$$

Esta es una **EDO en la incógnita $g$**.

**Paso 2 — Derivada de $f$.** $f'(x) = (3x^2 + 2)\,e^{x^3+2x} = (3x^2+2)\,f$.

**Paso 3 — Reemplazar y simplificar.** Dividimos todo por $f$, que nunca se anula porque es una exponencial:

$$(3x^2+2)\,g + g' = (3x^2+2)\,g'$$

$$g'\,\big[1 - (3x^2 + 2)\big] = -(3x^2+2)\,g \ \Rightarrow\ g'\,(-3x^2 - 1) = -(3x^2+2)\,g$$

$$\frac{g'}{g} = \frac{3x^2 + 2}{3x^2 + 1}$$

Es de **variables separables** ($g \equiv 0$ también es solución y se recupera con $K = 0$).

**Paso 4 — Integrar.** Escribimos la fracción como $\dfrac{3x^2+2}{3x^2+1} = 1 + \dfrac{1}{3x^2+1}$. Para la segunda integral usamos $u = \sqrt3\,x$:

$$\int \frac{dx}{3x^2+1} = \frac{1}{\sqrt3}\arctan(\sqrt3\,x)$$

Entonces:

$$\ln|g| = x + \frac{\arctan(\sqrt3\,x)}{\sqrt3} + c$$

**Paso 5 — Despejar.**

$$g(x) = K\,e^{\,x + \tan^{-1}(\sqrt3\,x)/\sqrt3}, \qquad K \in \mathbb{R}$$

</details>

**Respuesta:** $g(x) = K\,e^{\,x + \tan^{-1}(\sqrt{3}\,x)/\sqrt{3}}$, $K \in \mathbb{R}$.

</details>

---

### 06) La familia $y = 1/(C - x)$

Compruebe que todas las curvas de la familia $y = 1/(C - x)$ con $C \in \Re$, $x \neq C$ son soluciones de la ecuación diferencial $y' = y^2$. ¿Existe otra solución?, dibújelas y concluya.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Verificación.** $y = (C - x)^{-1} \Rightarrow y' = -(C-x)^{-2}\cdot(-1) = \dfrac{1}{(C-x)^2} = y^2$ ✓.

**Paso 2 — Buscar todas las soluciones resolviendo la EDO.** $y' = y^2$ es separable:

- **Caso $y \equiv 0$:** $y' = 0 = 0^2$ ✓. **Es solución.**
- **Caso $y \ne 0$:** $\dfrac{y'}{y^2} = 1 \Rightarrow -\dfrac{1}{y} = x - C \Rightarrow y = \dfrac{1}{C - x}$, que es la familia dada.

**Paso 3 — ¿$y = 0$ pertenece a la familia?** $\dfrac{1}{C-x} = 0$ no se cumple para ningún $C$ real. Sólo se obtiene como límite cuando $C \to \pm\infty$. Por lo tanto $y \equiv 0$ es **otra solución**, que no está incluida en la familia.

**Paso 4 — Gráfico y conclusión.** Cada curva $y = \dfrac{1}{C - x}$ es una hipérbola equilátera con asíntota vertical $x = C$ y asíntota horizontal $y = 0$:

- a la izquierda de $x = C$ es positiva y creciente;
- a la derecha de $x = C$ es negativa y creciente.

La solución $y = 0$ es justamente la asíntota horizontal común de todas las curvas. Por cada punto $(x_0, y_0)$ con $y_0 \ne 0$ pasa exactamente una curva de la familia ($C = x_0 + 1/y_0$), y por los puntos del eje $x$ pasa sólo $y \equiv 0$.

</details>

**Respuesta:** Se comprueba. Sí existe otra solución: $y = 0$.

</details>

---

### 07) S.G. o S.P. de ecuaciones de variables separables

Halle, según corresponda, la S.G. o la S.P. de las siguientes ecuaciones diferenciales.

- a) $y' = (x^2 + 1)/(2 - y)$ con $y(-3) = 4$
- b) $x\,\dfrac{dy}{dx} - y = 2\,x^2\,y$
- c) $y' = 2\,x\,\sqrt{y - 1}$
- d) $x^2\,dy = (x^2 + 1)\,dx/(3y^2 + 1)$ con $y(1) = 2$
- e) $y' = \dfrac{x}{\sqrt{x^2 + 9}}$ con $y(4) = 2$
- f) $y' = x\,y + x - 2\,y - 2$ con $y(0) = 2$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

Todas son de **variables separables**: se juntan las $y$ con $dy$ y las $x$ con $dx$, se integra y, si hay condición inicial, se calcula la constante al final.

**a)** $y' = \dfrac{x^2+1}{2-y}$, $y(-3) = 4$.

*Separar e integrar:*

$$(2 - y)\,dy = (x^2 + 1)\,dx \ \Rightarrow\ 2y - \frac{y^2}{2} = \frac{x^3}{3} + x + C$$

*Ordenar:* multiplicamos por $-6$ y completamos cuadrados ($3y^2 - 12y = 3(y-2)^2 - 12$):

$$3y^2 - 12y + 2x^3 + 6x + 6C = 0 \ \Rightarrow\ 3(y-2)^2 + 2x^3 + 6x + K = 0$$

*Condición $y(-3) = 4$:* $3\cdot 4 + 2(-27) + 6(-3) + K = 0 \Rightarrow 12 - 54 - 18 + K = 0 \Rightarrow K = 60$.

**b)** $x\,y' - y = 2x^2y \Rightarrow x\,y' = y\,(1 + 2x^2)$.

- $y \equiv 0$ es solución.
- Para $y \ne 0$:

$$\frac{y'}{y} = \frac1x + 2x \ \Rightarrow\ \ln|y| = \ln|x| + x^2 + c \ \Rightarrow\ y = C\,x\,e^{x^2}$$

Con $C = 0$ se incluye $y = 0$.

**c)** $y' = 2x\sqrt{y - 1}$ (requiere $y \ge 1$).

- $y \equiv 1$ es solución: $0 = 2x\cdot 0$.
- Para $y > 1$:

$$\frac{dy}{\sqrt{y-1}} = 2x\,dx \ \Rightarrow\ 2\sqrt{y-1} = x^2 + C$$

La solución $y = 1$ no se obtiene de esta familia: es una **solución singular**.

**d)** $x^2\,dy = \dfrac{(x^2+1)\,dx}{3y^2+1}$, $y(1) = 2$.

*Separar:*

$$(3y^2 + 1)\,dy = \frac{x^2 + 1}{x^2}\,dx = \left(1 + x^{-2}\right)dx$$

*Integrar:*

$$y^3 + y = x - \frac{1}{x} + C$$

*Condición $y(1) = 2$:* $8 + 2 = 1 - 1 + C \Rightarrow C = 10$.

*Forma sin denominadores* (multiplicamos por $x$): $x\,y^3 + x\,y = x^2 - 1 + 10x \Rightarrow x\,y^3 + x\,y - x^2 - 10x + 1 = 0$.

**e)** $y' = \dfrac{x}{\sqrt{x^2+9}}$, $y(4) = 2$. Es integración directa con la sustitución $u = x^2 + 9$:

$$y = \int \frac{x}{\sqrt{x^2+9}}\,dx = \sqrt{x^2 + 9} + C$$

*Condición:* $2 = \sqrt{16 + 9} + C = 5 + C \Rightarrow C = -3$.

**f)** $y' = xy + x - 2y - 2$, $y(0) = 2$.

*Factorizar* (la clave para ver que es separable):

$$y' = x(y + 1) - 2(y + 1) = (x - 2)(y + 1)$$

- $y \equiv -1$ es solución, pero no cumple $y(0) = 2$.
- Para $y \ne -1$:

$$\frac{y'}{y+1} = x - 2 \ \Rightarrow\ \ln|y+1| = \frac{x^2}{2} - 2x + c \ \Rightarrow\ y = K\,e^{\frac{x^2}{2} - 2x} - 1$$

*Condición:* $2 = K\,e^0 - 1 \Rightarrow K = 3$.

</details>

**Respuesta:**

- a) S.P.: $3(y - 2)^2 + 2x^3 + 6x + 60 = 0$
- b) S.G.: $y = C\,x\,e^{x^2}$
- c) S.G.: $2\sqrt{y - 1} = x^2 + C$ (y además la S.S. $y = 1$)
- d) S.P.: $x\,y^3 + x\,y - x^2 - 10x + 1 = 0$
- e) S.P.: $y = -3 + \sqrt{x^2 + 9}$
- f) S.P.: $y = 3\,\exp\!\left[\tfrac12 x^2 - 2x\right] - 1$

</details>

---

### 08) Curvas con pendiente $x/y$

Halle la familia de curvas tales que en cada punto $(x, y)$ tienen pendiente $x / y$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Traducir a EDO.** La pendiente de la recta tangente es $y'$, así que $y' = \dfrac{x}{y}$.

**Paso 2 — Separar e integrar.**

$$y\,dy = x\,dx \ \Rightarrow\ \frac{y^2}{2} = \frac{x^2}{2} + c \ \Rightarrow\ y^2 - x^2 = C$$

Es una familia de hipérbolas equiláteras. Con $C = 0$ se obtienen las rectas $y = \pm x$, y siempre $y \ne 0$.

</details>

**Respuesta:** $y^2 - x^2 = C$.

</details>

---

### 09) Pendiente igual al producto de las coordenadas

Sea $\Im$ la familia de curvas tales que en cada punto tienen pendiente igual al producto de las coordenadas del punto, halle la curva de $\Im$ que pasa por $(0, -2)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — EDO.** $y' = x\,y$.

**Paso 2 — Resolver.** Es separable. $y \equiv 0$ es solución y, para $y \ne 0$:

$$\frac{y'}{y} = x \ \Rightarrow\ \ln|y| = \frac{x^2}{2} + c \ \Rightarrow\ y = K\,e^{x^2/2}$$

**Paso 3 — Condición $(0, -2)$.** $-2 = K\,e^0 \Rightarrow K = -2$.

</details>

**Respuesta:** $y = -2\,e^{x^2/2}$.

</details>

---

### 10) Condiciones sobre la recta tangente

Halle la familia de curvas tales que su recta tangente en cada punto ...

- a) ... pasa por $(0,0)$
- b) ... es horizontal.
- c) ... tiene ordenada al origen igual a la suma de las coordenadas del punto.
- d) ... tiene abscisa al origen igual al triple de la abscisa del punto.
- e) ... es normal a la recta que pasa por dicho punto y el origen de coordenadas.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Planteo común.** En un punto genérico $(x, y)$ de la curva, la recta tangente (con coordenadas corrientes $X, Y$) es:

$$Y - y = y'\,(X - x)$$

- **Ordenada al origen** (cuando $X = 0$): $Y_0 = y - x\,y'$.
- **Abscisa al origen** (cuando $Y = 0$): $X_0 = x - \dfrac{y}{y'}$.

**a)** Que la tangente pase por $(0,0)$ significa que $(X, Y) = (0, 0)$ verifica la ecuación: $0 - y = y'(0 - x) \Rightarrow y = x\,y'$.

$$\frac{y'}{y} = \frac{1}{x} \ \Rightarrow\ \ln|y| = \ln|x| + c \ \Rightarrow\ y = C\,x$$

Son rectas por el origen. Hay que excluir $x = 0$, porque ahí dividimos.

**b)** Tangente horizontal en todo punto ⇒ $y' = 0$ ⇒ $y = C$.

**c)** Ordenada al origen igual a $x + y$:

$$y - x\,y' = x + y \ \Rightarrow\ -x\,y' = x \ \Rightarrow\ y' = -1 \quad (x \ne 0) \ \Rightarrow\ y = -x + C$$

**d)** Abscisa al origen igual a $3x$:

$$x - \frac{y}{y'} = 3x \ \Rightarrow\ -\frac{y}{y'} = 2x \ \Rightarrow\ \frac{y'}{y} = -\frac{1}{2x}$$

$$\ln|y| = -\tfrac12\ln|x| + c \ \Rightarrow\ y^2 = \frac{K}{|x|} \ \Rightarrow\ x\,y^2 = C$$

**e)** La recta que une el punto con el origen tiene pendiente $\dfrac{y}{x}$. Para que la tangente sea perpendicular a ella:

$$y' = -\frac{1}{y/x} = -\frac{x}{y} \ \Rightarrow\ y\,dy = -x\,dx \ \Rightarrow\ x^2 + y^2 = C, \ \ C > 0$$

Son circunferencias centradas en el origen: la tangente a una circunferencia es perpendicular al radio.

</details>

**Respuesta:**

- a) $y = C\,x$ (no incluye $x = 0$)
- b) $y = C$
- c) $y = -x + C$ (no incluye $x = 0$)
- d) $x\,y^2 = C$
- e) $x^2 + y^2 = C$ con $C > 0$

</details>

---

### 11) Normal tangente a la parábola $y = kx^2$

Sea $\Im$ la familia de curvas tales que su recta normal en cada punto es tangente a la parábola de ecuación $y = k\,x^2$ que pasa por dicho punto. Halle la curva $C \in \Im$ que pasa por $(0,1)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Pendiente de la parábola que pasa por $(x, y)$.** Como $y = kx^2$, el parámetro de esa parábola es $k = \dfrac{y}{x^2}$. Su pendiente en el punto es:

$$m_{\text{par}} = 2kx = 2\,\frac{y}{x^2}\,x = \frac{2y}{x}$$

**Paso 2 — Pendiente de la normal a la curva buscada.** Si la curva tiene pendiente $y'$, su normal tiene pendiente $-\dfrac{1}{y'}$.

**Paso 3 — Condición: la normal es tangente a la parábola**, o sea, tienen la misma pendiente:

$$-\frac{1}{y'} = \frac{2y}{x} \ \Rightarrow\ y' = -\frac{x}{2y}$$

Es decir, la curva buscada es **ortogonal** a las parábolas $y = kx^2$.

**Paso 4 — Resolver.**

$$2y\,dy = -x\,dx \ \Rightarrow\ y^2 = -\frac{x^2}{2} + c \ \Rightarrow\ x^2 + 2y^2 = C$$

**Paso 5 — Punto $(0,1)$.** $0 + 2 = C \Rightarrow C = 2$.

</details>

**Respuesta:** $x^2 + 2\,y^2 = 2$ (una elipse).

</details>

---

### 12) Normal con ordenada al origen 5

Halle las curvas que en cada punto tienen recta normal con ordenada al origen igual a 5.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Recta normal en $(x, y)$.**

$$Y - y = -\frac{1}{y'}\,(X - x)$$

**Paso 2 — Ordenada al origen** ($X = 0$): $\ Y_0 = y + \dfrac{x}{y'}$.

**Paso 3 — Condición $Y_0 = 5$:**

$$y + \frac{x}{y'} = 5 \ \Rightarrow\ \frac{x}{y'} = 5 - y \ \Rightarrow\ (5 - y)\,y' = x$$

**Paso 4 — Resolver (separable).**

$$\int (5 - y)\,dy = \int x\,dx \ \Rightarrow\ 5y - \frac{y^2}{2} = \frac{x^2}{2} + c$$

Multiplicamos por 2 y completamos cuadrados:

$$x^2 + y^2 - 10y = c' \ \Rightarrow\ x^2 + (y - 5)^2 = C$$

**Interpretación:** son circunferencias de centro $(0, 5)$. Toda normal a una circunferencia pasa por su centro, que es $(0,5)$, y por eso la ordenada al origen de la normal es siempre 5.

</details>

**Respuesta:** $x^2 + (y - 5)^2 = C$ con $C > 0$.

</details>

---

### 13) Ecuaciones lineales de 1.er orden

Resuelva las siguientes ecuaciones diferenciales lineales de 1° orden.

- a) $x\,y' - y - x^3 = 0$
- b) $y' + y\,\cos(x) = \operatorname{sen}(x)\cos(x)$
- c) $(x^2 + 4)\,y' - 3\,x\,y = x$, halle la S.P. tal que $y(0) = 1$
- d) $\dfrac{dy}{dx} - 2\,\dfrac{y}{x} = x^2\,\operatorname{sen}(3x)$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Método (variación de parámetros):**

1. Resolver la homogénea: $y_H = C\,\varphi(x)$.
2. Proponer $y_P = K(x)\,\varphi(x)$. Al reemplazar, los términos con $K$ se cancelan y queda $K'(x)\,\varphi(x) = $ (término independiente en forma normal).
3. $y = y_H + y_P$.

**a)** $x\,y' - y = x^3$. En forma normal: $y' - \dfrac{y}{x} = x^2$.

- *Homogénea:* $\dfrac{y'}{y} = \dfrac{1}{x} \Rightarrow y_H = C\,x$, así que $\varphi = x$.
- *Variación:* $K'(x)\cdot x = x^2 \Rightarrow K' = x \Rightarrow K = \dfrac{x^2}{2}$ ⇒ $y_P = \dfrac{x^3}{2}$.
- *S.G.:* $y = C\,x + \dfrac{x^3}{2}$.

**b)** $y' + \cos(x)\,y = \operatorname{sen}(x)\cos(x)$.

- *Homogénea:* $\dfrac{y'}{y} = -\cos x \Rightarrow y_H = C\,e^{-\operatorname{sen}x}$.
- *Variación:* $K'\,e^{-\operatorname{sen}x} = \operatorname{sen}x\cos x \Rightarrow K' = \operatorname{sen}x\,\cos x\,e^{\operatorname{sen}x}$.
- Con $u = \operatorname{sen}x$, $du = \cos x\,dx$, e integrando por partes:

$$K = \int u\,e^u\,du = (u - 1)\,e^u = (\operatorname{sen}x - 1)\,e^{\operatorname{sen}x}$$

- $y_P = K\,e^{-\operatorname{sen}x} = \operatorname{sen}x - 1$.
- *S.G.:* $y = -1 + \operatorname{sen}(x) + C\,e^{-\operatorname{sen}(x)}$.

**c)** $(x^2 + 4)\,y' - 3x\,y = x$, $y(0) = 1$. En forma normal:

$$y' - \frac{3x}{x^2+4}\,y = \frac{x}{x^2+4}$$

- *Homogénea:* $\dfrac{y'}{y} = \dfrac{3x}{x^2+4} \Rightarrow \ln|y| = \dfrac32\ln(x^2+4) + c \Rightarrow y_H = C\,(x^2+4)^{3/2}$.
- *Variación:* $K'\,(x^2+4)^{3/2} = \dfrac{x}{x^2+4} \Rightarrow K' = x\,(x^2+4)^{-5/2}$.
- Integrando con $u = x^2 + 4$:

$$K = \frac12\cdot\frac{(x^2+4)^{-3/2}}{-3/2} = -\frac{1}{3}(x^2+4)^{-3/2}$$

- $y_P = -\dfrac{1}{3}$. Se puede verificar: si $y = -\frac13$, $y' = 0$ y $-3x\left(-\frac13\right) = x$ ✓.
- *S.G.:* $y = C\,(x^2+4)^{3/2} - \dfrac13$.
- *Condición $y(0) = 1$:* $C\cdot 4^{3/2} - \dfrac13 = 1 \Rightarrow 8C = \dfrac43 \Rightarrow C = \dfrac16$.
- *S.P.:* $y = \dfrac{(x^2+4)^{3/2}}{6} - \dfrac13 \ \Rightarrow\ 6y = (x^2+4)^{3/2} - 2$.

**d)** $y' - \dfrac{2}{x}\,y = x^2\operatorname{sen}(3x)$.

- *Homogénea:* $\dfrac{y'}{y} = \dfrac{2}{x} \Rightarrow y_H = C\,x^2$.
- *Variación:* $K'\,x^2 = x^2\operatorname{sen}(3x) \Rightarrow K' = \operatorname{sen}(3x) \Rightarrow K = -\dfrac{\cos(3x)}{3}$.
- *S.G.:* $y = C\,x^2 - \dfrac{x^2\cos(3x)}{3} \ \Rightarrow\ 3y = x^2\big(C' - \cos(3x)\big)$.

</details>

**Respuesta:**

- a) $y = C\,x + x^3/2$
- b) $y = -1 + \operatorname{sen}(x) + C\,e^{-\operatorname{sen}(x)}$
- c) $6\,y = (x^2 + 4)^{3/2} - 2$
- d) $3\,y = x^2\big(C - \cos(3x)\big)$

</details>

---

### 14) Lineal y separable a la vez

La ecuación diferencial $y' + 2\,x\,y = 6\,x$ puede resolverse como lineal de 1º orden o bien como de variables separables, verifique que por ambos métodos de resolución se obtiene la misma solución general (o formas equivalentes).

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Método 1 — Variables separables.** Factorizamos: $y' = 6x - 2xy = 2x\,(3 - y)$.

- $y \equiv 3$ es solución.
- Para $y \ne 3$:

$$\frac{y'}{3 - y} = 2x \ \Rightarrow\ -\ln|3 - y| = x^2 + c \ \Rightarrow\ 3 - y = K\,e^{-x^2}$$

- Entonces $y = 3 - K\,e^{-x^2} = 3 + C\,e^{-x^2}$, y con $C = 0$ se incluye $y = 3$.

**Método 2 — Lineal.**

- *Homogénea:* $y' = -2xy \Rightarrow y_H = C\,e^{-x^2}$.
- *Variación:* $K'\,e^{-x^2} = 6x \Rightarrow K' = 6x\,e^{x^2} \Rightarrow K = 3\,e^{x^2} \Rightarrow y_P = 3$.
- *S.G.:* $y = 3 + C\,e^{-x^2}$.

Ambos métodos dan la misma S.G. ✓

</details>

**Respuesta:** Se verifica. La S.G. es $y = 3 + C\,e^{-x^2}$.

</details>

---

### 15) Curva integral por $(\pi/2, 1)$

Halle la curva integral de $y' + y/(x + 1) = \operatorname{sen}(x)$ que pasa por el punto $(\pi/2, 1)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

Es **lineal** con $P(x) = \dfrac{1}{x+1}$ y $Q(x) = \operatorname{sen}x$. El punto singular es $x = -1$; trabajamos en $x > -1$, que contiene a $\pi/2$.

**Paso 1 — Homogénea.**

$$\frac{y'}{y} = -\frac{1}{x+1} \ \Rightarrow\ \ln|y| = -\ln|x+1| + c \ \Rightarrow\ y_H = \frac{C}{x+1}$$

**Paso 2 — Variación.** $y_P = \dfrac{K(x)}{x+1}$ ⇒ $\dfrac{K'}{x+1} = \operatorname{sen}x \Rightarrow K' = (x+1)\operatorname{sen}x$.

Integramos por partes con $u = x + 1$ y $dv = \operatorname{sen}x\,dx$:

$$K = -(x+1)\cos x + \int\cos x\,dx = -(x+1)\cos x + \operatorname{sen}x$$

**Paso 3 — S.G.**

$$y = \frac{C - (x+1)\cos x + \operatorname{sen}x}{x+1} = \frac{C + \operatorname{sen}x}{x+1} - \cos x$$

**Paso 4 — Condición $y(\pi/2) = 1$.** Como $\cos(\pi/2) = 0$ y $\operatorname{sen}(\pi/2) = 1$:

$$1 = \frac{C + 1}{\pi/2 + 1} \ \Rightarrow\ C = \frac{\pi}{2}$$

</details>

**Respuesta:** $y = \dfrac{\pi/2 + \operatorname{sen}(x)}{x + 1} - \cos(x)$.

</details>

---

### 16) Problema de valor inicial

Resuelva el problema de valor inicial $y' + y = 2\operatorname{sen}(x)$ tal que $y(0) = 1$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Homogénea.** $y' = -y \Rightarrow y_H = C\,e^{-x}$.

**Paso 2 — Variación.** $K'\,e^{-x} = 2\operatorname{sen}x \Rightarrow K' = 2\,e^{x}\operatorname{sen}x$.

La integral $\int e^x\operatorname{sen}x\,dx$ se resuelve integrando por partes dos veces; la integral original reaparece y se despeja:

$$\int e^x\operatorname{sen}x\,dx = \frac{e^x(\operatorname{sen}x - \cos x)}{2}$$

Así que $K = e^x(\operatorname{sen}x - \cos x)$ y $y_P = K\,e^{-x} = \operatorname{sen}x - \cos x$.

**Paso 3 — S.G.** $y = \operatorname{sen}x - \cos x + C\,e^{-x}$.

**Paso 4 — Condición $y(0) = 1$.** $0 - 1 + C = 1 \Rightarrow C = 2$.

</details>

**Respuesta:** $y = \operatorname{sen}(x) - \cos(x) + 2\,e^{-x}$.

</details>

---

### 17) Movimiento rectilíneo

Determine la posición $x$ en función del tiempo $t$ de un punto que se desplaza sobre una recta si ...

- a) ... su velocidad $v \doteq x'$ es constante (movimiento rectilíneo uniforme), siendo $x(0) = x_o$.
- b) ... su aceleración $a \doteq v' = x''$ es constante (movimiento rectilíneo uniformemente acelerado), siendo $x(0) = x_o$ y $x'(0) = v_o$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** EDO: $x'(t) = v$, con $v$ constante. Integrando, $x(t) = v\,t + C$. Con $x(0) = x_o$ ⇒ $C = x_o$.

**b)** EDO: $x''(t) = a$, con $a$ constante. Es de orden 2 ⇒ se integra dos veces y aparecen 2 constantes.

- Primera integración: $x'(t) = a\,t + C_1$. Con $x'(0) = v_o$ ⇒ $C_1 = v_o$.
- Segunda integración: $x(t) = \dfrac12 a\,t^2 + v_o\,t + C_2$. Con $x(0) = x_o$ ⇒ $C_2 = x_o$.

</details>

**Respuesta:**

- a) $x = x_o + v\,t$
- b) $x = x_o + v_o\,t + \frac12\,a\,t^2$

</details>

---

### 18) Ley de enfriamiento de Newton

Sea un cuerpo cuya temperatura $T$ es mayor que la temperatura $T_A$ del ambiente que lo rodea, si $T_A$ se mantiene constante la temperatura del cuerpo disminuye con una velocidad ($dT / dt$) que es proporcional a la diferencia $T - T_A$. Es decir, $dT / dt = -k\,(T - T_A)$ donde $k$ es una constante positiva y $t$ es el tiempo.<sup>(#)</sup>

Suponga que en el instante inicial $t = 0$ la temperatura del cuerpo es $T_0 > T_A$, …

- a) … halle la expresión de la temperatura del cuerpo para $t \ge 0$.
- b) … demuestre que a medida que transcurre el tiempo ($t \to \infty$) la temperatura del cuerpo tiende a la del ambiente.
- c) … calcule el valor de $k$ sabiendo que en 30 minutos y con una temperatura ambiente de 0 ºC la temperatura del cuerpo disminuyó a la mitad de su valor inicial.

<sup>(#)</sup> Ley de enfriamiento de Newton.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** La EDO $\dfrac{dT}{dt} = -k\,(T - T_A)$ es de variables separables. Como $T > T_A$, podemos dividir por $T - T_A$:

$$\frac{dT}{T - T_A} = -k\,dt \ \Rightarrow\ \ln(T - T_A) = -k\,t + c \ \Rightarrow\ T - T_A = A\,e^{-kt}$$

Condición inicial: en $t = 0$, $T_0 - T_A = A$. Por lo tanto:

$$T(t) = T_A + (T_0 - T_A)\,e^{-kt}$$

**b)** Como $k > 0$, $e^{-kt} \xrightarrow[t\to\infty]{} 0$, y entonces:

$$\lim_{t\to\infty} T(t) = T_A + (T_0 - T_A)\cdot 0 = T_A$$

**c)** *Fórmula:* con $T_A = 0$ queda $T(t) = T_0\,e^{-kt}$. La condición $T(t_1) = \dfrac{T_0}{2}$ da:

$$T_0\,e^{-k t_1} = \frac{T_0}{2} \ \Rightarrow\ e^{-k t_1} = \frac12 \ \Rightarrow\ k = \frac{\ln 2}{t_1}$$

*Cálculo:* con $t_1 = 30\ \text{min} = \frac12\ \text{hora}$:

$$k = \frac{\ln 2}{1/2\ \text{h}} = 2\ln 2\ \text{h}^{-1} \approx 1{,}386\ \text{h}^{-1} \quad\left(= \frac{\ln 2}{30}\ \text{min}^{-1} \approx 0{,}0231\ \text{min}^{-1}\right)$$

</details>

**Respuesta:**

- a) $T = T_A + (T_0 - T_A)\,e^{-kt}$
- b) Con $k > 0$: $T \xrightarrow[t\to\infty]{} T_A$
- c) $k = 2\ln(2)\ \text{hora}^{-1}$

</details>

---

### 19) Familias ortogonales: verificación

Verifique que las siguientes familias de curvas son ortogonales.

- a) $\begin{cases} x^2 + 4y^2 = C_1 \\ y = C_2\,x^4 \end{cases}$
- b) $\begin{cases} x^2 - y^2 + \ln(\cos(2\,x\,y)) = C_1 \\ x^2 - y^2 + \ln(\operatorname{sen}(2\,x\,y)) = C_2 \end{cases}$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Criterio:** dos familias son ortogonales si en cada punto de intersección sus pendientes cumplen $y'_1\cdot y'_2 = -1$. Para esto, hallamos la EDO de cada familia, eliminando la constante, y multiplicamos las pendientes. Esto equivale a la sugerencia de la guía: comprobar que se pasa de una EDO a la otra reemplazando $y'$ por $-1/y'$.

**a)**

- Familia 1: $2x + 8y\,y' = 0 \Rightarrow y'_1 = -\dfrac{x}{4y}$.
- Familia 2: $y' = 4C_2\,x^3$, y como $C_2 = \dfrac{y}{x^4}$, queda $y'_2 = \dfrac{4y}{x}$.
- Producto: $y'_1\cdot y'_2 = -\dfrac{x}{4y}\cdot\dfrac{4y}{x} = -1$ ✓

**b)** Llamamos $t = \tan(2xy)$. Usamos que $\dfrac{d}{dx}(2xy) = 2(y + x\,y')$.

*Familia 1:* derivando $x^2 - y^2 + \ln\cos(2xy) = C_1$:

$$2x - 2y\,y' - \tan(2xy)\cdot 2(y + x\,y') = 0 \ \Rightarrow\ x - y\,y' - t\,y - t\,x\,y' = 0$$

$$y'_1 = \frac{x - t\,y}{y + t\,x}$$

*Familia 2:* derivando $x^2 - y^2 + \ln\operatorname{sen}(2xy) = C_2$, con $\cot(2xy) = 1/t$:

$$x - y\,y' + \frac{1}{t}(y + x\,y') = 0 \ \xrightarrow{\ \times t\ }\ t\,x - t\,y\,y' + y + x\,y' = 0$$

$$y'_2 = -\frac{y + t\,x}{x - t\,y}$$

*Producto:*

$$y'_1\cdot y'_2 = \frac{x - ty}{y + tx}\cdot\left(-\frac{y + tx}{x - ty}\right) = -1 \ ✓$$

</details>

**Respuesta:** En ambos casos se verifica que el producto de las pendientes es $-1$: las familias son ortogonales.

</details>

---

### 20) Familia ortogonal a la dada

Halle la familia de curvas ortogonal a la dada.

- a) $y = 2x + C$
- b) $y = C\,e^x$
- c) $y\,(C\,x + 1) = x$
- d) $y = \ln(x + C)$
- e) $y = C\,\operatorname{sen}(2x)$
- f) $(x + y)^2 = k\,x^2$, $k > 0$

> **Fe de erratas (31/07/18):** en la respuesta del ítem 20-e dice $\ln|\cos(2x)| - y^2 = C$, **debe decir** $\ln|\cos(2x)| - 2y^2 = K$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Procedimiento:**

1. Hallar la EDO de la familia, eliminando el parámetro.
2. Reemplazar $y'$ por $-1/y'$.
3. Resolver.

**a)** $y = 2x + C \Rightarrow y' = 2$. Ortogonal: $-\dfrac{1}{y'} = 2 \Rightarrow y' = -\dfrac12 \Rightarrow y = -\dfrac12 x + K$.

**b)** $y = Ce^x \Rightarrow y' = Ce^x = y$. Ortogonal: $-\dfrac{1}{y'} = y \Rightarrow y\,y' = -1 \Rightarrow \dfrac{y^2}{2} = -x + c \Rightarrow 2x + y^2 = K$.

**c)** $y\,(Cx + 1) = x$.

- Despejamos $C$: $Cx + 1 = \dfrac{x}{y} \Rightarrow C = \dfrac{1}{y} - \dfrac{1}{x}$.
- Derivamos: $0 = -\dfrac{y'}{y^2} + \dfrac{1}{x^2} \Rightarrow y' = \dfrac{y^2}{x^2}$.
- Ortogonal: $-\dfrac{1}{y'} = \dfrac{y^2}{x^2} \Rightarrow y' = -\dfrac{x^2}{y^2} \Rightarrow y^2\,dy = -x^2\,dx \Rightarrow x^3 + y^3 = C$.

**d)** $y = \ln(x + C)$.

- Derivamos: $y' = \dfrac{1}{x + C}$. Como $x + C = e^y$, queda $y' = e^{-y}$.
- Ortogonal: $-\dfrac{1}{y'} = e^{-y} \Rightarrow y' = -e^{y} \Rightarrow e^{-y}\,dy = -dx$.
- Integramos: $-e^{-y} = -x - K \Rightarrow e^{-y} = x + K \Rightarrow y = -\ln(x + K)$.

**e)** $y = C\operatorname{sen}(2x)$.

- Derivamos: $y' = 2C\cos(2x)$. Como $C = \dfrac{y}{\operatorname{sen}(2x)}$, queda $y' = 2y\,\dfrac{\cos 2x}{\operatorname{sen}2x}$.
- Ortogonal: $-\dfrac{1}{y'} = 2y\,\dfrac{\cos 2x}{\operatorname{sen}2x} \Rightarrow y\,y' = -\dfrac{\operatorname{sen}(2x)}{2\cos(2x)}$.
- Integramos, usando $\int\tan(2x)\,dx = -\frac12\ln|\cos 2x|$:

$$\frac{y^2}{2} = \frac14\ln|\cos(2x)| + c \ \Rightarrow\ \ln|\cos(2x)| - 2y^2 = K$$

**f)** $(x + y)^2 = kx^2$, $k > 0$.

- Despejamos: $\dfrac{x + y}{x} = \pm\sqrt{k}$, es decir, $\dfrac{y}{x} = $ constante ⇒ son **rectas por el origen**, $y = m\,x$ (con $x \ne 0$).
- Su EDO: $y' = m = \dfrac{y}{x}$.
- Ortogonal: $-\dfrac{1}{y'} = \dfrac{y}{x} \Rightarrow y\,y' = -x \Rightarrow x^2 + y^2 = C$, con $C > 0$.

</details>

**Respuesta:**

- a) $y = -\frac12 x + K$
- b) $2x + y^2 = K$
- c) $x^3 + y^3 = C$
- d) $y = -\ln(x + K)$
- e) $\ln|\cos(2x)| - 2y^2 = K$
- f) $x^2 + y^2 = C$, $C > 0$

</details>

---

### 21) Valor de $a$ para que sean ortogonales

Determine $a$ de manera que las familias $y^3 = A\,x$ y $x^2 + a\,y^2 = B^2$ sean ortogonales.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — EDO de la familia 1.** $y^3 = Ax \Rightarrow 3y^2\,y' = A = \dfrac{y^3}{x} \Rightarrow y'_1 = \dfrac{y}{3x}$.

**Paso 2 — EDO de la familia 2.** $x^2 + a y^2 = B^2 \Rightarrow 2x + 2a\,y\,y' = 0 \Rightarrow y'_2 = -\dfrac{x}{a\,y}$.

**Paso 3 — Condición de ortogonalidad** $y'_1\,y'_2 = -1$ en todo punto de intersección:

$$\frac{y}{3x}\cdot\left(-\frac{x}{a\,y}\right) = -\frac{1}{3a} = -1 \ \Rightarrow\ a = \frac13$$

</details>

**Respuesta:** $a = 1/3$.

</details>

---

### 22) Longitud de una curva ortogonal

Sea la familia de curvas de ecuación $y = C\,x + C$, calcule la longitud de la curva de la familia ortogonal que pasa por (1,2).

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Identificar la familia.** $y = C\,(x + 1)$ son las rectas que pasan por $(-1, 0)$.

**Paso 2 — EDO.** $y' = C = \dfrac{y}{x + 1}$.

**Paso 3 — EDO de la ortogonal.** $-\dfrac{1}{y'} = \dfrac{y}{x+1} \Rightarrow y\,y' = -(x + 1)$.

**Paso 4 — Resolver.**

$$\int y\,dy = -\int (x+1)\,dx \ \Rightarrow\ \frac{y^2}{2} = -\frac{(x+1)^2}{2} + c \ \Rightarrow\ (x + 1)^2 + y^2 = R^2$$

Son circunferencias con centro $(-1, 0)$. Tiene sentido geométricamente: las rectas por un punto son ortogonales a las circunferencias centradas en ese punto.

**Paso 5 — La que pasa por $(1, 2)$.**

$$R^2 = (1 + 1)^2 + 2^2 = 8 \ \Rightarrow\ R = 2\sqrt2$$

**Paso 6 — Longitud.** Es una circunferencia completa: $L = 2\pi R$. Reemplazando:

$$L = 2\pi\cdot 2\sqrt2 = 4\pi\sqrt2 \approx 17{,}77$$

</details>

**Respuesta:** $L = 4\pi\sqrt{2}$.

</details>

---

### 23) Reducción de orden

Dada $x\,y'' - 2\,y' = 0$ halle la S.P./ $y(1) = y'(1) = 3$ aplicando la transformación $w = y'$.<sup>(#)</sup>

<sup>(#)</sup> Transformación de *reducción de orden*, útil cuando en la ecuación diferencial no figura la $y$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Sustitución.** Con $w = y'$, $w' = y''$, la ecuación queda $x\,w' - 2w = 0$, que es de **primer orden** en $w$.

**Paso 2 — Resolver para $w$** (separable):

$$\frac{w'}{w} = \frac{2}{x} \ \Rightarrow\ \ln|w| = 2\ln|x| + c \ \Rightarrow\ w = C_1\,x^2$$

**Paso 3 — Usar $y'(1) = 3$**, que es una condición sobre $w$: $w(1) = C_1 = 3$, así que $y' = 3x^2$.

**Paso 4 — Volver a $y$ integrando.** $y = x^3 + C_2$.

**Paso 5 — Usar $y(1) = 3$.** $1 + C_2 = 3 \Rightarrow C_2 = 2$.

</details>

**Respuesta:** $y = x^3 + 2$.

</details>

---

### 24) S.G. de $y'' - 2y' = x$

Halle la S.G. de $y'' - 2\,y' = x$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Reducción de orden.** No aparece $y$ ⇒ $w = y'$, y queda $w' - 2w = x$ (lineal de 1.er orden).

**Paso 2 — Homogénea.** $w' = 2w \Rightarrow w_H = A\,e^{2x}$.

**Paso 3 — Variación de parámetros.** $w_P = K(x)\,e^{2x}$ ⇒ $K'\,e^{2x} = x \Rightarrow K' = x\,e^{-2x}$. Integrando por partes con $u = x$ y $dv = e^{-2x}dx$:

$$K = -\frac{x}{2}e^{-2x} - \frac14e^{-2x}$$

Por lo tanto $w_P = -\dfrac{x}{2} - \dfrac14$, y $w = A\,e^{2x} - \dfrac{x}{2} - \dfrac14$.

**Paso 4 — Volver a $y$** ($y' = w$) integrando:

$$y = \frac{A}{2}e^{2x} - \frac{x^2}{4} - \frac{x}{4} + B$$

Renombrando las constantes ($A/2 \to B$, $B \to A$):

$$y = A + B\,e^{2x} - \frac{x + x^2}{4}$$

</details>

**Respuesta:** $y = A + B\,e^{2x} - (x + x^2)/4$.

</details>

---

### 25) S.G. de $y''' - y'' = x$

Halle la S.G. de $y''' - y'' = x$.

> **Fe de erratas (31/07/18):** en el ítem 25 la EDO dice $y''' - y'' = x$, **debe decir** $y''' - y'' = 0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

No aparecen ni $y$ ni $y'$ ⇒ usamos $w = y''$, con $w' = y'''$. Se resuelven las dos versiones.

**Versión corregida: $y''' - y'' = 0$**

- $w' - w = 0 \Rightarrow w = C_1\,e^x$.
- $y' = \int w = C_1 e^x + C_2$.
- $y = C_1 e^x + C_2 x + C_3$.

**Versión original: $y''' - y'' = x$** (es la que está resuelta a mano en [TP01-Resuelto-Ej25.pdf](../aula-virtual/01-Ecuaciones-Diferenciales-1/TP01-Resuelto-Ej25.pdf))

- Queda $w' - w = x$, que es lineal.
- *Homogénea:* $w_H = A\,e^x$.
- *Variación:* $w_P = A(x)\,e^x \Rightarrow A'\,e^x = x \Rightarrow A' = x\,e^{-x}$. Por partes, $A = -e^{-x}(x + 1)$, así que $w_P = -x - 1$.
- $y'' = w = A\,e^x - x - 1$.
- Primera integración: $y' = A\,e^x - \dfrac{x^2}{2} - x + B$.
- Segunda integración: $y = A\,e^x - \dfrac{x^3}{6} - \dfrac{x^2}{2} + B\,x + C$.

</details>

**Respuesta:**

- Con la corrección ($y''' - y'' = 0$): $y = C_1\,e^x + C_2\,x + C_3$.
- Con el enunciado original ($= x$): $y = A\,e^x - \dfrac{x^3}{6} - \dfrac{x^2}{2} + Bx + C$.

</details>

---

### 26) Relación entre dos EDO

Si $y_p$ es S.P. que pasa por (2,3) de $x^2\,y'' - 2\,y = f(x)$, verifique que $y = x\,y_p$ es S.P. de la ecuación diferencial $x\,y'' - 2\,y' = f(x)$ que pasa por (2,$y_0$). Halle $y_0$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Derivar $y = x\,y_p$** con la regla del producto:

$$y' = y_p + x\,y_p', \qquad y'' = y_p' + y_p' + x\,y_p'' = 2y_p' + x\,y_p''$$

**Paso 2 — Reemplazar en $x\,y'' - 2y'$:**

$$x\,(2y_p' + x\,y_p'') - 2\,(y_p + x\,y_p') = 2x\,y_p' + x^2y_p'' - 2y_p - 2x\,y_p' = x^2\,y_p'' - 2\,y_p$$

**Paso 3 — Usar la hipótesis.** Como $y_p$ verifica $x^2y_p'' - 2y_p = f(x)$, queda $x\,y'' - 2y' = f(x)$ ✓.

**Paso 4 — Valor en $x = 2$.** $y(2) = 2\cdot y_p(2) = 2\cdot 3 = 6$.

</details>

**Respuesta:** Se verifica, y $y_0 = 6$.

</details>

---

### 27) Máximo absoluto de la S.P.

Sea $y = f(x)$ la S.P. de $x\,(x + y') = y$ que pasa por $(a,0)$ con $a > 0$, demuestre que $f$ produce un máximo absoluto en el intervalo $[0,a]$; ¿cuál es el valor de dicho máximo?.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Escribir como lineal.** $x^2 + x\,y' = y \Rightarrow y' - \dfrac{y}{x} = -x$.

**Paso 2 — Homogénea.** $\dfrac{y'}{y} = \dfrac1x \Rightarrow y_H = C\,x$.

**Paso 3 — Variación.** $K'\,x = -x \Rightarrow K = -x \Rightarrow y_P = -x^2$.

**Paso 4 — S.G.** $y = C\,x - x^2$.

**Paso 5 — Condición $(a, 0)$.** $0 = C\,a - a^2 \Rightarrow C = a$, ya que $a \ne 0$. Entonces $f(x) = a\,x - x^2 = x\,(a - x)$.

**Paso 6 — Máximo en $[0, a]$.**

- $f$ es continua en el intervalo cerrado $[0,a]$ ⇒ por el teorema de Weierstrass **alcanza un máximo absoluto**.
- Puntos críticos: $f'(x) = a - 2x = 0 \Rightarrow x = \dfrac{a}{2} \in [0, a]$, y $f''(x) = -2 < 0$ ⇒ es un máximo.
- Comparamos con los extremos del intervalo: $f(0) = f(a) = 0$.
- Valor en el punto crítico: $f\!\left(\tfrac a2\right) = \tfrac a2\left(a - \tfrac a2\right)$.

$$f_{\max} = f\!\left(\frac a2\right) = \frac{a^2}{4}$$

</details>

**Respuesta:** El máximo absoluto se alcanza en $x = a/2$ y vale $a^2/4$.

</details>

---

### 28) Existencia y unicidad

Dada la ecuación diferencial $(x^2 - 1)\,y' + x\,y\,(1 - y) = 0$, …

- a) … halle su solución general.
- b) … verifique que existe sólo una solución que pasa por el punto $(3, 2)$.
- c) … verifique que por los puntos $(-1,1)$ y $(1,1)$ pasan infinitas soluciones.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** Reordenamos: $(x^2 - 1)\,y' = x\,y\,(y - 1)$.

- **Puntos singulares:** $x = \pm 1$, donde se anula el coeficiente de $y'$.
- **Soluciones constantes:** $y \equiv 0$ e $y \equiv 1$ (ambas anulan el segundo miembro).
- Para $y \ne 0, 1$ y $x \ne \pm1$ separamos variables:

$$\frac{dy}{y\,(y - 1)} = \frac{x\,dx}{x^2 - 1}$$

*Fracciones simples:* $\dfrac{1}{y(y-1)} = \dfrac{1}{y - 1} - \dfrac{1}{y}$. Integrando:

$$\ln\left|\frac{y-1}{y}\right| = \frac12\ln|x^2 - 1| + c \ \Rightarrow\ \left(\frac{y-1}{y}\right)^2 = C\,(x^2 - 1)$$

$$\boxed{(y - 1)^2 = C\,y^2\,(x^2 - 1)}$$

La solución $y = 1$ corresponde a $C = 0$. La solución $y = 0$ no está incluida: es singular.

**b)** *Constante:* en $(3,2)$, $(2-1)^2 = C\cdot 4\cdot(9 - 1) \Rightarrow 1 = 32C \Rightarrow C = \dfrac{1}{32}$. Hay un **único** valor de $C$:

$$y^2\,(x^2 - 1) = 32\,(y - 1)^2$$

*Justificación teórica:* escribiendo $y' = F(x,y) = \dfrac{x\,y\,(y - 1)}{x^2 - 1}$, tanto $F$ como $\dfrac{\partial F}{\partial y} = \dfrac{x\,(2y - 1)}{x^2 - 1}$ son continuas cerca de $(3, 2)$ (porque $x^2 - 1 \ne 0$). El teorema de existencia y unicidad garantiza entonces una única solución.

**c)** En $(\pm 1, 1)$, reemplazando en la S.G.:

$$(1 - 1)^2 = C\cdot 1^2\cdot\big((\pm1)^2 - 1\big) \ \Rightarrow\ 0 = C\cdot 0$$

Esto se cumple **para todo $C$**. Por lo tanto, todas las curvas de la familia pasan por esos dos puntos: hay infinitas soluciones. No contradice el teorema, porque $x = \pm 1$ son puntos singulares, donde $F$ no es continua.

</details>

**Respuesta:**

- a) $(y - 1)^2 = C\,y^2\,(x^2 - 1)$
- b) Se verifica: es $y^2\,(x^2 - 1) = 32\,(y - 1)^2$.
- c) Se verifica.

</details>

---

### 29) Hallar $\beta(x)$ a partir de una solución conocida

Se sabe que $y = x^3 - x$ es una solución de la ecuación diferencial $y' + \beta(x)\,y = 2\,x^2$, halle la solución de dicha ecuación que verifica $y(1) = 4$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Hallar $\beta(x)$.** Reemplazamos la solución conocida $y = x^3 - x$ (con $y' = 3x^2 - 1$) en la ecuación:

$$3x^2 - 1 + \beta(x)\,(x^3 - x) = 2x^2 \ \Rightarrow\ \beta(x) = \frac{1 - x^2}{x\,(x^2 - 1)} = -\frac{1}{x}$$

**Paso 2 — Ecuación completa.** $y' - \dfrac{y}{x} = 2x^2$.

**Paso 3 — Homogénea.** $y_H = C\,x$.

**Paso 4 — Solución particular.** Ya tenemos una: $y_P = x^3 - x$. Así, $y = Cx + x^3 - x$, que reordenando queda $y = x^3 + C'x$. Se obtiene lo mismo por variación de parámetros: $K'x = 2x^2 \Rightarrow K = x^2 \Rightarrow y_P = x^3$.

**Paso 5 — Condición $y(1) = 4$.** $1 + C' = 4 \Rightarrow C' = 3$.

</details>

**Respuesta:** $y = x^3 + 3x$.

</details>

---

### 30) *Optativo*

*Optativo*: Halle las soluciones de $x^2\,(y')^2 - y^2 = 0$ que pasan por (1,1).

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Factorizar** como diferencia de cuadrados, $a^2 - b^2 = (a - b)(a + b)$:

$$(x\,y' - y)\,(x\,y' + y) = 0$$

Hay entonces dos EDO de primer grado.

**Paso 2 — Caso $x\,y' = y$.** $\dfrac{y'}{y} = \dfrac1x \Rightarrow y = C\,x$. Por $(1,1)$: $C = 1 \Rightarrow y = x$.

**Paso 3 — Caso $x\,y' = -y$.** $\dfrac{y'}{y} = -\dfrac1x \Rightarrow y = \dfrac{C}{x}$. Por $(1,1)$: $C = 1 \Rightarrow y = \dfrac{1}{x}$.

</details>

**Respuesta:** $y = x$ e $y = x^{-1}$.

</details>

---

### 31) *Optativo*

*Optativo*: Halle la solución general que se indica en el ítem "02) c)".

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

Hay que resolver $y\,y'^2 + y^2\,y'' = 0$.

**Paso 1 — Sacar factor común $y$.**

$$y\,\big(y'^2 + y\,y''\big) = 0$$

O bien $y \equiv 0$, o bien $y'^2 + y\,y'' = 0$.

**Paso 2 — Reconocer una derivada** (sugerencia de la guía):

$$(y\,y')' = y'\,y' + y\,y'' = y'^2 + y\,y''$$

Así que la ecuación es $(y\,y')' = 0$.

**Paso 3 — Integrar dos veces.**

$$y\,y' = A \ \Rightarrow\ \frac{y^2}{2} = A\,x + B \ \Rightarrow\ y^2 = C_1\,x + C_2$$

con $C_1 = 2A$ y $C_2 = 2B$. La solución $y \equiv 0$ queda incluida con $C_1 = C_2 = 0$.

</details>

**Respuesta:** $y^2 = C_1\,x + C_2$.

</details>

---

[← Volver al menú principal](../README.md)
