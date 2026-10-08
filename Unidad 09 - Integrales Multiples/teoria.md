# Unidad 9 — Integrales múltiples

Resumen del material teórico de la unidad ([U09-Teoria-Integrales-Multiples.pdf](../aula-virtual/09-Integrales-Multiples/U09-Teoria-Integrales-Multiples.pdf)) y de los apuntes [Cambio de variables en integrales múltiples](../aula-virtual/09-Integrales-Multiples/Cambio-Variables-Integrales-Multiples.pdf) y [Aplicaciones de las integrales múltiples](../aula-virtual/09-Integrales-Multiples/Aplicaciones-Integrales-Multiples.pdf).

**Objetivos de la unidad:**

1. Plantear integrales dobles y triples con los límites correctos (en ambos órdenes).
2. Usar cambios de variables: polares, cilíndricas, esféricas y transformaciones lineales.
3. Calcular áreas, volúmenes, masas, centros de masa y momentos de inercia.

---

## 1. Integral doble

**Idea:** $\iint_D f(x,y)\,dA$ es el límite de las sumas de Riemann $\sum f(x_i,y_i)\,\Delta A_i$. Si $f \ge 0$, es el **volumen** bajo la gráfica de $f$ sobre $D$.

**Propiedades:**

- Es lineal.
- Es aditiva respecto de la región: $\iint_{D_1\cup D_2} = \iint_{D_1} + \iint_{D_2}$ si $D_1$ y $D_2$ no se superponen.
- Conjuntos de área nula (curvas, puntos) no cambian el valor de la integral.

**Área de una región:** $A(D) = \iint_D dA$.

### Teorema de Fubini (integrales iteradas)

**Región tipo I** (entre dos funciones de $x$): $D = \{a \le x \le b,\ g_1(x) \le y \le g_2(x)\}$.

$$\iint_D f\,dA = \int_a^b dx\int_{g_1(x)}^{g_2(x)} f(x,y)\,dy$$

**Región tipo II** (entre dos funciones de $y$): $D = \{c \le y \le d,\ h_1(y) \le x \le h_2(y)\}$.

$$\iint_D f\,dA = \int_c^d dy\int_{h_1(y)}^{h_2(y)} f(x,y)\,dx$$

**Cómo plantear los límites:**

1. **Dibujar la región.**
2. Hallar las **intersecciones** de las curvas del borde.
3. Para el orden $dy\,dx$: recorrer con rectas **verticales**. "¿Por qué curva entra?" da el límite inferior de $y$; "¿por cuál sale?" da el superior. Si la curva de entrada o de salida cambia, **partir** la región.
4. Los límites exteriores son **constantes**.

**Invertir el orden de integración:** a veces la integral interna no tiene primitiva elemental (por ejemplo $\int e^{x^2}dx$). Se reescribe la **misma región** en el otro orden.

**Simetría:**

- Si $D$ es simétrica respecto del eje $y$ y $f$ es impar en $x$, la integral es 0.
- Análogamente con el eje $x$ y $f$ impar en $y$.

---

## 2. Cambio de variables

Si $T(u,v) = (x(u,v), y(u,v))$ es biyectiva y $C^1$ de $D^*$ en $D$, con jacobiano no nulo (salvo en un conjunto de área nula):

$$\boxed{\iint_D f(x,y)\,dx\,dy = \iint_{D^*} f(x(u,v), y(u,v))\,\left|\frac{\partial(x,y)}{\partial(u,v)}\right|\,du\,dv}$$

$$\frac{\partial(x,y)}{\partial(u,v)} = \det\begin{pmatrix} x'_u & x'_v \\ y'_u & y'_v \end{pmatrix}$$

**Interpretación geométrica:** $|J|\,du\,dv$ es el área del "paralelogramo" imagen de un rectangulito $du\times dv$. El jacobiano es el **factor de escala de áreas**.

> Si es más fácil calcular $\dfrac{\partial(u,v)}{\partial(x,y)}$, vale $\dfrac{\partial(x,y)}{\partial(u,v)} = \dfrac{1}{\partial(u,v)/\partial(x,y)}$.

### Coordenadas polares

$$x = \rho\cos\varphi, \quad y = \rho\operatorname{sen}\varphi, \qquad |J| = \rho \qquad \Rightarrow \qquad dx\,dy = \rho\,d\rho\,d\varphi$$

Son útiles con círculos, sectores, anillos y expresiones $x^2 + y^2 = \rho^2$.

- Circunferencia $x^2 + y^2 = 2ax$: $\rho = 2a\cos\varphi$, con $\varphi\in[-\pi/2, \pi/2]$.
- Recta $x = c$: $\rho = c/\cos\varphi$.
- Recta $y = c$: $\rho = c/\operatorname{sen}\varphi$.
- Recta $y = mx$: $\varphi = \arctan m$.

**Polares "elípticas":** $x = a\rho\cos\varphi$, $y = b\rho\operatorname{sen}\varphi$, con $|J| = ab\,\rho$. Transforman la elipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = \rho^2$ en un círculo.

### Transformaciones lineales

Si la región está limitada por rectas como $x + y = c_1$ y $x - y = c_2$, conviene tomar $u = x + y$, $v = x - y$. La región pasa a ser un rectángulo, y el jacobiano es constante.

**Ejemplo:** $|x| + |y| \le 4 \iff |x - y| \le 4$ y $|x + y| \le 4$.

---

## 3. Integral triple

$$\iiint_H f\,dV = \iint_{D_{xy}} dx\,dy\int_{z_1(x,y)}^{z_2(x,y)} f\,dz$$

Para las integrales triples:

- $D_{xy}$ es la **proyección** del cuerpo sobre el plano $xy$.
- $z_1$ y $z_2$ son las superficies "piso" y "techo".
- Se proyecta igualando las dos superficies que limitan: por ejemplo, si $x^2 \le z \le 32 - x^2 - 2y^2$, la proyección es $x^2 + y^2 \le 16$.

**Volumen:** $V = \iiint_H dV = \iint_{D}(z_{\text{techo}} - z_{\text{piso}})\,dA$.

### Coordenadas cilíndricas

$$x = \rho\cos\varphi, \quad y = \rho\operatorname{sen}\varphi, \quad z = z, \qquad dV = \rho\,d\rho\,d\varphi\,dz$$

**Superficies coordenadas:**

- $\rho$ constante: cilindros de eje $z$;
- $\varphi$ constante: semiplanos que contienen al eje $z$;
- $z$ constante: planos horizontales.

El eje puede ser cualquiera: por ejemplo, alrededor del eje $x$ se toma $y = \rho\cos\varphi$, $z = \rho\operatorname{sen}\varphi$.

### Coordenadas esféricas

$$x = r\operatorname{sen}\theta\cos\varphi, \quad y = r\operatorname{sen}\theta\operatorname{sen}\varphi, \quad z = r\cos\theta, \qquad dV = r^2\operatorname{sen}\theta\,dr\,d\theta\,d\varphi$$

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
| Masa | $M = \iint_D\delta\,dA$ | $M = \iiint_H\delta\,dV$ |
| Centro de masa | $x_G = \frac1M\iint x\,\delta\,dA$, … | $x_G = \frac1M\iiint x\,\delta\,dV$, … |
| Momento de inercia respecto de un eje | $I = \iint d^2\,\delta\,dA$ | $I = \iiint d^2\,\delta\,dV$ |

Las distancias habituales son:

- al eje $x$: $\sqrt{y^2 + z^2}$ (en el plano, $|y|$);
- al eje $z$: $\sqrt{x^2+y^2}$;
- al plano $yz$: $|x|$.

- **"Densidad proporcional a la distancia a ..."** significa $\delta = k\cdot\text{distancia}$, con $k$ constante.
- **Simetría:** si el cuerpo y la densidad son simétricos respecto de un plano, el centro de masa está en ese plano.
- **Steiner:** $I_r = I_G + M\,d^2$. El momento de inercia respecto de rectas paralelas es mínimo cuando la recta pasa por el centro de masa.

---

## 5. La integral de Gauss

$$\iint_{\mathbb{R}^2}e^{-x^2-y^2}\,dA = \int_0^{2\pi}\!\!\int_0^\infty e^{-\rho^2}\rho\,d\rho\,d\varphi = \pi \ \Rightarrow\ \int_{-\infty}^{\infty}e^{-u^2}\,du = \sqrt\pi$$

En cartesianas, la integral doble se separa en el producto de dos integrales iguales. Así se demuestra que la densidad normal $\frac{1}{\sqrt{2\pi}}e^{-z^2/2}$ integra 1.

---

## 6. Estrategia para los ejercicios

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

## 7. Resumen de fórmulas

| Concepto | Fórmula |
|---|---|
| Área | $\iint_D dA$ |
| Volumen | $\iiint_H dV = \iint_D(z_2 - z_1)\,dA$ |
| Cambio de variables | $dx\,dy = \lvert\partial(x,y)/\partial(u,v)\rvert\,du\,dv$ |
| Polares | $dx\,dy = \rho\,d\rho\,d\varphi$ |
| Polares elípticas | $dx\,dy = ab\,\rho\,d\rho\,d\varphi$ |
| Cilíndricas | $dV = \rho\,d\rho\,d\varphi\,dz$ |
| Esféricas | $dV = r^2\operatorname{sen}\theta\,dr\,d\theta\,d\varphi$ |
| Masa | $\int\delta$ |
| Centro de masa | $\frac{1}{M}\int x\,\delta$ |
| Inercia | $\int d^2\,\delta$ |

---

[← Volver al menú principal](../README.md)
