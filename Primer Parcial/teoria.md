# Teoría para el 1.er Parcial (Unidades 1 a 7)

Guía de todo lo que hace falta para resolver un 1.er parcial: definiciones y enunciados tal como se piden en los ejercicios teóricos ("Defina…", "Enuncie…"), y recetas paso a paso para cada tipo de ejercicio práctico. El detalle de cada tema está en el `teoria.md` de cada unidad y las fórmulas en una sola página en el [resumen de fórmulas](../FORMULAS.md).

**Formato habitual del examen:** 2 ejercicios teóricos + 4 prácticos. Para aprobar los TP hacen falta al menos dos prácticos bien; para aspirar a promoción, cuatro bien con al menos un teórico.

**Índice**

1. [Ecuaciones diferenciales de 1.er orden](#1-ecuaciones-diferenciales-de-1er-orden)
2. [Familias de curvas y trayectorias ortogonales](#2-familias-de-curvas-y-trayectorias-ortogonales)
3. [Dominio, conjuntos de nivel y topología](#3-dominio-conjuntos-de-nivel-y-topología)
4. [Límite](#4-límite)
5. [Continuidad](#5-continuidad)
6. [Derivadas parciales y direccionales](#6-derivadas-parciales-y-direccionales)
7. [Diferenciabilidad y gradiente](#7-diferenciabilidad-y-gradiente)
8. [Recta tangente, plano tangente y recta normal](#8-recta-tangente-plano-tangente-y-recta-normal)
9. [Funciones compuestas: regla de la cadena](#9-funciones-compuestas-regla-de-la-cadena)
10. [Funciones implícitas](#10-funciones-implícitas)
11. [Polinomio de Taylor y aproximaciones](#11-polinomio-de-taylor-y-aproximaciones)
12. [Extremos libres, ligados y absolutos](#12-extremos-libres-ligados-y-absolutos)
13. [Tabla: tipo de ejercicio → método](#13-tabla-tipo-de-ejercicio--método)

---

## 1. Ecuaciones diferenciales de 1.er orden

Detalle: [Unidad 1](../Unidad%2001%20-%20Ecuaciones%20Diferenciales%20I/teoria.md).

**Definiciones que se piden:**

- **Ecuación diferencial ordinaria (EDO):** relación entre una variable independiente $x$, una función incógnita $y(x)$ y sus derivadas: $F(x, y, y', \dots, y^{(n)}) = 0$. El **orden** es el de la derivada de mayor orden.
- **Solución general (SG):** familia de soluciones con tantas constantes arbitrarias (esenciales) como el orden.
- **Solución particular (SP):** la que se obtiene de la SG dando valores a las constantes (por ejemplo, con una condición inicial $y(x_0) = y_0$).
- **Solución singular:** solución que no se obtiene de la SG para ningún valor de las constantes (típico: $y = 0$ perdido al dividir por $y$).

**Cómo reconocer y resolver:**

| Tipo | Forma | Método |
|---|---|---|
| Variables separables | $y' = g(x)\thinspace h(y)$ | $\int\frac{dy}{h(y)} = \int g(x)\thinspace dx + C$. Revisar $h(y) = 0$ (posibles soluciones singulares). |
| Lineal | $y' + P(x)\thinspace y = Q(x)$ | $y = e^{-\int P}\left[\int Q\thinspace e^{\int P}dx + C\right]$, o $y = uv$, o variación de la constante. |
| Homogénea | $y' = g\left(\frac yx\right)$ (grado 0) | $y = zx$, $y' = z + xz'$ ⇒ queda separable en $z$ y $x$. |
| Bernoulli | $y' + P\thinspace y = Q\thinspace y^n$ | $z = y^{1-n}$ ⇒ lineal en $z$. |
| Diferencial total exacta | $P\thinspace dx + Q\thinspace dy = 0$ con $P'_y = Q'_x$ | Buscar $\varphi$ con $\nabla\varphi = (P,Q)$: SG $\varphi(x,y) = C$. |
| Falta $y$ (2.º orden) | $F(x, y', y'') = 0$ | $w = y'$ ⇒ 1.er orden en $w$. |

**Errores típicos:** olvidar la constante al integrar, perder la solución $y = 0$ al dividir, no despejar $y$ cuando se pide la SP, no verificar la condición inicial.

---

## 2. Familias de curvas y trayectorias ortogonales

**EDO de una familia de curvas:** si la familia tiene $n$ parámetros, se deriva $n$ veces y se eliminan los parámetros.

**Trayectorias ortogonales:**

1. Hallar la EDO de la familia: $y' = F(x,y)$.
2. Cambiar $y' \to -\dfrac{1}{y'}$: $y' = -\dfrac{1}{F(x,y)}$.
3. Resolver la nueva EDO y, si se pide, elegir la curva que pasa por el punto dado.

**Recta tangente y normal a una curva en $(x_0,y_0)$:** $Y - y_0 = y'(X - x_0)$ y $Y - y_0 = -\frac{1}{y'}(X - x_0)$. Muchos enunciados definen la curva por una propiedad de la tangente (por ejemplo, "la ordenada al origen de la recta tangente es…"): se escribe la tangente genérica, se impone la propiedad y sale la EDO.

Ejemplo de parcial: [1.er Parcial 15/10/2019, E4](primer-parcial-2019-10-15.md).

---

## 3. Dominio, conjuntos de nivel y topología

Detalle: [Unidad 2](../Unidad%2002%20-%20Funciones%20de%20Varias%20Variables%20y%20Topologia/teoria.md).

**Dominio natural:** juntar todas las condiciones: $\sqrt A \Rightarrow A \ge 0$; $\ln A \Rightarrow A > 0$; $\frac1A \Rightarrow A \ne 0$; $\arcsin A,\ \arccos A \Rightarrow |A| \le 1$. Graficar en el plano.

**Conjunto de nivel $k$:** $C_k = \lbrace\vec x \in D_f : f(\vec x) = k\rbrace$ (curvas de nivel en $\mathbb{R}^2$, superficies de nivel en $\mathbb{R}^3$).

**Topología:**

- **Punto interior** de $A$: existe una bola abierta centrada en él contenida en $A$.
- **Punto frontera:** toda bola centrada en él tiene puntos de $A$ y de su complemento.
- **Punto de acumulación:** toda bola reducida centrada en él tiene puntos de $A$. **Punto aislado:** pertenece a $A$ y no es de acumulación.
- **Abierto:** todos sus puntos son interiores. **Cerrado:** contiene a su frontera (o su complemento es abierto).
- **Acotado:** está contenido en alguna bola. **Compacto:** cerrado y acotado.
- **Conexo:** no se puede partir en dos abiertos disjuntos no vacíos. **Simplemente conexo:** conexo y "sin agujeros" (toda curva cerrada se contrae a un punto dentro del conjunto).

---

## 4. Límite

Detalle: [Unidad 3](../Unidad%2003%20-%20Limite%20y%20Continuidad/teoria.md).

**Definición:** $\lim\limits_{\vec x\to\vec A}f(\vec x) = L$ si para todo $\varepsilon > 0$ existe $\delta > 0$ tal que $0 < \Vert\vec x - \vec A\Vert < \delta$, $\vec x \in D_f$ ⇒ $|f(\vec x) - L| < \varepsilon$. ($\vec A$ tiene que ser punto de acumulación del dominio.)

**Receta para decidir si existe:**

1. Sustituir. Si no hay indeterminación, ese es el límite.
2. **Probar que no existe:**
   - Límites **iterados** distintos ⇒ no existe (si son iguales, no prueba nada).
   - **Curvas** que pasan por el punto: rectas $y - y_0 = m(x - x_0)$, parábolas $y = kx^2$, curvas $y = kx^p$ elegidas para igualar grados. Si el resultado depende de $m$ o $k$, o dos curvas dan valores distintos ⇒ no existe.
   - En polares el resultado depende de $\theta$ ⇒ no existe.
3. **Probar que existe** (y vale $L$, el candidato que dieron las curvas):
   - **Infinitésimo por acotada:** por ejemplo $\frac{x^2}{x^2 + y^2} \le 1$, $|\mathop{\mathrm{sen}}(\cdot)| \le 1$, $\frac{|x|}{\sqrt{x^2 + y^2}} \le 1$.
   - **Polares:** $|f - L| \le g(r)\thinspace h(\theta)$ con $g(r) \to 0$ y $h$ acotada.
   - Límites notables: $\frac{\mathop{\mathrm{sen}}u}{u} \to 1$, $\frac{1 - \cos u}{u^2} \to \frac12$, $\frac{e^u - 1}{u} \to 1$, $\frac{\ln(1 + u)}{u} \to 1$.

**Trampa clásica:** que el límite valga lo mismo por **todas las rectas** no alcanza: probar con parábolas o con la curva que iguala grados (por ejemplo, $\frac{x^2y}{x^4 + y^2}$ por $y = kx^2$).

---

## 5. Continuidad

**Definición:** $f$ es continua en $\vec A$ si $\vec A \in D_f$, existe $\lim\limits_{\vec x\to\vec A}f(\vec x)$ y es igual a $f(\vec A)$.

**Propiedades:** suma, producto, cociente (con denominador $\ne 0$) y composición de continuas es continua. **Weierstrass:** si $f$ es continua en un compacto, alcanza máximo y mínimo absolutos.

**Receta para funciones partidas** ($f = $ fórmula si $\vec x \ne \vec A$, $f(\vec A) = c$):

1. Calcular el límite de la fórmula en $\vec A$ (sección 4).
2. Comparar con $c$. Si se pide "hallar $k$ para que sea continua", igualar $k$ al límite.

Ejemplos: [Repaso R3](repaso-primer-parcial.md), [Simulacro P1](simulacro-primer-parcial.md).

---

## 6. Derivadas parciales y direccionales

Detalle: [Unidad 4](../Unidad%2004%20-%20Derivabilidad/teoria.md).

**Definiciones:**

- **Derivada respecto de un vector $\vec r$** en $\vec A$: $f'(\vec A, \vec r) = \lim\limits_{h\to0}\dfrac{f(\vec A + h\vec r) - f(\vec A)}{h}$.
- **Derivada direccional:** la misma con $\breve r$ versor ($\Vert\breve r\Vert = 1$).
- **Derivadas parciales:** direccionales según $\breve e_i$: $f'_x(\vec A) = \lim\limits_{h\to0}\dfrac{f(x_0 + h, y_0) - f(x_0,y_0)}{h}$.
- Homogeneidad: $f'(\vec A, \lambda\vec r) = \lambda f'(\vec A, \vec r)$.

**Cuándo usar la definición:** en funciones partidas, en el punto donde cambia la fórmula. Con $\breve r = (a,b)$ y $\vec A = (0,0)$:

$$f'(\vec 0, \breve r) = \lim_{h\to0}\frac{f(ha, hb) - f(0,0)}{h}$$

Si sale un resultado que depende de $(a,b)$ pero **no es lineal** en $(a,b)$, o existe en todas las direcciones pero $f$ no es continua, **no es diferenciable** (sección 7).

**Teorema de Schwarz:** si $f''_{xy}$ y $f''_{yx}$ existen y son continuas en un entorno, son iguales.

---

## 7. Diferenciabilidad y gradiente

Detalle: [Unidad 5](../Unidad%2005%20-%20Diferenciabilidad/teoria.md).

**Definición:** $f$ es diferenciable en $\vec A$ si existe una transformación lineal (dada por el gradiente) tal que

$$\lim_{\vec h\to\vec 0}\frac{f(\vec A + \vec h) - f(\vec A) - \nabla f(\vec A)\cdot\vec h}{\Vert\vec h\Vert} = 0$$

**Condiciones:**

- **Suficiente:** si las derivadas parciales existen en un entorno y son continuas en $\vec A$ ($f \in C^1$), $f$ es diferenciable.
- **Necesarias:** si $f$ es diferenciable en $\vec A$, entonces es continua en $\vec A$, existen todas las direccionales y $f'(\vec A, \breve r) = \nabla f(\vec A)\cdot\breve r$ (son **lineales** en $\breve r$).
- Para probar que **no** es diferenciable: mostrar que no es continua, o que alguna direccional no existe, o que $f'(\vec A,\breve r) \ne \nabla f\cdot\breve r$ para algún $\breve r$. Si nada de eso falla, aplicar la definición (con $\vec A = \vec 0$, en polares).

**Gradiente y derivada direccional máxima** (teorema que se pide enunciar y demostrar):

Si $f$ es diferenciable en $\vec A$ y $\nabla f(\vec A) \ne \vec 0$:

- La derivada direccional **máxima** es $\Vert\nabla f(\vec A)\Vert$ y se da en la dirección $\breve r = \frac{\nabla f(\vec A)}{\Vert\nabla f(\vec A)\Vert}$.
- La **mínima** es $-\Vert\nabla f(\vec A)\Vert$, en la dirección opuesta.
- Es **nula** en las direcciones perpendiculares a $\nabla f(\vec A)$.

*Demostración:* $f'(\vec A,\breve r) = \nabla f\cdot\breve r = \Vert\nabla f\Vert\cos\alpha$, que es máxima con $\alpha = 0$.

**Aproximación lineal:** $f(\vec A + \vec h) \approx f(\vec A) + \nabla f(\vec A)\cdot\vec h$. **Diferencial:** $df = f'_x\thinspace dx + f'_y\thinspace dy$.

Ejemplos: [1.er Parcial 15/10/2019, T1 y E1](primer-parcial-2019-10-15.md), [Repaso R13](repaso-primer-parcial.md).

---

## 8. Recta tangente, plano tangente y recta normal

| Objeto | Cómo se obtiene |
|---|---|
| Recta tangente a una curva $\vec g(t)$ en $t_0$ | $\vec X = \vec g(t_0) + \lambda\thinspace\vec g'(t_0)$ |
| Plano normal a la curva | $\vec g'(t_0)\cdot(\vec X - \vec g(t_0)) = 0$ |
| Plano tangente a $z = f(x,y)$ | $z = f(\vec A) + f'_x(\vec A)(x - x_0) + f'_y(\vec A)(y - y_0)$ |
| Plano tangente a $F(x,y,z) = 0$ | $\nabla F(P_0)\cdot(\vec X - P_0) = 0$ |
| Plano tangente a una superficie paramétrica $\vec\Sigma(u,v)$ | normal $\vec\Sigma'_u\wedge\vec\Sigma'_v$ |
| Recta normal | $\vec X = P_0 + \lambda\thinspace\vec n$ |
| Recta tangente a la intersección $F = 0$, $G = 0$ | dirección $\nabla F(P_0)\wedge\nabla G(P_0)$ |

El **gradiente es perpendicular a los conjuntos de nivel**: es la normal a la curva/superficie de nivel que pasa por el punto.

**Curvas que cortan perpendicularmente** a una superficie de nivel: su vector tangente debe ser paralelo a $\nabla F$ en el punto de corte.

Ejemplos: [Simulacro P2](simulacro-primer-parcial.md), [Repaso R1, R2, R7](repaso-primer-parcial.md).

---

## 9. Funciones compuestas: regla de la cadena

Detalle: [Unidad 6](../Unidad%2006%20-%20Funciones%20Compuestas%20e%20Implicitas/teoria.md).

**Teorema:** si $\vec g$ es diferenciable en $\vec A$ y $\vec f$ es diferenciable en $\vec g(\vec A)$, entonces $\vec f\circ\vec g$ es diferenciable en $\vec A$ y

$$D(\vec f\circ\vec g)(\vec A) = D\vec f(\vec g(\vec A))\cdot D\vec g(\vec A)$$

**Receta:**

1. Identificar las variables intermedias: $h(x,y) = f(u(x,y), v(x,y))$.
2. Calcular el punto intermedio $\vec B = (u(\vec A), v(\vec A))$. **Las derivadas de $f$ se evalúan en $\vec B$, no en $\vec A$.**
3. $h'_x = f'_u\thinspace u'_x + f'_v\thinspace v'_x$, $h'_y = f'_u\thinspace u'_y + f'_v\thinspace v'_y$ (o producto de matrices jacobianas).
4. Con $\nabla h(\vec A)$ se resuelve lo que se pida (aproximación, plano tangente, derivada máxima, etc.).

**Sobre una curva:** $\frac{d}{dt}f(\vec X(t)) = \nabla f(\vec X(t))\cdot\vec X'(t)$.

Ejemplos: [Simulacro P3](simulacro-primer-parcial.md), [Repaso R5](repaso-primer-parcial.md).

---

## 10. Funciones implícitas

**Teorema de Cauchy–Dini** (caso $F(x,y,z) = 0$): si $F \in C^1$ en un entorno de $P_0 = (x_0,y_0,z_0)$, $F(P_0) = 0$ y $F'_z(P_0) \ne 0$, entonces existe un entorno de $(x_0,y_0)$ y una única $z = f(x,y)$, $C^1$, con $f(x_0,y_0) = z_0$ y $F(x, y, f(x,y)) = 0$, y

$$z'_x = -\frac{F'_x}{F'_z}, \qquad z'_y = -\frac{F'_y}{F'_z}$$

(evaluadas en $P_0$). Para $F(x,y) = 0$: $y' = -\frac{F'_x}{F'_y}$.

**Receta:**

1. Verificar las tres hipótesis: $F \in C^1$, $F(P_0) = 0$ (a veces hay que **hallar** $z_0$ despejando), $F'_z(P_0) \ne 0$.
2. Calcular las derivadas con las fórmulas anteriores.
3. Aplicar lo que se pida: plano tangente, aproximación lineal, composición (sección 9) con la implícita como función intermedia.

**Sistemas** ($F = 0$, $G = 0$ definen $y(x)$, $z(x)$): el jacobiano $\frac{\partial(F,G)}{\partial(y,z)} \ne 0$; se derivan ambas ecuaciones respecto de $x$ y se resuelve el sistema lineal.

Ejemplos: [1.er Parcial 15/10/2019, E3](primer-parcial-2019-10-15.md), [Repaso R10](repaso-primer-parcial.md).

---

## 11. Polinomio de Taylor y aproximaciones

Detalle: [Unidad 7](../Unidad%2007%20-%20Taylor%20y%20Extremos/teoria.md).

**Polinomio de Taylor de 2.º orden** en $\vec A = (x_0,y_0)$, con $h = x - x_0$, $k = y - y_0$:

$$P_2(x,y) = f(\vec A) + f'_xh + f'_yk + \frac12\left(f''_{xx}h^2 + 2f''_{xy}hk + f''_{yy}k^2\right)$$

(todas las derivadas evaluadas en $\vec A$). $P_1$ es el plano tangente.

**Receta para aproximar $f(x_1,y_1)$:** elegir un $\vec A$ cercano donde todo sea fácil de calcular, escribir $P_1$ o $P_2$ y evaluar en $(x_1,y_1)$.

**Uso para extremos:** en un punto crítico, $f(\vec A + \vec h) - f(\vec A) \approx \frac12\vec h^{\thinspace T}H_f\thinspace\vec h$: el signo de la forma cuadrática decide máximo/mínimo.

---

## 12. Extremos libres, ligados y absolutos

**Definiciones:** $f$ tiene un **máximo (mínimo) local** en $\vec A$ si $f(\vec x) \le f(\vec A)$ ($\ge$) en un entorno de $\vec A$. **Punto crítico:** $\nabla f(\vec A) = \vec 0$ o $f$ no diferenciable en $\vec A$. **Punto silla:** crítico pero no extremo.

**Condición necesaria (Fermat):** si $f$ es diferenciable en $\vec A$ y tiene un extremo local allí, $\nabla f(\vec A) = \vec 0$.

**Extremos libres en $\mathbb{R}^2$** — criterio del hessiano en un punto con $\nabla f = \vec 0$ y $f \in C^2$:

$$H = f''_{xx}f''_{yy} - (f''_{xy})^2$$

| Condición | Conclusión |
|---|---|
| $H > 0$, $f''_{xx} > 0$ | mínimo local |
| $H > 0$, $f''_{xx} < 0$ | máximo local |
| $H < 0$ | punto silla |
| $H = 0$ | no decide: estudiar $f(\vec A + \vec h) - f(\vec A)$ por caminos |

**Extremos ligados (Lagrange):** extremos de $f$ sujetos a $g = 0$. Si $\nabla g \ne \vec 0$ en el punto, los candidatos cumplen

$$\nabla f = \lambda\nabla g, \qquad g = 0$$

Alternativa: despejar de la restricción y reemplazar (queda un problema de una variable).

**Extremos absolutos en un compacto:**

1. Puntos críticos interiores ($\nabla f = \vec 0$).
2. Extremos sobre la frontera (parametrizar cada tramo o usar Lagrange), incluidos los vértices.
3. Evaluar $f$ en todos los candidatos: el mayor es el máximo absoluto y el menor, el mínimo (Weierstrass garantiza que existen).

**Extremos de una función implícita** $F(x,y,z) = 0$: puntos con $F'_x = F'_y = 0$; en ellos $z''_{ij} = -\frac{F''_{ij}}{F'_z}$ y se aplica el hessiano.

Ejemplos: [Simulacro P4](simulacro-primer-parcial.md), [Repaso R4, R8](repaso-primer-parcial.md), [1.er Parcial 15/10/2019, E4](primer-parcial-2019-10-15.md).

---

## 13. Tabla: tipo de ejercicio → método

| Si el enunciado pide… | Usar |
|---|---|
| Resolver una EDO de 1.er orden | Identificar el tipo (sección 1) |
| Familia ortogonal, o curva definida por su tangente | EDO de la familia y $y' \to -1/y'$ (sección 2) |
| "Analizar continuidad" en un punto | Límite por caminos / acotación (secciones 4–5) |
| "Derivadas direccionales en el origen" | Definición por límite (sección 6) |
| "¿Es diferenciable?" | Continuidad, linealidad de las direccionales, definición (sección 7) |
| Dirección de máximo crecimiento, derivada máxima o nula | $\nabla f$ y su norma (sección 7) |
| Plano tangente / recta normal / aproximación lineal | Gradiente en el punto (secciones 7–8) |
| Recta tangente a una curva intersección | $\nabla F\wedge\nabla G$ (sección 8) |
| Derivada de una composición | Regla de la cadena; evaluar $f$ en el punto intermedio (sección 9) |
| $z$ definida por una ecuación | Cauchy–Dini, verificando hipótesis (sección 10) |
| Aproximar un valor "a segundo orden" | Taylor de orden 2 (sección 11) |
| Extremos locales | $\nabla f = \vec 0$ y hessiano (sección 12) |
| Extremos con restricción | Lagrange (sección 12) |
| Máximo y mínimo en una región cerrada y acotada | Interior + frontera + comparar (sección 12) |

---

[Volver al menú principal](../README.md)
