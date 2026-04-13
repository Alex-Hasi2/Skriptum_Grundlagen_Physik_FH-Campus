# AWII Prüfung SS2026 - Teil 2: Lösung



## Beispiel 1

1. **Wahr**  
   Die Einheitsvektoren-Darstellung lautet

   $\vec a = a_x \vec e_x + a_y \vec e_y + a_z \vec e_z.$ 

2. **Wahr**  
   Der Vektor $\vec a = (3,0)$ hat den Betrag

   $|\vec a| = \sqrt{3^2 + 0^2} = 3.$ 

3. **Falsch**  
   Die absolute Änderung ist die Differenz von Funktionswerten, nicht die durchschnittliche Änderung. Die durchschnittliche Änderung ist der Differenzenquotient.

4. **Falsch**  
   Es fehlt der Faktor $n$. Korrekt ist
   $n! = n \cdot (n-1) \cdot (n-2) \cdots 2 \cdot 1.$ 

5. **Wahr**  
   Das Vorzeichen von $f'(x)$ beschreibt lokal das Monotonieverhalten.

6. **Falsch**  
   Nicht jede Funktion besitzt eine Taylorreihe, die die Funktion in einer Umgebung von $x_0$ exakt beschreibt.

7. **Falsch**  
   Eine Taylorreihe entwickelt eine Funktion in Potenzen von $(x-x_0)$, nicht in eine Sinus-/Kosinusreihe.

8. **Wahr**  
   Es gilt
   $\vec v(t) = \frac{d\vec s(t)}{dt},$
   und bei bekannter Beschleunigung kann man die Geschwindigkeit durch Integration bestimmen.

9. **Wahr**  
   Für ein Integral mit gleichen Grenzen gilt immer
   $\int_a^a f(x)\,dx = 0.$ 

10. **Wahr**  
    Das Integral ist uneigentlich, weil eine Integrationsgrenze unendlich ist.

## Beispiel 2

Gegeben sind die Grenzwerte für $x \to 0$ beziehungsweise $x \to \infty$.

### a) $\displaystyle \lim_{x\to 0} \frac{\cos(x)}{x^2+1}$

Die Regel von de L'Hospital ist nicht anwendbar, da kein unbestimmter Ausdruck entsteht. Es gilt direkt
$\lim_{x\to 0} \frac{\cos(x)}{x^2+1} = \frac{\cos(0)}{0^2+1} = 1.$ 

### b) $\displaystyle \lim_{x\to 0} \frac{e^x-1}{x}$

Hier liegt der Typ $0/0$ vor, also ist de L'Hospital anwendbar:
$\lim_{x\to 0} \frac{e^x-1}{x} = \lim_{x\to 0} \frac{e^x}{1} = 1.$ 

### c) $\displaystyle \lim_{x\to 0} \frac{1-\cos(x)}{x^2}$

Wieder liegt $0/0$ vor, daher:
$\lim_{x\to 0} \frac{1-\cos(x)}{x^2} = \lim_{x\to 0} \frac{\sin(x)}{2x}.$
Nochmals de L'Hospital da weiterhin $0/0$ vorliegt:
$\lim_{x\to 0} \frac{\sin(x)}{2x} = \lim_{x\to 0} \frac{\cos(x)}{2} = \frac{1}{2}.$ 

### d) $\displaystyle \lim_{x\to 0} \frac{\ln(1+x)}{x}$

Es liegt $0/0$ vor, daher ist de L'Hospital anwendbar:
$\lim_{x\to 0} \frac{\ln(1+x)}{x} = \lim_{x\to 0} \frac{1/(1+x)}{1} = 1.$ 

### e) $\displaystyle \lim_{x\to \infty} \frac{x^2+1}{x+1}$

Hier liegt zunächst der Typ $\infty/\infty$ vor, daher ist de L'Hospital anwendbar:
$\lim_{x\to \infty} \frac{x^2+1}{x+1} = \lim_{x\to \infty} \frac{2x}{1}.$
Nach dem Ableiten ist der Ausdruck kein $0/0$- oder $\infty/\infty$-Term mehr, da der Nenner konstant ist. L'Hospital ist daher nicht weiter anwendbar. Der Grenzwert ist trotzdem eindeutig:
$\lim_{x\to \infty} 2x = \infty.$

## Beispiel 3

Gegeben ist
$\vec s(t) = \begin{pmatrix}\sin t\\ \cos t\\ 0\end{pmatrix}.$ 
Dabei wird die Zeit $t$ in Sekunden und der Ort $\vec s$ in Metern gemessen.

### 1. Entfernung vom Ursprung

Die Entfernung ist der Betrag des Ortsvektors:

$|\vec s(t)| = \sqrt{\sin^2 t + \cos^2 t + 0^2} = 1\,\mathrm{m}$ 

### 2. Geschwindigkeits- und Beschleunigungsvektor

Ableiten nach der Zeit liefert

$\vec v(t) = \frac{d\vec s(t)}{dt} = \begin{pmatrix}\cos t\\ -\sin t\\ 0\end{pmatrix}\,\mathrm{m/s},$

$\vec a(t) = \frac{d\vec v(t)}{dt} = \begin{pmatrix}-\sin t\\ -\cos t\\ 0\end{pmatrix}\,\mathrm{m/s^2}.$ 

### 3. Betrag von Geschwindigkeit und Beschleunigung bei $t=1\,\mathrm{s}$

Es gilt

$|\vec v(1)| = \sqrt{\cos^2(1) + \sin^2(1)} = 1\,\mathrm{m/s},$

$|\vec a(1)| = \sqrt{\sin^2(1) + \cos^2(1)} = 1\,\mathrm{m/s^2}.$ 

Numerisch ist also jeweils

$|\vec v(1)| = 1.00\,\mathrm{m/s}, \qquad |\vec a(1)| = 1.00\,\mathrm{m/s^2}.$ 

### 4. Bahnkurve

Aus
$x = \sin t, \qquad y = \cos t, \qquad z = 0$

folgt

$x^2 + y^2 = 1, \qquad z = 0.$ 

Die Bahnkurve ist also ein Einheitskreis in der $xy$-Ebene.

### 5. Geschwindigkeits- und Beschleunigungsvektor bei $t = \pi/2\,\mathrm{s}$

Für $t = \pi/2\,\mathrm{s}$ gilt

$\vec s\left(\frac{\pi}{2}\right) = \begin{pmatrix}1\\0\\0\end{pmatrix}, \;\;$
$\vec v\left(\frac{\pi}{2}\right) = \begin{pmatrix}0\\-1\\0\end{pmatrix}, \;\;$
$\vec a\left(\frac{\pi}{2}\right) = \begin{pmatrix}-1\\0\\0\end{pmatrix}.$ 

Der Ortsvektor zeigt also entlang der $x$-Achse, der Geschwindigkeitsvektor zeigt entlang der $y$-Achse nach unten, der Beschleunigungsvektor zeigt entlang der $x$-Achse nach links, jeweils tangential bzw. radial zum Kreis. Außerdem gilt $\vec{e}_r \cdot \vec{e}_v = 0,$ da die Richtungen von Orts- und Geschwindigkeitsvektor senkrecht zueinander stehen. Und $\vec{e}_r = -\vec{e}_a,$ da die Beschleunigung zum Zentrum des Kreises zeigt, also entgegengesetzt zum Ortsvektor.

## Beispiel 4

Gesucht ist die Taylorreihe von
$f(x) = \sqrt[3]{1+x} = (1+x)^{1/3}$
um $x_0 = 0$.

Zuerst werden die Ableitungen berechnet:

$f(x) = (1+x)^{1/3}$

$f'(x) = \frac{1}{3}(1+x)^{-2/3}$

$f''(x) = -\frac{2}{9}(1+x)^{-5/3}$

$f'''(x) = \frac{10}{27}(1+x)^{-8/3}$

$f''''(x) = -\frac{80}{81}(1+x)^{-11/3}$

Nun setzt man $x_0 = 0$ ein:

$f(0) = 1$

$f'(0) = \frac{1}{3}$

$f''(0) = -\frac{2}{9}$

$f'''(0) = \frac{10}{27}$

$f''''(0) = -\frac{80}{81}$

Damit ergibt sich die Taylorreihe um $x_0 = 0$:

$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \frac{f''''(0)}{4!}x^4 + \cdots$

$f(x) = 1 + \frac{1}{3}x - \frac{2}{9 \cdot 2}x^2 + \frac{10}{27 \cdot 6}x^3 - \frac{80}{81 \cdot 24}x^4 + \cdots$

$f(x) = 1 + \frac{x}{3} - \frac{x^2}{9} + \frac{5x^3}{81} - \frac{10x^4}{243} + \cdots$

## Beispiel 5

Die Kostenfunktion lautet
$C(T,h) = 50h + 3(20-T)h + 0.5h^2 = 110h - 3Th + 0.5h^2.$ 

### 1. Partielle Ableitung nach $T$

$\frac{\partial C}{\partial T} = -3h.$ 

Bedeutung: Wenn die Außentemperatur steigt, sinken die Heizkosten bei konstantem $h$ um $3h$ pro Temperatureinheit.

### 2. Partielle Ableitung nach $h$

$\frac{\partial C}{\partial h} = 50 + 3(20-T) + h = 110 - 3T + h.$ 

Bedeutung: Das ist die momentane Änderung der Kosten bei einer kleinen Änderung der Heizstunden, während $T$ konstant bleibt.

### 3. Totale Ableitung

Die totale Ableitung beschreibt, wie sich die Heizkosten ändern, wenn sich Temperatur und Heizstunden gleichzeitig mit der Zeit verändern:
$\frac{dC}{dt} = \frac{\partial C}{\partial T}\frac{dT}{dt} + \frac{\partial C}{\partial h}\frac{dh}{dt}.$ 

Sie kombiniert also beide Einflussgrößen zu einer zeitlichen Änderungsrate der Kosten.

## Beispiel 6

Gegeben ist
$T(t) = 20 + 80e^{-t/15}.$ 

### 1. Temperatur zu Beginn

$T(0) = 20 + 80e^0 = 100^\circ\mathrm C.$ 

### 2. Temperatur für $t \to \infty$

Da $e^{-t/15} \to 0$ für $t \to \infty$:
$\lim_{t\to\infty} T(t) = 20^\circ\mathrm C.$ 

### 3. Zeitpunkt für etwa $0{,}01^\circ\mathrm C$ über Umgebungstemperatur

Gesucht ist
$20 + 80e^{-t/15} = 20.01.$ 

Daraus folgt
$80e^{-t/15} = 0.01,$
$e^{-t/15} = \frac{0.01}{80} = \frac{1}{8000},$
$-\frac{t}{15} = \ln\left(\frac{1}{8000}\right),$
$t = 15\ln(8000) \approx 134.75\,\text{min}.$ 

### 4. Graph der Funktion

Der Graph ist eine fallende Exponentialfunktion mit horizontaler Asymptote bei
$T = 20^\circ\mathrm C.$ 

Markante Punkte:
- $T(0) = 100^\circ\mathrm C$
- Grenzwert für $t \to \infty$: $20^\circ\mathrm C$
- bei $t \approx 134.75\,\mathrm{min}$: $T \approx 20.01^\circ\mathrm C$

### 5. Zeitliche Änderungsrate


Die Ableitung lautet
$\frac{dT}{dt} = 80 \cdot \left(-\frac{1}{15}\right)e^{-t/15} = -\frac{80}{15}e^{-t/15}.$ 

Für $t = 15$ Minuten gilt
$\frac{dT}{dt}\bigg|_{t=15} = -\frac{80}{15}e^{-1} \approx -1.96$ $^\circ\mathrm{C/min}$.

Die Temperatur nimmt nach $15$ Minuten also mit etwa $1.96$ $^\circ\mathrm{C/min}$ ab.

## Beispiel 7

Das Volumen der Kugel ergibt sich aus dem gegebenen Integral
$V = \int_0^{2\pi} \int_0^{\pi} \int_0^R r^2\sin(\theta)\,dr\,d\theta\,d\varphi.$ 

Zuerst nach $r$ integrieren:
$\int_0^R r^2\,dr = \frac{R^3}{3}.$ 

Dann nach $\theta$:
$\int_0^{\pi} \sin(\theta)\,d\theta = 2.$ 

Und zuletzt nach $\varphi$:
$\int_0^{2\pi} d\varphi = 2\pi.$ 

Damit folgt
$V = \frac{R^3}{3} \cdot 2 \cdot 2\pi = \frac{4}{3}\pi R^3.$ 