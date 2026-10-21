# Unidad 7 — Polinomio de Taylor y extremos

Resumen del material teórico de la unidad ([U07-Teoria-Taylor-Extremos.pdf](../aula-virtual/07-Taylor-Extremos/U07-Teoria-Taylor-Extremos.pdf)), de las [notas de clase sobre extremos](../aula-virtual/07-Taylor-Extremos/Notas-2021-06-29-Extremos.pdf) y de la hoja [Condición suficiente para $n = 3$](../aula-virtual/07-Taylor-Extremos/Extremos-Condicion-Suficiente-n3.pdf), complementado con el [resumen de UTNianos](../UTNianos/Resumen%20AM2.pdf).

**Objetivos de la unidad:**

1. Aproximar campos escalares con polinomios de Taylor.
2. Hallar y clasificar extremos locales (puntos críticos, Hessiano).
3. Resolver problemas de extremos absolutos y de extremos condicionados (Lagrange).

---

## 1. Polinomio de Taylor en dos variables

Para $f \in C^n$ en un entorno de $(x_0, y_0)$, con $h = x - x_0$ y $k = y - y_0$:

**Orden 1** (es el plano tangente):

$$P_1 = f(x_0,y_0) + f'_x\,h + f'_y\,k$$

**Orden 2:**

$$P_2 = P_1 + \frac{1}{2!}\left(f''_{xx}\,h^2 + 2f''_{xy}\,hk + f''_{yy}\,k^2\right)$$

Todas las derivadas se evalúan en $(x_0,y_0)$.

**Orden 3** (se suman los términos de 3.er orden):

$$P_3 = P_2 + \frac{1}{3!}\left(f'''_{xxx}\,h^3 + 3f'''_{xxy}\,h^2k + 3f'''_{xyy}\,hk^2 + f'''_{yyy}\,k^3\right)$$

Los coeficientes son los binomiales, como en $(h\,\partial_x + k\,\partial_y)^n f$.

**Tres variables, orden 2:**

$$P_2 = f + f'_x h + f'_y k + f'_z l + \frac12\left(f''_{xx}h^2 + f''_{yy}k^2 + f''_{zz}l^2 + 2f''_{xy}hk + 2f''_{xz}hl + 2f''_{yz}kl\right)$$

**Forma matricial:**

$$P_2(\vec X) = f(\vec A) + \nabla f(\vec A)\cdot\vec H + \tfrac12\,\vec H^{T}\,Hf(\vec A)\,\vec H, \qquad \vec H = \vec X - \vec A$$

**Propiedades:**

- $P_n$ y $f$ tienen el **mismo valor y las mismas derivadas hasta orden $n$** en el punto. En particular, comparten el plano tangente.
- Un polinomio de grado $\le n$ es su propio polinomio de Taylor de orden $n$, sólo que **reescrito en potencias de $(x - x_0)$ y $(y - y_0)$**.
- **Atajo:** se pueden usar desarrollos conocidos de una variable. Por ejemplo, $e^u = 1 + u + \frac{u^2}{2} + \dots$ y $\cos u = 1 - \frac{u^2}{2} + \dots$, multiplicando y descartando los términos de grado mayor que $n$.
- **Aproximaciones:** se elige un punto cercano "cómodo". Por ejemplo, para $0{,}98^{2{,}01}$ se usa $f = x^y$ en $(1, 2)$.

---

## 2. Extremos locales: definiciones

$f(\vec A)$ es:

- **máximo local (relativo)** si $f(\vec X) \le f(\vec A)$ en un entorno de $\vec A$;
- **mínimo local** si $f(\vec X) \ge f(\vec A)$ en un entorno de $\vec A$;
- **en sentido estricto** si la desigualdad es estricta para $\vec X \ne \vec A$; si no, es **en sentido amplio**. Por ejemplo, $(x+y)^4$ tiene mínimo amplio en toda la recta $x + y = 0$.

**Absoluto:** la desigualdad vale en **todo** el dominio considerado.

**Condición necesaria (Fermat):** si $f$ es diferenciable en $\vec A$ (interior) y $f(\vec A)$ es extremo local, entonces $\nabla f(\vec A) = \vec 0$, es decir, el plano tangente es horizontal.

**Puntos críticos** (candidatos a extremo):

- **estacionarios:** $\nabla f = \vec 0$;
- puntos donde $f$ **no es diferenciable** (por ejemplo, $\sqrt{x^2+y^2}$ en el origen);
- puntos de la **frontera** del dominio (para extremos absolutos).

**Punto silla (de ensilladura):** es un punto estacionario que no es extremo. En todo entorno hay valores mayores y menores que $f(\vec A)$.

---

## 3. Clasificación con el Hessiano

$$Hf(\vec A) = \begin{pmatrix} f''_{xx} & f''_{xy} \\ f''_{xy} & f''_{yy} \end{pmatrix}_{\vec A}, \qquad H = \det Hf(\vec A) = f''_{xx}f''_{yy} - (f''_{xy})^2$$

**Caso $n = 2$** ($f \in C^2$, $\nabla f(\vec A) = \vec 0$):

| Condición | Conclusión |
|---|---|
| $H > 0$ y $f''_{xx} > 0$ | **mínimo** local estricto |
| $H > 0$ y $f''_{xx} < 0$ | **máximo** local estricto |
| $H < 0$ | **punto silla** |
| $H = 0$ | el criterio **no decide**: hay que estudiar el signo de $f(\vec X) - f(\vec A)$ cerca del punto |

**Caso $n = 3$** (menores principales $H_1 = f''_{xx}$, $H_2 = \det$ del bloque $2\times2$ y $H_3 = \det Hf$):

| Condición | Conclusión |
|---|---|
| $H_1 > 0$, $H_2 > 0$, $H_3 > 0$ | mínimo local |
| $H_1 < 0$, $H_2 > 0$, $H_3 < 0$ | máximo local |
| $H_3 \ne 0$ y no se da ninguno de los anteriores | no es extremo |

En general, el criterio de Sylvester dice: Hessiano **definido positivo** ⇒ mínimo, **definido negativo** ⇒ máximo, **indefinido** ⇒ silla. Equivalentemente, se puede mirar el signo de los autovalores.

**Cuando $H = 0$, o en puntos no diferenciables:** se analiza directamente $\Delta f = f(\vec X) - f(\vec A)$. Algunas técnicas:

- restringir a rectas o curvas y ver si cambia de signo;
- dibujar el conjunto de nivel $f = f(\vec A)$ y las regiones $f > f(\vec A)$ y $f < f(\vec A)$;
- acotar, por ejemplo $f \ge 2$ porque $\sqrt{|xy|} \ge 0$.

### Extremos de funciones implícitas

Si $z = f(x,y)$ está dada por $F(x,y,z) = 0$ y $(x_0, y_0)$ es estacionario, entonces $F'_x = F'_y = 0$, y las segundas derivadas se simplifican a:

$$f''_{xx} = -\frac{F''_{xx}}{F'_z}, \qquad f''_{xy} = -\frac{F''_{xy}}{F'_z}, \qquad f''_{yy} = -\frac{F''_{yy}}{F'_z}$$

---

## 4. Extremos absolutos en un compacto

**Teorema de Weierstrass:** si $f$ es continua en un conjunto **compacto** (cerrado y acotado), alcanza máximo y mínimo absolutos.

**Procedimiento:**

1. Hallar los puntos críticos **interiores** ($\nabla f = 0$ o $f$ no diferenciable) y evaluar $f$ en ellos.
2. Estudiar $f$ **sobre la frontera**: parametrizarla (y queda un problema de una variable) o usar Lagrange. Incluir los extremos de los tramos.
3. **Comparar todos los valores:** el mayor es el máximo absoluto y el menor, el mínimo absoluto.

> Para la frontera **no** hace falta clasificar con el Hessiano: alcanza con comparar valores.

---

## 5. Extremos condicionados (ligados): multiplicadores de Lagrange

**Problema:** maximizar o minimizar $f(\vec X)$ sujeto a $g(\vec X) = 0$.

**Método 1 — Sustitución / parametrización:** si se puede despejar una variable o parametrizar la restricción (una recta, una superficie dada como $\vec X(u,v)$, una elipse con $\cos$ y $\operatorname{sen}$), se reemplaza en $f$ y queda un problema **libre** con menos variables.

**Método 2 — Lagrange:** si $f, g \in C^1$ y $\nabla g \ne \vec 0$, los extremos condicionados cumplen

$$\boxed{\nabla f = \lambda\,\nabla g, \qquad g = 0}$$

Geométricamente, en el extremo la curva de nivel de $f$ es **tangente** a la restricción, así que sus normales son paralelas.

Con dos restricciones: $\nabla f = \lambda\nabla g_1 + \mu\nabla g_2$.

**Problemas de distancia:** conviene minimizar el **cuadrado** de la distancia, que tiene los mismos puntos óptimos y evita las raíces.

---

## 6. Complementos: fórmula de Taylor con resto y diferenciales sucesivos

**Repaso (una variable).** Si $f$ es derivable hasta el orden $n + 1$ en un entorno de $a$:

$$f(x) = \sum_{i=0}^n\frac{f^{(i)}(a)}{i!}(x - a)^i + T_{n+1}, \qquad T_{n+1} = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}\ \text{ con } c \text{ entre } a \text{ y } x$$

$T_{n+1}$ es el **término complementario** (resto de Lagrange) y permite **acotar el error** de usar el polinomio. Con $a = 0$ es la fórmula de **Mac Laurin**.

**Diferenciales sucesivos.** Si $F$ tiene derivadas continuas hasta el orden $n$, considerando $h = dx$ y $k = dy$ constantes:

$$dF = F'_xh + F'_yk, \qquad d^2F = F''_{xx}h^2 + 2F''_{xy}hk + F''_{yy}k^2$$

$$d^3F = F'''_{xxx}h^3 + 3F'''_{xxy}h^2k + 3F'''_{xyy}hk^2 + F'''_{yyy}k^3$$

En general, con el "operador binomio":

$$d^nF = \left(h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y}\right)^{(n)}F = \sum_{i=0}^n\binom{n}{i}\frac{\partial^nF}{\partial x^{n-i}\partial y^i}\,h^{n-i}k^i$$

(Schwarz permite juntar las derivadas cruzadas.)

**Deducción de Taylor en dos variables.** Se lleva a una variable con la recta de $P_0 = (a,b)$ a $P_1 = (a+h, b+k)$: $x = a + th$, $y = b + tk$, y $\varphi(t) = F(a + th, b + tk)$. Por la regla de la cadena:

- $\varphi'(t) = F'_x h + F'_y k$, así que $\varphi'(0) = dF(a,b)$;
- $\varphi''(0) = F''_{xx}h^2 + 2F''_{xy}hk + F''_{yy}k^2 = d^2F(a,b)$;
- en general $\varphi^{(n)}(0) = d^nF(a,b)$.

Aplicando Mac Laurin a $\varphi$ y evaluando en $t = 1$:

$$F(a + h, b + k) = F(a,b) + \sum_{i=1}^n\frac{d^iF(a,b)}{i!} + \frac{d^{n+1}F(a + ch,\ b + ck)}{(n+1)!}, \qquad 0 < c < 1$$

Con $h = x - a$ y $k = y - b$ se obtiene el polinomio en potencias de $(x - a)$ e $(y - b)$.

---

## 7. Complementos: punto de ensilladura y demostraciones de los criterios

**Punto de ensilladura (definición).** $(x_0, y_0, F(x_0,y_0))$ es de ensilladura si $F$ es diferenciable en $P_0$ y el **plano tangente atraviesa la superficie**: en todo entorno de $P_0$ hay puntos con $F \ge F(P_0)$ y puntos con $F \le F(P_0)$. Con $\Delta F = F(\vec X) - F(P_0)$:

- $\Delta F \le 0$ en un entorno ⇒ máximo relativo;
- $\Delta F \ge 0$ en un entorno ⇒ mínimo relativo;
- $\Delta F$ cambia de signo en todo entorno (y $F$ diferenciable) ⇒ ensilladura.

**Demostración de la condición necesaria** ($F(P_0)$ extremo ⇒ $F'_x(P_0) = F'_y(P_0) = 0$). Si $F(P_0)$ es, por ejemplo, mínimo, cortando la superficie con $x = x_0$ se obtiene $\varphi(y) = F(x_0, y)$, que tiene un mínimo en $y_0$. Por Análisis I, $\varphi'(y_0) = F'_y(P_0) = 0$. Lo mismo con $y = y_0$ da $F'_x(P_0) = 0$. $\blacksquare$

**Cuidado:** que las parciales se anulen no garantiza un extremo. $z = x^2 - y^2$ tiene $\nabla z(0,0) = \vec 0$ y en $(0,0)$ hay una ensilladura. Los puntos que cumplen la condición necesaria se llaman **críticos** o **estacionarios**.

### Demostración del criterio del Hessiano

**Hipótesis:** derivadas hasta el 2.º orden continuas en un entorno de $P_0$, $\nabla F(P_0) = \vec 0$ y derivadas segundas no todas nulas (supongamos $F''_{xx}(P_0) \ne 0$).

**Paso 1.** Por continuidad, $H$ y $F''_{xx}$ conservan su signo en un entorno de $P_0$.

**Paso 2.** Taylor de orden 1 con resto de orden 2 (las derivadas primeras se anulan):

$$2\,\Delta F = F''_{xx}h^2 + 2F''_{xy}hk + F''_{yy}k^2$$

con las derivadas segundas evaluadas en $(x_0 + ch, y_0 + ck)$, $0 < c < 1$.

**Paso 3.** Se saca $F''_{xx}$ de factor común y se completa el cuadrado:

$$2\,\Delta F = F''_{xx}\left(h + \frac{F''_{xy}}{F''_{xx}}k\right)^2 + \frac{F''_{xx}F''_{yy} - (F''_{xy})^2}{F''_{xx}}\,k^2 = F''_{xx}\left(h + \frac{F''_{xy}}{F''_{xx}}k\right)^2 + \frac{H}{F''_{xx}}\,k^2$$

**Paso 4 — casos:**

- **$H(P_0) > 0$:** los dos términos tienen el signo de $F''_{xx}$ (y no se anulan a la vez, porque eso significaría $h = k = 0$). Si $F''_{xx} > 0$, $\Delta F > 0$: **mínimo**. Si $F''_{xx} < 0$: **máximo**.
- **$H(P_0) < 0$:** con $k = 0$, $\Delta F$ tiene el signo de $F''_{xx}$; con $h + \frac{F''_{xy}}{F''_{xx}}k = 0$, $\Delta F$ tiene el signo de $H/F''_{xx}$, que es el opuesto. $\Delta F$ cambia de signo: **ensilladura**.
- **$H(P_0) = 0$:** con ejemplos se ve que puede pasar cualquier cosa. $\blacksquare$

---

## 8. Complementos: deducción de Lagrange y Hessiano orlado

**Ejemplo introductorio:** el rectángulo de perímetro 24 y área máxima. Se maximiza $A = xy$ con la restricción $\phi(x,y) = x + y - 12 = 0$. Fijar $A$ es elegir una curva de nivel de $A$; el extremo condicionado se da donde esa curva es **tangente** a la restricción, es decir donde sus normales son paralelas: $\nabla A = \lambda\nabla\phi$.

$$\begin{cases} y = \lambda \\ x = \lambda \\ x + y = 12 \end{cases} \ \Rightarrow\ x = y = 6,\ A = 36$$

Es el cuadrado de lado 6.

**Teorema.** Si $F$ y $\phi$ tienen derivadas parciales continuas, $F$ tiene un extremo en $(x_0,y_0)$ sujeto a $\phi = 0$ y $\nabla\phi(x_0,y_0) \ne \vec 0$, entonces existe $k_0$ con $\nabla F(x_0,y_0) = k_0\,\nabla\phi(x_0,y_0)$.

*Demostración.* La restricción es una curva $C$: $\vec r(t)$, con $\vec r(t_0) = P_0$. $F_C(t) = F(\vec r(t))$ tiene un extremo en $t_0$, así que $F_C'(t_0) = \nabla F(P_0)\cdot\vec r\,'(t_0) = 0$: $\nabla F(P_0)$ es perpendicular a la tangente de $C$. Además $\nabla\phi(P_0)$ también lo es, porque $C$ es una curva de nivel de $\phi$. Dos vectores perpendiculares a la misma dirección (en el plano) son paralelos. $\blacksquare$

**Función de Lagrange:** con $\lambda_0 = -k_0$, $L(x,y,\lambda) = F(x,y) + \lambda\,\phi(x,y)$, y los candidatos son los puntos con $\nabla L = \vec 0$. Con dos restricciones: $L = F + \lambda_1\phi_1 + \lambda_2\phi_2$.

**Condición suficiente: Hessiano orlado.** En un punto $(x_0, y_0, \lambda_0)$ con $\nabla L = \vec 0$:

$$H_0 = \begin{vmatrix} L''_{xx} & L''_{xy} & \phi'_x \\ L''_{xy} & L''_{yy} & \phi'_y \\ \phi'_x & \phi'_y & 0 \end{vmatrix}$$

- $H_0 > 0$ ⇒ **máximo** condicionado;
- $H_0 < 0$ ⇒ **mínimo** condicionado;
- $H_0 = 0$ ⇒ el criterio no decide.

**Ejemplo 1:** extremos de $F = x^2 + y$ sobre $x^2 + y^2 = 9$. Con $L = x^2 + y - \lambda(x^2 + y^2 - 9)$:

$$\begin{cases} 2x = 2\lambda x \\ 1 = 2\lambda y \\ x^2 + y^2 = 9 \end{cases}$$

- $x = 0$: $y = \pm3$, con $\lambda = \pm\frac16$.
- $\lambda = 1$: $y = \frac12$, $x = \pm\frac{\sqrt{35}}{2}$.

El Hessiano orlado da $H_0 = 8\lambda x^2 - 4y^2(2 - 2\lambda)$:

- $(0, 3)$ y $(0,-3)$: $H_0 < 0$ ⇒ mínimos condicionados ($F = 3$ y $F = -3$);
- $(\pm\frac{\sqrt{35}}{2}, \frac12)$: $H_0 = 70 > 0$ ⇒ máximos condicionados ($F = \frac{37}{4}$).

**Ejemplo 2:** puntos de $y^2 = 4x$ más cercanos a $(4,0)$. Se minimiza $F = (x - 4)^2 + y^2$ con $\phi = y^2 - 4x = 0$:

- $y = 0$ da $(0,0)$ con $\lambda = 2$, y $H_0 = 32 > 0$: **no** es mínimo.
- $\lambda = 1$ da $x = 2$, $y = \pm2\sqrt2$, con $H_0 = -64 < 0$: **mínimos**.

La distancia mínima es $\sqrt{(2-4)^2 + 8} = \sqrt{12} = 2\sqrt3$.

---

## 9. Estrategia para los ejercicios

1. **Taylor:** calcular todas las derivadas necesarias **numéricamente en el punto**, y después armar el polinomio. Revisar el factor $\frac12$ y el $2$ de la derivada cruzada.
2. **Extremos libres:**
   - resolver $\nabla f = \vec 0$, factorizando y separando casos ("$x = 0$ o $y = 0$");
   - calcular el Hessiano en cada punto y clasificar;
   - si $H = 0$, analizar el signo de $f - f(\vec A)$ por caminos.
3. **Absolutos en una región:** interior + frontera + comparación.
4. **Con restricción:** sustitución si es fácil; si no, Lagrange.

---

## 10. Resumen de fórmulas

| Concepto | Fórmula |
|---|---|
| Taylor orden 2 | $f + f'_xh + f'_yk + \frac12(f''_{xx}h^2 + 2f''_{xy}hk + f''_{yy}k^2)$ |
| Punto estacionario | $\nabla f = \vec 0$ |
| Hessiano ($n=2$) | $H = f''_{xx}f''_{yy} - (f''_{xy})^2$ |
| Mínimo / máximo / silla | $H>0, f''_{xx}>0$ / $H>0, f''_{xx}<0$ / $H<0$ |
| Lagrange | $\nabla f = \lambda\nabla g$, $g = 0$ |
| Implícita en punto estacionario | $f''_{ij} = -F''_{ij}/F'_z$ |

---

[← Volver al menú principal](../README.md)
