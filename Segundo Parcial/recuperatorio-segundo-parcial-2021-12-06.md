# Primer Recuperatorio del 2.º Parcial (06/12/2021)

Análisis Matemático II — UTN-FRBA.

Enunciado (foto, sin resolución oficial): [Recuperatorio2-2021-12-06.jpeg](../aula-virtual/Parciales/Segundo-Parcial/fotos/Recuperatorio2-2021-12-06.jpeg).

> La foto está desenfocada. Se transcribe todo lo legible; donde un número o símbolo es dudoso se aclara en una nota debajo del enunciado.

Las resoluciones son propias (no hay solución de la cátedra). Cada ejercicio tiene un botón **Solución**. Al abrirlo aparece la respuesta y, arriba de ella, un segundo botón **Solución paso a paso** con el desarrollo completo.

---

## Ejercicios Prácticos

### P1) Circulación sobre la intersección de un paraboloide y un cono

Sea $\bar f: R^3 \to R^3$ tal que $\bar f(x,y,z) = (3x^2y^2z + x^2z;\ 2yx^3z + y^2;\ x^3y^2 + z^2x)$ Calcular la circulación del campo $\bar f$ a través de la curva intersección de las superficies: $y = 8 - x^2 - z^2$ ; $y = \sqrt{x^2 + z^2}$ orientada en sentido horario.

> En la foto el número del paraboloide se lee "8" (podría ser un 6). El resultado no depende de ese valor.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Curva.** En coordenadas con eje $y$ ($x = r\cos\theta$, $z = r\mathop{\mathrm{sen}}\theta$): $r = 8 - r^2 \Rightarrow r_0 = \frac{-1 + \sqrt{33}}{2}$. La curva es la circunferencia $x^2 + z^2 = r_0^2$ en el plano $y = r_0$ (con un 6 sería $r_0 = 2$, $y = 2$).

**Paso 2 — Separar una parte conservativa.** $3x^2y^2z$, $2yx^3z$ y $x^3y^2$ son las derivadas de $x^3y^2z$. Entonces

$$\bar f = \nabla(x^3y^2z) + (x^2z,\ y^2,\ z^2x)$$

La parte gradiente tiene circulación 0 sobre una curva cerrada.

**Paso 3 — Rotor del resto.** $\vec g = (x^2z, y^2, z^2x)$:

$$\nabla\times\vec g = (0 - 0,\ x^2 - z^2,\ 0 - 0) = (0,\ x^2 - z^2,\ 0)$$

**Paso 4 — Stokes con el disco plano.** La curva borde el disco $S$: $y = r_0$, $x^2 + z^2 \le r_0^2$, de normal $\pm(0,1,0)$:

$$\oint\vec g\cdot d\bar s = \pm\iint_{x^2 + z^2 \le r_0^2}(x^2 - z^2)\thinspace dx\thinspace dz = \pm\int_0^{2\pi}\negthinspace\negthinspace\int_0^{r_0} r^2(\cos^2\theta - \mathop{\mathrm{sen}}^2\theta)\thinspace r\thinspace dr\thinspace d\theta = 0$$

porque $\int_0^{2\pi}\cos 2\theta\thinspace d\theta = 0$.

</details>

**Respuesta:** La circulación vale $0$ (en sentido horario y también en el antihorario).

</details>

---

### P2) Masa de un sólido entre una esfera y un cono

Plantear las integrales que permiten calcular la masa del sólido de $R^3$ definido por $x^2 + y^2 + z^2 \le 4$; $y \ge \sqrt{x^2 + z^2} - 2$ si la densidad en cada punto es proporcional a la distancia al eje y.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Geometría.** $y = \sqrt{x^2 + z^2} - 2$ es un cono de eje $y$ con vértice en $(0,-2,0)$ (un punto de la esfera) que se abre hacia $y > 0$. El sólido es la parte de la bola que queda dentro del cono (por encima en $y$).

**Paso 2 — Cilíndricas con eje $y$.** $x = r\cos\theta$, $z = r\mathop{\mathrm{sen}}\theta$, jacobiano $r$. Cono: $y = r - 2$; esfera: $y = \pm\sqrt{4 - r^2}$.

Intersección: $r^2 + (r - 2)^2 = 4 \Rightarrow 2r^2 - 4r = 0 \Rightarrow r = 0$ (vértice) o $r = 2$ (en $y = 0$).

Para $0 \le r \le 2$: $r - 2 \le y \le \sqrt{4 - r^2}$.

**Paso 3 — Densidad.** Distancia al eje $y$: $\sqrt{x^2 + z^2} = r$, así que $\delta = k\thinspace r$ ($k > 0$).

**Paso 4 — Planteo.**

$$M = \int_0^{2\pi}\negthinspace\negthinspace\int_0^2\negthinspace\negthinspace\int_{r - 2}^{\sqrt{4 - r^2}} k\thinspace r\cdot r\thinspace dy\thinspace dr\thinspace d\theta$$

**Paso 5 — (Opcional) Calcular.** $\int_0^2 r^2\sqrt{4 - r^2}\thinspace dr = \pi$ (sustitución $r = 2\mathop{\mathrm{sen}}u$) y $\int_0^2 r^2(2 - r)\thinspace dr = \frac43$:

$$M = 2\pi k\left(\pi + \frac43\right)$$

</details>

**Respuesta:** $M = \displaystyle\int_0^{2\pi}\negthinspace\negthinspace\int_0^2\negthinspace\negthinspace\int_{r - 2}^{\sqrt{4 - r^2}} k\thinspace r^2\thinspace dy\thinspace dr\thinspace d\theta = 2\pi k\left(\pi + \frac43\right)$.

</details>

---

### P3) Longitud de una elipse en el espacio y EDO

a) Calcular la longitud del arco de curva intersección de las superficies $x^2 + 2y^2 = 8$ ; $y + z = 2$

b) Hallar las soluciones de la ecuación diferencial $y'' + 3y' = x$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**a) Paso 1 — Parametrización.** $\frac{x^2}{8} + \frac{y^2}{4} = 1$: $x = 2\sqrt2\cos t$, $y = 2\mathop{\mathrm{sen}}t$, y del plano $z = 2 - 2\mathop{\mathrm{sen}}t$, $0 \le t \le 2\pi$.

**Paso 2 — Velocidad.** $\vec\alpha'(t) = (-2\sqrt2\mathop{\mathrm{sen}}t,\ 2\cos t,\ -2\cos t)$:

$$\Vert\vec\alpha'\Vert^2 = 8\mathop{\mathrm{sen}}^2t + 4\cos^2t + 4\cos^2t = 8 \Rightarrow \Vert\vec\alpha'\Vert = 2\sqrt2$$

**Paso 3 — Longitud.** $L = \int_0^{2\pi}2\sqrt2\thinspace dt = 4\sqrt2\thinspace\pi$. (La curva es una circunferencia de radio $2\sqrt2$.)

**b) Paso 1 — Homogénea.** $r^2 + 3r = 0 \Rightarrow r = 0,\ r = -3$: $y_h = C_1 + C_2e^{-3x}$.

**Paso 2 — Particular.** El segundo miembro es un polinomio de grado 1 y $r = 0$ es raíz simple ⇒ $y_p = x(Ax + B) = Ax^2 + Bx$.

$y_p'' + 3y_p' = 2A + 6Ax + 3B = x \Rightarrow A = \frac16$, $B = -\frac{2A}{3} = -\frac19$.

</details>

**Respuesta:** a) $L = 4\sqrt2\thinspace\pi$. b) $y = C_1 + C_2e^{-3x} + \dfrac{x^2}{6} - \dfrac{x}{9}$.

</details>

---

### P4) Flujo a través de un cilindro parabólico

Calcular el flujo del campo $\bar f: R^3 \to R^3$ tal que $\bar f(x,y,z) = (x + y;\ 2y;\ x^3y + z)$ a través de la porción de superficie $y = x^2$ con $z + y \le 4$ ; $z \ge 0$

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parametrización.** $\vec T(x,z) = (x,\ x^2,\ z)$ con $0 \le z \le 4 - x^2$, que exige $-2 \le x \le 2$.

**Paso 2 — Normal.** $\vec T'_x\wedge\vec T'_z = (1, 2x, 0)\wedge(0,0,1) = (2x,\ -1,\ 0)$.

**Paso 3 — Producto escalar.**

$$\bar f\cdot\vec n = (x + x^2)\thinspace 2x + 2x^2\cdot(-1) = 2x^3$$

**Paso 4 — Integrar.**

$$\Phi = \int_{-2}^2\negthinspace\negthinspace\int_0^{4 - x^2}2x^3\thinspace dz\thinspace dx = \int_{-2}^2 2x^3(4 - x^2)\thinspace dx = 0$$

por ser impar el integrando en un intervalo simétrico.

</details>

**Respuesta:** $\Phi = 0$ (con cualquiera de las dos orientaciones).

</details>

---

## Ejercicios Teóricos

### T1) Circulación de un gradiente más un campo

Sean el campo vectorial $\bar g(x,y) = (2xy + y^2;\ x^2 + 4)$ y el campo escalar $z = h(x,y)$ con $h \in C^2$, calcular $\int_C\bar f\thinspace\overline{ds}$ si $\bar f = \nabla h + \bar g$ y C es la curva frontera de la región $x^2 + y^2 \le 2x$

> En la foto hay caracteres tachados antes de $x^2 + 4$ y después de $C^2$; se transcribe lo que queda sin tachar.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Parte gradiente.** $h \in C^2$ ⇒ $\nabla h$ es conservativo en $\mathbb{R}^2$: su circulación sobre la curva cerrada $C$ es 0.

**Paso 2 — Green para $\bar g$.** Región: $(x - 1)^2 + y^2 \le 1$, con $C$ en sentido positivo:

$$Q'_x - P'_y = 2x - (2x + 2y) = -2y$$

$$\oint_C\bar g\cdot d\bar s = \iint_D -2y\thinspace dA = -2\thinspace\bar y\cdot\text{Área} = 0$$

porque el centroide del disco es $(1, 0)$.

</details>

**Respuesta:** $\displaystyle\oint_C\bar f\cdot d\bar s = 0$.

</details>

---

### T2) ¿Admite potencial?

Dado el campo $\bar f(x,y) = \left(-\dfrac{4y}{x^2 + y^2};\ \dfrac{4x}{x^2 + y^2}\right)$, justifique claramente el procedimiento utilizado.

> La pregunta no se ve completa en la foto. Por la anotación a mano ("si admite potencial") se interpreta que se pregunta si $\bar f$ admite función potencial.

<details>
<summary><b>Solución</b></summary>

<details>
<summary>Solución paso a paso</summary>

**Paso 1 — Dominio.** $D = \mathbb{R}^2 - \{(0,0)\}$, no simplemente conexo.

**Paso 2 — Condición necesaria.**

$$P'_y = -4\thinspace\frac{x^2 + y^2 - 2y^2}{(x^2 + y^2)^2} = \frac{4(y^2 - x^2)}{(x^2 + y^2)^2}, \qquad Q'_x = 4\thinspace\frac{x^2 + y^2 - 2x^2}{(x^2 + y^2)^2} = \frac{4(y^2 - x^2)}{(x^2 + y^2)^2}$$

Se cumple, pero no alcanza porque $D$ tiene un "agujero".

**Paso 3 — Circulación sobre la circunferencia unitaria.** $\vec\alpha(t) = (\cos t, \mathop{\mathrm{sen}}t)$:

$$\oint\bar f\cdot d\bar s = \int_0^{2\pi}(4\mathop{\mathrm{sen}}^2t + 4\cos^2t)\thinspace dt = 8\pi \ne 0$$

⇒ **no** admite función potencial en $D$.

**Paso 4 — En regiones simplemente conexas sí.** Si se saca una semirrecta que parte del origen (por ejemplo, $y = 0$, $x \le 0$), el campo admite potencial $\varphi = 4\theta$ (cuatro veces el ángulo polar).

</details>

**Respuesta:** No admite potencial en $\mathbb{R}^2 - \{0\}$ (la circulación sobre $x^2 + y^2 = 1$ es $8\pi$). Sí lo admite en cualquier región simplemente conexa que no contenga al origen ($\varphi = 4\theta$).

</details>

---

[Volver al menú principal](../README.md)
