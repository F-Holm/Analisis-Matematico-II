# Teoría y guía de ejercicios para el 1.er Parcial (Unidades 1 a 7)

Esta guía explica la teoría que se evalúa y muestra, **tipo por tipo**, cómo resolver cada ejercicio que puede aparecer en un 1.er parcial. Cada tipo tiene la misma estructura: cómo reconocerlo, el método paso a paso y un ejercicio resuelto en el que se explica por qué se hace cada cosa.

Los ejemplos salen de parciales reales, del simulacro y del repaso de la cátedra. Cuando un tema no aparece en esos materiales, el ejemplo viene de la guía de trabajos prácticos. El detalle de cada tema está en el `teoria.md` de cada unidad y las fórmulas, en el [resumen de fórmulas](../FORMULAS.md).

**Formato habitual del examen:** 2 ejercicios teóricos + 4 prácticos. Para aprobar los TP hacen falta al menos dos prácticos bien (los teóricos no cuentan), lo que equivale a un 6. Para aspirar a promoción hacen falta cuatro ejercicios bien, con al menos un teórico (8D).

## Si el enunciado pide…

| Pedido | Ir a |
|---|---|
| Resolver una EDO de 1.er orden | [Tipo 1](#tipo-1-edo-de-variables-separables), [Tipo 2](#tipo-2-edo-lineal-de-1er-orden), [Tipo 4](#tipo-4-homogéneas-bernoulli-y-exactas) |
| Hallar un término de la EDO con una solución conocida | [Tipo 3](#tipo-3-hallar-un-término-de-la-edo-a-partir-de-una-solución) |
| EDO de 2.º orden sin $y$ | [Tipo 5](#tipo-5-edo-de-2º-orden-en-la-que-falta-y) |
| Familia ortogonal | [Tipo 6](#tipo-6-familia-de-curvas-ortogonales) |
| Curva definida por una propiedad de su tangente | [Tipo 7](#tipo-7-curva-definida-por-una-propiedad-de-su-tangente) |
| Dominio natural, clasificar puntos, abierto/cerrado/compacto | [Tipo 8](#tipo-8-dominio-natural), [Tipo 9](#tipo-9-análisis-topológico-de-un-conjunto) |
| "Analice la existencia del límite" | [Tipo 10](#tipo-10-probar-que-un-límite-no-existe), [Tipo 11](#tipo-11-probar-que-un-límite-existe) |
| "Halle $k$ para que sea continua" | [Tipo 12](#tipo-12-hallar-un-parámetro-para-que-sea-continua) |
| Continuidad y derivadas de una función partida | [Tipo 13](#tipo-13-derivadas-direccionales-por-definición), [Tipo 14](#tipo-14-continuidad-y-derivadas-de-una-función-partida) |
| "¿Es diferenciable?" | [Tipo 15](#tipo-15-es-diferenciable) |
| Dirección de máximo crecimiento, derivada máxima o nula | [Tipo 16](#tipo-16-dirección-de-máximo-crecimiento) |
| Plano tangente o recta normal a una superficie | [Tipo 17](#tipo-17-plano-tangente-a-una-superficie) |
| Aproximación lineal | [Tipo 18](#tipo-18-aproximación-lineal-con-el-plano-como-dato), [Tipo 22](#tipo-22-aproximación-de-una-composición) |
| Recta tangente a una curva intersección | [Tipo 19](#tipo-19-recta-tangente-a-una-curva-intersección) |
| Curva perpendicular a una superficie | [Tipo 20](#tipo-20-curva-perpendicular-a-una-superficie) |
| Punto regular y plano normal a una curva | [Tipo 21](#tipo-21-punto-regular-y-plano-normal-a-una-curva) |
| Derivada de una composición | [Tipo 22](#tipo-22-aproximación-de-una-composición), [Tipo 23](#tipo-23-direcciones-de-derivada-máxima-mínima-y-nula-de-una-composición) |
| $z$ definida por una ecuación, composición con implícita | [Tipo 24](#tipo-24-composición-con-una-función-implícita) |
| Polinomio de Taylor, aproximación de orden 2 | [Tipo 25](#tipo-25-polinomio-de-taylor-y-aproximación) |
| Puntos críticos y su clasificación | [Tipo 26](#tipo-26-puntos-críticos-y-clasificación), [Tipo 27](#tipo-27-el-hessiano-no-decide), [Tipo 28](#tipo-28-extremos-de-una-función-armada-con-datos) |
| Extremos con restricción | [Tipo 29](#tipo-29-extremos-con-restricción-lagrange) |
| Máximo y mínimo en una región cerrada y acotada | [Tipo 30](#tipo-30-extremos-absolutos-en-un-compacto) |
| Extremos de una función implícita | [Tipo 31](#tipo-31-extremos-de-una-función-implícita) |
| "Defina…", "Enuncie…", "Demuestre…" | [Tipo 32](#tipo-32-definiciones-enunciados-y-demostraciones) |

## Índice

- **[Bloque A: Ecuaciones diferenciales de 1.er orden](#bloque-a-ecuaciones-diferenciales-de-1er-orden)**
  - [Tipo 1: EDO de variables separables](#tipo-1-edo-de-variables-separables)
  - [Tipo 2: EDO lineal de 1.er orden](#tipo-2-edo-lineal-de-1er-orden)
  - [Tipo 3: Hallar un término de la EDO a partir de una solución](#tipo-3-hallar-un-término-de-la-edo-a-partir-de-una-solución)
  - [Tipo 4: Homogéneas, Bernoulli y exactas](#tipo-4-homogéneas-bernoulli-y-exactas)
  - [Tipo 5: EDO de 2.º orden en la que falta $y$](#tipo-5-edo-de-2º-orden-en-la-que-falta-y)
  - [Tipo 6: Familia de curvas ortogonales](#tipo-6-familia-de-curvas-ortogonales)
  - [Tipo 7: Curva definida por una propiedad de su tangente](#tipo-7-curva-definida-por-una-propiedad-de-su-tangente)
- **[Bloque B: Dominio y topología](#bloque-b-dominio-y-topología)**
  - [Tipo 8: Dominio natural](#tipo-8-dominio-natural)
  - [Tipo 9: Análisis topológico de un conjunto](#tipo-9-análisis-topológico-de-un-conjunto)
- **[Bloque C: Límite y continuidad](#bloque-c-límite-y-continuidad)**
  - [Tipo 10: Probar que un límite no existe](#tipo-10-probar-que-un-límite-no-existe)
  - [Tipo 11: Probar que un límite existe](#tipo-11-probar-que-un-límite-existe)
  - [Tipo 12: Hallar un parámetro para que sea continua](#tipo-12-hallar-un-parámetro-para-que-sea-continua)
- **[Bloque D: Derivadas y diferenciabilidad](#bloque-d-derivadas-y-diferenciabilidad)**
  - [Tipo 13: Derivadas direccionales por definición](#tipo-13-derivadas-direccionales-por-definición)
  - [Tipo 14: Continuidad y derivadas de una función partida](#tipo-14-continuidad-y-derivadas-de-una-función-partida)
  - [Tipo 15: ¿Es diferenciable?](#tipo-15-es-diferenciable)
  - [Tipo 16: Dirección de máximo crecimiento](#tipo-16-dirección-de-máximo-crecimiento)
- **[Bloque E: Rectas y planos tangentes](#bloque-e-rectas-y-planos-tangentes)**
  - [Tipo 17: Plano tangente a una superficie](#tipo-17-plano-tangente-a-una-superficie)
  - [Tipo 18: Aproximación lineal con el plano como dato](#tipo-18-aproximación-lineal-con-el-plano-como-dato)
  - [Tipo 19: Recta tangente a una curva intersección](#tipo-19-recta-tangente-a-una-curva-intersección)
  - [Tipo 20: Curva perpendicular a una superficie](#tipo-20-curva-perpendicular-a-una-superficie)
  - [Tipo 21: Punto regular y plano normal a una curva](#tipo-21-punto-regular-y-plano-normal-a-una-curva)
- **[Bloque F: Funciones compuestas e implícitas](#bloque-f-funciones-compuestas-e-implícitas)**
  - [Tipo 22: Aproximación de una composición](#tipo-22-aproximación-de-una-composición)
  - [Tipo 23: Direcciones de derivada máxima, mínima y nula de una composición](#tipo-23-direcciones-de-derivada-máxima-mínima-y-nula-de-una-composición)
  - [Tipo 24: Composición con una función implícita](#tipo-24-composición-con-una-función-implícita)
- **[Bloque G: Taylor y extremos](#bloque-g-taylor-y-extremos)**
  - [Tipo 25: Polinomio de Taylor y aproximación](#tipo-25-polinomio-de-taylor-y-aproximación)
  - [Tipo 26: Puntos críticos y clasificación](#tipo-26-puntos-críticos-y-clasificación)
  - [Tipo 27: El hessiano no decide](#tipo-27-el-hessiano-no-decide)
  - [Tipo 28: Extremos de una función armada con datos](#tipo-28-extremos-de-una-función-armada-con-datos)
  - [Tipo 29: Extremos con restricción (Lagrange)](#tipo-29-extremos-con-restricción-lagrange)
  - [Tipo 30: Extremos absolutos en un compacto](#tipo-30-extremos-absolutos-en-un-compacto)
  - [Tipo 31: Extremos de una función implícita](#tipo-31-extremos-de-una-función-implícita)
- **[Bloque H: Ejercicios teóricos](#bloque-h-ejercicios-teóricos)**
  - [Tipo 32: Definiciones, enunciados y demostraciones](#tipo-32-definiciones-enunciados-y-demostraciones)
- **[Errores frecuentes](#errores-frecuentes)**

---

## Bloque A: Ecuaciones diferenciales de 1.er orden

### Teoría

- **Ecuación diferencial ordinaria (EDO):** relación entre una variable independiente $x$, una función incógnita $y(x)$ y sus derivadas: $F(x, y, y', \dots, y^{(n)}) = 0$. El **orden** es el de la derivada de mayor orden.
- **Solución general (SG):** familia de soluciones con tantas constantes arbitrarias esenciales como el orden de la ecuación.
- **Solución particular (SP):** la que se obtiene de la SG dando un valor a cada constante, por ejemplo con una condición inicial $y(x_0) = y_0$.
- **Solución singular (SS):** solución que no se obtiene de la SG para ningún valor de las constantes. Lo típico es perderla al dividir por una expresión que puede anularse.

Antes de resolver hay que identificar la forma de la ecuación:

| Tipo | Forma | Sustitución o método |
|---|---|---|
| Separable | $y' = g(x)\thinspace h(y)$ | Separar e integrar |
| Lineal | $y' + P(x)\thinspace y = Q(x)$ | $y = uv$, o $y = y_h + y_p$ |
| Homogénea | $y' = g(y/x)$ | $y = zx$ |
| Bernoulli | $y' + P\thinspace y = Q\thinspace y^n$ | $z = y^{1-n}$ |
| Exacta | $P\thinspace dx + Q\thinspace dy = 0$ con $P'_y = Q'_x$ | Potencial: $\varphi(x,y) = C$ |
| 2.º orden sin $y$ | $F(x, y', y'') = 0$ | $w = y'$ |

### Tipo 1: EDO de variables separables

**Cómo se reconoce.** Después de despejar $y'$, el segundo miembro se puede escribir como un producto de una función de $x$ por una función de $y$. A veces hay que factorizar para verlo.

**Método.**

1. Escribir $y' = g(x)\thinspace h(y)$.
2. Revisar los valores de $y$ con $h(y) = 0$: son soluciones constantes y se pierden al dividir.
3. Separar: $\dfrac{dy}{h(y)} = g(x)\thinspace dx$.
4. Integrar los dos lados y poner **una** constante.
5. Si hay condición inicial, calcular la constante.

**Ejemplo** ([TP1 – 07 f](../Unidad%2001%20-%20Ecuaciones%20Diferenciales%20I/practica.md)).

> Halle la SP de $y' = xy + x - 2y - 2$ con $y(0) = 2$.

*Paso 1 — Factorizar.* Así como está no parece separable. Se saca factor común por grupos:

$$y' = x(y + 1) - 2(y + 1) = (x - 2)(y + 1)$$

*Paso 2 — Solución constante.* $y + 1 = 0$ da $y \equiv -1$, que es solución pero no cumple $y(0) = 2$. Se descarta.

*Paso 3 — Separar e integrar* (ahora se puede dividir por $y + 1$):

$$\frac{dy}{y + 1} = (x - 2)\thinspace dx \ \Rightarrow\ \ln|y + 1| = \frac{x^2}{2} - 2x + c \ \Rightarrow\ y = K e^{\frac{x^2}{2} - 2x} - 1$$

*Paso 4 — Condición inicial.* $2 = K e^0 - 1 \Rightarrow K = 3$.

**Resultado:** $y = 3e^{x^2/2 - 2x} - 1$.

**Cuidado:** si no se pide una SP, hay que informar también las soluciones constantes que no estén incluidas en la SG.

### Tipo 2: EDO lineal de 1.er orden

**Cómo se reconoce.** $y$ e $y'$ aparecen a la primera potencia, sin multiplicarse entre sí ni dentro de otra función. Los coeficientes pueden depender de $x$.

**Método** (sustitución $y = uv$).

1. Reemplazar $y = uv$, $y' = u'v + uv'$.
2. Sacar $u$ de factor común en los términos que la contienen sin derivar.
3. Elegir $v$ para que ese paréntesis se anule. Es una ecuación separable, y **sin constante**: alcanza con una función $v$.
4. Con esa $v$, despejar $u'$ e integrar **con constante**.
5. Armar $y = uv$.

**Ejemplo** ([1.er Parcial 05/05/2017, P1](../UTNianos/La%20Gloria/AM2%20-%201er%20Parcial/08-11-14/IMG_6705.JPG)).

> Halle la SG de $\cos(x)\thinspace y' + \mathop{\mathrm{sen}}(x)\thinspace y = 1$.

*Paso 1 — Reemplazar y agrupar.*

$$\cos(x)\thinspace u'v + u\left[\cos(x)\thinspace v' + \mathop{\mathrm{sen}}(x)\thinspace v\right] = 1$$

*Paso 2 — Anular el corchete.* $\cos(x)\thinspace v' = -\mathop{\mathrm{sen}}(x)\thinspace v$, entonces $\dfrac{dv}{v} = -\dfrac{\mathop{\mathrm{sen}} x}{\cos x}\thinspace dx$, de donde $\ln|v| = \ln|\cos x|$. Se toma $v = \cos x$.

*Paso 3 — Hallar $u$.* Queda $\cos(x)\thinspace u'\cos(x) = 1$, así que $u' = \dfrac{1}{\cos^2 x}$ y $u = \operatorname{tg}x + C$.

*Paso 4 — Armar.* $y = (\operatorname{tg}x + C)\cos x$.

**Resultado:** $y = \mathop{\mathrm{sen}} x + C\cos x$.

**Verificación rápida:** $\cos x\thinspace (\cos x - C\mathop{\mathrm{sen}} x) + \mathop{\mathrm{sen}} x\thinspace (\mathop{\mathrm{sen}} x + C\cos x) = \cos^2x + \mathop{\mathrm{sen}}\nolimits^2x = 1$ ✓.

### Tipo 3: Hallar un término de la EDO a partir de una solución

**Cómo se reconoce.** El enunciado da una solución $y_p$ y una ecuación con una función desconocida.

**Método.**

1. Reemplazar $y_p$ e $y_p'$ en la ecuación: **una solución hace verdadera la igualdad**. Despejar lo que falta.
2. Resolver la homogénea asociada para obtener $y_h$.
3. Por ser lineal: $y = y_h + y_p$.

**Ejemplo** ([1.er Parcial 15/10/2019, T2](primer-parcial-2019-10-15.md)).

> Halle $f$ sabiendo que $y_p = \dfrac{x^4 + 2x^2}{2}$ es solución de $y' - \dfrac2x\thinspace y = f(x)$, y encuentre la solución general.

*Paso 1 — Hallar $f$.* Como $y_p' = 2x^3 + 2x$:

$$f(x) = 2x^3 + 2x - \frac2x\cdot\frac{x^4 + 2x^2}{2} = 2x^3 + 2x - x^3 - 2x = x^3$$

*Paso 2 — Homogénea.* $y' = \dfrac2x\thinspace y \Rightarrow \dfrac{dy}{y} = \dfrac{2\thinspace dx}{x} \Rightarrow y_h = kx^2$.

*Paso 3 — Sumar.*

**Resultado:** $f(x) = x^3$ e $y = kx^2 + \dfrac{x^4 + 2x^2}{2}$. Absorbiendo $x^2$ en la constante, $y = Cx^2 + \dfrac{x^4}{2}$.

### Tipo 4: Homogéneas, Bernoulli y exactas

No aparecen en los parciales recopilados, pero forman parte de la unidad. Los ejemplos son breves y propios de esta guía.

**Homogénea.** Se reconoce porque el segundo miembro depende sólo de $y/x$. Se hace $y = zx$, $y' = z + xz'$, y queda separable.

> $y' = \dfrac{x + y}{x} = 1 + \dfrac yx$.

Con la sustitución: $z + xz' = 1 + z$, entonces $z' = \dfrac1x$ y $z = \ln|x| + C$. **Resultado:** $y = x(\ln|x| + C)$.

**Bernoulli.** Se reconoce porque es como una lineal, pero con $y^n$ en el segundo miembro. Se divide por $y^n$ y se hace $z = y^{1-n}$; queda lineal en $z$.

> $y' + y = xy^2$.

Con $n = 2$, $z = y^{-1}$ y $z' = -y^{-2}y'$. Dividiendo por $y^2$: $y^{-2}y' + y^{-1} = x$, es decir $-z' + z = x$, o sea $z' - z = -x$. Resolviendo la lineal: $z = x + 1 + Ce^x$. **Resultado:** $y = \dfrac{1}{x + 1 + Ce^x}$, y además la solución $y \equiv 0$, perdida al dividir.

**Exacta.** Se reconoce escribiéndola como $P\thinspace dx + Q\thinspace dy = 0$ y comprobando $P'_y = Q'_x$. La solución es $\varphi(x,y) = C$, con $\nabla\varphi = (P, Q)$. Se integra igual que un potencial.

> $2xy\thinspace dx + (x^2 + 3y^2)\thinspace dy = 0$.

$P'_y = 2x = Q'_x$. Integrando $P$ en $x$: $\varphi = x^2y + D(y)$. Derivando en $y$: $x^2 + D' = x^2 + 3y^2$, entonces $D = y^3$. **Resultado:** $x^2y + y^3 = C$.

### Tipo 5: EDO de 2.º orden en la que falta $y$

**Cómo se reconoce.** Aparecen $y''$, $y'$ y $x$, pero no $y$ sin derivar.

**Método.**

1. Hacer $w = y'$, $w' = y''$. Queda de 1.er orden en $w$.
2. Resolverla.
3. Integrar $w$ para obtener $y$. Al final tiene que haber **dos** constantes.

**Ejemplo** ([TP1 – 24](../Unidad%2001%20-%20Ecuaciones%20Diferenciales%20I/practica.md)).

> Halle la SG de $y'' - 2y' = x$.

*Paso 1 — Sustituir.* $w' - 2w = x$, que es lineal.

*Paso 2 — Resolver con $w = uv$.* Se anula $v' - 2v = 0$ con $v = e^{2x}$. Queda $u'e^{2x} = x$, entonces:

$$u = \int xe^{-2x}\thinspace dx = -\frac x2e^{-2x} - \frac14e^{-2x} + C$$

Por lo tanto $w = uv = -\dfrac x2 - \dfrac14 + Ce^{2x}$.

*Paso 3 — Integrar.* $y = \displaystyle\int w\thinspace dx = -\frac{x^2}{4} - \frac x4 + \frac C2e^{2x} + A$.

**Resultado:** $y = A + Be^{2x} - \dfrac{x^2 + x}{4}$.

### Tipo 6: Familia de curvas ortogonales

**Cómo se reconoce.** "Halle el haz (o familia) ortogonal a…", "trayectorias ortogonales".

**Qué hay que saber.** Dos curvas son ortogonales en un punto si sus rectas tangentes son perpendiculares, y las pendientes de dos rectas perpendiculares cumplen $m_1m_2 = -1$. Por eso, si la familia cumple $y' = F(x,y)$, la ortogonal cumple $y' = -\dfrac{1}{F(x,y)}$.

**Método.**

1. Derivar la familia respecto de $x$, recordando que $y$ depende de $x$.
2. **Eliminar el parámetro** usando la ecuación original. La EDO no puede contener la constante.
3. Cambiar $y'$ por $-1/y'$.
4. Resolver la EDO nueva.
5. Si se pide, elegir la curva que pasa por el punto dado.

**Ejemplo** ([1.er Parcial 08/10/2014, P1](../UTNianos/La%20Gloria/AM2%20-%201er%20Parcial/08-11-14/IMG_1354.JPG)).

> Halle la familia de curvas ortogonales a $x = ky^2$ y, de ella, la curva que pasa por $(2,4)$.

*Paso 1 — Derivar.* $1 = 2ky\thinspace y'$.

*Paso 2 — Eliminar $k$.* De la familia, $k = \dfrac{x}{y^2}$. Reemplazando: $1 = \dfrac{2x}{y}\thinspace y'$, es decir $y' = \dfrac{y}{2x}$.

*Paso 3 — Ortogonal.* $y' = -\dfrac{2x}{y}$.

*Paso 4 — Resolver.* $y\thinspace dy = -2x\thinspace dx$, entonces $\dfrac{y^2}{2} = -x^2 + c$, o sea $2x^2 + y^2 = C$: elipses.

*Paso 5 — Punto.* $2\cdot4 + 16 = C \Rightarrow C = 24$.

**Resultado:** familia $2x^2 + y^2 = C$; curva pedida $2x^2 + y^2 = 24$.

Otro igual: [1.er Parcial 15/10/2019, E4 a](primer-parcial-2019-10-15.md), donde $y^3 - Cx = 0$ da $3x^2 + y^2 = C$.

### Tipo 7: Curva definida por una propiedad de su tangente

**Cómo se reconoce.** "Halle las curvas tales que su recta tangente en cada punto…".

**Método.**

1. En un punto genérico $(x,y)$, escribir la tangente con coordenadas corrientes $(X,Y)$: $Y - y = y'(X - x)$.
2. Calcular lo que menciona el enunciado. Ordenada al origen ($X = 0$): $y - xy'$. Abscisa al origen ($Y = 0$): $x - \dfrac{y}{y'}$.
3. Imponer la propiedad. Sale una EDO.
4. Resolverla.

**Ejemplo** ([TP1 – 10 d](../Unidad%2001%20-%20Ecuaciones%20Diferenciales%20I/practica.md)).

> Halle la familia de curvas cuya recta tangente tiene, en cada punto, abscisa al origen igual al triple de la abscisa del punto.

*Paso 1 — Propiedad.* $x - \dfrac{y}{y'} = 3x$, entonces $-\dfrac{y}{y'} = 2x$, o sea $\dfrac{y'}{y} = -\dfrac{1}{2x}$.

*Paso 2 — Integrar.* $\ln|y| = -\dfrac12\ln|x| + c$, es decir $y^2 = \dfrac{K}{|x|}$.

**Resultado:** $xy^2 = C$.

---

## Bloque B: Dominio y topología

### Teoría

Sea $A$ un conjunto:

- **Punto interior:** existe una bola abierta centrada en él contenida en $A$.
- **Punto exterior:** existe una bola centrada en él que no toca a $A$.
- **Punto frontera:** toda bola centrada en él tiene puntos de $A$ y de su complemento.
- **Punto de acumulación:** toda bola reducida centrada en él tiene puntos de $A$. **Punto aislado:** pertenece a $A$ y no es de acumulación.
- **Abierto:** todos sus puntos son interiores. **Cerrado:** contiene a toda su frontera.
- **Acotado:** está contenido en alguna bola. **Compacto:** cerrado y acotado.
- **Conexo:** no se puede partir en dos abiertos disjuntos no vacíos. **Simplemente conexo:** conexo y sin agujeros (toda curva cerrada se contrae a un punto dentro del conjunto).
- **Conjunto de nivel $k$:** $C_k = \lbrace\vec x \in D_f : f(\vec x) = k\rbrace$.

### Tipo 8: Dominio natural

**Método.**

1. Escribir **todas** las condiciones: $\sqrt A \Rightarrow A \ge 0$; $\ln A \Rightarrow A > 0$; $\dfrac1A \Rightarrow A \ne 0$; $\mathop{\mathrm{arcsen}} A,\ \arccos A \Rightarrow |A| \le 1$.
2. Si hay un cociente o producto bajo la condición, separar en casos según los signos.
3. Reconocer las curvas de borde, completando cuadrados si hace falta.
4. Graficar, indicando con línea llena los bordes incluidos y con línea punteada los excluidos.

**Ejemplo** ([TP2 – 05 h](../Unidad%2002%20-%20Funciones%20de%20Varias%20Variables%20y%20Topologia/practica.md)).

> Determine el dominio de $f(x,y) = \sqrt{\dfrac{x^2 + y^2 - x}{2x - x^2 - y^2}}$.

*Paso 1 — Condición.* El cociente tiene que ser $\ge 0$ con denominador no nulo. Hay dos casos.

*Caso 1 — numerador $\ge 0$ y denominador $> 0$:* $x^2 + y^2 \ge x$ y $x^2 + y^2 < 2x$.

*Caso 2 — numerador $\le 0$ y denominador $< 0$:* $x^2 + y^2 \le x$ y $x^2 + y^2 > 2x$. Juntas piden $2x < x$, o sea $x < 0$. Pero entonces $x^2 + y^2 \le x < 0$, que es imposible. Este caso es vacío.

*Paso 2 — Geometría.* Completando cuadrados: $x^2 + y^2 < 2x$ es el interior de la circunferencia de centro $(1,0)$ y radio 1, y $x^2 + y^2 \ge x$ es el exterior (con borde) de la de centro $(\tfrac12, 0)$ y radio $\tfrac12$.

**Resultado:** $D = \lbrace(x,y) : x \le x^2 + y^2 < 2x\rbrace$. La circunferencia grande no se incluye; la chica sí, salvo el origen.

### Tipo 9: Análisis topológico de un conjunto

**Método.**

1. Graficar el conjunto.
2. **Interior:** cambiar todas las desigualdades por estrictas.
3. **Frontera:** los puntos donde alguna desigualdad se vuelve igualdad y las demás se cumplen.
4. **Exterior:** lo que queda.
5. Concluir: ¿contiene toda su frontera? (cerrado) ¿No contiene ninguno de sus puntos frontera? (abierto) ¿Entra en una bola? (acotado) Cerrado y acotado es compacto. ¿Es de una sola pieza? (conexo)

**Ejemplo** ([TP2 – 03 a](../Unidad%2002%20-%20Funciones%20de%20Varias%20Variables%20y%20Topologia/practica.md)).

> Analice $A = \lbrace(x, y) : x^2 + y^2 - 4 \le 0,\ x + y \ge 1\rbrace$.

*Gráfico:* es el trozo del disco de radio 2 que queda del lado de la recta $x + y = 1$ opuesto al origen.

- *Interior:* $x^2 + y^2 < 4$, $x + y > 1$.
- *Frontera:* el arco $x^2 + y^2 = 4$ con $x + y \ge 1$, y la cuerda $x + y = 1$ con $x^2 + y^2 < 4$.
- *Exterior:* $x^2 + y^2 > 4$ o $x + y < 1$.

**Resultado:** las dos desigualdades admiten igualdad, así que $A$ contiene su frontera y es **cerrado**. No es abierto. Está contenido en la bola de radio 3, así que es **acotado** y por lo tanto **compacto**. Es **conexo**.

---

## Bloque C: Límite y continuidad

### Teoría

**Límite:** $\lim\limits_{\vec x\to\vec A}f(\vec x) = L$ si para todo $\varepsilon > 0$ existe $\delta > 0$ tal que $0 < \Vert\vec x - \vec A\Vert < \delta$, $\vec x \in D_f$ implica $|f(\vec x) - L| < \varepsilon$. El punto $\vec A$ tiene que ser de acumulación del dominio.

**Continuidad:** $f$ es continua en $\vec A$ si $\vec A \in D_f$, existe $\lim\limits_{\vec x\to\vec A}f(\vec x)$ y es igual a $f(\vec A)$.

**Propiedades:** suma, producto, cociente con denominador no nulo y composición de continuas son continuas. El producto de un infinitésimo por una función acotada tiende a 0.

**Idea central.** En una variable se llega al punto por dos lados. En varias variables hay infinitos caminos, y el límite existe sólo si **todos** dan lo mismo. Por eso un camino sirve para probar que el límite no existe, o para encontrar un candidato, pero nunca para probar que existe.

### Tipo 10: Probar que un límite no existe

**Cómo se reconoce.** Al sustituir queda $0/0$ y los términos del denominador tienen el mismo grado que los del numerador, o las potencias sugieren una curva especial.

**Método.**

1. Probar con rectas $y - y_0 = m(x - x_0)$. Si el resultado depende de $m$, no existe y ya se terminó.
2. Si por todas las rectas da lo mismo, **no se concluye nada**. Hay que buscar la curva que iguale los grados de los términos del denominador.
3. Si una familia de curvas da un resultado que depende del parámetro, o dos caminos dan valores distintos, el límite no existe.

**Ejemplo** ([TP3 – 05 j](../Unidad%2003%20-%20Limite%20y%20Continuidad/practica.md)).

> Analice $\displaystyle\lim_{(x,y)\to(0,0)}\frac{xy^3}{x^2 + y^6}$.

*Paso 1 — Rectas $y = mx$.*

$$\frac{m^3x^4}{x^2 + m^6x^6} = \frac{m^3x^2}{1 + m^6x^4} \to 0$$

Sobre $x = 0$ también da 0. Todas las rectas dan 0, pero eso no prueba nada.

*Paso 2 — Igualar grados.* En el denominador aparecen $x^2$ e $y^6$. Son del mismo orden si $x \sim y^3$, así que se prueba $x = ky^3$:

$$\frac{ky^6}{k^2y^6 + y^6} = \frac{k}{k^2 + 1}$$

*Paso 3 — Concluir.* El valor depende de $k$ (0 con $k = 0$, $\tfrac12$ con $k = 1$).

**Resultado:** el límite no existe.

### Tipo 11: Probar que un límite existe

**Cómo se reconoce.** Las rectas y curvas dan todas el mismo valor, o el grado del numerador es mayor que el del denominador.

**Método.**

1. Obtener un candidato $L$ con un camino sencillo.
2. Escribir la función como **infinitésimo por acotada**. Las acotaciones habituales son $\dfrac{x^2}{x^2 + y^2} \le 1$, $\dfrac{|x|}{\sqrt{x^2 + y^2}} \le 1$, $|\mathop{\mathrm{sen}}(\cdot)| \le 1$.
3. O bien pasar a polares y mostrar $|f - L| \le g(r)\thinspace h(\theta)$, con $g(r) \to 0$ y $h$ acotada.
4. Límites notables: $\dfrac{\mathop{\mathrm{sen}} u}{u} \to 1$, $\dfrac{1 - \cos u}{u^2} \to \dfrac12$, $\dfrac{e^u - 1}{u} \to 1$, $\dfrac{\ln(1 + u)}{u} \to 1$.

**Ejemplo** ([1.er Parcial 08/10/2014, T1](../UTNianos/La%20Gloria/AM2%20-%201er%20Parcial/08-11-14/IMG_1354.JPG)).

> Determine si $f(x,y) = \dfrac{x^3 - y^3}{x^2 + y^2}$, con $f(0,0) = 0$, es continua en $(0,0)$.

*Paso 1 — Candidato.* Sobre $y = 0$: $f = x \to 0$.

*Paso 2 — Separar en infinitésimo por acotada.*

$$f = \underbrace{x}_{\to0}\cdot\underbrace{\frac{x^2}{x^2 + y^2}}_{\in[0,1]} - \underbrace{y}_{\to0}\cdot\underbrace{\frac{y^2}{x^2 + y^2}}_{\in[0,1]} \to 0$$

*Paso 3 — Comparar con el valor en el punto.* $\lim f = 0 = f(0,0)$.

**Resultado:** $f$ es continua en $(0,0)$.

### Tipo 12: Hallar un parámetro para que sea continua

**Método.**

1. Justificar la continuidad fuera del punto problemático: cociente de continuas con denominador no nulo.
2. Calcular el límite en el punto (Tipos 10 y 11). Conviene trasladar con un cambio como $w = y - y_0$.
3. Igualar el parámetro al límite. Si el límite no existe, no hay ningún valor posible.

**Ejemplo** ([Repaso R3](repaso-primer-parcial.md)).

> Determine $k$ para que sea continua en $\mathbb{R}^2$: $f(x,y) = \dfrac{x^3 - x(y + 1)^2}{x^2 + (y + 1)^2}$ si $(x,y) \ne (0,-1)$, y $f(0,-1) = k$.

*Paso 1 — Fuera de $(0,-1)$* el denominador no se anula, así que $f$ es continua.

*Paso 2 — Límite.* Con $w = y + 1$:

$$f = \underbrace{x}_{\to0}\cdot\underbrace{\frac{x^2 - w^2}{x^2 + w^2}}_{|\cdot|\le1} \to 0$$

*Paso 3 — Igualar.*

**Resultado:** $k = 0$.

---

## Bloque D: Derivadas y diferenciabilidad

### Teoría

- **Derivada respecto de un vector $\vec r$** en $\vec A$: $f'(\vec A, \vec r) = \lim\limits_{h\to0}\dfrac{f(\vec A + h\vec r) - f(\vec A)}{h}$.
- **Derivada direccional:** la misma, con $\vec r$ versor. Si $\vec r$ no es versor, la derivada existe pero no es direccional.
- **Derivadas parciales:** direccionales según los ejes.
- **Homogeneidad:** $f'(\vec A, \lambda\vec r) = \lambda f'(\vec A, \vec r)$.
- **Schwarz:** si $f''_{xy}$ y $f''_{yx}$ existen y son continuas en un entorno, son iguales.

**Diferenciabilidad.** $f$ es diferenciable en $\vec A$ si

$$\lim_{\vec h\to\vec 0}\frac{f(\vec A + \vec h) - f(\vec A) - \nabla f(\vec A)\cdot\vec h}{\Vert\vec h\Vert} = 0$$

La idea es que el plano tangente aproxime a $f$ mejor que linealmente.

| Si $f$ es diferenciable en $\vec A$, entonces | Consecuencia si falla |
|---|---|
| Es continua en $\vec A$ | Discontinua ⇒ no diferenciable |
| Existen todas las direccionales | Alguna no existe ⇒ no diferenciable |
| $f'(\vec A,\breve r) = \nabla f(\vec A)\cdot\breve r$ | No es lineal en $\breve r$ ⇒ no diferenciable |

**Condición suficiente:** si las derivadas parciales existen en un entorno y son continuas en $\vec A$ ($f \in C^1$), $f$ es diferenciable.

**Gradiente y dirección.** Si $f$ es diferenciable y $\nabla f(\vec A) \ne \vec 0$, como $f'(\vec A,\breve r) = \Vert\nabla f\Vert\cos\alpha$:

- la derivada **máxima** vale $\Vert\nabla f(\vec A)\Vert$ en la dirección de $\nabla f(\vec A)$;
- la **mínima** vale $-\Vert\nabla f(\vec A)\Vert$ en la dirección opuesta;
- es **nula** en las direcciones perpendiculares a $\nabla f(\vec A)$.

### Tipo 13: Derivadas direccionales por definición

**Cómo se reconoce.** Función partida, en el punto donde cambia la fórmula. En esos casos **no** se pueden usar las reglas de derivación ni $\nabla f\cdot\breve r$.

**Método.**

1. Plantear $\breve r = (a,b)$ con $a^2 + b^2 = 1$.
2. Revisar qué rama corresponde al punto $\vec A + h\breve r$. Si alguna dirección cae siempre sobre la otra rama, tratarla aparte.
3. Calcular $\lim\limits_{h\to0}\dfrac{f(\vec A + h\breve r) - f(\vec A)}{h}$.
4. Responder lo pedido.

**Ejemplo** ([Simulacro P1 b](simulacro-primer-parcial.md)).

> Sea $f(x,y) = \dfrac{yx^2}{x^2 + 2y^2}$ si $(x,y) \ne (0,0)$, y $f(0,0) = 0$. Halle las direcciones de derivada nula en $(0,0)$.

*Paso 1 — Límite.*

$$f'(\vec 0, \breve r) = \lim_{h\to0}\frac1h\cdot\frac{h^3\thinspace ba^2}{h^2(a^2 + 2b^2)} = \frac{ba^2}{a^2 + 2b^2} = \frac{ba^2}{1 + b^2}$$

En el último paso se usó $a^2 + 2b^2 = (a^2 + b^2) + b^2 = 1 + b^2$.

*Paso 2 — Imponer que sea nula.* $ba^2 = 0$ implica $b = 0$ o $a = 0$.

**Resultado:** las direcciones de derivada nula son $(\pm1, 0)$ y $(0, \pm1)$.

**Variante con dos casos** ([1.er Parcial 15/10/2019, E1](primer-parcial-2019-10-15.md)): $f = \dfrac{x\mathop{\mathrm{sen}} y}{y}$ si $y \ne 0$, y $f = 0$ si $y = 0$. Si $b \ne 0$, $\dfrac{f(ha, hb)}{h} = a\dfrac{\mathop{\mathrm{sen}}(hb)}{hb} \to a$. Si $b = 0$, el punto $(ha, 0)$ cae en la otra rama, y la derivada es 0.

### Tipo 14: Continuidad y derivadas de una función partida

**Cómo se reconoce.** "Analice la continuidad y la existencia de derivadas direccionales en…". Se combinan los Tipos 10, 11 y 13.

**Ejemplo** ([1.er Parcial 1C 2014, E1](../UTNianos/La%20Gloria/AM2%20-%201er%20Parcial/AMII%20-%202014-05-26%20-%201er%20Parcial%20Campillo.jpg)).

> Sea $f(x,y) = \dfrac{x^2 + 2y^2}{x - y^2}$ si $x \ne y^2$, y $f(x,y) = 0$ si $x = y^2$. a) Analice la continuidad en el origen. b) ¿Existen las derivadas direccionales en $(0,0)$? c) ¿Se puede aplicar la fórmula de cálculo para las derivadas direccionales?

**a)** El denominador se anula sobre la parábola $x = y^2$, así que hay que acercarse a ella. Se toma $x = (1 + k)y^2$, con $k \ne 0$:

$$f = \frac{(1 + k)^2y^4 + 2y^2}{ky^2} = \frac{(1 + k)^2y^2 + 2}{k} \to \frac2k$$

El valor depende de $k$: el límite no existe y $f$ **no es continua**.

**b)** Con $\breve r = (a, b)$:

- Si $a \ne 0$: para $h$ chico, $ha \ne h^2b^2$, y $\dfrac{f(ha, hb)}{h} = \dfrac{a^2 + 2b^2}{h(a - hb^2)}$, que no tiene límite finito.
- Si $a = 0$, $b = \pm1$: $f(0, hb) = \dfrac{2h^2b^2}{-h^2b^2} = -2$, y $\dfrac{-2}{h}$ tampoco tiene límite finito.

**No existe ninguna derivada direccional** en el origen.

**c)** La fórmula $f'(\vec A,\breve r) = \nabla f(\vec A)\cdot\breve r$ exige que $f$ sea diferenciable en el punto. Como $f$ no es continua en el origen, no es diferenciable.

**Resultado:** no es continua, no existen las direccionales, y la fórmula no se puede aplicar.

### Tipo 15: ¿Es diferenciable?

**Método** (orden para no hacer cuentas de más).

1. **¿Es $C^1$?** Si la función es una fórmula única, con derivadas continuas alrededor del punto, es diferenciable. Fin.
2. **¿Es continua?** Si no, no es diferenciable. Fin.
3. **Calcular las direccionales por definición.** Si alguna no existe, no es diferenciable. Fin.
4. **Comparar** con $\nabla f\cdot\breve r$, usando las parciales. Si no coincide, no es diferenciable. Fin.
5. Si todo lo anterior pasó, **aplicar la definición**: ver si el cociente tiende a 0.

**Ejemplo 1: falla la linealidad** ([Repaso R9](repaso-primer-parcial.md)).

> Con $f(x,y) = \dfrac{x^2y + y^2\mathop{\mathrm{sen}} x}{x^2 + y^2}$ fuera del origen y $f(0,0) = 0$, analice $f'(\vec 0, \vec r)$ y la diferenciabilidad.

Con $\vec r = (a,b)$:

$$\frac{f(ha, hb)}{h} = \frac{a^2b}{a^2 + b^2} + \frac{b^2}{a^2 + b^2}\cdot\frac{\mathop{\mathrm{sen}}(ha)}{h} \to \frac{a^2b + ab^2}{a^2 + b^2} = \frac{ab(a + b)}{a^2 + b^2}$$

Existe para todo $\vec r$. Con $\vec r = (1,0)$ y $(0,1)$ da $f'_x = f'_y = 0$, o sea $\nabla f(\vec 0) = \vec 0$. Si fuera diferenciable, todas las derivadas valdrían 0. Pero con $\breve r = (1,1)/\sqrt2$ da $\dfrac{1}{\sqrt2} \ne 0$.

**Resultado:** existen todas las derivadas, pero **no es diferenciable**.

**Ejemplo 2: hay que usar la definición** ([Repaso R13](repaso-primer-parcial.md)).

> Sea $f(x,y) = y^2\cos\left(\dfrac{1}{x^2 + y^2}\right)$ fuera del origen y $f(0,0) = 0$. Analice la diferenciabilidad en el origen.

*Continuidad:* $y^2 \to 0$ y el coseno está acotado, así que $f \to 0 = f(0,0)$.

*Direccionales:* $\dfrac{h^2b^2\cos(1/h^2)}{h} = hb^2\cos(1/h^2) \to 0$. Todas valen 0 y $\nabla f(\vec 0) = \vec 0$.

*Definición,* con $\vec h = (h,k)$:

$$\frac{f(h,k) - 0 - 0}{\sqrt{h^2 + k^2}} = \underbrace{\frac{k}{\sqrt{h^2 + k^2}}}_{\text{acot.}}\cdot\underbrace{k}_{\to0}\cdot\underbrace{\cos\left(\frac{1}{h^2 + k^2}\right)}_{\text{acot.}} \to 0$$

**Resultado:** $f$ es diferenciable en $(0,0)$.

### Tipo 16: Dirección de máximo crecimiento

**Cómo se reconoce.** Aparecen "derivada máxima", "dirección de máximo crecimiento" o "derivada nula". A veces el dato es la dirección y hay que **reconstruir el gradiente**.

**Método.**

1. Obtener $\nabla f(\vec A)$. Si el dato es la dirección de máximo: $\nabla f = \lambda\breve r$ con $\lambda > 0$.
2. Máxima: $\Vert\nabla f\Vert$, en $\dfrac{\nabla f}{\Vert\nabla f\Vert}$. Mínima: el opuesto.
3. Nula: si $\nabla f = (p, q)$, los versores $\pm\dfrac{(q, -p)}{\Vert\nabla f\Vert}$.

**Ejemplo** ([Repaso R2 a](repaso-primer-parcial.md)).

> $f$ es diferenciable, $f(1,2) = 5$, su derivada direccional en $(1,2)$ es máxima según $\left(\tfrac{1}{\sqrt2}, \tfrac{1}{\sqrt2}\right)$ y $f'_x(1,2) = 3\sqrt2$. Halle el plano tangente en $(1, 2, 5)$.

*Paso 1 — Gradiente.* El gradiente apunta hacia la dirección de máximo: $\nabla f(1,2) = \lambda(1,1)$, con $\lambda > 0$. Su primera componente es $f'_x$, así que $\lambda = 3\sqrt2$.

*Paso 2 — Plano.* $z = f(\vec A) + f'_x(x - 1) + f'_y(y - 2)$.

**Resultado:** $z = 5 + 3\sqrt2\thinspace (x - 1) + 3\sqrt2\thinspace (y - 2)$.

---

## Bloque E: Rectas y planos tangentes

### Teoría

| Objeto | Cómo se obtiene |
|---|---|
| Recta tangente a una curva $\vec g(t)$ en $t_0$ | $\vec X = \vec g(t_0) + \lambda\thinspace \vec g'(t_0)$ |
| Plano normal a la curva | $\vec g'(t_0)\cdot(\vec X - \vec g(t_0)) = 0$ |
| Plano tangente a $z = f(x,y)$ | $z = f(\vec A) + f'_x(\vec A)(x - x_0) + f'_y(\vec A)(y - y_0)$ |
| Plano tangente a $F(x,y,z) = 0$ | $\nabla F(P_0)\cdot(\vec X - P_0) = 0$ |
| Plano tangente a una superficie paramétrica $\vec\Sigma(u,v)$ | normal $\vec\Sigma'_u\wedge\vec\Sigma'_v$ |
| Recta normal a una superficie | $\vec X = P_0 + \lambda\thinspace \vec n$ |
| Recta tangente a la intersección $F = 0$, $G = 0$ | dirección $\nabla F(P_0)\wedge\nabla G(P_0)$ |

**Idea clave.** El gradiente es perpendicular a los conjuntos de nivel. Por eso $\nabla F(P_0)$ es la normal a la superficie $F = 0$, y una curva contenida en dos superficies tiene tangente perpendicular a las dos normales: su producto vectorial.

**Aproximación lineal:** $f(\vec A + \vec h) \approx f(\vec A) + \nabla f(\vec A)\cdot\vec h$. El plano tangente evaluado en el punto es la aproximación.

### Tipo 17: Plano tangente a una superficie

**Método.**

1. Escribir la superficie como $F(x,y,z) = 0$ o $z = f(x,y)$.
2. Verificar que el punto pertenece a la superficie. Si falta una coordenada, calcularla.
3. Calcular la normal en el punto.
4. Armar el plano, o la recta normal.

**Ejemplo** ([1.er Parcial 08/10/2014, P2](../UTNianos/La%20Gloria/AM2%20-%201er%20Parcial/08-11-14/IMG_1354.JPG)).

> Halle el plano tangente a $h(x,y,z) = x^3y^4 + x^2z^3 - yz^2 - 1 = 0$ en $(1,1,1)$.

*Paso 1 — Punto.* $1 + 1 - 1 - 1 = 0$ ✓.

*Paso 2 — Gradiente.*

$$\nabla h = \left(3x^2y^4 + 2xz^3,\ 4x^3y^3 - z^2,\ 3x^2z^2 - 2yz\right) \ \Rightarrow\ \nabla h(1,1,1) = (5,\ 3,\ 1)$$

*Paso 3 — Plano.* $5(x - 1) + 3(y - 1) + (z - 1) = 0$.

**Resultado:** $5x + 3y + z = 9$.

### Tipo 18: Aproximación lineal con el plano como dato

**Cómo se reconoce.** No se conoce $f$, pero se conoce su plano tangente, a veces descripto de forma indirecta.

**Método.**

1. Identificar el plano tangente. Si es $z = L(x,y)$, de ahí salen $f(\vec A)$ y $\nabla f(\vec A)$.
2. Evaluar $L$ en el punto cercano.

**Ejemplo** ([1.er Parcial 15/10/2019, E2](primer-parcial-2019-10-15.md)).

> $f$ es diferenciable y su plano tangente en $(4, 2, f(4,2))$ es el plano normal a la curva $C$: $z = x^2 - 3y^2$, $x = 2y$. Calcule aproximadamente $f(3.94;\ 2.04)$.

*Paso 1 — Parametrizar $C$.* Con $y = t$: $\vec\alpha(t) = (2t,\ t,\ 4t^2 - 3t^2) = (2t,\ t,\ t^2)$.

*Paso 2 — Punto.* $(x, y) = (4, 2)$ da $t = 2$, y por lo tanto $z = 4$.

*Paso 3 — Plano normal a $C$.* Su normal es el vector tangente: $\vec\alpha'(2) = (2, 1, 4)$.

$$2(x - 4) + (y - 2) + 4(z - 4) = 0 \ \Rightarrow\ 2x + y + 4z = 26$$

*Paso 4 — Evaluar.* Se despeja $z = L(x,y) = \dfrac{26 - 2x - y}{4}$:

$$f(3{,}94;\ 2{,}04) \approx \frac{26 - 7{,}88 - 2{,}04}{4} = 4{,}02$$

**Resultado:** $f(3.94;\ 2.04) \approx 4.02$.

### Tipo 19: Recta tangente a una curva intersección

**Método.**

1. Completar el punto si falta una coordenada, y verificarlo en las dos superficies.
2. Calcular $\nabla F$ y $\nabla G$ en el punto.
3. Dirección: $\vec d = \nabla F\wedge\nabla G$.
4. Armar la recta y responder lo pedido.

**Ejemplo** ([Simulacro P2](simulacro-primer-parcial.md)).

> Sea $C$ la intersección de $S_1$: $3xy + \ln(x + yz - 6) - 2z = 0$ y $S_2$: $z = x^2y + x$. Analice si la recta tangente a $C$ en $A = (1, 2, z_0)$ corta al eje $x$.

*Paso 1 — $z_0$.* De $S_2$: $z_0 = 2 + 1 = 3$. En $S_1$: $6 + \ln(1) - 6 = 0$ ✓.

*Paso 2 — Gradientes.* Se escribe $f_2 = x^2y + x - z$. En $A$, el argumento del logaritmo vale 1:

$$\nabla f_1 = \left(3y + \frac{1}{x + yz - 6},\ 3x + \frac{z}{x + yz - 6},\ \frac{y}{x + yz - 6} - 2\right) \to (7,\ 6,\ 0)$$

$$\nabla f_2 = (2xy + 1,\ x^2,\ -1) \to (5,\ 1,\ -1)$$

*Paso 3 — Dirección.*

$$\vec d = \begin{vmatrix} \breve\imath & \breve\jmath & \breve k \cr 7 & 6 & 0 \cr 5 & 1 & -1 \end{vmatrix} = (-6,\ 7,\ -23)$$

*Paso 4 — Recta y eje $x$.* $\vec X = (1 - 6\alpha,\ 2 + 7\alpha,\ 3 - 23\alpha)$. Sobre el eje $x$ tienen que anularse $y$ y $z$ **con el mismo $\alpha$**: $y = 0$ da $\alpha = -\tfrac27$, y $z = 0$ da $\alpha = \tfrac{3}{23}$.

**Resultado:** los valores de $\alpha$ son distintos, así que la recta no corta al eje $x$.

Otros iguales: [Repaso R1](repaso-primer-parcial.md) (intersección con un plano) y [R12](repaso-primer-parcial.md) (distancia).

### Tipo 20: Curva perpendicular a una superficie

**Método.**

1. Hallar el punto común.
2. Calcular el vector tangente a la curva y la normal a la superficie.
3. La curva es perpendicular a la superficie si esos dos vectores son **paralelos**.

**Ejemplo** ([1.er Parcial 1C 2014, E2](../UTNianos/La%20Gloria/AM2%20-%201er%20Parcial/AMII%20-%202014-05-26%20-%201er%20Parcial%20Campillo.jpg)).

> Sea $S$ la superficie $\vec f(u,v) = (2u,\ u - v,\ u + v)$ y $C$: $x^2 + y + z = 2$, $x + z = 3$, con $x \ge 0$. Demuestre que $C$ es normal a $S$ en el punto común.

*Paso 1 — Ecuación de $S$.* Como $y + z = 2u = x$, $S$ es el plano $x - y - z = 0$, de normal $\vec n = (1, -1, -1)$.

*Paso 2 — Punto común.* En $C$ reemplazamos $y + z = x$: $x^2 + x = 2$, así que $x = 1$ (se descarta $x = -2$). Entonces $z = 2$ e $y = -1$. El punto es $(1, -1, 2)$.

*Paso 3 — Tangente a $C$.* Con $\nabla F_1 = (2x, 1, 1) = (2, 1, 1)$ y $\nabla F_2 = (1, 0, 1)$:

$$\vec d = (2, 1, 1)\wedge(1, 0, 1) = (1,\ -1,\ -1)$$

**Resultado:** $\vec d = \vec n$, son paralelos, y $C$ es normal a $S$ en $(1,-1,2)$. $\blacksquare$

Otro igual, con conjunto de nivel: [Repaso R7](repaso-primer-parcial.md).

### Tipo 21: Punto regular y plano normal a una curva

**Qué hay que saber.** Una **curva** es la imagen de una función continua $\vec g: I \to \mathbb{R}^n$. Un **punto regular** es uno donde $\vec g$ es derivable con $\vec g'(t) \ne \vec 0$.

**Ejemplo** ([1.er Parcial 1C 2014, T1](../UTNianos/La%20Gloria/AM2%20-%201er%20Parcial/AMII%20-%202014-05-26%20-%201er%20Parcial%20Campillo%282%29.jpg)).

> Dada $C$: $z = y - x^2$, $x - y = 0$, demuestre que todos sus puntos son regulares y halle el plano normal en $(1,1,0)$.

*Paso 1 — Parametrizar.* Con $x = t$: $y = t$, $z = t - t^2$, así que $\vec g(t) = (t, t, t - t^2)$.

*Paso 2 — Regularidad.* $\vec g'(t) = (1, 1, 1 - 2t)$. La primera componente nunca se anula, así que $\vec g' \ne \vec 0$ en todo punto.

*Paso 3 — Plano normal.* El punto corresponde a $t = 1$, con $\vec g'(1) = (1, 1, -1)$:

$$(x - 1) + (y - 1) - z = 0$$

**Resultado:** todos los puntos son regulares y el plano normal es $x + y - z = 2$.

---

## Bloque F: Funciones compuestas e implícitas

### Teoría

**Regla de la cadena:** si $\vec g$ es diferenciable en $\vec A$ y $\vec f$ es diferenciable en $\vec g(\vec A)$, entonces $\vec f\circ\vec g$ es diferenciable en $\vec A$ y

$$D(\vec f\circ\vec g)(\vec A) = D\vec f(\vec g(\vec A))\cdot D\vec g(\vec A)$$

Para $h(x,y) = f(u(x,y), v(x,y))$: $h'_x = f'_uu'_x + f'_vv'_x$ y $h'_y = f'_uu'_y + f'_vv'_y$. Sobre una curva: $\dfrac{d}{dt}f(\vec X(t)) = \nabla f(\vec X(t))\cdot\vec X'(t)$.

**Teorema de Cauchy–Dini** (caso $F(x,y,z) = 0$): si $F \in C^1$ en un entorno de $P_0 = (x_0,y_0,z_0)$, $F(P_0) = 0$ y $F'_z(P_0) \ne 0$, entonces existe un entorno de $(x_0,y_0)$ y una única $z = f(x,y)$ de clase $C^1$, con $f(x_0,y_0) = z_0$ y $F(x,y,f(x,y)) = 0$, y

$$z'_x = -\frac{F'_x}{F'_z}, \qquad z'_y = -\frac{F'_y}{F'_z}$$

Para $F(x,y) = 0$: $y' = -\dfrac{F'_x}{F'_y}$. Para un sistema $F = 0$, $G = 0$ que define $y(x)$, $z(x)$ hace falta que el jacobiano $\dfrac{\partial(F,G)}{\partial(y,z)}$ no se anule; se derivan ambas ecuaciones respecto de $x$ y se resuelve el sistema lineal.

### Tipo 22: Aproximación de una composición

**Método.**

1. Datos de la función de afuera $f$: del plano tangente salen el valor y el gradiente.
2. **Elegir el punto base** de la función compuesta: el que $\vec g$ manda al punto donde se conoce $f$, y que además esté cerca del punto pedido.
3. Jacobiana de $\vec g$ en ese punto.
4. $\nabla h = \nabla f(\vec g(\vec A))\cdot D\vec g(\vec A)$.
5. $h(\vec A + \vec\Delta) \approx h(\vec A) + \nabla h(\vec A)\cdot\vec\Delta$.

**Ejemplo** ([Simulacro P3](simulacro-primer-parcial.md)).

> El plano tangente al gráfico de $f$ en $(1, 0, z_0)$ es $2z - 6x + 3y = 0$. Calcule aproximadamente $h(-0.98;\ 1.02)$, con $h(u,v) = f(u^2v,\ u + v)$.

*Paso 1 — Datos de $f$.* Despejando: $z = 3x - \tfrac32y$. Entonces $f(1,0) = 3$ y $\nabla f(1,0) = \left(3, -\tfrac32\right)$.

*Paso 2 — Punto base.* $(-1, 1)$ está cerca de $(-0{,}98;\ 1{,}02)$, y $\vec g(-1,1) = (1, 0)$, justo donde se conoce $f$. Entonces $h(-1,1) = 3$.

*Paso 3 — Jacobiana.*

$$D\vec g = \begin{pmatrix} 2uv & u^2 \cr 1 & 1 \end{pmatrix} \ \Rightarrow\ D\vec g(-1,1) = \begin{pmatrix} -2 & 1 \cr 1 & 1 \end{pmatrix}$$

*Paso 4 — Cadena.*

$$\nabla h(-1,1) = \left(3,\ -\tfrac32\right)\begin{pmatrix} -2 & 1 \cr 1 & 1 \end{pmatrix} = \left(-\tfrac{15}{2},\ \tfrac32\right)$$

*Paso 5 — Aproximar.* Con $\vec\Delta = (0{,}02;\ 0{,}02)$: $3 - \tfrac{15}{2}(0{,}02) + \tfrac32(0{,}02) = 2{,}88$.

**Resultado:** $h(-0.98;\ 1.02) \approx 2.88$.

Otro igual: [Repaso R11](repaso-primer-parcial.md).

**Cuidado:** las derivadas de $f$ se evalúan en $\vec g(\vec A)$, y las de $\vec g$ en $\vec A$. Es el error más común de este tema.

### Tipo 23: Direcciones de derivada máxima, mínima y nula de una composición

Es la combinación de los Tipos 22 y 16.

**Ejemplo** ([Repaso R5](repaso-primer-parcial.md)).

> Sean $f(u,v) = u^2v + v^3$, $D\vec g(x,y) = \begin{pmatrix} \mathop{\mathrm{sen}}(y - 2) & x\cos(y - 2) \cr 3 & 2y \end{pmatrix}$, $\vec g(1,2) = (3,1)$ y $h = f\circ\vec g$. Halle los versores de derivada máxima, mínima y nula de $h$ en $(1,2)$ y los valores de esas derivadas.

*Paso 1 — Jacobiana en $(1,2)$.* $D\vec g(1,2) = \begin{pmatrix} 0 & 1 \cr 3 & 4 \end{pmatrix}$.

*Paso 2 — Gradiente de $f$ en $(3,1)$.* $\nabla f = (2uv,\ u^2 + 3v^2) = (6,\ 12)$.

*Paso 3 — Cadena.*

$$\nabla h(1,2) = (6,\ 12)\begin{pmatrix} 0 & 1 \cr 3 & 4 \end{pmatrix} = (36,\ 54) = 18\thinspace (2,\ 3)$$

*Paso 4 — Direcciones.* $\Vert\nabla h\Vert = 18\sqrt{13}$.

**Resultado:**

- Máxima: $\breve r = \dfrac{(2,3)}{\sqrt{13}}$, de valor $18\sqrt{13}$.
- Mínima: $\breve r = -\dfrac{(2,3)}{\sqrt{13}}$, de valor $-18\sqrt{13}$.
- Nula: $\breve r = \pm\dfrac{(3,-2)}{\sqrt{13}}$.

### Tipo 24: Composición con una función implícita

**Método.**

1. Punto intermedio: $\vec g(\vec A)$.
2. Hallar la coordenada que falta de la ecuación. Suele verse probando un valor que anule el logaritmo o la exponencial.
3. **Verificar Cauchy–Dini:** $F \in C^1$, $F(P_0) = 0$, $F'_z(P_0) \ne 0$.
4. Derivadas de la implícita con $-F'_x/F'_z$.
5. Jacobiana de $\vec g$ y regla de la cadena.
6. Responder lo pedido.

**Ejemplo** ([1.er Parcial 15/10/2019, E3](primer-parcial-2019-10-15.md)).

> Sea $z = f(x,y)$ definida por $xy + z + \ln(xz - 5) = 11$ en un entorno de $(2,4,z_0)$ y $\vec g(u,v) = (u^2 - 2v^2,\ 3u - 2v^2)$. Halle la derivada direccional máxima y las direcciones de derivada nula de $h = f\circ\vec g$ en $(2,1)$.

*Paso 1 — Punto intermedio.* $\vec g(2,1) = (2, 4)$.

*Paso 2 — $z_0$.* $8 + z_0 + \ln(2z_0 - 5) = 11$. Con $z_0 = 3$: $8 + 3 + \ln1 = 11$ ✓.

*Paso 3 — Cauchy–Dini.* $F = xy + z + \ln(xz - 5) - 11$ es $C^1$ donde $xz > 5$, y en $(2,4,3)$:

$$F'_x = y + \frac{z}{xz - 5} = 7, \qquad F'_y = x = 2, \qquad F'_z = 1 + \frac{x}{xz - 5} = 3 \ne 0$$

*Paso 4 — Derivadas.* $\nabla f(2,4) = \left(-\tfrac73,\ -\tfrac23\right)$.

*Paso 5 — Cadena.*

$$\nabla h(2,1) = \left(-\tfrac73,\ -\tfrac23\right)\begin{pmatrix} 4 & -4 \cr 3 & -4 \end{pmatrix} = \left(-\tfrac{34}{3},\ 12\right)$$

*Paso 6 — Máxima y nulas.* $\Vert\nabla h\Vert = \sqrt{\dfrac{1156}{9} + 144} = \dfrac{2\sqrt{613}}{3}$. Como $\nabla h \parallel (-17, 18)$, las direcciones nulas son perpendiculares a ese vector.

**Resultado:** derivada máxima $\dfrac{2\sqrt{613}}{3} \approx 16{,}51$; direcciones nulas $\pm\dfrac{(18, 17)}{\sqrt{613}}$.

**Variante: derivada respecto de un vector** ([1.er Parcial 1C 2014, E4](../UTNianos/La%20Gloria/AM2%20-%201er%20Parcial/AMII%20-%202014-05-26%20-%201er%20Parcial%20Campillo%282%29.jpg)).

> Sea $h = f\circ\vec g$, con $\vec g(x,y) = (2x - y^2,\ y - 3x)$ y $f(u,v)$ definida por $w - u + 2v + e^w = uv - 1$. Halle $\dfrac{\partial h}{\partial(-1,2)}(1,0)$ sin componer. ¿Es una derivada direccional?

- $\vec g(1,0) = (2, -3)$. Con $F = w - u + 2v + e^w - uv + 1$: $F(2,-3,w) = w + e^w - 1 = 0$ da $w = 0$.
- En $(2, -3, 0)$: $F'_u = -1 - v = 2$, $F'_v = 2 - u = 0$, $F'_w = 1 + e^w = 2 \ne 0$. Entonces $\nabla f(2,-3) = (-1, 0)$.
- $D\vec g(1,0) = \begin{pmatrix} 2 & 0 \cr -3 & 1 \end{pmatrix}$, así que $\nabla h(1,0) = (-2, 0)$.
- $h$ es diferenciable, y $h'((1,0), (-1,2)) = (-2, 0)\cdot(-1, 2) = 2$.

**Resultado:** vale 2. **No es direccional**, porque $(-1,2)$ no es versor ($\Vert(-1,2)\Vert = \sqrt5$). La direccional según $\frac{(-1,2)}{\sqrt5}$ vale $\frac{2}{\sqrt5}$.

---

## Bloque G: Taylor y extremos

### Teoría

**Polinomio de Taylor de 2.º orden** en $\vec A = (x_0,y_0)$, con $h = x - x_0$, $k = y - y_0$ y todas las derivadas evaluadas en $\vec A$:

$$P_2(x,y) = f(\vec A) + f'_xh + f'_yk + \frac12\left(f''_{xx}h^2 + 2f''_{xy}hk + f''_{yy}k^2\right)$$

$P_1$ es el plano tangente. El polinomio tiene en $\vec A$ el mismo valor y las mismas derivadas hasta orden 2 que $f$.

**Extremos.** $f$ tiene un **máximo (mínimo) local** en $\vec A$ si $f(\vec x) \le f(\vec A)$ ($\ge$) en un entorno de $\vec A$. **Punto crítico:** $\nabla f(\vec A) = \vec 0$ o $f$ no diferenciable en $\vec A$. **Punto silla:** punto con $\nabla f = \vec 0$ que no es extremo.

**Fermat:** si $f$ es diferenciable en $\vec A$ y tiene un extremo local allí, $\nabla f(\vec A) = \vec 0$.

**Criterio del hessiano** para $f \in C^2$ y $\nabla f(\vec A) = \vec 0$, con $H = f''_{xx}f''_{yy} - (f''_{xy})^2$:

| Condición | Conclusión |
|---|---|
| $H > 0$, $f''_{xx} > 0$ | mínimo local |
| $H > 0$, $f''_{xx} < 0$ | máximo local |
| $H < 0$ | punto silla |
| $H = 0$ | no decide |

**Por qué funciona.** Cerca de un punto crítico, $f(\vec A + \vec h) - f(\vec A) \approx \frac12\vec h^{\thinspace T}H_f\thinspace \vec h$: el signo de esa forma cuadrática decide si $f$ queda por encima o por debajo de $f(\vec A)$.

**Weierstrass:** una función continua en un compacto alcanza máximo y mínimo absolutos.

### Tipo 25: Polinomio de Taylor y aproximación

**Método.**

1. Calcular $f$, las primeras y las segundas derivadas **en general**.
2. Evaluarlas en $\vec A$.
3. Armar $P_2$ con $h = x - x_0$, $k = y - y_0$. No olvidar el factor $\tfrac12$ ni el 2 del término cruzado.
4. Para aproximar, elegir un $\vec A$ cercano donde todo sea fácil de calcular.

**Ejemplo** ([TP7 – 03 a](../Unidad%2007%20-%20Taylor%20y%20Extremos/practica.md)).

> Desarrolle $f(x,y) = x - y\sqrt{6 - x}$ hasta 2.º orden en $(2,3)$.

*Valor.* En $(2,3)$, $\sqrt{6 - x} = 2$ y $f = 2 - 6 = -4$.

*Primeras derivadas.* $f'_x = 1 + \dfrac{y}{2\sqrt{6 - x}} \to \dfrac74$ y $f'_y = -\sqrt{6 - x} \to -2$.

*Segundas derivadas.* $f''_{xx} = \dfrac{y}{4(6 - x)^{3/2}} \to \dfrac{3}{32}$, $f''_{xy} = \dfrac{1}{2\sqrt{6 - x}} \to \dfrac14$ y $f''_{yy} = 0$.

**Resultado:** $P_2 = -4 + \dfrac74(x - 2) - 2(y - 3) + \dfrac{3}{64}(x - 2)^2 + \dfrac14(x - 2)(y - 3)$.

**Aproximación** ([TP7 – 04 a](../Unidad%2007%20-%20Taylor%20y%20Extremos/practica.md)): para $0{,}98^{2{,}01}$ se toma $f = x^y$ en $(1,2)$. Como $f = 1$, $f'_x = yx^{y-1} = 2$ y $f'_y = x^y\ln x = 0$, resulta $0{,}98^{2{,}01} \approx 1 + 2(-0{,}02) = 0{,}96$.

### Tipo 26: Puntos críticos y clasificación

**Método.**

1. Plantear $f'_x = 0$, $f'_y = 0$. **Factorizar** y abrir en casos; no dividir por algo que pueda anularse.
2. Calcular $f''_{xx}$, $f''_{xy}$, $f''_{yy}$.
3. Evaluar $H$ en cada punto y clasificar.
4. Informar el valor de $f$ en los extremos.

**Ejemplo** ([Simulacro P4](simulacro-primer-parcial.md)).

> Halle y clasifique los puntos críticos de $f(x,y) = yx^2 + \frac43y^3 - 4y + 1$.

*Paso 1 — Críticos.* $f'_x = 2xy = 0$ y $f'_y = x^2 + 4y^2 - 4 = 0$.

- Si $x = 0$: $4y^2 = 4$, así que $y = \pm1$.
- Si $y = 0$: $x^2 = 4$, así que $x = \pm2$.

*Paso 2 — Hessiano.* $Hf = \begin{pmatrix} 2y & 2x \cr 2x & 8y \end{pmatrix}$.

| Punto | $H$ | $f''_{xx}$ | Clasificación | $f$ |
|---|---|---|---|---|
| $(\pm2, 0)$ | $-16 < 0$ | | silla | |
| $(0, 1)$ | $16 > 0$ | $2 > 0$ | mínimo local | $-\frac53$ |
| $(0, -1)$ | $16 > 0$ | $-2 < 0$ | máximo local | $\frac{11}{3}$ |

**Variante con parámetros** ([1.er Parcial 08/10/2014, P4](../UTNianos/La%20Gloria/AM2%20-%201er%20Parcial/08-11-14/IMG_1354.JPG)): para que $(2,3)$ sea crítico de $x^2 + y^2 + ax + by - 10$, se impone $\nabla f(2,3) = \vec 0$: $4 + a = 0$ y $6 + b = 0$. Con $a = -4$ y $b = -6$, $H = 2\cdot2 - 0 = 4 > 0$ y $f''_{xx} = 2 > 0$: es un mínimo local.

### Tipo 27: El hessiano no decide

**Cómo se reconoce.** $H = 0$, o $f$ no es diferenciable en el punto.

**Método.** Estudiar el **signo de $\Delta f = f(\vec A + \vec h) - f(\vec A)$** cerca del punto.

- Si $\Delta f \ge 0$ en un entorno: mínimo. Si $\Delta f \le 0$: máximo.
- Si toma los dos signos en todo entorno: no es extremo. Para probarlo alcanza con dos caminos.

**Ejemplo** ([TP7 – 06 b](../Unidad%2007%20-%20Taylor%20y%20Extremos/practica.md)).

> Analice si $f(0,0)$ es extremo de $f(x,y) = x^3 + xy^2$.

*Paso 1 — Hessiano.* $\nabla f(0,0) = \vec 0$. Como $f''_{xx} = 6x$, $f''_{xy} = 2y$ y $f''_{yy} = 2x$, en el origen $H = 0$: no decide.

*Paso 2 — Signo.* $f(0,0) = 0$ y $f = x(x^2 + y^2)$ tiene el signo de $x$. En todo entorno del origen hay puntos con $x > 0$ y puntos con $x < 0$.

**Resultado:** $f(0,0)$ no es extremo.

### Tipo 28: Extremos de una función armada con datos

**Cómo se reconoce.** No se da la fórmula completa, sino un polinomio de Taylor o un plano tangente.

**Método.**

1. Leer los datos: el polinomio de Taylor de orden 2 en $\vec A$ tiene el mismo valor y las mismas derivadas hasta orden 2 que $f$ en $\vec A$.
2. Derivar la función nueva con regla de la cadena.
3. Verificar que el gradiente se anula y aplicar el hessiano.

**Ejemplo** ([Repaso R8](repaso-primer-parcial.md)).

> $f \in C^2$ tiene polinomio de Taylor de 2.º orden en $(1,-1)$ igual a $p(x,y) = 4 - x^2 + y^2 + xy + y$. Demuestre que $g = f^2 + 6x^2$ alcanza un mínimo local en $(1,-1)$.

*Paso 1 — Datos,* evaluando $p$ en $(1,-1)$: $f = 2$, $f'_x = -2x + y = -3$, $f'_y = 2y + x + 1 = 0$, $f''_{xx} = -2$, $f''_{xy} = 1$, $f''_{yy} = 2$.

*Paso 2 — Gradiente de $g$.* $g'_x = 2ff'_x + 12x = 2\cdot2\cdot(-3) + 12 = 0$ y $g'_y = 2ff'_y = 0$. Es punto crítico.

*Paso 3 — Hessiano.*

- $g''_{xx} = 2(f'_x)^2 + 2ff''_{xx} + 12 = 18 - 8 + 12 = 22$.
- $g''_{xy} = 2f'_xf'_y + 2ff''_{xy} = 4$.
- $g''_{yy} = 2(f'_y)^2 + 2ff''_{yy} = 8$.

**Resultado:** $H = 22\cdot8 - 16 = 160 > 0$ y $g''_{xx} > 0$: mínimo local. $\blacksquare$

**Variante** ([Repaso R6](repaso-primer-parcial.md)): si $h = f - p$, con $p$ el plano tangente a $f$ en el punto, entonces $h$ vale 0, tiene gradiente nulo, y su hessiano es el de $f$ porque $p$ es lineal.

### Tipo 29: Extremos con restricción (Lagrange)

**Cómo se reconoce.** Extremos "sobre una curva", "punto más próximo", "sujeto a".

**Teoría.** En un extremo sobre $g = 0$, la curva de nivel de $f$ y la restricción son tangentes, así que sus gradientes son paralelos. Si $\nabla g \ne \vec 0$, los candidatos cumplen $\nabla f = \lambda\nabla g$, $g = 0$.

**Método.**

1. Función a optimizar (para distancias, usar $d^2$) y restricción.
2. Plantear el sistema.
3. Resolver **abriendo en casos**; no dividir por algo que pueda anularse.
4. Evaluar $f$ en los candidatos. Si la restricción es compacta, Weierstrass garantiza que el mayor y el menor son los extremos.

Alternativa: parametrizar la restricción y derivar en una variable.

**Ejemplo** ([TP7 – 18](../Unidad%2007%20-%20Taylor%20y%20Extremos/practica.md)).

> Determine los puntos de la curva $4y^2 - 18x + 9x^2 - 16y = 11$ más próximo y más alejado de $(1,7)$.

*Paso 1 — Reconocer la curva.* Completando cuadrados: $g = 9(x - 1)^2 + 4(y - 2)^2 - 36 = 0$. Es una elipse, y por lo tanto un compacto.

*Paso 2 — Sistema,* con $f = (x - 1)^2 + (y - 7)^2$:

$$2(x - 1) = 18\lambda(x - 1), \qquad 2(y - 7) = 8\lambda(y - 2), \qquad g = 0$$

*Paso 3 — Casos* de la primera ecuación: $(x - 1)(1 - 9\lambda) = 0$.

- $x = 1$: $4(y - 2)^2 = 36$, de donde $y = 5$ o $y = -1$.
- $\lambda = \tfrac19$: $18(y - 7) = 8(y - 2)$ da $y = 11$. Entonces $4\cdot81 = 324 > 36$, y $9(x - 1)^2$ debería ser negativo: imposible.

*Paso 4 — Comparar.* $f(1, 5) = 4$ y $f(1, -1) = 64$.

**Resultado:** el más cercano es $(1,5)$ y el más alejado, $(1,-1)$.

### Tipo 30: Extremos absolutos en un compacto

**Método.**

1. Justificar la existencia con Weierstrass: la región es cerrada y acotada, y $f$ es continua.
2. **Interior:** resolver $\nabla f = \vec 0$ y quedarse con los puntos de adentro.
3. **Frontera:** reemplazar la ecuación del borde en $f$, parametrizar o usar Lagrange. Incluir los vértices.
4. **Comparar** todos los valores. No hace falta el hessiano.

**Ejemplo** ([TP7 – 09](../Unidad%2007%20-%20Taylor%20y%20Extremos/practica.md)).

> Halle los extremos absolutos de $f(x,y) = \dfrac{x}{x^2 + y^2 + 1}$ en $D = \lbrace x^2 + y^2 \le 2x\rbrace$.

*Paso 1 — Existencia.* $D$ es el disco cerrado $(x - 1)^2 + y^2 \le 1$, y $f$ es continua.

*Paso 2 — Interior.*

$$f'_x = \frac{1 - x^2 + y^2}{(x^2 + y^2 + 1)^2}, \qquad f'_y = \frac{-2xy}{(x^2 + y^2 + 1)^2}$$

De $f'_y = 0$: $x = 0$ o $y = 0$. Con $x = 0$ el numerador de $f'_x$ es $1 + y^2 \ne 0$. Con $y = 0$: $x = \pm1$, y sólo $(1, 0)$ es interior. $f(1, 0) = \tfrac12$.

*Paso 3 — Frontera.* Reemplazando $x^2 + y^2 = 2x$, con $x \in [0, 2]$: $f = \varphi(x) = \dfrac{x}{2x + 1}$. Como $\varphi' = \dfrac{1}{(2x + 1)^2} > 0$, los extremos están en las puntas: $\varphi(0) = 0$ y $\varphi(2) = \tfrac25$.

*Paso 4 — Comparar* $\tfrac12$, $0$ y $\tfrac25$.

**Resultado:** máximo absoluto $f(1,0) = \tfrac12$; mínimo absoluto $f(0,0) = 0$.

### Tipo 31: Extremos de una función implícita

**Método** para $z = \varphi(x,y)$ definida por $F(x,y,z) = 0$.

1. Críticos: $F'_x = F'_y = 0$, junto con $F = 0$ y $F'_z \ne 0$.
2. En esos puntos, las derivadas segundas se simplifican: $z''_{ij} = -\dfrac{F''_{ij}}{F'_z}$.
3. Aplicar el hessiano.

**Ejemplo** ([TP7 – 16](../Unidad%2007%20-%20Taylor%20y%20Extremos/practica.md)).

> En $x^2 + 4y^2 + 9z^2 = 1$, suponiendo $z = \varphi(x,y)$, ¿en qué puntos $\varphi$ produce extremos? ¿Es única $\varphi$?

*Paso 1 — Críticos.* $F'_x = 2x = 0$ y $F'_y = 8y = 0$, así que $(x, y) = (0, 0)$ y $9z^2 = 1$: $z = \pm\tfrac13$, con $F'_z = 18z \ne 0$.

*Paso 2 — No es única:* hay una función por cada mitad del elipsoide.

*Paso 3 — Clasificar,* con $F''_{xx} = 2$, $F''_{yy} = 8$, $F''_{xy} = 0$.

- $z = \tfrac13$, $F'_z = 6$: $z''_{xx} = -\tfrac13$, $z''_{yy} = -\tfrac43$, $H = \tfrac49 > 0$ y $z''_{xx} < 0$: máximo.
- $z = -\tfrac13$, $F'_z = -6$: $z''_{xx} = \tfrac13$, $z''_{yy} = \tfrac43$, $H = \tfrac49 > 0$ y $z''_{xx} > 0$: mínimo.

**Resultado:** en $(0,0)$, la función de la mitad superior tiene máximo $\tfrac13$ y la de la mitad inferior, mínimo $-\tfrac13$.

---

## Bloque H: Ejercicios teóricos

### Tipo 32: Definiciones, enunciados y demostraciones

**Cómo encararlos.** Las definiciones de cada bloque se piden tal como están arriba. Un enunciado completo lleva hipótesis y tesis; escribir sólo la fórmula no alcanza. Muchas veces la consigna combina una definición con un ejercicio práctico corto, como en el [Tipo 3](#tipo-3-hallar-un-término-de-la-edo-a-partir-de-una-solución).

**Demostración 1: derivada direccional máxima** ([1.er Parcial 15/10/2019, T1](primer-parcial-2019-10-15.md)).

> Si $f$ es diferenciable en $\vec A$ y $\nabla f(\vec A) \ne \vec 0$, existe la derivada direccional máxima y vale $\Vert\nabla f(\vec A)\Vert$.

1. Por ser diferenciable: $f'(\vec A,\breve r) = \nabla f(\vec A)\cdot\breve r = \Vert\nabla f(\vec A)\Vert\cos\theta$, con $\theta$ el ángulo entre ambos vectores.
2. Como $\cos\theta \le 1$, resulta $f'(\vec A,\breve r) \le \Vert\nabla f(\vec A)\Vert$ para todo versor.
3. La cota se alcanza: como $\nabla f(\vec A) \ne \vec 0$, se puede tomar $\breve r_0 = \dfrac{\nabla f(\vec A)}{\Vert\nabla f(\vec A)\Vert}$, y entonces $f'(\vec A, \breve r_0) = \dfrac{\nabla f\cdot\nabla f}{\Vert\nabla f\Vert} = \Vert\nabla f(\vec A)\Vert$. $\blacksquare$

**Demostración 2: diferenciable implica continua** ([1.er Parcial 08/10/2014, T1](../UTNianos/La%20Gloria/AM2%20-%201er%20Parcial/08-11-14/IMG_1354.JPG)).

1. Se llama $\varepsilon(\vec h)$ al cociente de la definición, que tiende a 0. Entonces $f(\vec A + \vec h) - f(\vec A) = \nabla f(\vec A)\cdot\vec h + \Vert\vec h\Vert\thinspace \varepsilon(\vec h)$.
2. Cuando $\vec h \to \vec 0$, los dos términos de la derecha tienden a 0.
3. Por lo tanto $\lim\limits_{\vec h\to\vec 0}f(\vec A + \vec h) = f(\vec A)$. $\blacksquare$

**Demostración 3: diferenciable implica derivable en toda dirección** ([1.er Parcial 1C 2014, T2](../UTNianos/La%20Gloria/AM2%20-%201er%20Parcial/AMII%20-%202014-05-26%20-%201er%20Parcial%20Campillo%282%29.jpg)).

1. En la definición de diferenciable se toma $\vec h = t\breve r$, con $t \to 0$ y $\Vert\breve r\Vert = 1$, de modo que $\Vert\vec h\Vert = |t|$:

$$\lim_{t\to0}\frac{f(\vec A + t\breve r) - f(\vec A) - t\thinspace \nabla f(\vec A)\cdot\breve r}{|t|} = 0$$

2. Multiplicar por $\frac{|t|}{t}$, que vale $\pm1$ y está acotado, conserva el límite 0:

$$\lim_{t\to0}\left[\frac{f(\vec A + t\breve r) - f(\vec A)}{t} - \nabla f(\vec A)\cdot\breve r\right] = 0$$

3. Entonces la derivada existe y vale $f'(\vec A,\breve r) = \nabla f(\vec A)\cdot\breve r$. $\blacksquare$

**Demostración 4: una función vectorial es derivable si y sólo si lo son sus componentes** ([1.er Parcial 08/10/2014, T2](../UTNianos/La%20Gloria/AM2%20-%201er%20Parcial/08-11-14/IMG_1354.JPG)).

El cociente incremental de $\vec\lambda = (\lambda_1, \dots, \lambda_n)$ es un vector cuyas componentes son los cocientes incrementales de cada $\lambda_i$. Un límite vectorial existe si y sólo si existe el límite de cada componente. Por lo tanto, $\vec\lambda'(t_0)$ existe si y sólo si existe cada $\lambda_i'(t_0)$, y $\vec\lambda'(t_0) = (\lambda_1'(t_0), \dots, \lambda_n'(t_0))$. $\blacksquare$

---

## Errores frecuentes

- **Concluir que un límite existe porque dio igual por todas las rectas.** Hay que acotar.
- **Derivar con las reglas en el punto donde cambia la fórmula** de una función partida. Ahí se usa la definición.
- **Usar $\nabla f\cdot\breve r$ sin saber que $f$ es diferenciable.**
- **Evaluar las derivadas de $f$ en $\vec A$** en vez de en $\vec g(\vec A)$.
- **No verificar las hipótesis de Cauchy–Dini**, en particular $F'_z \ne 0$.
- **Perder soluciones al dividir** por $y$, $x - 1$ o $\lambda$. Hay que factorizar y abrir en casos.
- **Dejar el parámetro en la EDO** de una familia antes de pasar a la ortogonal.
- **Olvidar el factor $\tfrac12$** o el 2 del término cruzado en Taylor.
- **Dar como dirección un vector que no es versor.**
- **En extremos absolutos, olvidar la frontera o los vértices.**

---

[Volver al menú principal](../README.md)
