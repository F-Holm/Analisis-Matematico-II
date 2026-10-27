# Unidad 11 — Teoremas integrales: Green, Gauss (divergencia) y Stokes (rotor)

Resumen del material teórico de la unidad ([U11-Teoria-Teoremas-Integrales.pdf](../aula-virtual/11-Teoremas-Integrales/U11-Teoria-Teoremas-Integrales.pdf)), complementado con el resumen [Condiciones de existencia de la función potencial](../aula-virtual/08-Curvas-Integrales-Linea/Funcion-Potencial-Condiciones.pdf) y los [repasos del segundo parcial](../aula-virtual/Parciales/Segundo-Parcial/Repaso-Segundo-Parcial-Resuelto.pdf) y el [resumen de UTNianos](../UTNianos/Resumen%20AM2.pdf).

**Objetivos de la unidad:**

1. Conocer los operadores divergencia, rotor y laplaciano.
2. Aplicar el teorema de Green (circulación en el plano), el de la divergencia (flujo a través de superficies cerradas) y el del rotor (circulación en el espacio).
3. Usar los teoremas para decidir si un campo admite potencial.

---

## 1. Operadores diferenciales

Para $\vec f = (P, Q, R)$:

| Operador | Definición | Resultado |
|---|---|---|
| Gradiente | $\nabla\phi = (\phi'_x, \phi'_y, \phi'_z)$ | vector |
| Divergencia | $\mathop{\mathrm{div}}\vec f = \nabla\cdot\vec f = P'_x + Q'_y + R'_z$ | escalar |
| Rotor | $\mathop{\mathrm{rot}}\vec f = \nabla\wedge\vec f = (R'_y - Q'_z,\ P'_z - R'_x,\ Q'_x - P'_y)$ | vector |
| Laplaciano | $\nabla^2\phi = \mathop{\mathrm{div}}(\nabla\phi) = \phi''_{xx} + \phi''_{yy} + \phi''_{zz}$ | escalar |

El rotor se calcula con el "determinante":

$$\mathop{\mathrm{rot}}\vec f = \begin{vmatrix} \breve\imath & \breve\jmath & \breve k \cr \partial_x & \partial_y & \partial_z \cr P & Q & R \end{vmatrix}$$

**Clasificación de campos:**

- **Solenoidal:** $\mathop{\mathrm{div}}\vec f \equiv 0$ (no tiene "fuentes" ni "sumideros").
- **Irrotacional:** $\mathop{\mathrm{rot}}\vec f \equiv \vec 0$, que equivale a que $D\vec f$ sea simétrica.
- **Armónico** (para un campo escalar): $\nabla^2\phi \equiv 0$.

**Identidades:**

- $\mathop{\mathrm{rot}}(\nabla\phi) = \vec 0$ (con $\phi\in C^2$).
- $\mathop{\mathrm{div}}(\mathop{\mathrm{rot}}\vec g) = 0$ (con $\vec g\in C^2$).
- $\mathop{\mathrm{div}}(f\vec g) = f\mathop{\mathrm{div}}\vec g + \nabla f\cdot\vec g$.
- $\mathop{\mathrm{rot}}(f\vec g) = f\mathop{\mathrm{rot}}\vec g + \nabla f\wedge\vec g$.
- $\mathop{\mathrm{div}}(\vec f\wedge\vec g) = \mathop{\mathrm{rot}}\vec f\cdot\vec g - \vec f\cdot\mathop{\mathrm{rot}}\vec g$.

**Interpretación física:**

- la divergencia mide cuánto "sale" el campo por unidad de volumen alrededor de un punto;
- el rotor mide la tendencia a "girar" (como un molinito en un fluido).

---

## 2. Teorema de Green (en el plano)

**Hipótesis:**

- $D \subset \mathbb{R}^2$ es una región acotada cuya frontera $\partial D$ está formada por curvas cerradas simples, suaves a trozos.
- $\vec f = (P, Q) \in C^1$ en un abierto que contiene a $D$ y a su frontera.

**Tesis:**

$$\boxed{\oint_{\partial D^+}P\thinspace dx + Q\thinspace dy = \iint_D\left(Q'_x - P'_y\right)dx\thinspace dy}$$

**Orientación positiva:** se recorre la frontera dejando la región **a la izquierda**. La curva exterior va en sentido antihorario y las curvas interiores (los "agujeros"), en sentido horario.

![Figura 11.25: región con un agujero; la frontera exterior C₁ se recorre en sentido antihorario y la interior C₂ en sentido horario](img/teoria-fig-11-25-region-doblemente-conexa.png)

### Aplicaciones

- **Área con una integral de línea:** si $Q'_x - P'_y = 1$, entonces $A(D) = \oint_{\partial D^+}\vec f\cdot d\vec s$. Por ejemplo:

$$A = \oint x\thinspace dy = -\oint y\thinspace dx = \frac12\oint(x\thinspace dy - y\thinspace dx)$$

  En general, si $Q'_x - P'_y = k \ne 0$ es constante, $A = \frac1k\oint\vec f\cdot d\vec s$.
- **Circulación fácil:** si $Q'_x - P'_y$ es simple (constante, o lineal con una región simétrica), Green ahorra parametrizar curvas complicadas.
- **Curvas no cerradas:** se "cierra" la curva con un segmento, se aplica Green y se resta lo que aporta el segmento.

### Regiones con "agujeros" (puntos donde $\vec f$ no es $C^1$)

Si $\vec f$ no es $C^1$ en un punto $A$, **no** se puede aplicar Green a una región que lo contenga. Se aplica a la región **entre dos curvas** que rodean a $A$:

$$\oint_{C_1^+}\vec f\cdot d\vec s - \oint_{C_2^+}\vec f\cdot d\vec s = \iint_{\text{entre } C_1 \text{ y } C_2}(Q'_x - P'_y)\thinspace dA$$

donde ambas curvas se recorren en sentido antihorario.

**Consecuencia:** si $Q'_x = P'_y$, todas las curvas que rodean a $A$ (una vez y en el mismo sentido) dan la **misma** circulación.

---

## 3. Green y la función potencial en el plano

Sea $\vec f\in C^1$ con $D\vec f$ simétrica ($Q'_x = P'_y$) en su dominio $D$.

| Dominio | ¿Admite potencial? |
|---|---|
| Simplemente conexo (sin agujeros), por ejemplo $\mathbb{R}^2$ | **Sí**: por Green toda circulación cerrada es 0 |
| $\mathbb{R}^2 - \lbrace A\rbrace$ | **Sí, si y sólo si** la circulación sobre **una** curva que rodee a $A$ es 0. Si da $\ne 0$, no admite |

**Ejemplo típico:** $\left(\dfrac{-y}{x^2+y^2}, \dfrac{x}{x^2+y^2}\right)$ tiene jacobiana simétrica y circulación $2\pi$ alrededor del origen ⇒ no admite potencial.

---

## 4. Teorema de la divergencia (Gauss-Ostrogradski)

**Hipótesis:**

- $H\subset\mathbb{R}^3$ es un cuerpo cuya frontera $\partial H$ es una superficie cerrada, suave a trozos, orientada con **normal saliente**.
- $\vec f\in C^1$ en un abierto que contiene a $H$.

**Tesis:**

$$\boxed{\oint\negthinspace\negthinspace\negthinspace\oint_{\partial H}\vec f\cdot\breve n\thinspace d\sigma = \iiint_H\mathop{\mathrm{div}}\vec f\thinspace dV}$$

### Usos típicos

- **Flujo a través de una superficie cerrada:** con una sola integral triple, en lugar de una integral por cada cara.
- **Flujo a través de una superficie abierta $S$** (por ejemplo, un paraboloide): se la **cierra** con una "tapa" $T$ simple, como un disco plano:

$$\Phi_S = \iiint_H\mathop{\mathrm{div}}\vec f\thinspace dV - \Phi_T$$

  Hay que cuidar que las normales de $S$ y $T$ sean salientes, y ajustar el signo según la orientación pedida.
- **Campos solenoidales** ($\mathop{\mathrm{div}} = 0$): el flujo a través de cualquier superficie cerrada es 0, y el flujo a través de superficies con el **mismo borde** es el mismo.
- **Campos con una singularidad** en $A$ y $\mathop{\mathrm{div}} = 0$ fuera de $A$: el flujo a través de una superficie cerrada es 0 si no encierra a $A$, y es **siempre el mismo** si lo encierra (ley de Gauss: $4\pi kq$ para el campo de una carga puntual).
- **Simetrías:** si $\mathop{\mathrm{div}}\vec f$ es impar respecto de un plano de simetría del cuerpo, la integral triple es 0.

---

## 5. Teorema del rotor (Stokes)

**Hipótesis:**

- $S$ es una superficie orientable, suave a trozos, con borde $\partial S$: una curva cerrada, suave a trozos.
- $\vec f\in C^1$ en un abierto que contiene a $S$.

**Tesis:**

$$\boxed{\oint_{\partial S^+}\vec f\cdot d\vec s = \iint_S\mathop{\mathrm{rot}}\vec f\cdot\breve n\thinspace d\sigma}$$

**Orientaciones compatibles (regla de la mano derecha):** si el pulgar apunta como $\breve n$, los dedos indican el sentido de recorrido de $\partial S$. Equivalentemente, caminando sobre el borde con la cabeza hacia $\breve n$, la superficie queda **a la izquierda**.

![Figura 11.34: superficie S con su normal n y el borde ∂S⁺ recorrido en el sentido compatible](img/teoria-fig-11-34-orientacion-stokes.png)

### Usos típicos

- **Circulación en el espacio** sobre una curva cerrada complicada (la intersección de dos superficies): se elige la superficie **más simple** cuyo borde sea esa curva (casi siempre un trozo de plano) y se calcula el flujo del rotor.
- **Green es el caso plano de Stokes:** $\breve n = \breve k$ y $\mathop{\mathrm{rot}}\vec f\cdot\breve k = Q'_x - P'_y$.
- **Potencial en el espacio:** si $\mathop{\mathrm{rot}}\vec f = \vec 0$ en un dominio **simplemente conexo** (por ejemplo $\mathbb{R}^3$, o $\mathbb{R}^3 - \lbrace A\rbrace$, que sí lo es), toda curva cerrada es borde de una superficie dentro del dominio, por Stokes la circulación es 0 y existe la potencial. $\mathbb{R}^3$ menos una **recta** (por ejemplo el eje $z$) **no** es simplemente conexo.

---

## 6. Complementos: el operador nabla e interpretaciones físicas

**Operador nabla:** $\nabla = \dfrac{\partial}{\partial x}\breve\imath + \dfrac{\partial}{\partial y}\breve\jmath + \dfrac{\partial}{\partial z}\breve k$. Se comporta como un vector, así que puede:

- multiplicar a un campo escalar: **gradiente** $\nabla\phi$ (da un campo vectorial);
- multiplicarse **escalarmente** por un campo vectorial: **divergencia** $\nabla\cdot\vec F$ (da un campo escalar);
- multiplicarse **vectorialmente** por un campo vectorial: **rotor** $\nabla\times\vec F$ (da un campo vectorial).

### Interpretación física de la divergencia

Sea $\vec F = \delta\thinspace\vec v$ ($\delta$ densidad de un fluido, $\vec v$ su velocidad): $\vec F$ mide la masa por unidad de área y de tiempo. En un prisma chico de aristas $\Delta x, \Delta y, \Delta z$ con vértice en $P_0$, en la dirección $\breve\jmath$ la masa que sale por una cara menos la que entra por la opuesta es

$$[F_2(x_0, y_0 + \Delta y, z_0) - F_2(x_0, y_0, z_0)]\thinspace\Delta x\thinspace\Delta z$$

Dividiendo por el volumen y tomando límite se obtiene $\dfrac{\partial F_2}{\partial y}$. Sumando las tres direcciones:

$$\mathop{\mathrm{div}}\vec F(P_0) = \frac{\partial F_1}{\partial x} + \frac{\partial F_2}{\partial y} + \frac{\partial F_3}{\partial z}$$

es la variación total de masa por unidad de tiempo y de volumen en $P_0$.

- $\mathop{\mathrm{div}}\vec F > 0$: en $P_0$ hay una **fuente** (manantial): se genera fluido.
- $\mathop{\mathrm{div}}\vec F < 0$: hay un **sumidero** (pozo): se pierde fluido.

**Interpretación del teorema de la divergencia:** el flujo neto que sale por la frontera de $V$ (lo que sale menos lo que entra) es igual a la masa que se genera adentro por unidad de tiempo.

### Interpretación física del rotor

En un cuerpo rígido que gira alrededor de un eje con velocidad angular $\vec w$, la velocidad tangencial de cada punto es $\vec v = \vec w\times\vec r$. Si gira alrededor del eje $z$, $\vec w = w\breve k$ y $\vec v = (-wy,\ wx,\ 0)$:

$$\nabla\times\vec v = \begin{vmatrix} \breve\imath & \breve\jmath & \breve k \cr \partial_x & \partial_y & \partial_z \cr -wy & wx & 0 \end{vmatrix} = (0,\ 0,\ 2w) = 2\vec w$$

**El rotor del campo de velocidades es el doble de la velocidad angular.** Un campo con rotor nulo no produce rotaciones: es **irrotacional** (como los campos de gradientes).

---

## 7. Complementos: demostración de Green y consecuencias

**Demostración de Green** (para un recinto $R$ tal que toda paralela a los ejes corta a su borde en a lo sumo dos puntos). Se demuestran por separado $\iint_R Q'_x = \oint Q\thinspace dy$ y $-\iint_R P'_y = \oint P\thinspace dx$.

- Mirando $R$ como tipo I, $y_1(x) \le y \le y_2(x)$:

$$-\iint_R\frac{\partial P}{\partial y}\thinspace dx\thinspace dy = -\int_a^b\big[P(x, y_2(x)) - P(x, y_1(x))\big]dx = \int_{\text{abajo}}P\thinspace dx + \int_{\text{arriba}}P\thinspace dx = \oint_C P\thinspace dx$$

  (el arco de abajo se recorre de izquierda a derecha y el de arriba al revés, por eso aparecen los signos).

- Mirando $R$ como tipo II, $x_1(y) \le x \le x_2(y)$, del mismo modo $\iint_R\frac{\partial Q}{\partial x} = \oint_C Q\thinspace dy$.

Sumando se obtiene el teorema. Si el recinto no cumple la condición, se lo divide en finitos recintos que sí la cumplen: las integrales sobre los cortes interiores se recorren dos veces en sentidos opuestos y se cancelan. $\blacksquare$

**Consecuencia del teorema del rotor:** si dos superficies abiertas, orientables y regulares tienen **el mismo borde** $C$, el flujo del rotor a través de ambas es el mismo (las dos valen la circulación sobre $C$). Así se puede elegir la superficie más cómoda.

**Hipótesis de Gauss (como en el resumen):** $\vec F$ con derivadas parciales continuas en un sólido simple $V$, proyectable sobre los tres planos coordenados, limitado por una superficie cerrada orientable con versor normal (exterior) que varía con continuidad.

---

## 8. Estrategia para los ejercicios

1. **Circulación en el plano sobre una curva cerrada:** usar Green. Si hay un punto singular adentro, usar Green entre dos curvas. Si la curva es abierta, cerrarla.
2. **Circulación en el espacio sobre una curva cerrada:** usar Stokes, eligiendo una superficie simple y la normal compatible con el sentido de recorrido.
3. **Flujo a través de una superficie cerrada:** usar la divergencia.
4. **Flujo a través de una superficie abierta "difícil":** cerrarla con una tapa y usar la divergencia.
5. **¿Admite potencial?**
   1. ¿$D\vec f$ es simétrica (o el rotor es nulo)? Si no, **no** admite.
   2. Si lo es, ¿el dominio es simplemente conexo? Si sí, **sí** admite.
   3. Si no lo es, calcular la circulación alrededor del agujero: si es 0 admite, y si no, no.

---

## 9. Resumen de fórmulas

| Teorema | Fórmula |
|---|---|
| Green | $\oint_{\partial D^+}\vec f\cdot d\vec s = \iint_D(Q'_x - P'_y)\thinspace dA$ |
| Área con Green | $A = \oint x\thinspace dy = -\oint y\thinspace dx = \frac12\oint(x\thinspace dy - y\thinspace dx)$ |
| Divergencia | $\oint\negthinspace\negthinspace\oint_{\partial H}\vec f\cdot\breve n\thinspace d\sigma = \iiint_H\mathop{\mathrm{div}}\vec f\thinspace dV$ |
| Rotor (Stokes) | $\oint_{\partial S}\vec f\cdot d\vec s = \iint_S\mathop{\mathrm{rot}}\vec f\cdot\breve n\thinspace d\sigma$ |
| Identidades | $\mathop{\mathrm{rot}}\nabla\phi = \vec 0$, $\ \mathop{\mathrm{div}}\mathop{\mathrm{rot}}\vec g = 0$ |
| Ley de Gauss | $\oint\negthinspace\negthinspace\oint\frac{kq\thinspace\vec r}{r^3}\cdot\breve n\thinspace d\sigma = 4\pi kq$ (si encierra al origen) |

---

[← Volver al menú principal](../README.md)
