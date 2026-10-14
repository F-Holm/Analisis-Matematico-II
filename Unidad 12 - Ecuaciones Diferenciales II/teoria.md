# Unidad 12 — Ecuaciones diferenciales (2.ª parte)

Resumen del material teórico de la unidad ([U12-Teoria-Ecuaciones-Diferenciales-2.pdf](../aula-virtual/12-Ecuaciones-Diferenciales-2/U12-Teoria-Ecuaciones-Diferenciales-2.pdf)), de las [notas de clase sobre líneas de campo](../aula-virtual/12-Ecuaciones-Diferenciales-2/Notas-2021-10-26-Lineas-de-Campo.pdf), del [método de variación de parámetros anotado](../aula-virtual/12-Ecuaciones-Diferenciales-2/Metodo-Variacion-Parametros-Anotado.pdf) y de los pizarrones sobre ecuaciones homogéneas y exactas ([2024](../aula-virtual/01-Ecuaciones-Diferenciales-1/Pizarron-2024-10-22-EDO-Homogeneas-Exactas.pdf), [2021](../aula-virtual/01-Ecuaciones-Diferenciales-1/Notas-2021-10-26-EDO-Homogeneas-Exactas.pdf)).

**Objetivos de la unidad:**

1. Resolver EDO homogéneas, totales exactas y reducibles a exactas mediante factores integrantes.
2. Hallar líneas de campo de un campo vectorial.
3. Resolver EDO lineales de orden $n$ a coeficientes constantes y sistemas de EDO lineales.

---

## 1. Ecuaciones homogéneas de primer orden

$f(x,y)$ es **homogénea de grado 0** si $f(tx, ty) = f(x,y)$. Entonces $f$ depende sólo de $y/x$.

La EDO $y' = f(x,y)$, con $f$ homogénea de grado 0, se resuelve con el cambio

$$z = \frac yx, \qquad y = zx, \qquad y' = z + x\,z'$$

y queda **separable**: $\ x\,z' = f(1,z) - z$.

- También vale escrito como $M\,dx + N\,dy = 0$ con $M$ y $N$ homogéneas del **mismo grado**.
- **Ecuaciones "casi homogéneas"**, como $y' = \dfrac{a_1x + b_1y + c_1}{a_2x + b_2y + c_2}$: se trasladan el origen al punto donde se cortan las rectas ($x = u + h$, $y = v + k$) y quedan homogéneas en $u$, $v$.

---

## 2. Ecuaciones diferenciales totales exactas

$M(x,y)\,dx + N(x,y)\,dy = 0$ es **exacta** si existe $U$ con $U'_x = M$ y $U'_y = N$. Es decir, $(M,N)$ es un campo de gradientes.

**Criterio** (en un dominio simplemente conexo, con $M, N \in C^1$):

$$\boxed{M'_y = N'_x}$$

**Solución general:** $U(x,y) = C$. Son las **líneas equipotenciales** del campo $(M, N)$.

**Cómo hallar $U$:** igual que la función potencial (Unidad 8). Se integra $M$ respecto de $x$, se deriva respecto de $y$, se iguala a $N$ y se despeja la función de $y$.

### Factor integrante

Si $M'_y \ne N'_x$, se busca $\mu \ne 0$ tal que $\mu M\,dx + \mu N\,dy = 0$ sea exacta. Hay dos casos útiles:

| Si … depende sólo de | Factor integrante |
|---|---|
| $\dfrac{M'_y - N'_x}{N}$ depende sólo de $x$ | $\mu(x) = e^{\int\frac{M'_y - N'_x}{N}dx}$ |
| $\dfrac{N'_x - M'_y}{M}$ depende sólo de $y$ | $\mu(y) = e^{\int\frac{N'_x - M'_y}{M}dy}$ |

> Al multiplicar por $\mu$ se pueden **perder o ganar soluciones**, donde $\mu$ se anula o no está definido. Hay que revisarlas aparte; suelen ser soluciones constantes como $y = 0$.

---

## 3. Líneas de campo

Las **líneas de campo** (o líneas de flujo) de $\vec f$ son las curvas que en cada punto son **tangentes al campo**. Si $\vec g(t)$ es una línea de campo, $\vec g'(t) = \lambda\,\vec f(\vec g(t))$.

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
| Real simple $r$ | $C\,e^{rx}$ |
| Real de multiplicidad $m$ | $(C_1 + C_2x + \dots + C_mx^{m-1})\,e^{rx}$ |
| Complejas $\alpha \pm \beta i$ | $e^{\alpha x}(C_1\cos\beta x + C_2\operatorname{sen}\beta x)$ |

### Solución particular: coeficientes indeterminados

Se usa cuando $f$ es un polinomio, una exponencial, un seno/coseno, o productos y sumas de ellos:

| $f(x)$ | Se propone $y_P$ |
|---|---|
| Polinomio de grado $k$ | Polinomio completo de grado $k$ |
| $e^{ax}\cdot$ polinomio | $e^{ax}\cdot$ polinomio completo |
| $\operatorname{sen}(bx)$ o $\cos(bx)$ | $A\cos bx + B\operatorname{sen}bx$ |

> **Regla de resonancia:** si la propuesta (o parte de ella) ya es solución de la homogénea, se **multiplica por $x^m$**, con $m$ la multiplicidad de la raíz correspondiente. Por ejemplo, $f = 2x$ con raíz $r = 0$ ⇒ $y_P = x(Ax + B)$.

**Superposición:** si $f = f_1 + f_2$, entonces $y_P = y_{P_1} + y_{P_2}$.

### Solución particular: variación de parámetros

Sirve para **cualquier** $f$ continua, por ejemplo $\sec x$ o $e^x/x$. Para el orden 2, $y'' + p\,y' + q\,y = f$ (coeficiente principal 1):

- Con $y_H = C_1y_1 + C_2y_2$, se propone $y_P = C_1(x)y_1 + C_2(x)y_2$, imponiendo:

$$\begin{cases} C_1'y_1 + C_2'y_2 = 0 \\ C_1'y_1' + C_2'y_2' = f \end{cases}$$

- Resolviendo con el **wronskiano** $W = y_1y_2' - y_2y_1'$:

$$C_1' = -\frac{y_2\,f}{W}, \qquad C_2' = \frac{y_1\,f}{W}$$

### Problemas de valores iniciales

Primero se halla la S.G. completa ($y_H + y_P$) y **después** se imponen las condiciones $y(x_0)$, $y'(x_0)$, …

Las condiciones de "recta tangente" o "recta normal" en un punto dan $y(x_0)$ y $y'(x_0)$; la pendiente de la normal es $-1/y'$.

---

## 5. Aplicaciones: sistemas masa-resorte-amortiguador y circuitos RLC

$$M\,x'' + d\,x' + k\,x = F \qquad\longleftrightarrow\qquad LC\,v'' + RC\,v' + v = E$$

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
- si son reales y distintos, $\vec X = \sum C_i\,e^{\lambda_it}\,\vec v_i$.

**Sistemas no homogéneos:** a veces una ecuación queda **desacoplada** (depende de una sola incógnita): se resuelve primero esa y se reemplaza en las otras.

---

## 7. Estrategia para los ejercicios

1. **Primer orden:** ¿es separable? ¿lineal? ¿homogénea? ¿exacta? Si no, ¿se puede hacer exacta con $\mu(x)$ o $\mu(y)$?
2. **Lineal de orden $n$:**
   - ecuación característica ⇒ $y_H$;
   - $y_P$ por coeficientes indeterminados (atención a la resonancia) o por variación de parámetros;
   - condiciones iniciales **al final**.
3. **Líneas de campo:** $dy/dx = Q/P$ y se resuelve con alguno de los métodos anteriores.
4. **Sistemas:** eliminar incógnitas o usar autovalores.

---

## 8. Resumen de fórmulas

| Tema | Fórmula |
|---|---|
| Homogénea | $y = zx$, $\ y' = z + xz'$ |
| Exacta | $M'_y = N'_x$ ⇒ $U = C$ con $\nabla U = (M,N)$ |
| Factor integrante $\mu(x)$ | $e^{\int(M'_y - N'_x)/N\,dx}$ |
| Factor integrante $\mu(y)$ | $e^{\int(N'_x - M'_y)/M\,dy}$ |
| Líneas de campo | $dx/P = dy/Q\ (= dz/R)$ |
| Raíces complejas $\alpha\pm\beta i$ | $e^{\alpha x}(C_1\cos\beta x + C_2\operatorname{sen}\beta x)$ |
| Variación de parámetros | $C_1' = -y_2f/W$, $\ C_2' = y_1f/W$ |
| Wronskiano | $W = y_1y_2' - y_2y_1'$ |

---

[← Volver al menú principal](../README.md)
