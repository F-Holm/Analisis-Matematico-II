# Unidad 12 — Ecuaciones diferenciales (2.ª parte)

Resumen del material teórico de la unidad ([U12-Teoria-Ecuaciones-Diferenciales-2.pdf](../aula-virtual/12-Ecuaciones-Diferenciales-2/U12-Teoria-Ecuaciones-Diferenciales-2.pdf)), de las [notas de clase sobre líneas de campo](../aula-virtual/12-Ecuaciones-Diferenciales-2/Notas-2021-10-26-Lineas-de-Campo.pdf), del [método de variación de parámetros anotado](../aula-virtual/12-Ecuaciones-Diferenciales-2/Metodo-Variacion-Parametros-Anotado.pdf) y de los pizarrones sobre ecuaciones homogéneas y exactas ([2024](../aula-virtual/01-Ecuaciones-Diferenciales-1/Pizarron-2024-10-22-EDO-Homogeneas-Exactas.pdf), [2021](../aula-virtual/01-Ecuaciones-Diferenciales-1/Notas-2021-10-26-EDO-Homogeneas-Exactas.pdf)), complementado con el [resumen de UTNianos](../UTNianos/Resumen%20AM2.pdf).

**Objetivos de la unidad:**

1. Resolver EDO homogéneas, totales exactas y reducibles a exactas mediante factores integrantes.
2. Hallar líneas de campo de un campo vectorial.
3. Resolver EDO lineales de orden $n$ a coeficientes constantes y sistemas de EDO lineales.

---

## 1. Ecuaciones homogéneas de primer orden

$f(x,y)$ es **homogénea de grado 0** si $f(tx, ty) = f(x,y)$. Entonces $f$ depende sólo de $y/x$.

La EDO $y' = f(x,y)$, con $f$ homogénea de grado 0, se resuelve con el cambio

$$z = \frac yx, \qquad y = zx, \qquad y' = z + x\thinspace z'$$

y queda **separable**: $\ x\thinspace z' = f(1,z) - z$.

- También vale escrito como $M\thinspace dx + N\thinspace dy = 0$ con $M$ y $N$ homogéneas del **mismo grado**.
- **Ecuaciones "casi homogéneas"**, como $y' = \dfrac{a_1x + b_1y + c_1}{a_2x + b_2y + c_2}$: se trasladan el origen al punto donde se cortan las rectas ($x = u + h$, $y = v + k$) y quedan homogéneas en $u$, $v$.

---

## 2. Ecuaciones diferenciales totales exactas

$M(x,y)\thinspace dx + N(x,y)\thinspace dy = 0$ es **exacta** si existe $U$ con $U'_x = M$ y $U'_y = N$. Es decir, $(M,N)$ es un campo de gradientes.

**Criterio** (en un dominio simplemente conexo, con $M, N \in C^1$):

$$\boxed{M'_y = N'_x}$$

**Solución general:** $U(x,y) = C$. Son las **líneas equipotenciales** del campo $(M, N)$.

**Cómo hallar $U$:** igual que la función potencial (Unidad 8). Se integra $M$ respecto de $x$, se deriva respecto de $y$, se iguala a $N$ y se despeja la función de $y$.

### Factor integrante

Si $M'_y \ne N'_x$, se busca $\mu \ne 0$ tal que $\mu M\thinspace dx + \mu N\thinspace dy = 0$ sea exacta. Hay dos casos útiles:

| Si … depende sólo de | Factor integrante |
|---|---|
| $\dfrac{M'_y - N'_x}{N}$ depende sólo de $x$ | $\mu(x) = e^{\int\frac{M'_y - N'_x}{N}dx}$ |
| $\dfrac{N'_x - M'_y}{M}$ depende sólo de $y$ | $\mu(y) = e^{\int\frac{N'_x - M'_y}{M}dy}$ |

> Al multiplicar por $\mu$ se pueden **perder o ganar soluciones**, donde $\mu$ se anula o no está definido. Hay que revisarlas aparte; suelen ser soluciones constantes como $y = 0$.

---

## 3. Líneas de campo

Las **líneas de campo** (o líneas de flujo) de $\vec f$ son las curvas que en cada punto son **tangentes al campo**. Si $\vec g(t)$ es una línea de campo, $\vec g'(t) = \lambda\thinspace\vec f(\vec g(t))$.

**En el plano**, con $\vec f = (P, Q)$:

$$\frac{dy}{dx} = \frac QP \qquad \text{o, en forma simétrica,} \qquad \frac{dx}{P} = \frac{dy}{Q}$$

**En el espacio:** $\dfrac{dx}{P} = \dfrac{dy}{Q} = \dfrac{dz}{R}$. Las líneas son intersecciones de dos familias de superficies.

**Planteo paramétrico:** $\vec g'(t) = \vec f(\vec g(t))$ es un **sistema de EDO** (ver la sección 6). Para campos lineales, $\vec f(\vec X) = A\vec X$, se resuelve con autovalores.

**Propiedades:**

- Las líneas se **orientan** según el sentido del campo.
- Si $\vec f = \nabla\phi$, las líneas de campo son **ortogonales a las equipotenciales** $\phi = C$ (en $\mathbb{R}^3$, a las superficies equipotenciales).
- La forma cartesiana de las líneas **no** determina el campo: campos distintos pueden tener las mismas líneas.

---

## 4. EDO lineales de orden $n$ a coeficientes constantes

$$a_n y^{(n)} + \dots + a_1 y' + a_0 y = f(x), \qquad y = y_H + y_P$$

### Solución de la homogénea: ecuación característica

Se reemplaza $y = e^{rx}$ y queda $a_nr^n + \dots + a_1r + a_0 = 0$.

| Raíces de la característica | Aporte a $y_H$ |
|---|---|
| Real simple $r$ | $C\thinspace e^{rx}$ |
| Real de multiplicidad $m$ | $(C_1 + C_2x + \dots + C_mx^{m-1})\thinspace e^{rx}$ |
| Complejas $\alpha \pm \beta i$ | $e^{\alpha x}(C_1\cos\beta x + C_2\mathop{\mathrm{sen}}\beta x)$ |

### Solución particular: coeficientes indeterminados

Se usa cuando $f$ es un polinomio, una exponencial, un seno/coseno, o productos y sumas de ellos:

| $f(x)$ | Se propone $y_P$ |
|---|---|
| Polinomio de grado $k$ | Polinomio completo de grado $k$ |
| $e^{ax}\cdot$ polinomio | $e^{ax}\cdot$ polinomio completo |
| $\mathop{\mathrm{sen}}(bx)$ o $\cos(bx)$ | $A\cos bx + B\mathop{\mathrm{sen}}bx$ |

> **Regla de resonancia:** si la propuesta (o parte de ella) ya es solución de la homogénea, se **multiplica por $x^m$**, con $m$ la multiplicidad de la raíz correspondiente. Por ejemplo, $f = 2x$ con raíz $r = 0$ ⇒ $y_P = x(Ax + B)$.

**Superposición:** si $f = f_1 + f_2$, entonces $y_P = y_{P_1} + y_{P_2}$.

### Solución particular: variación de parámetros

Sirve para **cualquier** $f$ continua, por ejemplo $\sec x$ o $e^x/x$. Para el orden 2, $y'' + p\thinspace y' + q\thinspace y = f$ (coeficiente principal 1):

- Con $y_H = C_1y_1 + C_2y_2$, se propone $y_P = C_1(x)y_1 + C_2(x)y_2$, imponiendo:

$$\begin{cases} C_1'y_1 + C_2'y_2 = 0 \cr C_1'y_1' + C_2'y_2' = f \end{cases}$$

- Resolviendo con el **wronskiano** $W = y_1y_2' - y_2y_1'$:

$$C_1' = -\frac{y_2\thinspace f}{W}, \qquad C_2' = \frac{y_1\thinspace f}{W}$$

### Problemas de valores iniciales

Primero se halla la S.G. completa ($y_H + y_P$) y **después** se imponen las condiciones $y(x_0)$, $y'(x_0)$, …

Las condiciones de "recta tangente" o "recta normal" en un punto dan $y(x_0)$ y $y'(x_0)$; la pendiente de la normal es $-1/y'$.

---

## 5. Aplicaciones: sistemas masa-resorte-amortiguador y circuitos RLC

$$M\thinspace x'' + d\thinspace x' + k\thinspace x = F \qquad\longleftrightarrow\qquad LC\thinspace v'' + RC\thinspace v' + v = E$$

Con la característica $Mr^2 + dr + k = 0$ (discriminante $\Delta = d^2 - 4Mk$):

| Caso | Comportamiento |
|---|---|
| $\Delta < 0$ (raíces complejas) | **oscilación amortiguada** (subamortiguado) |
| $\Delta = 0$ | amortiguamiento crítico |
| $\Delta > 0$ (dos raíces reales negativas) | sobreamortiguado: tiende al equilibrio **sin oscilar** |

El equilibrio (régimen permanente) es $x \to F/k$, es decir $v \to E$.

---

## 6. Sistemas de EDO lineales de primer orden

**Método de eliminación (sustitución):** se despeja una incógnita de una ecuación, se reemplaza en la otra y queda una EDO de orden mayor en una sola incógnita. Por ejemplo, $x' + y = \cos t$ da $y = \cos t - x'$.

**Método matricial:** para $\vec X' = A\vec X$:

- se hallan los autovalores $\lambda_i$ y los autovectores $\vec v_i$ de $A$;
- si son reales y distintos, $\vec X = \sum C_i\thinspace e^{\lambda_it}\thinspace\vec v_i$.

**Sistemas no homogéneos:** a veces una ecuación queda **desacoplada** (depende de una sola incógnita): se resuelve primero esa y se reemplaza en las otras.

---

## 7. Complementos: ecuaciones homogéneas y exactas

**Función homogénea de grado $n$:** $F(tx, ty) = t^nF(x,y)$ para todo $t$. Ejemplos:

- $x^3 + x^2y$ es homogénea de grado 3;
- $e^{x/y}$ es homogénea de grado 0.

**Propiedad:** toda función homogénea de grado 0 se puede escribir en función de $y/x$. Tomando $t = \frac1x$: $F(x,y) = F\left(1, \frac yx\right) = G\left(\frac yx\right)$. Por eso $y' = F(x,y)$, con $F$ homogénea de grado 0, se resuelve con $z = y/x$:

$$\ln|x| = \int\frac{dz}{G(z) - z} + C$$

(los valores con $G(z) = z$ pueden dar soluciones singulares).

**Exactas: un error a evitar.** La función potencial $U(x,y)$ es un campo escalar de **dos** variables, y lo que se busca es una familia de funciones de **una** variable: las **curvas de nivel** $U(x,y) = C$. Es un error grave dar $U(x,y)$ como solución general.

**Ejemplo:** $(\cos y + y\cos x)\thinspace dx + (\mathop{\mathrm{sen}}x - x\mathop{\mathrm{sen}}y)\thinspace dy = 0$. Es exacta: $M'_y = -\mathop{\mathrm{sen}}y + \cos x = N'_x$. Integrando: $U = x\cos y + y\mathop{\mathrm{sen}}x + \varphi(y)$, y derivando respecto de $y$, $\varphi' = 0$. **S.G.:** $x\cos y + y\mathop{\mathrm{sen}}x = C$.

**Deducción del factor integrante.** Se busca $\mu$ tal que $\mu M\thinspace dx + \mu N\thinspace dy = 0$ sea exacta: $(\mu M)'_y = (\mu N)'_x$. En general es una ecuación en derivadas parciales para $\mu$; sólo se puede resolver si $\mu$ depende de una sola variable.

- Si $\mu = \mu(x)$: $\mu M'_y = \mu'N + \mu N'_x$, así que $\dfrac{\mu'}{\mu} = \dfrac{M'_y - N'_x}{N}$. Hace falta que el segundo miembro dependa **sólo de $x$**.
- Si $\mu = \mu(y)$: $\mu'M + \mu M'_y = \mu N'_x$, así que $\dfrac{\mu'}{\mu} = \dfrac{N'_x - M'_y}{M}$. Hace falta que dependa **sólo de $y$**.

**Líneas de campo y equipotenciales.** Si $\vec F = \nabla U$, las **equipotenciales** son las curvas de nivel de $U$. Como el gradiente es perpendicular a ellas y tangente a las líneas de campo, **las líneas de campo son las trayectorias ortogonales de las equipotenciales**.

---

## 8. Complementos: teoría de las EDO lineales de 2.º orden

**Funciones linealmente independientes.** $\lbrace y_1, \dots, y_n\rbrace$ es **L.I.** en $(a,b)$ si la única combinación lineal que da la función nula (para todo $x$ del intervalo) es la de coeficientes todos nulos.

**Wronskiano** de $n$ funciones derivables hasta el orden $n - 1$:

$$W(y_1, \dots, y_n) = \begin{vmatrix} y_1 & y_2 & \cdots & y_n \cr y_1' & y_2' & \cdots & y_n' \cr \vdots & & & \vdots \cr y_1^{(n-1)} & y_2^{(n-1)} & \cdots & y_n^{(n-1)} \end{vmatrix}$$

**Teorema:** si $W \ne 0$ en $(a,b)$, las funciones son L.I. *Demostración:* si $C_1y_1 + \dots + C_ny_n = 0$, derivando $n - 1$ veces se obtiene un sistema lineal homogéneo en los $C_i$ cuyo determinante es $W \ne 0$; la única solución es la trivial. $\blacksquare$

**Ecuación lineal de 2.º orden:** $a_0(x)y'' + a_1(x)y' + a_2(x)y = Q(x)$. Si los $a_i$ son constantes, es a **coeficientes constantes**; si $Q = 0$, es **homogénea** (reducida).

**Propiedades de la homogénea:**

1. Si $y_1$ e $y_2$ son soluciones, toda combinación lineal $C_1y_1 + C_2y_2$ también lo es (reemplazando, cada paréntesis se anula).
2. Si $y_1$, $y_2$ son soluciones **L.I.**, toda solución $y$ (con $y(x_0) = y_0$, $y'(x_0) = y_0'$) es combinación de ellas: el sistema $C_1y_1(x_0) + C_2y_2(x_0) = y_0$, $C_1y_1'(x_0) + C_2y_2'(x_0) = y_0'$ tiene solución única porque su determinante es el wronskiano. Entonces la **S.G. es $C_1y_1 + C_2y_2$**.

**Ecuación característica.** Proponiendo $y = e^{rx}$: $e^{rx}(a_0r^2 + a_1r + a_2) = 0$, y como $e^{rx} \ne 0$, $a_0r^2 + a_1r + a_2 = 0$.

- **Raíces reales distintas:** $y_1 = e^{r_1x}$, $y_2 = e^{r_2x}$, con $W = e^{(r_1+r_2)x}(r_2 - r_1) \ne 0$ ⇒ L.I.
- **Raíces complejas $a \pm bi$:** con la fórmula de Euler $e^{i\varphi} = \cos\varphi + i\mathop{\mathrm{sen}}\varphi$,

$$c_1e^{(a+bi)x} + c_2e^{(a-bi)x} = e^{ax}\big[(c_1 + c_2)\cos bx + i(c_1 - c_2)\mathop{\mathrm{sen}}bx\big] = e^{ax}(A_1\cos bx + A_2\mathop{\mathrm{sen}}bx)$$

- **Raíz doble $r_1$:** además de $e^{r_1x}$, también $y_2 = x\thinspace e^{r_1x}$ es solución. Al reemplazar queda $e^{r_1x}[x(a_0r_1^2 + a_1r_1 + a_2) + (2a_0r_1 + a_1)]$; el primer paréntesis es 0 porque $r_1$ es raíz, y el segundo también, porque una raíz doble es raíz del polinomio derivado. Su wronskiano es $e^{2r_1x} \ne 0$.

**Ecuación no homogénea:**

- **Teorema 1:** la diferencia de dos soluciones de la completa es solución de la homogénea (se restan las ecuaciones).
- **Teorema 2:** toda solución de la completa es $y_P + C_1u_1 + C_2u_2$. Si $\varphi$ es solución, $\varphi - y_P$ resuelve la homogénea, así que es combinación de $u_1$ y $u_2$. Por lo tanto **$y = y_H + y_P$**.

### Deducción de variación de parámetros

Se propone $y_P = C_1(x)u_1 + C_2(x)u_2$. Hay dos incógnitas y una sola ecuación, así que se impone una condición extra que simplifique: $C_1'u_1 + C_2'u_2 = 0$. Entonces $y_P' = C_1u_1' + C_2u_2'$, y al reemplazar en $a_0y'' + a_1y' + a_2y = Q$ los términos con $C_1$ y $C_2$ se anulan (porque $u_1$, $u_2$ resuelven la homogénea). Queda el sistema:

$$\begin{cases} C_1'u_1 + C_2'u_2 = 0 \cr C_1'u_1' + C_2'u_2' = \dfrac{Q(x)}{a_0} \end{cases}$$

Por Cramer, con $W = u_1u_2' - u_2u_1' \ne 0$: $C_1' = -\dfrac{u_2\thinspace Q/a_0}{W}$ y $C_2' = \dfrac{u_1\thinspace Q/a_0}{W}$. Se integra y se reemplaza.

> Si el coeficiente principal $a_0$ no es 1, en el segundo miembro va $Q/a_0$.

### Coeficientes indeterminados: tabla completa

| $Q(x)$ | Condición en la ecuación característica | Se propone $y_P$ |
|---|---|---|
| Polinomio de grado $n$ | 0 no es raíz ($a_2 \ne 0$) | polinomio **completo** de grado $n$ |
| | 0 es raíz simple ($a_2 = 0$) | $x\cdot$ polinomio completo de grado $n$ |
| | 0 es raíz doble ($a_1 = a_2 = 0$) | $x^2\cdot$ polinomio completo de grado $n$ |
| $B\thinspace e^{\alpha x}$ | $\alpha$ no es raíz | $A\thinspace e^{\alpha x}$ |
| | $\alpha$ raíz simple | $A\thinspace x\thinspace e^{\alpha x}$ |
| | $\alpha$ raíz doble | $A\thinspace x^2e^{\alpha x}$ |
| $M\cos\beta x + N\mathop{\mathrm{sen}}\beta x$ | $\pm\beta i$ no son raíces | $A_1\cos\beta x + A_2\mathop{\mathrm{sen}}\beta x$ |
| | $\pm\beta i$ son raíces | $x(A_1\cos\beta x + A_2\mathop{\mathrm{sen}}\beta x)$ |
| Combinación lineal de los anteriores | | combinación de las propuestas |

Aunque $M$ o $N$ sean 0, se propone **seno y coseno**; y aunque al polinomio le falten términos, se propone el polinomio **completo**.

**Ejemplo:** $y'' - 2y' = x^2 + 3e^{2x} + \cos x$. La característica $\lambda^2 - 2\lambda = 0$ tiene raíces $0$ y $2$, así que:

$$y_P = x(A_2x^2 + A_1x + A_0) + A_3\thinspace x\thinspace e^{2x} + A_4\cos x + A_5\mathop{\mathrm{sen}}x$$

---

## 9. Estrategia para los ejercicios

1. **Primer orden:** ¿es separable? ¿lineal? ¿homogénea? ¿exacta? Si no, ¿se puede hacer exacta con $\mu(x)$ o $\mu(y)$?
2. **Lineal de orden $n$:**
   - ecuación característica ⇒ $y_H$;
   - $y_P$ por coeficientes indeterminados (atención a la resonancia) o por variación de parámetros;
   - condiciones iniciales **al final**.
3. **Líneas de campo:** $dy/dx = Q/P$ y se resuelve con alguno de los métodos anteriores.
4. **Sistemas:** eliminar incógnitas o usar autovalores.

---

## 10. Resumen de fórmulas

| Tema | Fórmula |
|---|---|
| Homogénea | $y = zx$, $\ y' = z + xz'$ |
| Exacta | $M'_y = N'_x$ ⇒ $U = C$ con $\nabla U = (M,N)$ |
| Factor integrante $\mu(x)$ | $e^{\int(M'_y - N'_x)/N\thinspace dx}$ |
| Factor integrante $\mu(y)$ | $e^{\int(N'_x - M'_y)/M\thinspace dy}$ |
| Líneas de campo | $dx/P = dy/Q\ (= dz/R)$ |
| Raíces complejas $\alpha\pm\beta i$ | $e^{\alpha x}(C_1\cos\beta x + C_2\mathop{\mathrm{sen}}\beta x)$ |
| Variación de parámetros | $C_1' = -y_2f/W$, $\ C_2' = y_1f/W$ |
| Wronskiano | $W = y_1y_2' - y_2y_1'$ |

---

[← Volver al menú principal](../README.md)
