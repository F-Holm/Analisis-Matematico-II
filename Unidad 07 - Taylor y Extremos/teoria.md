# Unidad 7 — Polinomio de Taylor y extremos

Resumen del material teórico de la unidad ([U07-Teoria-Taylor-Extremos.pdf](../aula-virtual/07-Taylor-Extremos/U07-Teoria-Taylor-Extremos.pdf)), de las [notas de clase sobre extremos](../aula-virtual/07-Taylor-Extremos/Notas-2021-06-29-Extremos.pdf) y de la hoja [Condición suficiente para $n = 3$](../aula-virtual/07-Taylor-Extremos/Extremos-Condicion-Suficiente-n3.pdf).

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

## 6. Estrategia para los ejercicios

1. **Taylor:** calcular todas las derivadas necesarias **numéricamente en el punto**, y después armar el polinomio. Revisar el factor $\frac12$ y el $2$ de la derivada cruzada.
2. **Extremos libres:**
   - resolver $\nabla f = \vec 0$, factorizando y separando casos ("$x = 0$ o $y = 0$");
   - calcular el Hessiano en cada punto y clasificar;
   - si $H = 0$, analizar el signo de $f - f(\vec A)$ por caminos.
3. **Absolutos en una región:** interior + frontera + comparación.
4. **Con restricción:** sustitución si es fácil; si no, Lagrange.

---

## 7. Resumen de fórmulas

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
