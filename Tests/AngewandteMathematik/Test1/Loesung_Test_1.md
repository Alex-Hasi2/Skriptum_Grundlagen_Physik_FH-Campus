## Beispiel 2.1 (6 Punkte)

Die Fahrt einer U-Bahn zwischen zwei Stationen dauert 70 Sekunden und wird durch die folgende Weg-Zeit-Funktion $s(t)$ modelliert:

$$s(t) = -\frac{2}{245}t^3 + \frac{6}{7}t^2$$

$t \dots$ Zeit in Sekunden ($0 \leq t \leq 70$)  
$s(t) \dots$ zurückgelegter Weg im Zeitintervall $[0; t]$ in Metern.

1. Berechnen Sie die **absolute Änderung** von $s$ in $[0; 70]$. Was bedeutet dieses Ergebnis?
2. Berechnen Sie die **mittlere Änderungsrate** von $s$ in $[20; 50]$. Was bedeutet dieses Ergebnis?

---

## Lösung

### 1. Absolute Änderung in $[0; 70]$

Die absolute Änderung ist die Differenz der Funktionswerte am Ende und am Anfang des Intervalls: $\Delta s = s(70) - s(0)$.

* **Berechnung von $s(0)$:**
    $$s(0) = -\frac{2}{245}(0)^3 + \frac{6}{7}(0)^2 = 0 \,\text{m}$$
* **Berechnung von $s(70)$:**
    $$s(70) = -\frac{2}{245}(70)^3 + \frac{6}{7}(70)^2$$
    $$s(70) = -\frac{2}{245}(343000) + \frac{6}{7}(4900)$$
    $$s(70) = -2800 + 4200 = 1400 \,\text{m}$$
* **Absolute Änderung:**
    $$\Delta s = 1400 - 0 = 1400 \,\text{m}$$

**Bedeutung:** Das Ergebnis gibt den **gesamten zurückgelegten Weg** der U-Bahn zwischen den beiden Stationen an (die Distanz zwischen den Stationen beträgt $1400 \,\text{m}$).

---

### 2. Mittlere Änderungsrate in $[20; 50]$

Die mittlere Änderungsrate entspricht dem Differenzenquotienten: $\frac{s(t_2) - s(t_1)}{t_2 - t_1}$.

* **Berechnung von $s(20)$:**
    $$s(20) = -\frac{2}{245}(20)^3 + \frac{6}{7}(20)^2 = -\frac{16000}{245} + \frac{2400}{7} \approx 277,55 \,\text{m}$$
* **Berechnung von $s(50)$:**
    $$s(50) = -\frac{2}{245}(50)^3 + \frac{6}{7}(50)^2 = -\frac{250000}{245} + \frac{15000}{7} \approx 1122,45 \,\text{m}$$
* **Berechnung der Änderungsrate:**
    $$\frac{s(50) - s(20)}{50 - 20} = \frac{1122,45 - 277,55}{30} = \frac{844,9}{30} \approx 28,16 \text{ m/s}$$

**Bedeutung:** Die mittlere Änderungsrate des Weges nach der Zeit entspricht der **Durchschnittsgeschwindigkeit** der U-Bahn im Zeitintervall von $20$ bis $50$ Sekunden. Sie betrug ca. **$28,16 \,\text{m/s}$** (bzw. ca. $101,4 \,\text{km/h}$).



## Beispiel 2.2 (4 Punkte)

Bestimmen Sie den Grenzwert der folgenden Funktionen mithilfe der Regel von de l'Hospital:

a) $\lim_{x \to \infty} \frac{2x^2}{e^x} =$

b) $\lim_{x \to 0} \frac{e^x - 1}{x^2} =$

---

## Lösung

Die **Regel von de l'Hospital** besagt, dass bei Grenzwerten der Form $\frac{0}{0}$ oder $\frac{\infty}{\infty}$ gilt:
$$\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}$$

### a) $\lim_{x \to \infty} \frac{2x^2}{e^x}$

1. **Prüfung:** Für $x \to \infty$ gehen sowohl Zähler ($2x^2$) als auch Nenner ($e^x$) gegen $\infty$. Wir haben also den Fall $\frac{\infty}{\infty}$.
2. **Erste Anwendung von de l'Hospital:**
   Wir leiten Zähler und Nenner getrennt ab:
   * Zähler: $(2x^2)' = 4x$
   * Nenner: $(e^x)' = e^x$
   $$\lim_{x \to \infty} \frac{2x^2}{e^x} = \lim_{x \to \infty} \frac{4x}{e^x}$$
3. **Erneute Prüfung:** Der neue Grenzwert ist immer noch vom Typ $\frac{\infty}{\infty}$. Wir wenden die Regel ein zweites Mal an.
4. **Zweite Anwendung von de l'Hospital:**
   * Zähler: $(4x)' = 4$
   * Nenner: $(e^x)' = e^x$
   $$\lim_{x \to \infty} \frac{4}{e^x}$$
5. **Ergebnis:** Da der Zähler nun konstant 4 ist und der Nenner gegen $\infty$ strebt, geht der gesamte Bruch gegen 0.

**Lösung:** $\mathbf{0}$

---

### b) $\lim_{x \to 0} \frac{e^x - 1}{x^2}$

1. **Prüfung:** Setzt man $x=0$ ein, erhält man $\frac{e^0 - 1}{0^2} = \frac{1 - 1}{0} = \frac{0}{0}$. Die Regel ist anwendbar.
2. **Erste Anwendung von de l'Hospital:**
   * Zähler: $(e^x - 1)' = e^x$
   * Nenner: $(x^2)' = 2x$
   $$\lim_{x \to 0} \frac{e^x}{2x}$$
3. **Analyse des neuen Grenzwerts:**
   * Der Zähler $e^x$ nähert sich für $x \to 0$ dem Wert **1**.
   * Der Nenner $2x$ nähert sich für $x \to 0$ dem Wert **0**.
4. **Ergebnis:** Da der Zähler gegen eine Zahl ungleich Null strebt und der Nenner gegen Null geht, existiert kein endlicher Grenzwert (der Ausdruck strebt gegen Unendlich). Da der Nenner das Vorzeichen je nach Annäherung von links oder rechts wechselt ($-0$ vs $+0$), betrachtet man oft:
   * $\lim_{x \to 0^+} \frac{e^x}{2x} = +\infty$
   * $\lim_{x \to 0^-} \frac{e^x}{2x} = -\infty$

**Lösung:** Der Grenzwert ist **nicht definiert** (bzw. $\pm \infty$).




## Beispiel 3 (10 Punkte)

Ein Massenpunkt bewegt sich im Raum, wobei sein Ortsvektor durch die Funktion

$$\vec{r}(t) = \begin{pmatrix} (v_0 \cdot \sin(\alpha)) \cdot t^2 \\ 10\sqrt{t} \\ (v_0 \cdot \cos(\alpha)) \cdot t - \frac{1}{2}gt^2 \end{pmatrix}$$

gegeben ist, wobei $v_0$ die Anfangsgeschwindigkeit und $\alpha$ der Abwurfwinkel und $g$ die Erdbeschleunigung ist. Die Zeit $t$ wird in Sekunden gemessen.

1. Identifizieren Sie in der gegebenen Ortsvektorfunktion
    * die unabhängige Variable,
    * die abhängige(n) Variable(n)
    * und die Konstanten.
2. Bestimmen Sie den Geschwindigkeitsvektor $\vec{v}(t)$.
3. Berechnen Sie den Beschleunigungsvektor $\vec{a}(t)$.
4. Ermitteln Sie die Geschwindigkeit und Beschleunigung zum Zeitpunkt $t = 1 \text{ s}$ für $v_0 = 10 \text{ m/s}$, $\alpha = 30^\circ$ und $g = 9,81 \text{ m/s}^2$.

---

## Lösung

### 1. Variablen und Konstanten
* **Unabhängige Variable:** $t$ (die Zeit).
* **Abhängige Variable(n):** $\vec{r}$ (der Ortsvektor) bzw. die einzelnen Komponenten $x(t), y(t), z(t)$.
* **Konstanten:** $v_0$, $\alpha$ und $g$.

### 2. Geschwindigkeitsvektor $\vec{v}(t)$
Die Geschwindigkeit ist die erste Ableitung des Ortsvektors nach der Zeit: $\vec{v}(t) = \dot{\vec{r}}(t)$.

$$\vec{v}(t) = \begin{pmatrix} 2 \cdot (v_0 \cdot \sin(\alpha)) \cdot t \\ \frac{10}{2\sqrt{t}} \\ (v_0 \cdot \cos(\alpha)) - gt \end{pmatrix} = \begin{pmatrix} 2v_0 \sin(\alpha) t \\ \frac{5}{\sqrt{t}} \\ v_0 \cos(\alpha) - gt \end{pmatrix}$$

### 3. Beschleunigungsvektor $\vec{a}(t)$
Die Beschleunigung ist die Ableitung des Geschwindigkeitsvektors: $\vec{a}(t) = \dot{\vec{v}}(t)$.
*(Hinweis: $\frac{5}{\sqrt{t}} = 5t^{-1/2} \rightarrow$ Ableitung: $-\frac{5}{2}t^{-3/2}$)*

$$\vec{a}(t) = \begin{pmatrix} 2v_0 \sin(\alpha) \\ -\frac{5}{2\sqrt{t^3}} \\ -g \end{pmatrix}$$

### 4. Berechnung für $t = 1 \text{ s}$
Werte: $v_0 = 10, \alpha = 30^\circ, g = 9,81$.  
(*Beachte:* $\sin(30^\circ) = 0,5$ und $\cos(30^\circ) = \frac{\sqrt{3}}{2} \approx 0,866$)

* **Geschwindigkeitsvektor bei $t=1$:**
    $$\vec{v}(1) = \begin{pmatrix} 2 \cdot 10 \cdot 0,5 \cdot 1 \\ \frac{5}{\sqrt{1}} \\ 10 \cdot 0,866 - 9,81 \cdot 1 \end{pmatrix} = \begin{pmatrix} 10 \\ 5 \\ -1,15 \end{pmatrix}$$
    **Betrag der Geschwindigkeit:** $|\vec{v}(1)| = \sqrt{10^2 + 5^2 + (-1,15)^2} \approx \mathbf{11,24 \text{ m/s}}$

* **Beschleunigungsvektor bei $t=1$:**
    $$\vec{a}(1) = \begin{pmatrix} 2 \cdot 10 \cdot 0,5 \\ -\frac{5}{2\sqrt{1^3}} \\ -9,81 \end{pmatrix} = \begin{pmatrix} 10 \\ -2,5 \\ -9,81 \end{pmatrix}$$
    **Betrag der Beschleunigung:** $|\vec{a}(1)| = \sqrt{10^2 + (-2,5)^2 + (-9,81)^2} \approx \mathbf{14,23 \text{ m/s}^2}$



## Beispiel 4 (10 Punkte)

Bestimmen Sie für die Funktion $f(x) = x \cdot \cos(x)$ an der Stelle $x_0 = 0$ die ersten vier Terme der Taylorreihe.

Vereinfachen Sie die Terme und geben Sie die vollständige Taylorreihe (in Bruchdarstellung) bis zur geforderten Potenz an.



## Lösung

Die Taylorreihe einer Funktion $f(x)$ an der Entwicklungsstelle $x_0 = 0$ (auch Maclaurin-Reihe genannt) ist definiert als:

$$T(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots$$

Da bei Sinus- und Kosinus-Funktionen oft jeder zweite Term null wird, berechnen wir die ersten vier **von Null verschiedenen** Terme.

Für die Lösung gibt es zwei gängige Wege. Weg 1 ist der klassische über die Ableitungen, Weg 2 ist ein eleganter Trick über bekannte Standardreihen. Da es 10 Punkte gibt, wird oft der ausführliche Weg 1 erwartet.

### Weg 1: Klassisch über Ableitungen

Wir leiten die Funktion $f(x) = x \cdot \cos(x)$ mehrfach mit der Produktregel ab und setzen $x = 0$ ein:

* **$n=0$:** $f(x) = x \cdot \cos(x)$ 
> $\Rightarrow f(0) = 0 \cdot 1 = 0$
* **$n=1$:** $f'(x) = 1 \cdot \cos(x) + x \cdot (-\sin(x)) = \cos(x) - x\sin(x)$
> $\Rightarrow f'(0) = 1 - 0 = 1$
* **$n=2$:** $f''(x) = -\sin(x) - (1 \cdot \sin(x) + x \cdot \cos(x)) = -2\sin(x) - x\cos(x)$
> $\Rightarrow f''(0) = -0 - 0 = 0$
* **$n=3$:** $f'''(x) = -2\cos(x) - (\cos(x) - x\sin(x)) = -3\cos(x) + x\sin(x)$
> $\Rightarrow f'''(0) = -3 + 0 = -3$
* **$n=4$:** $f^{(4)}(x) = 3\sin(x) + (\sin(x) + x\cos(x)) = 4\sin(x) + x\cos(x)$
> $\Rightarrow f^{(4)}(0) = 0 + 0 = 0$
* **$n=5$:** $f^{(5)}(x) = 4\cos(x) + (\cos(x) - x\sin(x)) = 5\cos(x) - x\sin(x)$
> $\Rightarrow f^{(5)}(0) = 5 - 0 = 5$
* **$n=6$:** $f^{(6)}(x) = -5\sin(x) - (\sin(x) + x\cos(x)) = -6\sin(x) - x\cos(x)$
> $\Rightarrow f^{(6)}(0) = 0 - 0 = 0$
* **$n=7$:** $f^{(7)}(x) = -6\cos(x) - (\cos(x) - x\sin(x)) = -7\cos(x) + x\sin(x)$
> $\Rightarrow f^{(7)}(0) = -7 + 0 = -7$


Nun setzen wir diese Werte in die Formel der Taylorreihe ein, um die ersten vier nicht-verschwindenden Terme zu erhalten:

$$T(x) = \frac{1}{1!}x^1 - \frac{3}{3!}x^3 + \frac{5}{5!}x^5 - \frac{7}{7!}x^7$$

Jetzt vereinfachen wir die Fakultäten ($3! = 6$, $5! = 120$, $7! = 5040$) und kürzen die Brüche:

$$T(x) = x - \frac{3}{6}x^3 + \frac{5}{120}x^5 - \frac{7}{5040}x^7$$

**Vollständige Taylorreihe (Bruchdarstellung) bis zur geforderten Potenz ($x^7$):**
$$T(x) = x - \frac{1}{2}x^3 + \frac{1}{24}x^5 - \frac{1}{720}x^7$$

*(Anmerkung: Falls mit "erste vier Terme" strikt $n=0$ bis $n=3$ gemeint war, ist das Ergebnis einfach $T(x) = x - \frac{1}{2}x^3$. Meistens sind bei solchen Angaben aber die ersten vier echten Glieder gemeint).*

---

### Weg 2: Der schnelle Weg (über die Standardreihe)

Wenn du die Taylorreihe für $\cos(x)$ auswendig weißt, kannst du dir sehr viel Arbeit sparen:
$$\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} \pm \dots$$

Da $f(x) = x \cdot \cos(x)$ ist, musst du diese gesamte Reihe einfach nur mit $x$ multiplizieren:
$$f(x) = x \cdot \left( 1 - \frac{x^2}{2} + \frac{x^4}{24} - \frac{x^6}{720} \pm \dots \right)$$

Ausmultipliziert ergibt das sofort unsere vier Terme:
**$$T(x) = x - \frac{1}{2}x^3 + \frac{1}{24}x^5 - \frac{1}{720}x^7$$**



## Beispiel 5 (10 Punkte)

Ein Krankenhaus modelliert den Energieverbrauch seiner Klimaanlage mit der folgenden (fiktiven) Funktion

$$E(H, B) = 0.5 H^2 + 2B^2 + 10H \cdot B$$

wobei $H$ die Heizleistung (kW) und $B$ die Belüftungsrate ($\text{m}^3/\text{h}$) ist.

*Die Funktion modelliert den Energieverbrauch einer Klimaanlage in willkürlichen Einheiten. Die Einheiten dienen nur der Veranschaulichung. Die Formel ist ein vereinfachtes Modell.*

1. Berechnen Sie die partiellen Ableitungen $\frac{\partial E}{\partial H}$ und $\frac{\partial E}{\partial B}$.
2. Interpretieren Sie die physikalische Bedeutung dieser partiellen Ableitungen.
3. Das Krankenhaus möchte bei Werten von $H = 4\text{ kW}$ und $B = 2\text{ m}^3/\text{h}$ Energie sparen. Welche Maßnahme reduziert den Verbrauch effektiver: Eine Reduzierung der Heizleistung um $1\text{ kW}$ oder eine Reduzierung der Belüftungsrate um $1\text{ m}^3/\text{h}$? Begründen Sie mithilfe der berechneten Ableitungen.

---

## Lösung

### 1. Partielle Ableitungen berechnen

Bei der partiellen Ableitung nach einer Variablen wird die andere Variable wie eine Konstante (eine feste Zahl) behandelt.

* **Partielle Ableitung nach $H$:** (Hier wird $B$ als Konstante betrachtet)
  $$\frac{\partial E}{\partial H} = 2 \cdot 0.5 H^{2-1} + 0 + 10 \cdot 1 \cdot B$$
  $$\frac{\partial E}{\partial H} = H + 10B$$

* **Partielle Ableitung nach $B$:** (Hier wird $H$ als Konstante betrachtet)
  $$\frac{\partial E}{\partial B} = 0 + 2 \cdot 2 B^{2-1} + 10 \cdot H \cdot 1$$
  $$\frac{\partial E}{\partial B} = 4B + 10H$$

---

### 2. Physikalische Bedeutung interpretieren

* **$\frac{\partial E}{\partial H}$:** Beschreibt die **Änderungsrate des Energieverbrauchs**, wenn die **Heizleistung** ($H$) geringfügig erhöht wird, während die Belüftungsrate ($B$) konstant bleibt. Es ist der zusätzliche Energieaufwand pro zusätzlich eingesetztem kW Heizleistung (Grenzkosten der Heizung).
* **$\frac{\partial E}{\partial B}$:** Beschreibt die **Änderungsrate des Energieverbrauchs**, wenn die **Belüftungsrate** ($B$) geringfügig erhöht wird, während die Heizleistung ($H$) konstant bleibt. Es ist der zusätzliche Energieaufwand pro zusätzlich eingesetztem Kubikmeter Belüftung pro Stunde (Grenzkosten der Belüftung).

Zusammenfassend geben sie an, wie sensibel der Gesamtenergieverbrauch auf die Veränderung jeweils *eines* einzelnen Parameters reagiert.

---

### 3. Effektivste Maßnahme zur Energieeinsparung

Um zu beurteilen, welche Reduzierung effektiver ist, setzen wir die aktuellen Werte ($H = 4$, $B = 2$) in unsere partiellen Ableitungen ein. Das liefert uns die ungefähre Änderung des Energieverbrauchs bei einer Änderung der jeweiligen Variable um 1 Einheit.

* **Auswirkung einer Änderung der Heizleistung ($H$):**
  $$\frac{\partial E}{\partial H}(4, 2) = 4 + 10 \cdot 2 = 4 + 20 = 24$$
  Eine Reduzierung der Heizleistung um **1 kW** senkt den Energieverbrauch näherungsweise um **24 Einheiten**.

* **Auswirkung einer Änderung der Belüftungsrate ($B$):**
  $$\frac{\partial E}{\partial B}(4, 2) = 4 \cdot 2 + 10 \cdot 4 = 8 + 40 = 48$$
  Eine Reduzierung der Belüftungsrate um **1 m³/h** senkt den Energieverbrauch näherungsweise um **48 Einheiten**.

**Fazit / Begründung:**
Da der Wert der partiellen Ableitung nach $B$ (48) doppelt so groß ist wie der nach $H$ (24), reagiert das System am aktuellen Betriebspunkt $(4, 2)$ wesentlich empfindlicher auf Änderungen der Belüftung. **Die Reduzierung der Belüftungsrate um 1 m³/h ist somit die deutlich effektivere Maßnahme**, um Energie zu sparen.


## Beispiel 6 (10 Punkte)

Betrachtet wird die Funktion $f(x) = (x - 2)^2 \cdot (x + 1)$

1. In welchen Punkten schneidet die Funktion $f(x)$ die $x$-Achse?
2. Untersuchen Sie die Funktion $f(x)$ auf Extremwerte.
3. Untersuchen Sie die Funktion $f(x)$ auf ihr Krümmungsverhalten und berechnen Sie alle Wendepunkte.
4. Berechnen Sie den Inhalt der vom Grafen der Funktion $f(x)$ und der $x$-Achse begrenzten endlichen Fläche.
5. Die Funktion wird nun im Bereich zwischen den beiden Nullstellen um die $x$-Achse gedreht und es entsteht dabei ein Rotationskörper. Bestimmen Sie das Volumen des Rotationskörpers.

---

## Lösung

**Vorbereitung:**
Für die Ableitungen und Integrale in den folgenden Aufgaben ist es hilfreich, die Funktion $f(x)$ zunächst auszumultiplizieren:
$$f(x) = (x^2 - 4x + 4)(x + 1) = x^3 + x^2 - 4x^2 - 4x + 4x + 4$$
$$f(x) = x^3 - 3x^2 + 4$$

---

### 1. Schnittpunkte mit der $x$-Achse (Nullstellen)

Um die Nullstellen zu finden, setzen wir $f(x) = 0$. Dafür verwenden wir am besten die ursprüngliche, faktorisierte Form der Gleichung:
$$(x - 2)^2 \cdot (x + 1) = 0$$

Ein Produkt ist null, wenn mindestens einer der Faktoren null ist:
* $(x - 2)^2 = 0 \Rightarrow x_1 = 2$ (doppelte Nullstelle, der Graph berührt hier die $x$-Achse)
* $x + 1 = 0 \Rightarrow x_2 = -1$ (einfache Nullstelle, der Graph schneidet die $x$-Achse)

Die Schnittpunkte mit der $x$-Achse sind: **$N_1(2 | 0)$** und **$N_2(-1 | 0)$**.

---

### 2. Extremwerte

Hierfür benötigen wir die erste und zweite Ableitung der Polynomfunktion:
* $f'(x) = 3x^2 - 6x$
* $f''(x) = 6x - 6$

**Notwendige Bedingung ($f'(x) = 0$):**
$$3x^2 - 6x = 0$$
$$3x(x - 2) = 0$$
Daraus ergeben sich die möglichen Extremstellen: $x_1 = 0$ und $x_2 = 2$.

**Hinreichende Bedingung (Prüfung mit $f''(x)$):**
* Für $x = 0$: $f''(0) = -6 < 0 \Rightarrow$ **Hochpunkt (Maximum)**

    $y$-Koordinate: $f(0) = 0^3 - 3(0)^2 + 4 = 4$

    $\rightarrow$ **Hochpunkt $H(0 | 4)$**
* Für $x = 2$: $f''(2) = 6(2) - 6 = 6 > 0 \Rightarrow$ **Tiefpunkt (Minimum)**

    $y$-Koordinate: $f(2) = 2^3 - 3(2)^2 + 4 = 8 - 12 + 4 = 0$

    $\rightarrow$ **Tiefpunkt $T(2 | 0)$**

---

### 3. Krümmungsverhalten und Wendepunkte

Für Wendepunkte benötigen wir die zweite und dritte Ableitung:
* $f''(x) = 6x - 6$
* $f'''(x) = 6$

**Wendepunkt berechnen ($f''(x) = 0$):**
$$6x - 6 = 0 \Rightarrow 6x = 6 \Rightarrow x = 1$$
Da $f'''(1) = 6 \neq 0$, liegt hier tatsächlich ein Wendepunkt vor.
$y$-Koordinate: $f(1) = 1^3 - 3(1)^2 + 4 = 2$.
$\rightarrow$ **Wendepunkt $W(1 | 2)$**

**Krümmungsverhalten:**
* Für $x < 1$ (z.B. $x=0$): $f''(0) = -6 < 0 \Rightarrow$ Der Graph ist **rechtsgekrümmt** (konkav).
* Für $x > 1$ (z.B. $x=2$): $f''(2) = 6 > 0 \Rightarrow$ Der Graph ist **linksgekrümmt** (konvex).

---

### 4. Flächeninhalt

Die Fläche wird von den Nullstellen $x = -1$ und $x = 2$ begrenzt. Da der Graph in diesem Intervall oberhalb der $x$-Achse verläuft (wie wir am Hochpunkt $H(0|4)$ sehen), müssen wir nur das bestimmte Integral berechnen:

$$A = \int_{-1}^{2} (x^3 - 3x^2 + 4) \, dx$$
$$A = \left[ \frac{1}{4}x^4 - x^3 + 4x \right]_{-1}^{2} = $$
$$ = \left[\frac{1}{4}(16) - 8 + 8\right] - \left[\frac{1}{4}(1) - (-1) - 4\right] = $$
$$ = 4 + 2,75 = 6,75 \,\text{Flächeneinheiten}$$

---

### 5. Volumen des Rotationskörpers

Die Formel für das Volumen eines Rotationskörpers um die $x$-Achse lautet: $V = \pi \cdot \int_{a}^{b} (f(x))^2 \, dx$

Zuerst quadrieren wir die Funktion $f(x) = x^3 - 3x^2 + 4$:
$$(x^3 - 3x^2 + 4)^2 = x^6 - 6x^5 + 9x^4 + 8x^3 - 24x^2 + 16$$


Nun integrieren wir in den Grenzen von $-1$ bis $2$:
$$V = \pi \cdot \int_{-1}^{2} (x^6 - 6x^5 + 9x^4 + 8x^3 - 24x^2 + 16) \, dx$$

Stammfunktion bilden:
$$V_F(x) = \left[ \frac{1}{7}x^7 - x^6 + \frac{9}{5}x^5 + 2x^4 - 8x^3 + 16x \right]_{-1}^{2}$$

Grenzen einsetzen (dies erfordert etwas Bruchrechnen):
* $V_F(2) = \frac{128}{7} - 64 + \frac{288}{5} + 32 - 64 + 32 = \frac{128}{7} + \frac{288}{5} - 64 = \frac{416}{35}$
* $V_F(-1) = -\frac{1}{7} - 1 - \frac{9}{5} + 2 + 8 - 16 = -\frac{1}{7} - \frac{9}{5} - 7 = -\frac{313}{35}$

Integralwert ausrechnen:
$$V = \pi \cdot \left( \frac{416}{35} - \left(-\frac{313}{35}\right) \right) = \pi \cdot \frac{729}{35}$$

**Ergebnis:** Das Volumen beträgt **$\frac{729}{35}\pi \approx 65,43 \text{ Volumeneinheiten}$**.



## Beispiel 7 (10 Punkte)

Gegeben sei ein Quader im Raum mit den Kantenlängen $x = 1, y = 2, z = 3$.

1. Zeichnen Sie den Quader in das unten angegebene Koordinatensystem.
2. Berechnen Sie das Volumen des Quaders als Dreifachintegral
   $$V = \int_{0}^{1} \int_{0}^{2} \int_{0}^{3} 1 \, dz \, dy \, dx$$
3. Der Quader hat eine Dichtefunktion $\rho(x, y, z) = xyz$. Berechnen Sie die Gesamtmasse
   $$M = \int_{0}^{1} \int_{0}^{2} \int_{0}^{3} \rho(x, y, z) \, dz \, dy \, dx$$

---

## Lösung

### 1. Zeichnung des Quaders

** siehe Lösung **

---

### 2. Volumen als Dreifachintegral berechnen

Wir lösen das Integral von innen nach außen. Die Integrationsreihenfolge ist $dz$, dann $dy$, dann $dx$.

$$V = \int_{0}^{1} \int_{0}^{2} \left( \int_{0}^{3} 1 \, dz \right) dy \, dx$$

* **Inneres Integral (nach $z$):**
  $$\int_{0}^{3} 1 \, dz = [z]_{0}^{3} = 3 - 0 = 3$$

* **Mittleres Integral (nach $y$):** Wir setzen das Ergebnis (3) in das nächste Integral ein.
  $$\int_{0}^{2} 3 \, dy = [3y]_{0}^{2} = 3(2) - 3(0) = 6 - 0 = 6$$

* **Äußeres Integral (nach $x$):** Wir setzen das Ergebnis (6) in das letzte Integral ein.
  $$\int_{0}^{1} 6 \, dx = [6x]_{0}^{1} = 6(1) - 6(0) = 6$$

**Ergebnis:** Das Volumen beträgt **$6 \text{ Volumeneinheiten}$**.
*Kontrolle mit der klassischen Formel:* 
$$ V = a \cdot b \cdot c = 1 \cdot 2 \cdot 3 = 6$$

---

### 3. Gesamtmasse mit Dichtefunktion berechnen

Wir setzen die Dichtefunktion $\rho(x,y,z) = xyz$ in das Integral ein und integrieren wieder schrittweise von innen nach außen.

$$M = \int_{0}^{1} \int_{0}^{2} \int_{0}^{3} xyz \, dz \, dy \, dx$$

* **Inneres Integral (nach $z$):** $x$ und $y$ werden als Konstanten behandelt.
  $$\int_{0}^{3} xyz \, dz = xy \cdot \left[ \frac{1}{2}z^2 \right]_{0}^{3} = xy \cdot \left( \frac{1}{2}(3)^2 - 0 \right) = xy \cdot \frac{9}{2} = \frac{9}{2}xy$$

* **Mittleres Integral (nach $y$):** $x$ wird als Konstante behandelt. Wir integrieren das vorherige Ergebnis.
  $$\int_{0}^{2} \frac{9}{2}xy \, dy = \frac{9}{2}x \cdot \left[ \frac{1}{2}y^2 \right]_{0}^{2} = \frac{9}{2}x \cdot \left( \frac{1}{2}(2)^2 - 0 \right) = \frac{9}{2}x \cdot 2 = 9x$$

* **Äußeres Integral (nach $x$):** Wir integrieren das letzte Ergebnis.
  $$\int_{0}^{1} 9x \, dx = \left[ \frac{9}{2}x^2 \right]_{0}^{1} = \frac{9}{2}(1)^2 - 0 = \frac{9}{2} = 4,5$$

**Ergebnis:** Die Gesamtmasse des Quaders beträgt $4,5 \text{ Masseneinheiten}$.

*(Pro-Tipp für Prüfungen: Da die Integrationsgrenzen alle Konstanten sind und die Funktion $xyz$ ein reines Produkt der einzelnen Variablen ist, darfst du die Integrale auch komplett aufspalten und miteinander multiplizieren: $\int_0^1 x \,dx \cdot \int_0^2 y \,dy \cdot \int_0^3 z \,dz = \frac{1}{2} \cdot 2 \cdot \frac{9}{2} = 4,5$)*

