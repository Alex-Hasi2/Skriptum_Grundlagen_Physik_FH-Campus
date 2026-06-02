# AWII Pruefung SS2026 - Pruefungstermin 4: Loesung

## Beispiel 1

1. **Falsch**  
   $\vec a = (a_x,a_y,a_z)$ ist die Komponenten- oder Koordinatendarstellung. Die Einheitsvektordarstellung lautet zum Beispiel
   $$
   \vec a = a_x\vec e_x + a_y\vec e_y + a_z\vec e_z.
   $$

2. **Wahr**  
   Fuer $A(4,-3,5)$ und $B(-1,3,-6)$ gilt
   $$
   \overrightarrow{BA}=A-B=(4-(-1),-3-3,5-(-6))=(5,-6,11).
   $$

3. **Falsch**  
   Bei parallelen Vektoren ist das Skalarprodukt im Allgemeinen nicht null. Null wird es bei senkrechten Vektoren.

4. **Wahr**  
   Es gilt
   $$
   n! = n\cdot(n-1)\cdot(n-2)\cdots 2\cdot 1.
   $$

5. **Falsch**  
   Die zweite Ableitung beschreibt das Kruemmungsverhalten. Das Monotonieverhalten haengt vom Vorzeichen der ersten Ableitung ab.

6. **Falsch**  
   Eine Taylorreihe kann auch um andere Entwicklungspunkte $x_0$ entwickelt werden, nicht nur um $x_0=0$.

7. **Wahr**  
   Genau das ist die Grundidee der Fourierreihe.

8. **Wahr**  
   Es gilt
   $$
   \vec v(t)=\frac{d\vec r(t)}{dt},
   $$
   und der Ortsvektor ergibt sich umgekehrt durch Integration der Geschwindigkeit ueber die Zeit.

9. **Falsch**  
   Die Bogenlaenge einer Kurve $y=f(x)$ im Intervall $[a,b]$ berechnet sich mit
   $$
   L=\int_a^b \sqrt{1+\left(f'(x)\right)^2}\,dx
   $$
   und nicht mit
   $$
   \int_a^b \sqrt{f(x)^2}\,dx.
   $$

10. **Falsch**  
    Aus $F'(x)=f(x)$ folgt nicht
    $$
    \int F(x)\,dx = f(x),
    $$
    sondern $\int F(x)\,dx$ ist eine Stammfunktion von $F(x)$.

## Beispiel 2

### a) $\displaystyle \lim_{x \to 0} \frac{\sin(3x)}{x}$

Es liegt die Form $\frac{0}{0}$ vor, daher ist de l'Hospital anwendbar:

$$
\lim_{x \to 0} \frac{\sin(3x)}{x}
= \lim_{x \to 0} \frac{3\cos(3x)}{1}
= 3.
$$

### b) $\displaystyle \lim_{x \to 0} \frac{e^{2x}-1-2x}{x^2}$

Zunaechst liegt ebenfalls die Form $\frac{0}{0}$ vor:

$$
\lim_{x \to 0} \frac{e^{2x}-1-2x}{x^2}
= \lim_{x \to 0} \frac{2e^{2x}-2}{2x}
= \lim_{x \to 0} \frac{e^{2x}-1}{x}.
$$

Nochmals de l'Hospital:

$$
\lim_{x \to 0} \frac{e^{2x}-1}{x}
= \lim_{x \to 0} \frac{2e^{2x}}{1}
= 2.
$$

### c) $\displaystyle \lim_{x \to \infty} \frac{\ln(x)}{x}$

Hier liegt die Form $\frac{\infty}{\infty}$ vor:

$$
\lim_{x \to \infty} \frac{\ln(x)}{x}
= \lim_{x \to \infty} \frac{1/x}{1}
= \lim_{x \to \infty} \frac{1}{x}
= 0.
$$

### d) $\displaystyle \lim_{x \to 1} \frac{x^2-1}{x-1}$

Zerlegen des Zaehlers:

$$
\frac{x^2-1}{x-1} = \frac{(x-1)(x+1)}{x-1} = x+1 \qquad (x \neq 1).
$$

Damit folgt direkt

$$
\lim_{x \to 1} \frac{x^2-1}{x-1} = \lim_{x \to 1} (x+1) = 2.
$$

## Beispiel 3

Gegeben ist

$$
\vec r(t)=\begin{pmatrix}
t^2-1 \\
2t \\
\frac{1}{2}t^2
\end{pmatrix}.
$$

### 1. Geschwindigkeitsvektor

Die Geschwindigkeit ist die erste Ableitung des Ortsvektors nach der Zeit:

$$
\vec v(t)=\frac{d\vec r(t)}{dt}
= \begin{pmatrix}
2t \\
2 \\
t
\end{pmatrix}\,\mathrm{m/s}.
$$

### 2. Beschleunigungsvektor

Die Beschleunigung ist die Ableitung der Geschwindigkeit:

$$
\vec a(t)=\frac{d\vec v(t)}{dt}
= \begin{pmatrix}
2 \\
0 \\
1
\end{pmatrix}\,\mathrm{m/s^2}.
$$

### 3. Ort, Geschwindigkeit und Beschleunigung bei $t=2\,\mathrm{s}$

Einsetzen von $t=2$ liefert:

$$
\vec r(2)=\begin{pmatrix}
2^2-1 \\
2\cdot 2 \\
\frac{1}{2}\cdot 2^2
\end{pmatrix}
= \begin{pmatrix}
3 \\
4 \\
2
\end{pmatrix}\,\mathrm{m},
$$

$$
\vec v(2)=\begin{pmatrix}
4 \\
2 \\
2
\end{pmatrix}\,\mathrm{m/s},
$$

$$
\vec a(2)=\begin{pmatrix}
2 \\
0 \\
1
\end{pmatrix}\,\mathrm{m/s^2}.
$$

### 4. Betrag der Geschwindigkeit bei $t=3\,\mathrm{s}$

$$
\vec v(3)=\begin{pmatrix}
6 \\
2 \\
3
\end{pmatrix}\,\mathrm{m/s}.
$$

Damit ergibt sich

$$
|\vec v(3)| = \sqrt{6^2+2^2+3^2}
= \sqrt{36+4+9}
= \sqrt{49}
= 7.00\,\mathrm{m/s}.
$$

## Beispiel 4

Aus einem quadratischen Blech mit Seitenlaenge $30\,\mathrm{cm}$ wird eine oben offene Schachtel gebildet.

### 1. Volumenfunktion

Nach dem Ausschneiden hat die Grundflaeche die Seitenlaenge

$$
30-2x
$$

und die Hoehe der Schachtel ist

$$
x.
$$

Damit ist das Volumen

$$
V(x)=x(30-2x)^2.
$$

### 2. Sinnvoller Definitionsbereich

Damit alle Laengen positiv sind, muss gelten

$$
x>0
\qquad \text{und} \qquad 30-2x>0.
$$

Daraus folgt

$$
0 < x < 15.
$$

### 3. Maximum des Volumens

Zunaechst wird die Funktion ausmultipliziert:

$$
V(x)=x(30-2x)^2 = x(900-120x+4x^2)=900x-120x^2+4x^3.
$$

Ableiten ergibt

$$
V'(x)=900-240x+12x^2.
$$

Faktorisieren liefert

$$
V'(x)=12(x^2-20x+75)=12(x-5)(x-15).
$$

Kritische Stellen sind daher

$$
x=5 \qquad \text{und} \qquad x=15.
$$

Da nur $x=5$ im sinnvollen Intervall liegt, ist dies der relevante Kandidat fuer das Maximum.

### 4. Maximales Volumen

Einsetzen von $x=5$:

$$
V(5)=5\cdot (30-10)^2 = 5\cdot 20^2 = 5\cdot 400 = 2000.
$$

Also ist das maximale Volumen

$$
V_{\max}=2000\,\mathrm{cm^3}.
$$

### 5. Nachweis, dass ein Maximum vorliegt

Die zweite Ableitung lautet

$$
V''(x)=24x-240.
$$

An der Stelle $x=5$ gilt

$$
V''(5)=24\cdot 5-240=120-240=-120<0.
$$

Also liegt bei $x=5$ tatsaechlich ein Maximum vor.

## Beispiel 5

Gesucht ist die Taylorreihe bis zur 3. Ordnung von

$$
f(x)=\ln(x)
$$

um den Entwicklungspunkt $x_0=1$.

### 1. Benoetigte Ableitungen

$$
f(x)=\ln(x)
$$

$$
f'(x)=\frac{1}{x}
$$

$$
f''(x)=-\frac{1}{x^2}
$$

$$
f'''(x)=\frac{2}{x^3}.
$$

Am Entwicklungspunkt $x_0=1$ gilt

$$
f(1)=0, \qquad f'(1)=1, \qquad f''(1)=-1, \qquad f'''(1)=2.
$$

### 2. Taylorpolynom 3. Ordnung

Die allgemeine Form lautet

$$
T_3(x)=f(1)+f'(1)(x-1)+\frac{f''(1)}{2!}(x-1)^2+\frac{f'''(1)}{3!}(x-1)^3.
$$

Einsetzen ergibt

$$
T_3(x)=0 + 1\cdot(x-1) + \frac{-1}{2}(x-1)^2 + \frac{2}{6}(x-1)^3.
$$

Also

$$
T_3(x)=(x-1)-\frac{1}{2}(x-1)^2+\frac{1}{3}(x-1)^3.
$$

### 3. Naeherung von $\ln(1.1)$ und Vergleich mit dem exakten Wert

Fuer $x=1.1$ ist

$$
x-1=0.1.
$$

Somit folgt

$$
T_3(1.1)=0.1-\frac{1}{2}(0.1)^2+\frac{1}{3}(0.1)^3.
$$

$$
T_3(1.1)=0.1-0.005+\frac{1}{3}\cdot 0.001
=0.1-0.005+0.000333\ldots
=0.095333\ldots
$$

Damit ist

$$
\ln(1.1) \approx 0.09533.
$$

Der exakte Wert lautet naehrungsweise

$$
\ln(1.1) \approx 0.09531.
$$

Die Abweichung ist daher sehr klein:

$$
|0.09533-0.09531| \approx 0.00002.
$$

## Beispiel 6

Gegeben ist

$$
f(x,y)=x^2y+e^{xy}.
$$

### 1. Partielle Ableitungen

Partielle Ableitung nach $x$:

$$
\frac{\partial f}{\partial x}=2xy+ye^{xy}.
$$

Partielle Ableitung nach $y$:

$$
\frac{\partial f}{\partial y}=x^2+xe^{xy}.
$$

### 2. Gemischte zweite Ableitung $\frac{\partial^2 f}{\partial y\partial x}$

Wir leiten $\frac{\partial f}{\partial x}$ nach $y$ ab:

$$
\frac{\partial^2 f}{\partial y\partial x}
= \frac{\partial}{\partial y}(2xy+ye^{xy})
= 2x + e^{xy} + xye^{xy}.
$$

### 3. Partielle Ableitungen an der Stelle $(1,0)$

Zunaechst ist

$$
e^{1\cdot 0}=e^0=1.
$$

Damit ergibt sich

$$
\frac{\partial f}{\partial x}(1,0)=2\cdot 1\cdot 0 + 0\cdot 1 = 0,
$$

$$
\frac{\partial f}{\partial y}(1,0)=1^2 + 1\cdot 1 = 2,
$$

$$
\frac{\partial^2 f}{\partial y\partial x}(1,0)=2\cdot 1 + 1 + 1\cdot 0\cdot 1 = 3.
$$

Also gelten an der Stelle $(1,0)$:

$$
\frac{\partial f}{\partial x}(1,0)=0,
\qquad
\frac{\partial f}{\partial y}(1,0)=2,
\qquad
\frac{\partial^2 f}{\partial y\partial x}(1,0)=3.
$$

### 4. Bedeutung von $\frac{\partial f}{\partial x}$

Die partielle Ableitung $\frac{\partial f}{\partial x}$ beschreibt, wie stark sich die Funktion $f$ aendert, wenn nur die Variable $x$ veraendert wird und $y$ konstant bleibt.

## Beispiel 7

Gegeben ist

$$
I=\int_0^2 \int_0^{1+x} (x+2y)\,dy\,dx.
$$

### 1. Berechnung des Doppelintegrals

Zuerst wird nach $y$ integriert:

$$
\int_0^{1+x} (x+2y)\,dy
= \left[xy+y^2\right]_0^{1+x}.
$$

Einsetzen ergibt

$$
x(1+x)+(1+x)^2.
$$

Ausmultipliziert:

$$
x+x^2+1+2x+x^2 = 1+3x+2x^2.
$$

Damit wird das aeussere Integral zu

$$
I=\int_0^2 (1+3x+2x^2)\,dx.
$$

Nun nach $x$ integrieren:

$$
I=\left[x+\frac{3}{2}x^2+\frac{2}{3}x^3\right]_0^2.
$$

Einsetzen liefert

$$
I=2+\frac{3}{2}\cdot 4 + \frac{2}{3}\cdot 8 = 2+6+\frac{16}{3} = \frac{40}{3}.
$$

Also ist

$$
I=\frac{40}{3}.
$$

### 2. Integrationsbereich in der $xy$-Ebene

Der Bereich ist gegeben durch

$$
0 \le x \le 2,
\qquad
0 \le y \le 1+x.
$$

Es handelt sich um die Flaeche unter der Geraden

$$
y=1+x
$$

zwischen $x=0$ und $x=2$, oberhalb der $x$-Achse.

Die Eckpunkte des Bereichs sind

$$
(0,0), \quad (0,1), \quad (2,3), \quad (2,0).
$$

### 3. Volumen des Rotationskoerpers um die $x$-Achse

Bei Rotation der Flaeche aus Teil 2 um die $x$-Achse entsteht ein Rotationskoerper. Mit der Scheibenmethode gilt

$$
V=\pi\int_0^2 (1+x)^2\,dx.
$$

Ausmultiplizieren liefert

$$
(1+x)^2 = 1+2x+x^2.
$$

Somit folgt

$$
V=\pi\int_0^2 (1+2x+x^2)\,dx
= \pi\left[x+x^2+\frac{x^3}{3}\right]_0^2.
$$

Einsetzen ergibt

$$
V=\pi\left(2+4+\frac{8}{3}\right)
=\pi\cdot \frac{26}{3}.
$$

Also ist das Volumen des Rotationskoerpers

$$
V=\frac{26\pi}{3}.
$$