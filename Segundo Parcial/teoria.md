# Teoría para el 2.º Parcial (Unidades 8 a 12)

Guía de todo lo que hace falta para resolver un 2.º parcial: definiciones y enunciados tal como se piden en los ejercicios teóricos ("Enuncie…", "Defina…"), y recetas paso a paso para cada tipo de ejercicio práctico. El detalle de cada tema está en el `teoria.md` de cada unidad y las fórmulas en una sola página en el [resumen de fórmulas](../FORMULAS.md).

**Formato habitual del examen:** 2 ejercicios teóricos + 4 prácticos. Para aprobar los TP hacen falta al menos dos prácticos bien (los teóricos no cuentan); para aspirar a promoción, cuatro bien con al menos un teórico.

**Índice**

1. [Curvas e integrales de línea](#1-curvas-e-integrales-de-línea)
2. [Campos conservativos y función potencial](#2-campos-conservativos-y-función-potencial)
3. [Líneas de campo](#3-líneas-de-campo)
4. [Integrales dobles y triples, cambios de variable](#4-integrales-dobles-y-triples-cambios-de-variable)
5. [Superficies: área, masa y flujo](#5-superficies-área-masa-y-flujo)
6. [Divergencia y rotor](#6-divergencia-y-rotor)
7. [Teorema de Green](#7-teorema-de-green)
8. [Teorema de la divergencia (Gauss)](#8-teorema-de-la-divergencia-gauss)
9. [Teorema del rotor (Stokes)](#9-teorema-del-rotor-stokes)
10. [Ecuaciones diferenciales lineales de orden 2 y superior](#10-ecuaciones-diferenciales-lineales-de-orden-2-y-superior)
11. [Tabla: tipo de ejercicio → método](#11-tabla-tipo-de-ejercicio--método)
12. [Errores frecuentes](#12-errores-frecuentes)

---

## 1. Curvas e integrales de línea

Detalle: [Unidad 8](../Unidad%2008%20-%20Curvas%20e%20Integrales%20de%20Linea/teoria.md).

**Curva:** imagen de una función $\vec g: [a,b] \to \mathbb{R}^n$ continua. **Suave** si $\vec g \in C^1$ y $\vec g' \ne \vec 0$; **simple** si no se corta a sí misma; **cerrada** si $\vec g(a) = \vec g(b)$.

**Parametrizaciones que siempre aparecen:**

| Curva | Parametrización |
|---|---|
| Segmento de $A$ a $B$ | $\vec g(t) = A + t(B - A)$, $0 \le t \le 1$ |
| Circunferencia $(x - a)^2 + (y - b)^2 = R^2$ | $(a + R\cos t,\ b + R\mathop{\mathrm{sen}}t)$ |
| Elipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ | $(a\cos t,\ b\mathop{\mathrm{sen}}t)$ |
| Gráfico $y = f(x)$ | $(x,\ f(x))$ |
| Intersección de un cilindro $x^2 + y^2 = R^2$ con una superficie $z = h(x,y)$ | $(R\cos t,\ R\mathop{\mathrm{sen}}t,\ h(R\cos t, R\mathop{\mathrm{sen}}t))$ |
| Intersección de un plano con una cuádrica | Reemplazar el plano en la cuádrica para obtener la proyección (elipse o circunferencia) y después despejar la coordenada restante |

Para $(t_0 \le t \le t_1)$ el sentido de recorrido es el de $t$ creciente: verificar que coincide con el pedido.

**Integrales:**

| Qué | Fórmula |
|---|---|
| Longitud | $L = \int_a^b\Vert\vec g'(t)\Vert\thinspace dt$ |
| Campo escalar (masa de un alambre, etc.) | $\int_C f\thinspace ds = \int_a^b f(\vec g(t))\thinspace\Vert\vec g'(t)\Vert\thinspace dt$ |
| Campo vectorial (trabajo, circulación) | $\int_C\vec f\cdot d\vec s = \int_a^b\vec f(\vec g(t))\cdot\vec g'(t)\thinspace dt$ |

La integral de un campo escalar **no** depende del sentido; la de un campo vectorial **cambia de signo** al invertirlo. "Circulación" = integral de línea de un campo vectorial (sobre una curva cerrada o no).

---

## 2. Campos conservativos y función potencial

**Definiciones:** $\vec f$ es **conservativo** (campo de gradientes) en un abierto $D$ si existe $\varphi: D \to \mathbb{R}$ diferenciable con $\nabla\varphi = \vec f$; $\varphi$ es una **función potencial**.

**Teorema (condición necesaria y suficiente):** sea $\vec f$ continuo en un abierto conexo $D$. Son equivalentes:

1. $\vec f$ admite función potencial en $D$.
2. $\int_C\vec f\cdot d\vec s$ depende solo de los extremos de $C$ (para toda curva suave a trozos en $D$).
3. $\oint_C\vec f\cdot d\vec s = 0$ para toda curva cerrada suave a trozos en $D$.

Y en ese caso $\int_C\vec f\cdot d\vec s = \varphi(B) - \varphi(A)$ (**teorema fundamental de las integrales de línea**).

**Condición necesaria:** si $\vec f \in C^1$ es conservativo, su **matriz jacobiana es simétrica**: en $\mathbb{R}^2$, $P'_y = Q'_x$; en $\mathbb{R}^3$, $\nabla\times\vec f = \vec 0$.

**Condición suficiente:** jacobiana simétrica **en un dominio simplemente conexo** ⇒ conservativo.

**Receta para hallar el potencial:**

1. Verificar simetría (y que el dominio sea simplemente conexo, si no se conoce el potencial).
2. $\varphi = \int P\thinspace dx + D(y,z)$.
3. Derivar respecto de $y$, igualar a $Q$, despejar $D'_y$ e integrar. Repetir con $z$.
4. Comprobar $\nabla\varphi = \vec f$.

**Truco muy usado — separar la parte conservativa:** si $\vec f = \nabla\varphi + \vec g$ con $\vec g$ simple, la parte gradiente aporta $\varphi(B) - \varphi(A)$ (o 0 en una curva cerrada) y solo hay que calcular la integral de $\vec g$ (directamente, o con Green/Stokes).

**Campos con parámetros o funciones incógnita** ($g(x)$, $a$, $b$): imponer la simetría $P'_y = Q'_x$ y resolver la ecuación (muchas veces es una EDO para $g$), usando las condiciones dadas.

### El caso singular (aparece en casi todos los parciales)

$$\vec f(x,y) = \left(\frac{-y}{x^2 + y^2},\ \frac{x}{x^2 + y^2}\right), \qquad D = \mathbb{R}^2 - \lbrace\vec 0\rbrace$$

- La jacobiana es simétrica en $D$, pero $D$ **no** es simplemente conexo.
- Sobre la circunferencia unitaria antihoraria, $\oint\vec f\cdot d\vec s = 2\pi \ne 0$ ⇒ **no** es conservativo en $D$.
- **Toda** curva cerrada simple positiva que rodea el origen da $2\pi$ (Green en la región entre la curva y una circunferencia chica); las que no lo rodean dan 0.
- Sí es conservativo en un dominio simplemente conexo sin el origen (por ejemplo, el plano menos una semirrecta): potencial $\varphi = \theta$, el ángulo polar.
- Variantes: $\frac{(-y, x)}{a x^2 + b y^2}$ da $\frac{2\pi}{\sqrt{ab}}$ (calcular sobre la elipse $ax^2 + by^2 = 1$, donde el denominador vale 1); un factor $k$ multiplica el resultado.

**Contraste:** $\vec f = \left(\frac{2x}{x^2 + y^2}, \frac{2y}{x^2 + y^2}\right) = \nabla\ln(x^2 + y^2)$ **sí** es conservativo en $\mathbb{R}^2 - \lbrace\vec 0\rbrace$: el potencial está definido en todo el dominio. Su circulación sobre cualquier curva cerrada es 0, y sobre un arco es la diferencia de $\ln(x^2 + y^2)$ entre los extremos.

**Varias singularidades** (dominio $\mathbb{R}^2 - \lbrace A, B\rbrace$ con jacobiana simétrica): la circulación sobre una curva que rodea a $A$ y a $B$ es la suma de las circulaciones sobre curvas chicas alrededor de cada una (con la misma orientación). Ejemplo: [2.º Parcial 01/12/2012, T2](segundo-parcial-2012-12-01.md).

---

## 3. Líneas de campo

**Definición:** las líneas de campo de $\vec f$ son las curvas cuyo vector tangente en cada punto es paralelo a $\vec f$.

**En $\mathbb{R}^2$:** $\dfrac{dy}{dx} = \dfrac{Q(x,y)}{P(x,y)}$; se resuelve la EDO de 1.er orden (en general, separable) y se elige la constante con el punto dado.

**En $\mathbb{R}^3$:** $\dfrac{dx}{P} = \dfrac{dy}{Q} = \dfrac{dz}{R}$ (sistema de dos EDO).

Usos típicos: área encerrada por una línea de campo, trabajo de otro campo a lo largo de ella, longitud de un arco.

---

## 4. Integrales dobles y triples, cambios de variable

Detalle: [Unidad 9](../Unidad%2009%20-%20Integrales%20Multiples/teoria.md).

**Fubini:** en una región elemental, $\iint_D f\thinspace dA = \int_a^b\int_{\varphi_1(x)}^{\varphi_2(x)}f\thinspace dy\thinspace dx$ (o en el otro orden).

**Teorema de cambio de variables:** si $\vec T: D^* \to D$, $(u,v) \mapsto (x,y)$, es $C^1$, biyectiva (salvo en un conjunto de área nula) y con jacobiano no nulo,

$$\iint_D f(x,y)\thinspace dx\thinspace dy = \iint_{D^*}f(\vec T(u,v))\left|\frac{\partial(x,y)}{\partial(u,v)}\right|du\thinspace dv$$

| Coordenadas | Transformación | $\lvert J\rvert$ |
|---|---|---|
| Polares | $x = r\cos\theta$, $y = r\mathop{\mathrm{sen}}\theta$ | $r$ |
| Polares desplazadas (centro $(a,b)$) | $x = a + r\cos\theta$, $y = b + r\mathop{\mathrm{sen}}\theta$ | $r$ |
| Polares elípticas | $x = a\thinspace r\cos\theta$, $y = b\thinspace r\mathop{\mathrm{sen}}\theta$ | $ab\thinspace r$ |
| Cilíndricas | $(r\cos\theta,\ r\mathop{\mathrm{sen}}\theta,\ z)$ | $r$ |
| Cilíndricas con eje $y$ | $x = r\cos\theta$, $z = r\mathop{\mathrm{sen}}\theta$, $y = y$ | $r$ |
| Esféricas | $x = \rho\mathop{\mathrm{sen}}\varphi\cos\theta$, $y = \rho\mathop{\mathrm{sen}}\varphi\mathop{\mathrm{sen}}\theta$, $z = \rho\cos\varphi$ | $\rho^2\mathop{\mathrm{sen}}\varphi$ |
| Lineal $u = ax + by$, $v = cx + dy$ | $\left\lvert\frac{\partial(x,y)}{\partial(u,v)}\right\rvert = \frac{1}{\lvert ad - bc\rvert}$ | |

**Aplicaciones:** área $\iint_D dA$; volumen $\iiint_H dV$ o $\iint_D(z_{sup} - z_{inf})\thinspace dA$; masa $\iiint\delta\thinspace dV$; centro de masa $\bar x = \frac1M\iiint x\delta\thinspace dV$; momento de inercia respecto de un eje $\iiint d^2\delta\thinspace dV$.

**Receta para volúmenes y masas:**

1. Dibujar o identificar las superficies: $z = \sqrt{x^2 + y^2}$ cono, $z = a - x^2 - y^2$ paraboloide, $x^2 + y^2 + z^2 = R^2$ esfera, $x^2 + y^2 = R^2$ cilindro, $ax + by + cz = d$ plano.
2. Hallar la intersección (igualar) ⇒ da la proyección (casi siempre un disco).
3. Decidir cuál superficie está arriba (probar un punto).
4. Elegir coordenadas según la simetría; cuidado con el eje de simetría (puede ser $y$ o $x$).
5. Usar simetrías: la integral de una función impar sobre una región simétrica es 0 (por ejemplo, $\iint y\thinspace dA = 0$ en un disco centrado en el eje $x$), e $\iint_D x\thinspace dA = \bar x\cdot\text{Área}$ con el centroide.

**"Densidad proporcional a la distancia a…":** al eje $z$: $k\sqrt{x^2 + y^2}$; al eje $y$: $k\sqrt{x^2 + z^2}$; al origen: $k\sqrt{x^2 + y^2 + z^2}$; al plano $xy$: $k|z|$.

**Cambiar el orden de integración:** dibujar la región a partir de los límites y volver a describirla en el otro orden.

---

## 5. Superficies: área, masa y flujo

Detalle: [Unidad 10](../Unidad%2010%20-%20Integrales%20de%20Superficie/teoria.md).

**Superficie paramétrica:** $\vec\Sigma: D \subset \mathbb{R}^2 \to \mathbb{R}^3$; vector normal $\vec n = \vec\Sigma'_u\wedge\vec\Sigma'_v$. **Suave** si $\vec n \ne \vec 0$. **Orientable** si se puede elegir una normal unitaria que varíe con continuidad.

**Parametrizaciones típicas:**

| Superficie | Parametrización | Normal |
|---|---|---|
| Gráfico $z = f(x,y)$ | $(x,\ y,\ f(x,y))$ | $(-f'_x,\ -f'_y,\ 1)$ (hacia arriba) |
| Gráfico $y = f(x,z)$ | $(x,\ f(x,z),\ z)$ | $\pm(-f'_x,\ 1,\ -f'_z)$ |
| Cono $z = \sqrt{x^2 + y^2}$ | $(x,\ y,\ \sqrt{x^2 + y^2})$ | $\Vert\vec n\Vert = \sqrt2$ |
| Cilindro $x^2 + y^2 = R^2$ | $(R\cos\theta,\ R\mathop{\mathrm{sen}}\theta,\ z)$ | $(R\cos\theta,\ R\mathop{\mathrm{sen}}\theta,\ 0)$ (exterior) |
| Esfera de radio $R$ | $(R\mathop{\mathrm{sen}}\varphi\cos\theta,\ R\mathop{\mathrm{sen}}\varphi\mathop{\mathrm{sen}}\theta,\ R\cos\varphi)$ | $\Vert\vec n\Vert = R^2\mathop{\mathrm{sen}}\varphi$ (exterior) |
| Plano $z = a + bx + cy$ | $(x,\ y,\ a + bx + cy)$ | $(-b,\ -c,\ 1)$, $\Vert\vec n\Vert = \sqrt{1 + b^2 + c^2}$ |

**Integrales:**

| Qué | Fórmula |
|---|---|
| Área | $A = \iint_D\Vert\vec\Sigma'_u\wedge\vec\Sigma'_v\Vert\thinspace du\thinspace dv$; para $z = f(x,y)$: $\iint_D\sqrt{1 + f'^2_x + f'^2_y}\thinspace dx\thinspace dy$ |
| Masa de una chapa | $M = \iint_S\delta\thinspace dS = \iint_D\delta(\vec\Sigma)\thinspace\Vert\vec n\Vert\thinspace du\thinspace dv$ |
| Flujo | $\Phi = \iint_S\vec f\cdot\breve n\thinspace dS = \iint_D\vec f(\vec\Sigma(u,v))\cdot(\vec\Sigma'_u\wedge\vec\Sigma'_v)\thinspace du\thinspace dv$ |

En el flujo **no** se divide por la norma: el producto escalar va con el vector normal sin normalizar. Si $\vec\Sigma'_u\wedge\vec\Sigma'_v$ apunta al revés de lo elegido, se cambia el signo.

**Orientación — "indique la orientación elegida":** siempre decir con palabras qué normal se usó ("normal hacia arriba", "normal exterior", "$\vec n = (2x, 1, 0)$") y que con la opuesta el flujo cambia de signo.

**Cuidado con la densidad:** si $\delta$ trae un factor como $\frac{1}{\sqrt{1 + 4x^2 + 4y^2}}$, suele simplificarse con $\Vert\vec n\Vert$.

---

## 6. Divergencia y rotor

Para $\vec f = (P, Q, R)$:

$$\operatorname{div}\vec f = \nabla\cdot\vec f = P'_x + Q'_y + R'_z$$

$$\operatorname{rot}\vec f = \nabla\times\vec f = (R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y)$$

**Propiedades** (con funciones $C^2$):

- $\nabla\times(\nabla\varphi) = \vec 0$: el rotor de un gradiente es nulo.
- $\operatorname{div}(\nabla\times\vec f) = 0$: la divergencia de un rotor es nula. Por eso el **flujo de un rotor a través de una superficie cerrada es 0**.
- $\operatorname{div}(\nabla\varphi) = \Delta\varphi$ (laplaciano).
- **Solenoidal:** $\operatorname{div}\vec f = 0$. **Irrotacional:** $\nabla\times\vec f = \vec 0$.

**Truco:** términos como $h(z)$ en la primera componente, $\mu(x)$ en la tercera o $\mathop{\mathrm{sen}}(y^2)$ en la primera **no aportan a la divergencia** (no dependen de la variable que se deriva). En el rotor, $g(x)$ en $P$, $g(y)$ en $Q$ o $g(z)$ en $R$ tampoco aportan.

---

## 7. Teorema de Green

Detalle: [Unidad 11](../Unidad%2011%20-%20Teoremas%20Integrales/teoria.md).

**Enunciado:** sea $D \subset \mathbb{R}^2$ una región acotada cuya frontera $C = \partial D$ es una curva cerrada, simple, suave a trozos y orientada positivamente (dejando $D$ a la izquierda), y sea $\vec f = (P, Q)$ de clase $C^1$ en un abierto que contiene a $D$. Entonces

$$\oint_C P\thinspace dx + Q\thinspace dy = \iint_D(Q'_x - P'_y)\thinspace dx\thinspace dy$$

Vale también para regiones con agujeros: la frontera exterior antihoraria y las interiores horarias.

**Áreas con integrales de línea:** con un campo tal que $Q'_x - P'_y = 1$:

$$\text{Área}(D) = \oint_C x\thinspace dy = -\oint_C y\thinspace dx = \frac12\oint_C(x\thinspace dy - y\thinspace dx)$$

Si al calcular sale negativo, la parametrización recorría la curva en sentido horario: el área es el valor absoluto.

**Recetas:**

- **Circulación sobre una curva cerrada en el plano:** calcular $Q'_x - P'_y$ (normalmente se simplifica mucho) e integrar sobre la región (en polares si es circular).
- **Circulación sobre una curva abierta:** cerrarla con un segmento (sobre un eje si es posible), aplicar Green a la curva cerrada y restar la integral sobre el segmento. Cuidar el sentido: si la curva cerrada queda horaria, Green lleva un signo menos.
- **"Para toda curva cerrada vale $k$ veces el área"**: imponer $Q'_x - P'_y = k$ en todo punto.
- **Campo con singularidad dentro de la región:** Green no se aplica directamente; rodear la singularidad con una curva chica (sección 2).

---

## 8. Teorema de la divergencia (Gauss)

**Enunciado:** sea $H \subset \mathbb{R}^3$ un sólido acotado cuya frontera $\partial H$ es una superficie cerrada, suave a trozos, orientada con la **normal exterior**, y sea $\vec f$ de clase $C^1$ en un abierto que contiene a $H$. Entonces

$$\iint_{\partial H}\vec f\cdot\breve n\thinspace dS = \iiint_H\operatorname{div}\vec f\thinspace dV$$

**Recetas:**

- **Flujo saliente por la frontera de un sólido:** calcular la divergencia (suele ser una constante o algo simple) e integrar sobre el sólido. Si $\operatorname{div}\vec f = c$, el flujo es $c\cdot V$.
- **Flujo por una superficie abierta** (semiesfera, paraboloide, cono): **cerrarla con una tapa** plana, aplicar Gauss al sólido y restar el flujo por la tapa (sobre la tapa el campo suele simplificarse; a veces el enunciado da el campo solo sobre el plano de la tapa).
- **Datos incompletos** (se conoce $\operatorname{div}\vec f$ y $\vec f$ sobre un plano): exactamente la receta anterior.
- Si el campo no es $C^1$ en todo el sólido (por ejemplo, singular en el origen), excluir una bola chica.

---

## 9. Teorema del rotor (Stokes)

**Enunciado:** sea $S$ una superficie orientable, suave a trozos, con normal $\breve n$, cuyo borde $\partial S$ es una curva cerrada simple, suave a trozos, **orientada de forma coherente con $\breve n$** (regla de la mano derecha: caminando por el borde con la cabeza hacia $\breve n$, la superficie queda a la izquierda). Si $\vec f$ es $C^1$ en un abierto que contiene a $S$,

$$\oint_{\partial S}\vec f\cdot d\vec s = \iint_S(\nabla\times\vec f)\cdot\breve n\thinspace dS$$

**Consecuencia:** dos superficies con el **mismo borde** (y orientación coherente) tienen el mismo flujo del rotor. Se puede reemplazar la superficie dada por la más simple con ese borde (casi siempre un disco plano).

**Recetas:**

- **Circulación sobre la curva intersección de dos superficies:** elegir como $S$ la porción del **plano** (o la superficie más simple) que la curva encierra, calcular $\nabla\times\vec f$ y su flujo. Si un término del campo es un gradiente, sacarlo antes (sección 2).
- **Flujo del rotor por una superficie** (cono, paraboloide, semiesfera): calcular la circulación sobre el borde, o el flujo del rotor por el disco que tiene el mismo borde. En un disco horizontal solo hace falta la componente $z$ del rotor, $Q'_x - P'_y$.
- **Superficie cerrada:** el flujo del rotor es 0.
- **Indicar la orientación:** decir la normal elegida y el sentido inducido en la curva ("antihorario visto desde arriba", o la lista de vértices recorridos).

---

## 10. Ecuaciones diferenciales lineales de orden 2 y superior

Detalle: [Unidad 12](../Unidad%2012%20-%20Ecuaciones%20Diferenciales%20II/teoria.md).

**Estructura de la solución:** para $y^{(n)} + a_{n-1}y^{(n-1)} + \dots + a_0y = q(x)$ con coeficientes constantes,

$$y = y_h + y_p$$

donde $y_h$ es la solución general de la homogénea ($n$ constantes) e $y_p$ una solución particular.

**Homogénea:** ecuación característica $r^n + a_{n-1}r^{n-1} + \dots + a_0 = 0$.

| Raíces | Aporte a $y_h$ |
|---|---|
| Real simple $r$ | $Ce^{rx}$ |
| Real doble $r$ | $(C_1 + C_2x)e^{rx}$ |
| Real de multiplicidad $m$ | $(C_1 + C_2x + \dots + C_mx^{m-1})e^{rx}$ |
| Complejas $\alpha \pm \beta i$ | $e^{\alpha x}(C_1\cos\beta x + C_2\mathop{\mathrm{sen}}\beta x)$ |

**Particular por coeficientes indeterminados:**

| $q(x)$ | Proponer $y_p$ |
|---|---|
| Polinomio de grado $k$ | Polinomio completo de grado $k$ |
| $Ae^{ax}$ | $Be^{ax}$ |
| $P_k(x)e^{ax}$ | $Q_k(x)e^{ax}$ (polinomio completo) |
| $A\cos bx + B\mathop{\mathrm{sen}}bx$ | $C\cos bx + D\mathop{\mathrm{sen}}bx$ (siempre los dos) |

**Resonancia:** si la propuesta (o parte de ella) ya es solución de la homogénea, multiplicarla por $x^m$, con $m$ la multiplicidad de la raíz correspondiente ($a$ en $e^{ax}$; $0$ para polinomios; $bi$ para senos y cosenos). Ejemplo: $y'' + 3y' = x$ tiene $r = 0$ simple ⇒ $y_p = x(Ax + B)$.

**Tipos de ejercicio:**

- **Armar la EDO desde sus soluciones:** cada solución da una raíz: $e^{rx} \to r$; $xe^{rx} \to r$ doble; $x \to 0$ doble; $x^2 \to 0$ triple; $\cos bx$ o $\mathop{\mathrm{sen}}bx \to \pm bi$. El polinomio característico es el producto de los factores y su grado es el orden mínimo.
- **"$y_1 = xe^{2x}$ es solución de la homogénea; hallar $a$ y $b$":** $r = 2$ es doble ⇒ $(r - 2)^2 = r^2 - 4r + 4$.
- **Recta tangente como condición inicial:** "en $(0, y_0)$ tiene recta tangente $y = mx + c$" ⇒ $y(0) = c$ e $y'(0) = m$.
- **Forma de $y_p$ sin calcularla:** escribir la propuesta con resonancia.
- **EDO de un campo:** a veces la condición de campo conservativo, solenoidal o "circulación $= k\cdot$área" da una EDO para una función incógnita.

---

## 11. Tabla: tipo de ejercicio → método

| Si el enunciado pide… | Usar |
|---|---|
| Trabajo o circulación sobre un arco, campo con jacobiana simétrica | Potencial y $\varphi(B) - \varphi(A)$ (sección 2) |
| Trabajo o circulación sobre un arco, campo **no** conservativo | Parametrizar, o cerrar la curva y usar Green/Stokes (secciones 1, 7, 9) |
| Circulación sobre una curva cerrada plana | Green (sección 7) |
| Circulación sobre una curva cerrada en el espacio | Stokes con la superficie más simple (sección 9) |
| Circulación sobre una curva que rodea una singularidad | Comparar con una circunferencia o elipse chica (sección 2) |
| ¿Admite potencial? | Simetría + dominio simplemente conexo, o una circulación cerrada no nula (sección 2) |
| Hallar $g$ o parámetros para que sea conservativo | $P'_y = Q'_x$ ⇒ EDO o ecuación (secciones 2 y 10) |
| Área de una región plana con integrales de línea | $\oint x\thinspace dy$ (sección 7) |
| Área de una región plana con integrales dobles | $\iint dA$, polares o elípticas (sección 4) |
| Volumen o masa de un sólido | Integral triple; cilíndricas o esféricas (sección 4) |
| Área o masa de una superficie | $\iint\Vert\vec n\Vert$ o $\iint\delta\Vert\vec n\Vert$ (sección 5) |
| Flujo por una superficie abierta | Directo con $\vec\Sigma'_u\wedge\vec\Sigma'_v$, o cerrar y Gauss (secciones 5 y 8) |
| Flujo por la frontera de un sólido | Gauss (sección 8) |
| Flujo de un rotor | Stokes: circulación sobre el borde o disco con el mismo borde (sección 9) |
| Líneas de campo | $dy/dx = Q/P$ (sección 3) |
| Resolver una EDO lineal | Característica + coeficientes indeterminados (sección 10) |
| EDO de menor orden con soluciones dadas | Raíces y su multiplicidad (sección 10) |

---

## 12. Errores frecuentes

- **No indicar la orientación** cuando se pide: se pierde el ejercicio aunque la cuenta esté bien.
- **Aplicar Green o Gauss con una singularidad dentro** de la región.
- **Concluir que es conservativo solo porque la jacobiana es simétrica** sin revisar que el dominio sea simplemente conexo.
- **Olvidar la tapa** al cerrar una superficie, o restarla con la normal equivocada (la normal de la tapa debe ser exterior al sólido).
- **Olvidar el jacobiano** ($r$, $\rho^2\mathop{\mathrm{sen}}\varphi$, $ab\thinspace r$).
- **Normalizar la normal en el flujo** (no se divide por $\Vert\vec n\Vert$) o **no normalizarla en el área** (ahí sí va $\Vert\vec n\Vert$).
- **Sentido del borde en Stokes** incoherente con la normal elegida.
- En EDO, **no aplicar resonancia** cuando la propuesta ya es solución de la homogénea, o proponer solo $\cos$ sin $\mathop{\mathrm{sen}}$.
- En "recta tangente $y = mx + c$ en $x = 0$", confundir $y(0) = c$ con $y'(0) = m$.

---

[Volver al menú principal](../README.md)
