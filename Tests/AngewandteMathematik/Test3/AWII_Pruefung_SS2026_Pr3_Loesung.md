# AWII Pruefung SS2026 - Pruefungstermin 3: Loesung

## Hinweise zur Angabe

- Beispiel 7, Teil 3, interpretiere ich als Rotation des in Teil 2 skizzierten Bereichs um die $x$-Achse, nicht als Rotation der Flaeche $z=x^2y$.

## Beispiel 1

1. **Falsch**  
   $\vec a = (a_x,a_y,a_z)$ ist die Komponenten- oder Koordinatendarstellung, nicht die Einheitsvektordarstellung. Die Einheitsvektordarstellung waere zum Beispiel $\vec a = a_x \vec e_x + a_y \vec e_y + a_z \vec e_z$.

2. **Falsch**  
   Fuer $A(4,-3,5)$ und $B(-1,3,-6)$ gilt
   $\overrightarrow{AB} = B-A = (-5,6,-11)$.
   
3. **Falsch**  
   Stehen zwei Vektoren senkrecht aufeinander, dann gilt fuer das Skalarprodukt
   $\vec a \cdot \vec b = 0$.

4. **Wahr**  
   Es gilt
   $n! = n\cdot(n-1)\cdot(n-2)\cdots 2\cdot 1$.

5. **Falsch**  
   Die zweite Ableitung beschreibt die Kruemmung, nicht das Monotonieverhalten. Das Monotonieverhalten haengt vom Vorzeichen der ersten Ableitung ab.

6. **Falsch**  
   Eine Taylorreihe kann auch um andere Entwicklungspunkte $x_0$ entwickelt werden, nicht nur um $x_0=0$.

7. **Wahr**  
   Genau das ist die Idee der Fourierreihe.

8. **Wahr**  
   Es gilt
   $\vec v(t)=\frac{d\vec r}{dt}$,
   und umgekehrt ergibt sich der Ortsvektor durch Integration der Geschwindigkeit ueber die Zeit.

9. **Wahr**  
   Im Grundgedanken ist die Aussage richtig: einfache Integrale beschreiben Flaecheninhalte, doppelte Integrale Volumina unter Flaechen, und dreifache Integrale Volumina im Raum.

10. **Falsch**  
   $\int_{-\infty}^{\infty} e^x\,dx$ ist kein einseitiges, sondern ein zweiseitiges uneigentliches Integral. Zudem divergiert es.

## Beispiel 2

Gegeben sind
$f(x)=x^2-2x+3$
und
$g(x)=x+3$.

### 1. Schnittpunkte $S_1$ und $S_2$

Die Schnittpunkte erhaelt man aus
$f(x)=g(x)$:

$x^2-2x+3=x+3$

$x^2-3x=0$

$x(x-3)=0$

Also sind die Loesungen $x=0$ und $x=3$.

Die zugehoerigen $y$-Werte sind:

bei $x=0$: $y=3$

bei $x=3$: $y=6$

Damit:

$S_1=(0,3)$

$S_2=(3,6)$

### 2. Eingeschlossene Flaeche zwischen $f$ und $g$

Zwischen den Schnittpunkten gilt
$g(x)-f(x) = (x+3)-(x^2-2x+3) = -x^2+3x$.

Die eingeschlossene Flaeche ist daher

$A = \int_0^3 (g(x)-f(x))\,dx = \int_0^3 (-x^2+3x)\,dx$.

$A = \left[-\frac{x^3}{3}+\frac{3}{2}x^2\right]_0^3 = -9+\frac{27}{2} = \frac{9}{2}$.

Also ist

$A = \frac{9}{2} = 4.5$.

### 3. Integral $\int_{x_{S1}}^{x_{S2}} f(x)\,dx$

Ich interpretiere die Aufgabe als

$\int_0^3 f(x)\,dx = \int_0^3 (x^2-2x+3)\,dx$.

Das ergibt

$\left[\frac{x^3}{3}-x^2+3x\right]_0^3 = 9-9+9 = 9$.

Also:

$\int_{x_{S1}}^{x_{S2}} f(x)\,dx = 9$.

### 4. Integral $\int_{y_{S1}}^{y_{S2}} g^{-1}(y)\,dy$

Da $g(x)=x+3$ gilt fuer die Umkehrfunktion

$g^{-1}(y)=y-3$.

Mit $y_{S1}=3$ und $y_{S2}=6$ folgt

$\int_3^6 g^{-1}(y)\,dy = \int_3^6 (y-3)\,dy$.

$\int_3^6 (y-3)\,dy = \left[\frac{(y-3)^2}{2}\right]_3^6 = \frac{9}{2}$.

Also:

$\int_{y_{S1}}^{y_{S2}} g^{-1}(y)\,dy = \frac{9}{2} = 4.5$.

## Beispiel 3

Gegeben ist
$\vec r(t)=\begin{pmatrix}t^2\\0\\2t\end{pmatrix}$,
mit $t$ in Sekunden und $\vec r$ in Metern.

### 1. Bahnkurve

Es gilt
$x=t^2$, $y=0$, $z=2t$.

Aus $z=2t$ folgt
$t=\frac{z}{2}$.

Einsetzen in $x=t^2$ ergibt

$x=\left(\frac{z}{2}\right)^2 = \frac{z^2}{4}$,

also

$z=2\sqrt{x}$ fuer $x\ge 0$.

Die Bahnkurve ist also eine Parabel in der $xz$-Ebene mit $y=0$.

### 2. Geschwindigkeits- und Beschleunigungsvektor

$\vec v(t)=\frac{d\vec r}{dt}=\begin{pmatrix}2t\\0\\2\end{pmatrix}\,\mathrm{m/s}$

$\vec a(t)=\frac{d\vec v}{dt}=\begin{pmatrix}2\\0\\0\end{pmatrix}\,\mathrm{m/s^2}$

### 3. Betraege bei $t=10\,\mathrm{s}$

$\vec v(10)=\begin{pmatrix}20\\0\\2\end{pmatrix}\,\mathrm{m/s}$

$|\vec v(10)| = \sqrt{20^2+0^2+2^2} = \sqrt{404} \approx 20.10\,\mathrm{m/s}$

$\vec a(10)=\begin{pmatrix}2\\0\\0\end{pmatrix}\,\mathrm{m/s^2}$

$|\vec a(10)| = 2.00\,\mathrm{m/s^2}$

### 4. Vektoren bei $t=1\,\mathrm{s}$

$\vec r(1)=\begin{pmatrix}1\\0\\2\end{pmatrix}\,\mathrm{m}$

$\vec v(1)=\begin{pmatrix}2\\0\\2\end{pmatrix}\,\mathrm{m/s}$

$\vec a(1)=\begin{pmatrix}2\\0\\0\end{pmatrix}\,\mathrm{m/s^2}$

Diese beiden Vektoren sind an der Stelle $\vec r(1)$ einzuzeichnen.

## Beispiel 4

Gesucht ist ein geschlossener Drehzylinder mit minimaler Oberflaeche bei vorgegebenem Volumen

$V=250\,\mathrm{cm^3}$.

### 1. Volumengleichung

Fuer einen Zylinder gilt

$V=\pi r^2 h$.

Hier also

$\pi r^2 h = 250$.

### 2. Oberflaeche

Die Oberflaeche eines geschlossenen Zylinders ist

$O = 2\cdot \pi r^2 + 2\pi r h$.

Dabei ist

- $2\pi r^2$ die Flaeche von Deckel und Boden,
- $2\pi r h$ die Mantelflaeche.

### 3. $h$ als Funktion von $r$

Aus der Volumengleichung folgt

$h = \frac{250}{\pi r^2}$,

mit $r>0$.

### 4. Oberflaeche als Funktion von $r$

Einsetzen ergibt

$O(r)=2\pi r^2 + 2\pi r\cdot \frac{250}{\pi r^2}$

$O(r)=2\pi r^2 + \frac{500}{r}$.

### 5. Optimale Abmessungen

Ableiten:

$O'(r)=4\pi r - \frac{500}{r^2}$

Kritischer Punkt aus $O'(r)=0$:

$4\pi r - \frac{500}{r^2}=0$

$4\pi r^3 = 500$

$r^3 = \frac{125}{\pi}$

$r = \sqrt[3]{\frac{125}{\pi}} = \frac{5}{\sqrt[3]{\pi}} \approx 3.41\,\mathrm{cm}$

Dann ist

$h = \frac{250}{\pi r^2} \approx 6.83\,\mathrm{cm}$.

Man kann auch direkt sehen:

$h = 2r \approx 6.83\,\mathrm{cm}$.

Minimalitaetsnachweis:

$O''(r)=4\pi + \frac{1000}{r^3}$

und wegen $r>0$ gilt stets $O''(r)>0$.

Also liegt tatsaechlich ein Minimum vor.

Die optimalen Abmessungen sind damit:

$r \approx 3.41\,\mathrm{cm}$

$h \approx 6.83\,\mathrm{cm}$

Die optimale Oberfläche ist $O = 2\pi r^2 + \frac{500}{r} \approx 146.8\,\mathrm{cm^2}$.

## Beispiel 5

Gegeben ist
$f(x)=x^3$
und der Entwicklungspunkt
$x_0=1$.

### 1. Taylorreihe bis $n=3$

Die Ableitungen sind:

$f(x)=x^3$

$f'(x)=3x^2$

$f''(x)=6x$

$f'''(x)=6$

Am Entwicklungspunkt $x_0=1$ gilt:

$f(1)=1$

$f'(1)=3$

$f''(1)=6$

$f'''(1)=6$

Damit lautet die Taylorreihe bis Ordnung 3:

$T_3(x)=f(1)+f'(1)(x-1)+\frac{f''(1)}{2!}(x-1)^2+\frac{f'''(1)}{3!}(x-1)^3$

$T_3(x)=1+3(x-1)+3(x-1)^2+(x-1)^3$

Also:

$T_3(x)=1+3(x-1)+3(x-1)^2+(x-1)^3 = 1 + 3x - 3 + 3(x^2 -2x + 1) + (x^3 - 3x^2 + 3x - 1) = (1-3+3-1) + (3-6+3)x + (3-3)x^2 + x^3 = x^3$.

Das ist bereits exakt gleich $x^3$.

### 2. Fehlerabschaetzung mit dem Lagrange-Fehlerterm

Hier ist die Aufgabe didaktisch unguenstig, denn fuer ein Polynom dritten Grades ist die Taylorentwicklung bereits ab Ordnung 3 exakt.

Fuer $n=3$ ist

$R_3(x)=\frac{f^{(4)}(\zeta)}{4!}(x-1)^4$.

Da aber

$f^{(4)}(x)=0$

fuer alle $x$ gilt, folgt direkt

$R_3(x)=0$.

Also ist die Approximation fuer jeden Punkt exakt, nicht nur in der Naehe von $x_0=1$.

## Beispiel 6

Gegeben ist die Funktion

$f(x,y,z)=(2x-y)^2 + 6\ln(x) + 2xy^2 e^{xz^3}$.

### a) Erste partielle Ableitung nach $x$

$\frac{\partial f}{\partial x} = 2(2x-y)\cdot 2 + \frac{6}{x} + 2y^2 e^{xz^3} + 2xy^2 z^3 e^{xz^3}$

$\frac{\partial f}{\partial x} = 8x-4y+\frac{6}{x} + 2y^2 e^{xz^3} + 2xy^2 z^3 e^{xz^3}$

$\frac{\partial f}{\partial x} = 8x-4y+\frac{6}{x} + 2y^2 e^{xz^3}(1+xz^3)$

### b) Gemischte zweite Ableitung $\frac{\partial^2 f}{\partial y\partial x}$

Aus Teil a):

$\frac{\partial^2 f}{\partial y\partial x} = \frac{\partial}{\partial y}\left(8x-4y+\frac{6}{x} + 2y^2 e^{xz^3}(1+xz^3)\right)$

$\frac{\partial^2 f}{\partial y\partial x} = -4 + 4y e^{xz^3}(1+xz^3)$

### c) Gemischte dritte Ableitung $\frac{\partial^3 f}{\partial z\partial y\partial x}$

$\frac{\partial^3 f}{\partial z\partial y\partial x} = \frac{\partial}{\partial z}\left(-4 + 4y e^{xz^3}(1+xz^3)\right)$

$\frac{\partial^3 f}{\partial z\partial y\partial x} = 4y\cdot \frac{\partial}{\partial z}\left(e^{xz^3}(1+xz^3)\right)$

$\frac{\partial^3 f}{\partial z\partial y\partial x} = 4y\left(3xz^2 e^{xz^3}(1+xz^3) + 3xz^2 e^{xz^3}\right)$

$\frac{\partial^3 f}{\partial z\partial y\partial x} = 12xyz^2 e^{xz^3}(2+xz^3)$

### d) Bedeutung der partiellen Ableitungen

- $\frac{\partial f}{\partial x}$ beschreibt, wie sich $f$ aendert, wenn nur $x$ variiert und $y,z$ konstant gehalten werden.
- $\frac{\partial^2 f}{\partial y\partial x}$ beschreibt, wie sich die Aenderungsrate in $x$ veraendert, wenn zusaetzlich $y$ geaendert wird.
- $\frac{\partial^3 f}{\partial z\partial y\partial x}$ beschreibt die gemeinsame, sukzessive Aenderung dieser Aenderungsraten bei Variation von $x$, dann $y$, dann $z$.

## Beispiel 7

### 1. Doppelintegral

Gesucht ist

$\int_0^1 \int_0^{3-2x} x^2 y\,dy\,dx$.

Zuerst integrieren wir nach $y$:

$\int_0^{3-2x} x^2 y\,dy = x^2 \left[\frac{y^2}{2}\right]_0^{3-2x} = \frac{x^2}{2}(3-2x)^2$.

Damit wird das Integral zu

$\frac{1}{2}\int_0^1 x^2(3-2x)^2\,dx$.

Ausmultiplizieren:

$(3-2x)^2 = 9-12x+4x^2$,

also

$\frac{1}{2}\int_0^1 (9x^2-12x^3+4x^4)\,dx = \frac{1}{2}\left[3x^3-3x^4+\frac{4}{5}x^5\right]_0^1 = \frac{1}{2}\left(3-3+\frac{4}{5}\right) =\frac{1}{2}\cdot \frac{4}{5} = \frac{2}{5}$.

Also:

$\int_0^1 \int_0^{3-2x} x^2 y\,dy\,dx = \frac{2}{5}$.

### 2. Integrationsbereich

Der Bereich ist gegeben durch

$0\le x\le 1$, $0\le y\le 3-2x$.

Er ist ein Trapez mit Eckpunkten

$(0,0)$, $(0,3)$, $(1,1)$, $(1,0)$.

Die obere Begrenzung ist die Gerade

$y=3-2x$.

### 3. Volumen des Rotationskoerpers um die $x$-Achse

Hier interpretiere ich die Aufgabe als Rotation des in Teil 2 beschriebenen Bereichs um die $x$-Achse.

Mit der Scheibenmethode ergibt sich

$V = \pi \int_0^1 (3-2x)^2\,dx$.

Also

$V = \pi \int_0^1 (9-12x+4x^2)\,dx$

$V = \pi \left[9x-6x^2+\frac{4}{3}x^3\right]_0^1$

$V = \pi\left(9-6+\frac{4}{3}\right)=\pi\cdot \frac{13}{3}$.

Damit ist das Volumen

$V = \frac{13\pi}{3}$.