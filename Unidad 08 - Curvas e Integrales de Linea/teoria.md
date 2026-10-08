# Unidad 8 — Curvas, integrales de línea y función potencial

Resumen del material teórico de la unidad ([U08-Teoria-Curvas-Integrales-Linea.pdf](../aula-virtual/08-Curvas-Integrales-Linea/U08-Teoria-Curvas-Integrales-Linea.pdf)) y de los apuntes [Repaso de curvas](../aula-virtual/08-Curvas-Integrales-Linea/Repaso-Curvas.pdf), [Propiedades de la derivada de una función vectorial](../aula-virtual/08-Curvas-Integrales-Linea/Derivada-Funcion-Vectorial-Propiedades.pdf), [Resumen de integrales de línea](../aula-virtual/08-Curvas-Integrales-Linea/Resumen-Integrales-Linea.pdf), [Aplicaciones](../aula-virtual/08-Curvas-Integrales-Linea/Aplicaciones-Integrales-Linea.pdf) y [Condiciones de existencia de la función potencial](../aula-virtual/08-Curvas-Integrales-Linea/Funcion-Potencial-Condiciones.pdf).

**Objetivos de la unidad:**

1. Parametrizar curvas y calcular longitudes de arco.
2. Calcular integrales de línea de campos escalares (masa, centro de masa) y vectoriales (trabajo, circulación).
3. Reconocer campos conservativos y hallar su función potencial.

---

## 1. Curvas parametrizadas

Una **trayectoria** es una función continua $\vec g: [a,b] \to \mathbb{R}^n$. Su imagen $C$ es una **curva**, de ecuación $\vec X = \vec g(t)$.

- **Orientación:** la parametrización impone un sentido de recorrido, el de $t$ creciente.
- **Regular:** existe $\vec g'$ y $\vec g' \ne \vec 0$ en todo $[a,b]$. **Suave:** además $\vec g'$ es continua.
- **Suave a trozos:** se puede partir $[a,b]$ en finitos tramos suaves (por ejemplo, una poligonal).
- **Cerrada:** $\vec g(a) = \vec g(b)$. **Simple:** no se corta a sí misma.
- En curvas planas cerradas simples, la **orientación positiva** es la antihoraria (la región queda a la izquierda).

### Parametrizaciones típicas

| Curva | Parametrización |
|---|---|
| Gráfico $y = f(x)$, $x\in[a,b]$ | $(t,\ f(t))$ |
| Segmento de $A$ a $B$ | $A + t\,(B - A)$, $\ t\in[0,1]$ |
| Circunferencia de centro $(x_0,y_0)$ y radio $R$ (antihoraria) | $(x_0 + R\cos t,\ y_0 + R\operatorname{sen}t)$, $\ t\in[0,2\pi]$ |
| Elipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ | $(a\cos t,\ b\operatorname{sen}t)$ |
| Hélice | $(R\cos t,\ R\operatorname{sen}t,\ ct)$ |

**Invertir el sentido:** si $\vec g$ va de $A$ a $B$ con $t\in[a,b]$, entonces $\vec g(a + b - u)$, con $u\in[a,b]$, recorre la misma curva de $B$ a $A$. Otra forma es intercambiar $\cos$ y $\operatorname{sen}$ en una circunferencia.

**Curva intersección de dos superficies:** se despejan variables o se usa la ecuación más simple para parametrizar (ver Unidad 4).

### Derivada de funciones vectoriales

Se deriva **componente a componente**. Valen las propiedades:

- $(k\vec f)' = k\vec f'$ y $(\vec f + \vec g)' = \vec f' + \vec g'$;
- $(\vec f\cdot\vec g)' = \vec f'\cdot\vec g + \vec f\cdot\vec g'$;
- $(\vec f\times\vec g)' = \vec f'\times\vec g + \vec f\times\vec g'$.

**Consecuencia:** si $\lVert\vec h\rVert$ es constante, entonces $\vec h\perp\vec h'$.

**Cinemática:** si $\vec X(t)$ es la posición, la velocidad es $\vec v = \vec X'$ (tangente a la trayectoria) y la aceleración es $\vec a = \vec X''$.

![Figura 8.23: recta tangente y plano normal a una curva en un punto](img/teoria-fig-8-23-recta-tangente-plano-normal.png)

---

## 2. Longitud de arco

$$L(C) = \int_a^b \lVert\vec g\,'(t)\rVert\,dt, \qquad ds = \lVert\vec g\,'(t)\rVert\,dt$$

La longitud **no depende de la parametrización** ni de la orientación.

Para una curva suave a trozos, se suman las longitudes de cada tramo.

**Integrales útiles:**

$$\int\sqrt{1 + u^2}\,du = \frac{u\sqrt{1+u^2}}{2} + \frac{\operatorname{argsenh}(u)}{2} + C, \qquad \int u\sqrt{a + bu^2}\,du = \frac{(a + bu^2)^{3/2}}{3b} + C$$

### Abscisa curvilínea, triedro de Frenet y curvaturas

- **Abscisa curvilínea:** $s = \lambda(t) = \int_{t_0}^t \lVert\vec g'(u)\rVert\,du$. Despejando $t = \lambda^{-1}(s)$ se obtiene la **ecuación normal** $\vec X = \vec G(s)$, que recorre la curva con velocidad 1.
- **Versor tangente:** $T = \dfrac{\vec g'}{\lVert\vec g'\rVert}$.
- **Versor binormal:** $B = \dfrac{\vec g'\times\vec g''}{\lVert\vec g'\times\vec g''\rVert}$.
- **Versor normal principal:** $N = B\times T$.
- **Planos:**
  - **normal**, perpendicular a $T$;
  - **osculador**, perpendicular a $B$ (contiene a $T$ y $N$);
  - **rectificante**, perpendicular a $N$.
- **Curvatura de flexión** y **torsión**:

$$cf = \frac{\lVert\vec g'\times\vec g''\rVert}{\lVert\vec g'\rVert^3}, \qquad ct = -\frac{(\vec g'\times\vec g'')\cdot\vec g'''}{\lVert\vec g'\times\vec g''\rVert^2}$$

- **Radio de curvatura:** $\rho = 1/cf$. El **centro de curvatura** es $\vec X_0 + \rho\,N$.
- **Casos particulares:** una recta tiene $cf = 0$; una circunferencia de radio $R$ tiene $cf = 1/R$; una curva plana tiene torsión 0.
- **Aceleración:** $\vec a = s''\,T + (s')^2\,cf\,N$. Siempre está en el plano osculador.

---

## 3. Integral de línea de un campo escalar

$$\int_C f\,ds = \int_a^b f(\vec g(t))\,\lVert\vec g\,'(t)\rVert\,dt$$

- **No depende** de la parametrización ni de la orientación.
- Con $f = 1$ da la longitud.

**Aplicaciones (alambres)**, con densidad lineal $\delta$:

| Magnitud | Fórmula |
|---|---|
| Masa | $M = \int_C \delta\,ds$ |
| Centro de masa | $x_{CM} = \dfrac{1}{M}\int_C x\,\delta\,ds$ (ídem $y$, $z$) |
| Momento de inercia respecto de un eje | $I = \int_C d^2\,\delta\,ds$ ($d$ = distancia al eje) |
| Resistencia de un hilo (resistividad lineal $\rho$) | $R = \int_C \rho\,ds$ |

"Proporcional a la distancia a ..." significa $\delta = k\cdot\text{distancia}$, con $k$ constante.

---

## 4. Integral de línea de un campo vectorial (trabajo, circulación)

$$\int_C \vec f\cdot d\vec s = \int_a^b \vec f(\vec g(t))\cdot\vec g\,'(t)\,dt = \int_C P\,dx + Q\,dy\ (+\,R\,dz)$$

- Sólo cuenta la **componente tangencial** del campo: $\vec f\cdot d\vec s = (\vec f\cdot T)\,ds$.
- **Cambia de signo** si se invierte la orientación.
- Si la curva es cerrada se llama **circulación** y se escribe $\oint_C$.

![Figura 8.35: sólo la componente tangencial f_T del campo contribuye a la integral de línea](img/teoria-fig-8-35-componente-tangencial.png)

**Casos útiles:**

- **Campo constante sobre un segmento:** $\int_{\overline{AB}}\vec F\cdot d\vec s = \vec F\cdot(B - A)$ (trabajo = fuerza · desplazamiento).
- **Campo tangente de módulo constante $H$:** $\int_C \vec H\cdot d\vec s = H\cdot L(C)$.
- **Fuerza proporcional a la velocidad** ($\vec F = k\vec v$): su circulación sobre una trayectoria cerrada es $k\int\lVert\vec v\rVert^2dt \ne 0$ ⇒ no es conservativa.

---

## 5. Campos conservativos y función potencial

$\vec f$ es un **campo de gradientes** (conservativo) si existe $\phi$ con $\nabla\phi = \vec f$. A $\phi$ se la llama **función potencial**. En física se usa $U = -\phi$, que da $\vec f = -\nabla U$.

**Teorema (independencia del camino):** si $\vec f = \nabla\phi$ es continuo y $C$ va de $A$ a $B$:

$$\boxed{\int_C \vec f\cdot d\vec s = \phi(B) - \phi(A)}$$

Es como la regla de Barrow: **sólo importan los extremos**.

**Equivalencias** (para $\vec f$ continuo en un abierto conexo):

$$\vec f = \nabla\phi \iff \oint_C\vec f\cdot d\vec s = 0 \ \ \forall C \text{ cerrada} \iff \int_C\vec f\cdot d\vec s \text{ no depende del camino}$$

### Condición necesaria: matriz jacobiana simétrica

Si $\vec f = \nabla\phi$ con $\phi \in C^2$, por Schwarz $D\vec f$ (el Hessiano de $\phi$) es **simétrica**:

- en $\mathbb{R}^2$: $P'_y = Q'_x$;
- en $\mathbb{R}^3$: $P'_y = Q'_x$, $\ P'_z = R'_x$, $\ Q'_z = R'_y$.

**Si no es simétrica ⇒ NO admite potencial.**

### ¿Cuándo la simetría alcanza?

- Si el dominio es **simplemente conexo** (por ejemplo todo $\mathbb{R}^2$, $\mathbb{R}^3$, un disco, un semiplano), la jacobiana simétrica y continua **garantiza** que existe la potencial.
- Si el dominio **tiene "agujeros"** (por ejemplo $\mathbb{R}^2 - \{\vec 0\}$), la simetría no alcanza: hay que verificar que la circulación alrededor de cada agujero sea 0.

**Ejemplo clásico:** $\vec f = \left(\dfrac{y}{x^2+y^2}, \dfrac{-x}{x^2+y^2}\right)$ tiene jacobiana simétrica, pero su circulación sobre una circunferencia centrada en el origen es $-2\pi \ne 0$ ⇒ **no** es conservativo en $\mathbb{R}^2 - \{\vec 0\}$.

### Cómo hallar la función potencial

1. Verificar la simetría de $D\vec f$.
2. Integrar la primera componente respecto de $x$: $\phi = \int P\,dx + g(y,z)$.
3. Derivar respecto de $y$ e igualar a $Q$ ⇒ despejar $g'_y$ ⇒ integrar ⇒ $g = \dots + h(z)$.
4. Derivar respecto de $z$ e igualar a $R$ ⇒ despejar $h'$ ⇒ integrar.
5. $\phi$ queda determinada salvo una constante $C$.

---

## 6. Estrategia para los ejercicios

1. **Longitud o integral de un campo escalar:** parametrizar, calcular $\lVert\vec g'\rVert$, armar $\int f(\vec g(t))\lVert\vec g'\rVert\,dt$ e integrar.
2. **Trabajo o circulación:**
   - ¿El campo es conservativo (jacobiana simétrica en un dominio simplemente conexo)? Entonces se usa $\phi(B) - \phi(A)$, que suele ser mucho más fácil.
   - Si no, parametrizar **respetando el sentido** pedido y calcular $\int \vec f(\vec g(t))\cdot\vec g'(t)\,dt$.
   - Para curvas cerradas planas, se puede usar Green (Unidad 11).
3. **Curvas por tramos:** sumar las integrales de cada tramo, cada uno parametrizado en el sentido correcto.

---

## 7. Resumen de fórmulas

| Concepto | Fórmula |
|---|---|
| Longitud | $\int_a^b\lVert\vec g'\rVert\,dt$ |
| Integral de campo escalar | $\int_C f\,ds = \int f(\vec g)\lVert\vec g'\rVert\,dt$ |
| Integral de campo vectorial | $\int_C\vec f\cdot d\vec s = \int\vec f(\vec g)\cdot\vec g'\,dt$ |
| Campo conservativo | $\int_C\nabla\phi\cdot d\vec s = \phi(B) - \phi(A)$ |
| Condición necesaria | $D\vec f$ simétrica |
| Curvatura de flexión | $\lVert\vec g'\times\vec g''\rVert/\lVert\vec g'\rVert^3$ |
| Torsión | $-\dfrac{(\vec g'\times\vec g'')\cdot\vec g'''}{\lVert\vec g'\times\vec g''\rVert^2}$ |
| Triedro | $T = \frac{\vec g'}{\lVert\vec g'\rVert}$, $B = \frac{\vec g'\times\vec g''}{\lVert\vec g'\times\vec g''\rVert}$, $N = B\times T$ |

---

[← Volver al menú principal](../README.md)
