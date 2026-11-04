# Simulacro del 1.er Parcial

Análisis Matemático II — UTN-FRBA.

Enunciado y resolución manuscrita: [Parcial1-Simulacro-Resuelto.pdf](../aula-virtual/Parciales/Primer-Parcial/Parcial1-Simulacro-Resuelto.pdf).

Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

### P1) Continuidad y direcciones de derivada nula

Sea $f: \mathbb{R}^2 \to \mathbb{R}$ definida por $f(x,y) = \begin{cases} \dfrac{yx^2}{x^2 + 2y^2} & (x,y) \ne (0,0) \cr 0 & (x,y) = (0,0) \end{cases}$

- a) Estudiar continuidad de $f$ en $(0,0)$.
- b) Halle las direcciones de derivada nula de $f$ en $(0,0)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a)** Infinitésimo por acotada:

$$f = \underbrace{y}_{\to0}\cdot\underbrace{\frac{x^2}{x^2 + 2y^2}}_{\in[0,1]} \to 0 = f(0,0)$$

⇒ $f$ es **continua** en el origen.

**b)** Con $\breve r = (a, b)$, $a^2 + b^2 = 1$:

$$f'(\vec 0, \breve r) = \lim_{h\to0}\frac{1}{h}\cdot\frac{h^3\thinspace ba^2}{h^2(a^2 + 2b^2)} = \frac{ba^2}{a^2 + 2b^2} = \frac{ba^2}{1 + b^2}$$

En el último paso se usó $a^2 + 2b^2 = (a^2 + b^2) + b^2 = 1 + b^2$.

Es nula si y sólo si $ba^2 = 0$, es decir $b = 0$ o $a = 0$.

</details>

**Respuesta:**

- a) $f$ es continua en $(0,0)$.
- b) $f'(\vec 0, (a,b)) = \dfrac{ba^2}{1 + b^2}$; es nula en las direcciones $(\pm1, 0)$ y $(0, \pm1)$.

</details>

---

### P2) Recta tangente a una curva intersección

Sea $C$ la curva definida por la intersección de las superficies $S_1$: $3xy + \ln(x + yz - 6) - 2z = 0$; $S_2$: $z = x^2y + x$, analice si la recta tangente a $C$ en $A = (1, 2, z_0)$ tiene algún punto en común con el eje $x$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — $z_0$** (de $S_2$): $z_0 = 1\cdot2 + 1 = 3$. Se verifica en $S_1$: $6 + \ln(1 + 6 - 6) - 6 = 0$ ✓. Entonces $A = (1, 2, 3)$.

**Paso 2 — Gradientes** con $f_1 = 3xy + \ln(x + yz - 6) - 2z$ y $f_2 = x^2y + x - z$. En $A$, el argumento del logaritmo es $x + yz - 6 = 1$:

- $\nabla f_1 = \left(3y + \dfrac{1}{x+yz-6},\ 3x + \dfrac{z}{x+yz-6},\ \dfrac{y}{x+yz-6} - 2\right) \to (7,\ 6,\ 0)$.
- $\nabla f_2 = (2xy + 1,\ x^2,\ -1) \to (5,\ 1,\ -1)$.

**Paso 3 — Dirección tangente.**

$$\vec v_t = \nabla f_1\wedge\nabla f_2 = \begin{vmatrix} \breve\imath & \breve\jmath & \breve k \cr 7 & 6 & 0 \cr 5 & 1 & -1 \end{vmatrix} = (-6,\ 7,\ -23)$$

**Paso 4 — Recta tangente.** $\vec X = (1, 2, 3) + \alpha(-6, 7, -23)$.

**Paso 5 — ¿Corta al eje $x$?** Hace falta $y = 0$ y $z = 0$ a la vez:

- $y = 2 + 7\alpha = 0 \Rightarrow \alpha = -\frac27$;
- $z = 3 - 23\alpha = 0 \Rightarrow \alpha = \frac{3}{23}$.

Son valores distintos ⇒ no hay punto en común.

> En la resolución manuscrita aparece "$7\alpha + 1 = 0$", pero la segunda coordenada es $2 + 7\alpha$. La conclusión no cambia.

</details>

**Respuesta:** Recta tangente: $\vec X = (1,2,3) + \alpha(-6, 7, -23)$. No tiene puntos en común con el eje $x$.

</details>

---

### P3) Aproximación de una composición

Dado el campo $z = f(x,y)$ tal que la ecuación del plano tangente al gráfico de $f$ en el punto $P = (1, 0, z_0)$ es $2z - 6x + 3y = 0$, calcular aproximadamente $h(-0.98;\ 1.02)$ si el campo $h$ está definido por $h(u,v) = f(u^2v,\ u + v)$.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Datos de $f$ en $(1,0)$.** Del plano tangente, $z = 3x - \frac32y$:

- $f(1,0) = 3$;
- $\nabla f(1,0) = \left(3,\ -\frac32\right)$.

**Paso 2 — Punto base.** Elegimos $(u,v) = (-1, 1)$, porque $\vec g(-1,1) = ((-1)^2\cdot1,\ 0) = (1, 0)$. Entonces $h(-1,1) = f(1,0) = 3$.

**Paso 3 — Jacobiana de $\vec g = (u^2v,\ u + v)$:**

$$D\vec g = \begin{pmatrix} 2uv & u^2 \cr 1 & 1 \end{pmatrix} \ \Rightarrow\ D\vec g(-1,1) = \begin{pmatrix} -2 & 1 \cr 1 & 1 \end{pmatrix}$$

**Paso 4 — Regla de la cadena.**

$$\nabla h(-1,1) = \left(3,\ -\tfrac32\right)\begin{pmatrix} -2 & 1 \cr 1 & 1 \end{pmatrix} = \left(-6 - \tfrac32,\ 3 - \tfrac32\right) = \left(-\tfrac{15}{2},\ \tfrac32\right)$$

**Paso 5 — Aproximación** con incremento $(0{,}02;\ 0{,}02)$:

$$h(-0{,}98;\ 1{,}02) \approx 3 - \frac{15}{2}(0{,}02) + \frac32(0{,}02) = 3 - 0{,}15 + 0{,}03 = 2{,}88$$

</details>

**Respuesta:** $h(-0.98;\ 1.02) \approx 2.88$.

</details>

---

### P4) Puntos críticos

Sea $f: \mathbb{R}^2 \to \mathbb{R}$ definida por $f(x,y) = yx^2 + \frac43y^3 - 4y + 1$ hallar los puntos críticos de $f$ y determinar si son máximos o mínimos locales.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Puntos críticos.**

$$f'_x = 2xy = 0, \qquad f'_y = x^2 + 4y^2 - 4 = 0$$

- $x = 0$: $4y^2 = 4 \Rightarrow y = \pm1$.
- $y = 0$: $x^2 = 4 \Rightarrow x = \pm2$.

Los puntos son $(0,1)$, $(0,-1)$, $(2,0)$ y $(-2,0)$.

**Paso 2 — Hessiano.** $Hf = \begin{pmatrix} 2y & 2x \cr 2x & 8y \end{pmatrix}$.

| Punto | $\det H$ | $f''_{xx}$ | Clasificación | $f$ |
|---|---|---|---|---|
| $(\pm2, 0)$ | $0 - 16 < 0$ | | punto silla | |
| $(0, 1)$ | $16 > 0$ | $2 > 0$ | **mínimo local** | $\frac43 - 4 + 1 = -\frac53$ |
| $(0, -1)$ | $16 > 0$ | $-2 < 0$ | **máximo local** | $-\frac43 + 4 + 1 = \frac{11}{3}$ |

</details>

**Respuesta:** Puntos críticos: $(0,1)$, $(0,-1)$, $(\pm2, 0)$. $f(0,1) = -5/3$ es mínimo local; $f(0,-1) = 11/3$ es máximo local; en $(\pm2, 0)$ hay puntos silla.

</details>

---

[← Volver al menú principal](../README.md)
