# Unidad 9 — Integrales múltiples

Resumen del material teórico de la unidad ([U09-Teoria-Integrales-Multiples.pdf](../aula-virtual/09-Integrales-Multiples/U09-Teoria-Integrales-Multiples.pdf)) y de los apuntes [Cambio de variables en integrales múltiples](../aula-virtual/09-Integrales-Multiples/Cambio-Variables-Integrales-Multiples.pdf) y [Aplicaciones de las integrales múltiples](../aula-virtual/09-Integrales-Multiples/Aplicaciones-Integrales-Multiples.pdf), complementado con el [resumen de UTNianos](../UTNianos/Resumen%20AM2.pdf).

**Objetivos de la unidad:**

1. Plantear integrales dobles y triples con los límites correctos (en ambos órdenes).
2. Usar cambios de variables: polares, cilíndricas, esféricas y transformaciones lineales.
3. Calcular áreas, volúmenes, masas, centros de masa y momentos de inercia.

---

## 1. Integral doble

**Idea:** $\iint_D f(x,y)\thinspace dA$ es el límite de las sumas de Riemann $\sum f(x_i,y_i)\thinspace\Delta A_i$. Si $f \ge 0$, es el **volumen** bajo la gráfica de $f$ sobre $D$.

**Propiedades:**

- Es lineal.
- Es aditiva respecto de la región: $\iint_{D_1\cup D_2} = \iint_{D_1} + \iint_{D_2}$ si $D_1$ y $D_2$ no se superponen.
- Conjuntos de área nula (curvas, puntos) no cambian el valor de la integral.

**Área de una región:** $A(D) = \iint_D dA$.

### Teorema de Fubini (integrales iteradas)

**Región tipo I** (entre dos funciones de $x$): $D = \lbrace a \le x \le b,\ g_1(x) \le y \le g_2(x)\rbrace$.

$$\iint_D f\thinspace dA = \int_a^b dx\int_{g_1(x)}^{g_2(x)} f(x,y)\thinspace dy$$

**Región tipo II** (entre dos funciones de $y$): $D = \lbrace c \le y \le d,\ h_1(y) \le x \le h_2(y)\rbrace$.

$$\iint_D f\thinspace dA = \int_c^d dy\int_{h_1(y)}^{h_2(y)} f(x,y)\thinspace dx$$

**Cómo plantear los límites:**

1. **Dibujar la región.**
2. Hallar las **intersecciones** de las curvas del borde.
3. Para el orden $dy\thinspace dx$: recorrer con rectas **verticales**. "¿Por qué curva entra?" da el límite inferior de $y$; "¿por cuál sale?" da el superior. Si la curva de entrada o de salida cambia, **partir** la región.
4. Los límites exteriores son **constantes**.

**Invertir el orden de integración:** a veces la integral interna no tiene primitiva elemental (por ejemplo $\int e^{x^2}dx$). Se reescribe la **misma región** en el otro orden.

**Simetría:**

- Si $D$ es simétrica respecto del eje $y$ y $f$ es impar en $x$, la integral es 0.
- Análogamente con el eje $x$ y $f$ impar en $y$.

---

## 2. Cambio de variables

Si $T(u,v) = (x(u,v), y(u,v))$ es biyectiva y $C^1$ de $D^*$ en $D$, con jacobiano no nulo (salvo en un conjunto de área nula):

$$\boxed{\iint_D f(x,y)\thinspace dx\thinspace dy = \iint_{D^*} f(x(u,v), y(u,v))\thinspace\left|\frac{\partial(x,y)}{\partial(u,v)}\right|\thinspace du\thinspace dv}$$

$$\frac{\partial(x,y)}{\partial(u,v)} = \det\begin{pmatrix} x'_u & x'_v \cr y'_u & y'_v \end{pmatrix}$$

**Interpretación geométrica:** $|J|\thinspace du\thinspace dv$ es el área del "paralelogramo" imagen de un rectangulito $du\times dv$. El jacobiano es el **factor de escala de áreas**.

> Si es más fácil calcular $\dfrac{\partial(u,v)}{\partial(x,y)}$, vale $\dfrac{\partial(x,y)}{\partial(u,v)} = \dfrac{1}{\partial(u,v)/\partial(x,y)}$.

### Coordenadas polares

$$x = \rho\cos\varphi, \quad y = \rho\mathop{\mathrm{sen}}\varphi, \qquad |J| = \rho \qquad \Rightarrow \qquad dx\thinspace dy = \rho\thinspace d\rho\thinspace d\varphi$$

Son útiles con círculos, sectores, anillos y expresiones $x^2 + y^2 = \rho^2$.

- Circunferencia $x^2 + y^2 = 2ax$: $\rho = 2a\cos\varphi$, con $\varphi\in[-\pi/2, \pi/2]$.
- Recta $x = c$: $\rho = c/\cos\varphi$.
- Recta $y = c$: $\rho = c/\mathop{\mathrm{sen}}\varphi$.
- Recta $y = mx$: $\varphi = \arctan m$.

**Polares "elípticas":** $x = a\rho\cos\varphi$, $y = b\rho\mathop{\mathrm{sen}}\varphi$, con $|J| = ab\thinspace\rho$. Transforman la elipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = \rho^2$ en un círculo.

### Transformaciones lineales

Si la región está limitada por rectas como $x + y = c_1$ y $x - y = c_2$, conviene tomar $u = x + y$, $v = x - y$. La región pasa a ser un rectángulo, y el jacobiano es constante.

**Ejemplo:** $|x| + |y| \le 4 \iff |x - y| \le 4$ y $|x + y| \le 4$.

---

## 3. Integral triple

$$\iiint_H f\thinspace dV = \iint_{D_{xy}} dx\thinspace dy\int_{z_1(x,y)}^{z_2(x,y)} f\thinspace dz$$

Para las integrales triples:

- $D_{xy}$ es la **proyección** del cuerpo sobre el plano $xy$.
- $z_1$ y $z_2$ son las superficies "piso" y "techo".
- Se proyecta igualando las dos superficies que limitan: por ejemplo, si $x^2 \le z \le 32 - x^2 - 2y^2$, la proyección es $x^2 + y^2 \le 16$.

**Volumen:** $V = \iiint_H dV = \iint_{D}(z_{\text{techo}} - z_{\text{piso}})\thinspace dA$.

### Coordenadas cilíndricas

$$x = \rho\cos\varphi, \quad y = \rho\mathop{\mathrm{sen}}\varphi, \quad z = z, \qquad dV = \rho\thinspace d\rho\thinspace d\varphi\thinspace dz$$

**Superficies coordenadas:**

- $\rho$ constante: cilindros de eje $z$;
- $\varphi$ constante: semiplanos que contienen al eje $z$;
- $z$ constante: planos horizontales.

El eje puede ser cualquiera: por ejemplo, alrededor del eje $x$ se toma $y = \rho\cos\varphi$, $z = \rho\mathop{\mathrm{sen}}\varphi$.

### Coordenadas esféricas

$$x = r\mathop{\mathrm{sen}}\theta\cos\varphi, \quad y = r\mathop{\mathrm{sen}}\theta\mathop{\mathrm{sen}}\varphi, \quad z = r\cos\theta, \qquad dV = r^2\mathop{\mathrm{sen}}\theta\thinspace dr\thinspace d\theta\thinspace d\varphi$$

Con $r \ge 0$, $\theta\in[0,\pi]$ (ángulo con el semieje $z^+$) y $\varphi\in[0, 2\pi]$.

**Superficies coordenadas:**

- $r$ constante: esferas;
- $\theta$ constante: conos de eje $z$;
- $\varphi$ constante: semiplanos.

**Ejemplo:** el cono $z = \sqrt{x^2+y^2}$ es $\theta = \pi/4$.

> En polares, cilíndricas y esféricas el jacobiano se anula en el eje o en el origen. Eso **no impide** usarlas: son conjuntos de medida nula.

---

## 4. Aplicaciones físicas

Con densidad $\delta$ (superficial en placas, volumétrica en cuerpos):

| Magnitud | Placa ($\iint$) | Cuerpo ($\iiint$) |
|---|---|---|
| Masa | $M = \iint_D\delta\thinspace dA$ | $M = \iiint_H\delta\thinspace dV$ |
| Centro de masa | $x_G = \frac1M\iint x\thinspace\delta\thinspace dA$, … | $x_G = \frac1M\iiint x\thinspace\delta\thinspace dV$, … |
| Momento de inercia respecto de un eje | $I = \iint d^2\thinspace\delta\thinspace dA$ | $I = \iiint d^2\thinspace\delta\thinspace dV$ |

Las distancias habituales son:

- al eje $x$: $\sqrt{y^2 + z^2}$ (en el plano, $|y|$);
- al eje $z$: $\sqrt{x^2+y^2}$;
- al plano $yz$: $|x|$.

- **"Densidad proporcional a la distancia a ..."** significa $\delta = k\cdot\text{distancia}$, con $k$ constante.
- **Simetría:** si el cuerpo y la densidad son simétricos respecto de un plano, el centro de masa está en ese plano.
- **Steiner:** $I_r = I_G + M\thinspace d^2$. El momento de inercia respecto de rectas paralelas es mínimo cuando la recta pasa por el centro de masa.

---

## 5. La integral de Gauss

$$\iint_{\mathbb{R}^2}e^{-x^2-y^2}\thinspace dA = \int_0^{2\pi}\negthinspace\negthinspace\int_0^\infty e^{-\rho^2}\rho\thinspace d\rho\thinspace d\varphi = \pi \ \Rightarrow\ \int_{-\infty}^{\infty}e^{-u^2}\thinspace du = \sqrt\pi$$

En cartesianas, la integral doble se separa en el producto de dos integrales iguales. Así se demuestra que la densidad normal $\frac{1}{\sqrt{2\pi}}e^{-z^2/2}$ integra 1.

---

## 6. Complementos: definición de la integral doble

**Sumas inferiores y superiores.** Sea $F$ continua y $\ge 0$ en el rectángulo $A = [a,b]\times[c,d]$. Se quiere el volumen del sólido entre $z = 0$ y $z = F$. Por Weierstrass, $F$ alcanza un mínimo $m$ y un máximo $M$, y $(b-a)(d-c)\thinspace m \le V \le (b-a)(d-c)\thinspace M$.

Se hace una partición $P$ de $[a,b]$ y de $[c,d]$ en subrectángulos $R_{ij}$ de área $\Delta x_i\Delta y_j$, y en cada uno $F$ tiene mínimo $m_{ij}$ y máximo $M_{ij}$:

$$\underline S_P = \sum_i\sum_j m_{ij}\thinspace\Delta x_i\Delta y_j \le V \le \overline S_P = \sum_i\sum_j M_{ij}\thinspace\Delta x_i\Delta y_j$$

- $\underline S_P$ es el volumen de los prismas **inscriptos** (aproximación por defecto) y $\overline S_P$ el de los **circunscriptos** (por exceso).
- Al refinar la partición, las inferiores crecen y las superiores decrecen, y la diferencia se achica. Ambas sucesiones tienen un **límite común**: la **integral doble**.

**Sumas de Riemann.** Eligiendo un punto arbitrario $P_{ij}$ en cada subrectángulo, $\underline S_P \le \sum F(P_{ij})\Delta x_i\Delta y_j \le \overline S_P$, y en el límite:

$$\iint_A F\thinspace dx\thinspace dy = \lim_{n,m\to\infty}\sum_i\sum_j F(P_{ij})\thinspace\Delta x_i\thinspace\Delta y_j$$

**Condiciones de integrabilidad** ($F$ definida y acotada en $A$):

1. $F$ es integrable $\iff$ para todo $\varepsilon > 0$ existe una partición con $\overline S_P - \underline S_P < \varepsilon$.
2. Si $F$ es continua en $A$, es integrable.
3. También es integrable si sus discontinuidades forman un conjunto de **medida nula**.

**Medida nula:** $A \subseteq \mathbb{R}^2$ tiene medida nula si para todo $\varepsilon > 0$ se puede cubrir con finitos rectángulos de área total menor que $\varepsilon$. Ejemplos: un segmento, una circunferencia, un arco de parábola.

**Propiedades:**

- Si $A_1$ y $A_2$ se cortan en un conjunto de medida nula y $A_1\cup A_2 = A$: $\iint_A = \iint_{A_1} + \iint_{A_2}$.
- $\iint(F + G) = \iint F + \iint G$.

---

## 7. Complementos: por qué la integral doble se calcula con integrales iteradas

**Recinto rectangular (secciones).** Cortando el sólido con el plano $x = x_0$, el área de la sección es $A(x_0) = \int_c^dF(x_0, y)\thinspace dy$. El volumen es la "suma" de esas secciones:

$$V = \lim\sum A(c_i)\thinspace\Delta x_i = \int_a^bA(x)\thinspace dx = \int_a^b dx\int_c^d F(x,y)\thinspace dy$$

Cortando con $y = $ cte se obtiene el otro orden, y ambos dan lo mismo.

**Recintos no rectangulares.** Un recinto **simple de tipo I** es $a \le x \le b$, $y_1(x) \le y \le y_2(x)$; uno de **tipo II** es $c \le y \le d$, $x_1(y) \le x \le x_2(y)$. Los demás se descomponen en uniones de recintos simples.

Para integrar sobre $D$ (tipo I), se lo encierra en un rectángulo $A$ y se define

$$F^*(x,y) = \begin{cases} F(x,y) & (x,y) \in D \cr 0 & (x,y) \in A - D \end{cases}$$

$F^*$ es integrable (sus discontinuidades están en el borde de $D$, de medida nula), y en cada vertical sólo aporta el tramo entre $y_1(x)$ e $y_2(x)$:

$$\iint_D F = \iint_A F^* = \int_a^b dx\int_{y_1(x)}^{y_2(x)}F(x,y)\thinspace dy$$

### De dónde sale el $\rho$ de las polares

Una partición en $\rho$ y $\varphi$ divide el recinto en **trapecios circulares** (entre dos circunferencias y dos semirrectas). Su área es

$$A_{ij} = \tfrac12(\rho_2^2 - \rho_1^2)\Delta\varphi = \tfrac{\rho_1 + \rho_2}{2}(\rho_2 - \rho_1)\Delta\varphi = \rho_m\thinspace\Delta\rho\thinspace\Delta\varphi$$

y por eso $dA = \rho\thinspace d\rho\thinspace d\varphi$. El mismo factor sale como el **jacobiano** de la transformación:

$$\frac{\partial(x,y)}{\partial(\rho,\varphi)} = \begin{vmatrix} \cos\varphi & -\rho\mathop{\mathrm{sen}}\varphi \cr \mathop{\mathrm{sen}}\varphi & \rho\cos\varphi \end{vmatrix} = \rho(\cos^2\varphi + \mathop{\mathrm{sen}}\nolimits^2\varphi) = \rho$$

Como el factor representa un área, se toma siempre su **módulo** (cambiar el orden de filas o columnas cambia el signo del determinante).

**Teorema de cambio de variables (hipótesis).** Sean $D$ y $D^*$ regiones simples y $T: D^* \to D$, $T(u,v) = (x(u,v), y(u,v))$, de clase $C^1$, **inyectiva** y con $T(D^*) = D$. Si $F$ es integrable en $D$:

$$\iint_D F(x,y)\thinspace dx\thinspace dy = \iint_{D^*}F(x(u,v), y(u,v))\left\lvert\frac{\partial(x,y)}{\partial(u,v)}\right\rvert du\thinspace dv$$

Pedir que $T$ sea inyectiva y "sobre" $D$ va de la mano con pedir $\frac{\partial(x,y)}{\partial(u,v)} \ne 0$ en $D^*$.

---

## 8. Complementos: integrales triples

**Definición.** En un prisma $A = [a,b]\times[c,d]\times[e,f]$, con particiones regulares y un punto arbitrario en cada prisma elemental de volumen $\Delta x_i\Delta y_j\Delta z_k$:

$$\iiint_A F\thinspace dx\thinspace dy\thinspace dz = \lim\sum_i\sum_j\sum_k F(\alpha_i, \beta_j, \gamma_k)\thinspace\Delta x_i\Delta y_j\Delta z_k$$

Si $F$ es continua (o sus discontinuidades tienen medida nula) es integrable, y se calcula con **tres integrales iteradas**. Hay **6 órdenes** posibles, todos iguales. Para un recinto $V$ cualquiera se usa el mismo truco de extender por 0 en un prisma que lo contenga.

**Tipos de recintos:**

| Tipo | Descripción |
|---|---|
| I | $(x,y)$ en una región plana; $z_1(x,y) \le z \le z_2(x,y)$ |
| II | $(x,z)$ en una región plana; $y_1(x,z) \le y \le y_2(x,z)$ |
| III | $(y,z)$ en una región plana; $x_1(y,z) \le x \le x_2(y,z)$ |

**Cilíndricas:** con $\rho$ constante se obtienen cilindros de eje $z$; con $\varphi$ constante, semiplanos de borde $z$; con $z$ constante, planos horizontales. El elemento de volumen es (área del trapecio circular)·$\Delta z$ = $\rho\thinspace\Delta\rho\thinspace\Delta\varphi\thinspace\Delta z$, que coincide con el jacobiano $\rho$.

**Esféricas:** con $r$ la distancia al origen, $\lambda$ (o $\theta$) el ángulo con el semieje $z^+$ ($\lambda \in [0,\pi]$) y $\varphi$ el ángulo de la proyección con el semieje $x^+$:

$$x = r\mathop{\mathrm{sen}}\lambda\cos\varphi, \quad y = r\mathop{\mathrm{sen}}\lambda\mathop{\mathrm{sen}}\varphi, \quad z = r\cos\lambda, \qquad x^2 + y^2 + z^2 = r^2$$

El jacobiano vale $r^2\mathop{\mathrm{sen}}\lambda$. Geométricamente, el elemento de volumen es un "ladrillo" de aristas $\Delta r$, $r\Delta\lambda$ (arco de meridiano) y $r\mathop{\mathrm{sen}}\lambda\thinspace\Delta\varphi$ (arco de paralelo):

$$\Delta V = \Delta r\cdot r\thinspace\Delta\lambda\cdot r\mathop{\mathrm{sen}}\lambda\thinspace\Delta\varphi = r^2\mathop{\mathrm{sen}}\lambda\thinspace\Delta r\thinspace\Delta\lambda\thinspace\Delta\varphi$$

---

## 9. Complementos: momentos estáticos y de inercia

**Momento estático de primer orden** de una masa puntual respecto de un eje (o plano): masa · distancia. Para una lámina $D$ con densidad $\delta(x,y)$:

$$M_x = \iint_D y\thinspace\delta\thinspace dx\thinspace dy, \qquad M_y = \iint_D x\thinspace\delta\thinspace dx\thinspace dy$$

Para un sólido $V$: $M_{xy} = \iiint z\thinspace\delta$, $M_{yz} = \iiint x\thinspace\delta$, $M_{xz} = \iiint y\thinspace\delta$.

**Centro de masa:** es el punto donde habría que concentrar toda la masa para conservar los momentos estáticos: $x_G = \dfrac{M_y}{M}$, $y_G = \dfrac{M_x}{M}$ (lámina), y $x_G = \dfrac{M_{yz}}{M}$, $y_G = \dfrac{M_{xz}}{M}$, $z_G = \dfrac{M_{xy}}{M}$ (sólido).

**Momentos de inercia** ($I = m\thinspace d^2$ para una masa puntual):

| | Respecto del eje $x$ | Respecto del eje $y$ | Respecto del eje $z$ |
|---|---|---|---|
| Lámina | $\iint y^2\delta$ | $\iint x^2\delta$ | $\iint(x^2 + y^2)\delta$ |
| Sólido | $\iiint(y^2 + z^2)\delta$ | $\iiint(x^2 + z^2)\delta$ | $\iiint(x^2 + y^2)\delta$ |

---

## 10. Estrategia para los ejercicios

1. **Dibujar la región o el cuerpo** y hallar las intersecciones.
2. **Elegir las coordenadas:**
   - **cartesianas** con rectas y parábolas;
   - **polares o cilíndricas** con círculos y $x^2+y^2$;
   - **esféricas** con esferas y conos;
   - **lineales** con rectas oblicuas.
3. **Plantear los límites** (del más interno al más externo) y **no olvidar el jacobiano**.
4. Integrar de adentro hacia afuera. Si una integral es imposible, cambiar el orden o las coordenadas.
5. **Controlar:** áreas y volúmenes positivos, y simetrías.

---

## 11. Resumen de fórmulas

| Concepto | Fórmula |
|---|---|
| Área | $\iint_D dA$ |
| Volumen | $\iiint_H dV = \iint_D(z_2 - z_1)\thinspace dA$ |
| Cambio de variables | $dx\thinspace dy = \lvert\partial(x,y)/\partial(u,v)\rvert\thinspace du\thinspace dv$ |
| Polares | $dx\thinspace dy = \rho\thinspace d\rho\thinspace d\varphi$ |
| Polares elípticas | $dx\thinspace dy = ab\thinspace\rho\thinspace d\rho\thinspace d\varphi$ |
| Cilíndricas | $dV = \rho\thinspace d\rho\thinspace d\varphi\thinspace dz$ |
| Esféricas | $dV = r^2\mathop{\mathrm{sen}}\theta\thinspace dr\thinspace d\theta\thinspace d\varphi$ |
| Masa | $\int\delta$ |
| Centro de masa | $\frac{1}{M}\int x\thinspace\delta$ |
| Inercia | $\int d^2\thinspace\delta$ |

---

[← Volver al menú principal](../README.md)
