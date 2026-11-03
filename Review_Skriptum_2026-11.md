# Prüfbericht Skriptum „Grundlagen Physik“ (Stand 01.11.2026)

Geprüft: alle in `main.tex` eingebundenen Kapitel (1–11) plus Anhänge (Herleitungen, Mathematische Einschübe).
Nicht geprüft: Tests, `uebungsbeispiele.tex`, `combined_main_*.tex`, Abbildungen (nur Bildunterschriften).

Gesamteindruck: Die Sprache ist überwiegend klar, gut gegliedert und studierendenfreundlich. Die Merk-/Wichtig-Boxen sind didaktisch stark. Es gibt aber einige **echte Formel- und Zahlenfehler** und mehrere Stellen, an denen die Vereinfachung **physikalisch falsch** wird. Diese stehen in Teil A und B.

Legende: **A** = eindeutiger Fehler (bitte korrigieren) · **B** = physikalisch ungenau/missverständlich · **C** = Konsistenz zwischen Kapiteln · **D** = Tippfehler

> **Umsetzungsstand:** Alle Punkte aus **A** und **D** sowie fast alle aus **B** sind direkt in den .tex-Dateien korrigiert (Zeilennummern unten beziehen sich auf den Stand *vor* der Korrektur). `main.tex` kompiliert danach ohne Fehler.
> **Noch offen (bewusst nicht geändert, weil es eine Entscheidung oder ein Blick ins Bild braucht):**
> - Teil **C** (Symbol-Vereinheitlichung) – umgesetzt sind nur: Drehmoment $\vec D \to \vec M$ und $I \to J$ in Kap. 6, $I_\text{v}$, $\Omega$ statt $W$, fehlendes $\nu$ in Kap. 11. Offen: $M$ = Masse/Drehmoment in Kap. 9, $n$ vs. $\nu$, $\vartheta$ vs. $T[°\text{C}]$, $[x]$ für Dimensionen, $\Delta Q$-Schreibweise, signifikante Stellen in Beispielen.
> - Abbildungen: grüner Pfeil im Pendelbild Kap. 2 (nur der Code-Kommentar wurde korrigiert). *Erledigt:* Schiefe-Ebene-Grafiken in Kap. 6 als TikZ neu gezeichnet ($\vec F_{G,\perp}$ vs. $\vec F_N$, Reibungsrichtung in der Abbildung Fall (i)/(ii)); Rollgrafik in Kap. 9 zeigt jetzt $\vec F_\perp$ statt $\vec F_N$.
> - Kap. 8, Z. 242 (Energie als „Fähigkeit, Arbeit zu verrichten“), Kap. 9, Z. 408 ($\vec r_\perp$ im Drehimpuls), Hinweise zur Sprache (Kap. 2 Einleitung, Mathe-Anhang).

---

## A – Eindeutige Fehler

### Formeln und Zahlenwerte

| # | Stelle | Problem | Korrektur |
|---|---|---|---|
| A1 | [chapter_3:54](chapter_3-MaßeinheitenMessverfahren.tex#L54) | Cäsium-Frequenz falsch: 9 **16**2 631 770 Hz (zweimal) | **9 192 631 770 Hz** |
| A2 | [chapter_5-Kinematik.tex:1241](chapter_5-Kinematik.tex#L1241) | Zentripetalbeschleunigung $\frac{v}{R^2}$ | $\frac{v^2}{R}$ |
| A3 | [chapter_5-Kinematik.tex:965](chapter_5-Kinematik.tex#L965) | „optimaler Wurfwinkel = 45°“ – gilt nur für Abwurfhöhe $h = 0$. Die Formel davor hat aber $h>0$. | „Für $h = 0$ ist $\varphi_\text{opt} = 45°$; für $h > 0$ ist der optimale Winkel kleiner.“ |
| A4 | [chapter_5-Kinematik.tex:587](chapter_5-Kinematik.tex#L587) | $\vec v = \lvert\vec r_j-\vec r_i\rvert/\lvert t_j-t_i\rvert$ – links Vektor, rechts Skalar; Richtung geht verloren | $\vec v = (\vec r_j-\vec r_i)/(t_j-t_i)$ |
| A5 | [chapter_5-Kinematik.tex:1142](chapter_5-Kinematik.tex#L1142) | $-\tan^{-1}(\varphi)$ wird als arctan gelesen | $-\frac{1}{\tan\varphi} = -\cot\varphi$ |
| A6 | [chapter_5-Kinematik.tex:1084](chapter_5-Kinematik.tex#L1084) | „Ortsvektor des **Ursprungs**“ | „des **Mittelpunkts**“ |
| A7 | [chapter_11-HauptsaetzeThermodynamik.tex:337](chapter_11-HauptsaetzeThermodynamik.tex#L337) | Adiabatengleichung $T\cdot V^{\kappa}$ | $T\cdot V^{\kappa-1} = \text{const}$ (das Ergebnis $V_2/V_1 = V_3/V_4$ bleibt richtig) |
| A8 | [chapter_11:382](chapter_11-HauptsaetzeThermodynamik.tex#L382), [:386](chapter_11-HauptsaetzeThermodynamik.tex#L386) | Vorzeichen der Entropieänderung vertauscht: Bei Wärmeaufnahme ergibt sich $R\ln(V_1/V_2) < 0$ – Entropie würde sinken | $\Delta S_{1\to2} = \nu R\ln(V_2/V_1) > 0$, $\Delta S_{3\to4} = \nu R\ln(V_4/V_3) < 0$ |
| A9 | [chapter_11:40](chapter_11-HauptsaetzeThermodynamik.tex#L40), [:46](chapter_11-HauptsaetzeThermodynamik.tex#L46), [:333](chapter_11-HauptsaetzeThermodynamik.tex#L333) | $C_V, C_p$ sind molar, $\nu$ fehlt (in :333 fällt $\nu$ ohne Erklärung weg) | $\dd Q = \nu C_V \dd T$ bzw. „für $\nu = 1$ mol“ dazuschreiben |
| A10 | [chapter_App-Herleitungen.tex:159](chapter_App-Herleitungen.tex#L159) | Zwischenergebnis Vollkugel $\frac{4\pi}{15}\rho R^5$ | $\frac{8\pi}{15}\rho R^5$ (Endergebnis $\frac25 MR^2$ stimmt) |
| A11 | [chapter_3:279](chapter_3-MaßeinheitenMessverfahren.tex#L279) | „Demnach muss die Dichte ebenso im **Nenner** stehen“ | „im **Zähler**“ |
| A12 | [chapter_1-Allgemeines.tex:200](chapter_1-Allgemeines.tex#L200) | Beispiel falsch: kg·m/s und g·km/s sind **gleich** (beide = 10³ g·m/s) | Besseres Beispiel: $1\,\text{km}^2 = 10^6\,\text{m}^2$ (nicht $10^3$), weil das Präfix mitpotenziert wird |
| A13 | [chapter_10-Waermelehre.tex:610](chapter_10-Waermelehre.tex#L610), [:612](chapter_10-Waermelehre.tex#L612) | Mit $H = 8$ km liegt die Halbwertshöhe bei $H\ln 2 \approx 5{,}5$ km und der Everest-Druck bei $e^{-8849/8000} \approx 33\,\%$. Die Angaben 5,8 km und 34,5 % passen zu $H \approx 8{,}4$ km. | Zahlen vereinheitlichen |
| A14 | [chapter_10-Waermelehre.tex:1469](chapter_10-Waermelehre.tex#L1469) | $v_D = RT/p$ – $v_D$ ist spezifisches Volumen (pro kg) | $v_D = \frac{RT}{M\,p}$ ($M$ = molare Masse) |
| A15 | [chapter_4:45](chapter_4-MessgenauigkeitMessfehler.tex#L45) | „50 liegt zwischen 49,5 und 50,4“ | $49{,}5 \le x < 50{,}5$ |
| A16 | [chapter_4:133-135](chapter_4-MessgenauigkeitMessfehler.tex#L133) | Als Unsicherheit des Mittelwerts wird $\sigma$ der Einzelmessung angegeben; außerdem heißt das Ergebnis $T_W$ („wahrer Wert“). Satz „Man misst“ bricht ab (Z. 132). | Unsicherheit des Mittelwerts: $\sigma_m = \sigma/\sqrt{10} \approx 0{,}015$ s → $T = (2{,}000 \pm 0{,}015)$ s |
| A17 | [chapter_3:202](chapter_3-MaßeinheitenMessverfahren.tex#L202) | In der Spalte „Richtig“ steht $123 \pm 5\,\text{g}$ – das ist laut SI-Broschüre mehrdeutig | $(123 \pm 5)\,\text{g}$ |
| A18 | [chapter_App-Mathematische:971](chapter_App-MathematischeEinschübe.tex#L971) | $f(x,y) = \cos(x) + \sin(\mathbf{x})$ | $\sin(y)$ |
| A19 | [chapter_App-Mathematische:1159](chapter_App-MathematischeEinschübe.tex#L1159) | $\int \frac1x \dd x = \mathbf{c}\ln\lvert x\rvert + C$ | ohne $c$ |
| A20 | [chapter_App-Mathematische:6](chapter_App-MathematischeEinschübe.tex#L6), [:14](chapter_App-MathematischeEinschübe.tex#L14) | Folge $1, \frac12, \frac14, \dots$ wird als $a_n = \frac1n$ mit $n \in \mathbb{R}$ definiert; die Reihe danach ist $\sum \frac{1}{n^2}$ – passt beides nicht | $a_n = \left(\frac12\right)^{n}$, $n \in \mathbb{N}_0$; Reihe dazu $\sum (\frac12)^n = 2$; `\cdot .` → `\cdots` |
| A21 | [chapter_8-Arbeit-Energie.tex:398](chapter_8-Arbeit-Energie.tex#L398) | Verirrtes `{\text{ext}}` im Fließtext – erscheint als „ext“ im PDF | Zeile löschen |

### Physikalische Aussagen, die falsch sind

| # | Stelle | Problem | Vorschlag |
|---|---|---|---|
| A22 | [chapter_8-Arbeit-Energie.tex:553](chapter_8-Arbeit-Energie.tex#L553) | Kernspaltung: „Das größere Ausgangsatom hat eine **größere** Bindungsenergie als die Zerfallsprodukte“ – genau umgekehrt | Die Spaltprodukte sind **stärker** gebunden (höhere Bindungsenergie pro Nukleon); die Differenz wird frei – überwiegend als kinetische Energie der Spaltprodukte, dazu Neutronen und γ-Strahlung. Außerdem „Atomkern“ statt „Atom“. |
| A23 | [chapter_8-Arbeit-Energie.tex:485-486](chapter_8-Arbeit-Energie.tex#L485) | Federarbeit: Deutung vertauscht. $W_\text{Feder} < 0$ heißt: der **Block** verrichtet Arbeit an der Feder (Energie wird gespeichert). Außerdem entscheidet $\lvert x_E\rvert > \lvert x_A\rvert$, nicht $x_E > x_A$ (Bsp.: $x_A=-2$, $x_E=1$ → $W>0$). | Bedingungen auf Beträge umstellen und Deutung tauschen |
| A24 | [chapter_10-Waermelehre.tex:2](chapter_10-Waermelehre.tex#L2), [:4](chapter_10-Waermelehre.tex#L4) | „Wärme … die mikroskopische Bewegungsenergie der Atome“ – das ist die **innere Energie**. Wärme ist übertragene Energie (Prozessgröße). Widerspricht Z. 1084 und Anhang ([Herleitungen:452](chapter_App-Herleitungen.tex#L452): „es gibt keinen Wärmeinhalt“). | „…dass Wärme eine Form der Energieübertragung ist und die innere Energie eines Körpers auf der Bewegung seiner Teilchen beruht…“ |
| A25 | [chapter_11:101](chapter_11-HauptsaetzeThermodynamik.tex#L101) | „Wärme kann nie vollständig in Arbeit verwandelt werden (Dissipation)“ – bei der isothermen Expansion geschieht genau das (Z. 57, Z. 303). Die Grenze gilt nur für **periodisch arbeitende** Maschinen. „Dissipation“ bezeichnet den umgekehrten Vorgang. | „…in einem Kreisprozess nie vollständig…“; Klammer streichen |
| A26 | [chapter_11:401-416](chapter_11-HauptsaetzeThermodynamik.tex#L401) | $\eta = 1 - T_2/T_1$, $\varepsilon = T_2/(T_1-T_2)$ usw. als allgemeine Definitionen; „arbeiten typischerweise nach dem Carnot-Prinzip“ (Otto, Diesel tun das nicht). Widerspricht Z. 373. | Definition $\eta = W/Q_1$; Temperaturformel als **Obergrenze** (ideal/reversibel) kennzeichnen |
| A27 | [chapter_5-Kinematik.tex:1267](chapter_5-Kinematik.tex#L1267) | „$\vec v$ ändert sich nach Betrag und Richtung, **weil** sich die Beschleunigung ändert“ – falsch (schräger Wurf: $\vec a$ konstant, $\vec v$ ändert Betrag und Richtung) | „…weil $\vec a$ im Allgemeinen nicht parallel zu $\vec v$ ist“ |
| A28 | [chapter_5-Kinematik.tex:43](chapter_5-Kinematik.tex#L43) | „Kinematik … vernachlässigt die **Ausdehnung** des Körpers“ | Kinematik beschreibt Bewegung **ohne nach den Ursachen (Kräften)** zu fragen (passt dann auch zur Grafik) |
| A29 | [chapter_6-Dynamik.tex:42](chapter_6-Dynamik.tex#L42) | „Ursache für den Bewegungszustand **und** dessen Änderungen“ – das ist aristotelisch. Nach Newton braucht nur die **Änderung** eine Ursache. | „…Ursache für **Änderungen** des Bewegungszustands…“ |
| A30 | [chapter_6-Dynamik.tex:549](chapter_6-Dynamik.tex#L549) | „Gleitbereich ($\lvert F_R\rvert > \lvert F_{R,h,max}\rvert$)“ – im Gleitbereich ist $F_R$ **kleiner** als $F_{R,h,max}$ | „Gleitbereich ($\lvert F_A\rvert > \lvert F_{R,h,max}\rvert$)“ |
| A31 | [chapter_6-Dynamik.tex:755](chapter_6-Dynamik.tex#L755) | „Gekrümmte Bahnkurve ⇒ stets $\vec L \neq 0$“ – falsch: $\vec L$ hängt vom Bezugspunkt ab, eine Gerade, die nicht durch den Ursprung geht, hat auch $\vec L \neq 0$ | Satz streichen oder: „Bewegt sich ein Körper nicht radial, ist $\vec L \neq 0$.“ |
| A32 | [chapter_6:793](chapter_6-Dynamik.tex#L793), [:833](chapter_6-Dynamik.tex#L833) | $\vec\omega = \vec r\times\vec v/r^2$ steht in der Merkbox als allgemeine Formel – gilt nur, wenn $\vec r \perp \vec\omega$ (wird erst danach hergeleitet) | Bedingung in die Box schreiben |
| A33 | [chapter_6-Dynamik.tex:906](chapter_6-Dynamik.tex#L906) | $\vec r\,' = x(t)\vec e_x\,' + \dots$ | $x'(t)\vec e_x\,' + y'(t)\dots$ |
| A34 | [chapter_6-Dynamik.tex:926](chapter_6-Dynamik.tex#L926) | „$(\dd\vec e_x'/\dd t)\times\vec e_x$ zeigt entlang $\vec\omega$“ – falsche Reihenfolge (zeigt gegen $\vec\omega$) und ungestrichenes $\vec e_x$; Verweis auf Gl. *omega_r_x_v* statt *v_eq_omega_cross_r* (Z. 922) | $\vec e_x\,'\times(\dd\vec e_x\,'/\dd t) \parallel \vec\omega$ |
| A35 | [chapter_7-Gravitation.tex:164](chapter_7-Gravitation.tex#L164) | „Aus dem 2. Keplerschen Gesetz wissen wir, dass die Kraft vom **Abstand** abhängen muss“ – das 2. Gesetz zeigt nur, dass es eine **Zentralkraft** ist | Abstandsabhängigkeit kommt aus dem 3. Gesetz (wird ja danach gezeigt) |
| A36 | [chapter_9-RotationStarrerKoerper.tex:40](chapter_9-RotationStarrerKoerper.tex#L40) | Schwerpunkt: „Die Gewichtung erfolgt über den **Abstand**“ | „…über die **Masse** der Massenelemente“ |
| A37 | [chapter_9-RotationStarrerKoerper.tex:348](chapter_9-RotationStarrerKoerper.tex#L348) | „$b$ gibt an, welcher Anteil der kinetischen Energie in die Rotation fließt“ – der Anteil ist $\frac{b}{1+b}$; $b = E_\text{rot}/E_\text{trans}$ | Satz anpassen |
| A38 | [chapter_9-RotationStarrerKoerper.tex:63](chapter_9-RotationStarrerKoerper.tex#L63) | „zweimal differenzieren“ | „einmal“ |
| A39 | [chapter_10-Waermelehre.tex:614](chapter_10-Waermelehre.tex#L614) | „exponentielle (**schneller** als linear) Abnahme“ – umgekehrt: bei gleicher Anfangssteigung fällt die Exponentialkurve langsamer und erreicht nie null | „langsamer als linear; keine scharfe Obergrenze“ |
| A40 | [chapter_10-Waermelehre.tex:725](chapter_10-Waermelehre.tex#L725) | $\vec F_\text{Gew} = -\vec F_\text{Auf}$ – gilt nur für schwebende Körper; in Z. 723 heißt $F_\text{Gew}$ außerdem das Gewicht des verdrängten Gases | „Die Auftriebskraft zeigt der Gewichtskraft entgegen.“ (ohne Gleichung) |
| A41 | [chapter_10-Waermelehre.tex:219](chapter_10-Waermelehre.tex#L219) | Gase „2–3 Größenordnungen“ stärker als Feststoffe **und Flüssigkeiten** – laut eigener Tabelle: Wasser ×17, Ethanol ×3 | „…etwa 2 Größenordnungen größer als bei Festkörpern und etwa 1 Größenordnung größer als bei Flüssigkeiten“ |
| A42 | [chapter_App-Herleitungen.tex:116](chapter_App-Herleitungen.tex#L116), [:118](chapter_App-Herleitungen.tex#L118) | Hohlzylinder: Achse „**senkrecht** zur Zylinderachse“ – gerechnet wird aber um die Zylinderachse ($J = MR^2$) | „…um die Zylinderachse ($z$-Achse)“ |
| A43 | [chapter_App-Herleitungen.tex:459](chapter_App-Herleitungen.tex#L459) | $\dd S = \delta Q/T$ ohne „rev“ | $\dd S = \delta Q_\text{rev}/T$ |
| A44 | [chapter_8-Arbeit-Energie.tex:60](chapter_8-Arbeit-Energie.tex#L60) | Wegintegral als Summe von drei gewöhnlichen Integralen $\int_{x_1}^{x_2}F_x(x,y,z)\dd x+\dots$ – geht nur, wenn $y, z$ entlang des Weges als Funktion eingesetzt werden. So aufgeschrieben wäre jede Arbeit wegunabhängig. | Hinweis ergänzen: „wobei entlang $\mathcal C$ $y = y(x)$, $z = z(x)$ eingesetzt werden“ oder Parametrisierung $\vec r(t)$ |
| A45 | [chapter_8-Arbeit-Energie.tex:28](chapter_8-Arbeit-Energie.tex#L28) | Bildunterschrift: „Massenpunkt … verrichtet dabei die Arbeit“ | „Die **Kraft** verrichtet am Massenpunkt die Arbeit“ |
| A46 | [chapter_1-Allgemeines.tex:48](chapter_1-Allgemeines.tex#L48) | $\stackrel{!}{=}$ = „bekannte Gleichheit“ – bedeutet „soll gleich sein“ (Forderung/Bedingung); so wird es im Skriptum auch benutzt | „Forderung (soll gleich sein)“ |
| A47 | [chapter_1-Allgemeines.tex:151](chapter_1-Allgemeines.tex#L151) | „Basiseinheit (wie Meter, **Gramm** oder Sekunde)“ – Basiseinheit ist das Kilogramm | „Einheit (wie Meter, Gramm oder Sekunde)“ |
| A48 | [chapter_2-Grundlagen.tex:142](chapter_2-Grundlagen.tex#L142) | Thales: „von einem Halbkreis **umschriebene** Dreiecke“ | „Jedes Dreieck, dessen eine Seite der Durchmesser eines Kreises ist und dessen dritte Ecke auf dem Kreis liegt, ist rechtwinklig.“ |
| A49 | [chapter_3:234](chapter_3-MaßeinheitenMessverfahren.tex#L234) | „Einheiten sind eindeutig“ – falsch: N·m = J (Drehmoment/Energie), Hz = Bq = s⁻¹, Gy = Sv | Die Einheit verrät **nicht** eindeutig die Größe; aber eine Gleichung muss auf beiden Seiten dieselbe Einheit haben |
| A50 | [chapter_App-Mathematische:315](chapter_App-MathematischeEinschübe.tex#L315) | Erklärung zum 4. Quadranten falsch: arctan liefert dort bereits den richtigen (negativen) Winkel – widerspricht der Box darüber | Erklärung auf Q2 (arctan liefert Q4) und Q3 (arctan liefert Q1) umstellen; Hinweis auf `atan2` |
| A51 | [chapter_App-Mathematische:645](chapter_App-MathematischeEinschübe.tex#L645) | Box-Titel „Skalarmultiplikation“ über dem **Skalarprodukt** – genau die Verwechslung, vor der der Text warnt | Titel „Skalarprodukt“ |
| A52 | [chapter_App-Mathematische:717](chapter_App-MathematischeEinschübe.tex#L717) | „Das Kreuzprodukt ist eine Bilinear**form**“ – eine Bilinearform liefert einen Skalar | „bilineare Abbildung“; außerdem `V×V ∈ V` → `V×V → V` (auch Z. 649) |
| A53 | [chapter_App-Mathematische:559](chapter_App-MathematischeEinschübe.tex#L559) | „derselben Richtung … $\lvert\vec u\rvert = s\lvert\vec r\rvert$“ | $\lvert\vec u\rvert = \lvert s\rvert\,\lvert\vec r\rvert$; gleiche Richtung nur für $s>0$ |

---

## B – Physikalisch ungenau oder missverständlich

**Kapitel 1–2**
- [chapter_1:93-95](chapter_1-Allgemeines.tex#L93): „reversibel = ohne Energie**verlust**“ widerspricht dem Energieerhaltungssatz, den das Skriptum später betont. Besser: „ohne Entropiezunahme / ohne bleibende Änderung der Umgebung“. „konservativ“ → „**mechanische** Energie bleibt erhalten“.
- [chapter_2:8-9](chapter_2-Grundlagen.tex#L8): Zerfallsreihen quantifizieren nichts; quantitativ ist das Zerfallsgesetz $N(t) = N_0 e^{-\lambda t}$. „Voraussagbar“ gilt nur statistisch – der einzelne Zerfall ist zufällig. Genau das ist eine schöne Pointe für Studierende.
- [chapter_2:28](chapter_2-Grundlagen.tex#L28): Hypothese gilt nur für **kleine Auslenkungen**. In der Pendel-Grafik ([Z. 87](chapter_2-Grundlagen.tex#L87)) ist ein Kraftpfeil mit $\vec g$ beschriftet → $\vec F_G = m\vec g$. Der grüne Pfeil zeigt laut Code vom Aufhängepunkt **weg** (Radialkomponente der Gewichtskraft), der Code-Kommentar nennt ihn „Spannkraft“.
- [chapter_2:132](chapter_2-Grundlagen.tex#L132): „Zwei parallele Linien schneiden sich nie“ ist eher die Definition von „parallel“. Das Axiom (Euklid): „Zu einer Geraden und einem Punkt außerhalb gibt es genau eine Parallele.“ Didaktischer Bonus: In nicht-euklidischer Geometrie (Kugeloberfläche) gilt es nicht.
- [chapter_2:153](chapter_2-Grundlagen.tex#L153): $U = R\cdot I$ ist die Definition des Widerstands. Das Ohm'sche **Gesetz** sagt, dass $R$ bei konstanter Temperatur unabhängig von $U$ und $I$ ist.
- [chapter_2:154](chapter_2-Grundlagen.tex#L154): Abstand der „Schwerpunkte“ gilt exakt nur für Punktmassen bzw. kugelsymmetrische Körper.

**Kapitel 3–4**
- [chapter_3:11](chapter_3-MaßeinheitenMessverfahren.tex#L11): In der Box ist „Vergleich mit dem Normal“ = Eichung. Fachlich ist das die **Kalibrierung**; die **Eichung** ist die behördliche Prüfung, ob Fehlergrenzen eingehalten werden (der Absatz darunter stimmt).
- [chapter_3:68-100](chapter_3-MaßeinheitenMessverfahren.tex#L68): „seit 2018“ → beschlossen 2018, **in Kraft seit 20. Mai 2019**. Bei $h$, $e$, $k$ fehlt die Einheit direkt beim Zahlenwert (z. B. $h = 6{,}626\,070\,15\cdot10^{-34}$ J·s). Z. 72: „die **Masse** ist festgelegt“ → „die **Einheit Kilogramm** ist festgelegt“.
- [chapter_3:96](chapter_3-MaßeinheitenMessverfahren.tex#L96): Am absoluten Nullpunkt hört die Bewegung nicht völlig auf (Nullpunktsenergie). Besser wie in Kap. 10, Z. 56: „…kleinstmögliche Energie (Grundzustand)“.
- [chapter_3:141](chapter_3-MaßeinheitenMessverfahren.tex#L141) + Bildunterschrift Z. 139: „Kegel mit Öffnungs**winkel** $\Omega$“ – $\Omega$ ist der Raumwinkel, kein Öffnungswinkel. Ergänzen: volle Kugel = $4\pi$ sr.
- [chapter_3:206-211](chapter_3-MaßeinheitenMessverfahren.tex#L206): Physikalisch muss nur die **Dimension** gleich sein; $3\,\text{m} + 20\,\text{cm} = 3{,}2\,\text{m}$ ist korrekt. Für das **Rechnen mit Zahlenwerten** muss man vorher auf dieselbe Einheit umrechnen – so formuliert stimmt es.
- [chapter_3:250](chapter_3-MaßeinheitenMessverfahren.tex#L250): Eckige Klammern stehen hier für die Dimension, sonst im Skriptum für die Einheit ($[h] = \text{kg m}^2/\text{s}$). Vorschlag: $\dim x$ für Dimensionen, $[x]$ für Einheiten.
- [chapter_4:24](chapter_4-MessgenauigkeitMessfehler.tex#L24): Die Tabelle ordnet 4500 eindeutig 2 signifikante Stellen zu; Z. 43 sagt, 320 „könnte 2 oder 3“ haben, Z. 45 behandelt die letzte Null von 50 als signifikant. Vorschlag: „2–4 (mehrdeutig)“ und Z. 45 daran anpassen.
- [chapter_4:102](chapter_4-MessgenauigkeitMessfehler.tex#L102): Normalverteilung ergibt sich nicht automatisch, sondern wenn viele kleine, unabhängige Störungen zusammenwirken (zentraler Grenzwertsatz) – „meist näherungsweise“.

**Kapitel 5 – Kinematik**
- [Z. 121](chapter_5-Kinematik.tex#L121) Fußnote „Kreisbewegungen eines Massenpunktes sind Translation“ – kollidiert mit Kap. 6/9 (Drehimpuls eines Massenpunkts, $J = mr^2$). Vorschlag: „Bahnbewegung“ und „Eigenrotation“ unterscheiden.
- [Z. 129](chapter_5-Kinematik.tex#L129): „Geradlinig, **sofern** alle Koordinaten maximal linear“ – hinreichend, nicht notwendig ($x = t^2$, $y = 2t^2$ ist auch eine Gerade). → „zum Beispiel, wenn…“
- [Z. 323](chapter_5-Kinematik.tex#L323), [387](chapter_5-Kinematik.tex#L387), [464](chapter_5-Kinematik.tex#L464): „Δx ist streng genommen ein Vektor“, „Zeitänderung hat ein Vorzeichen und somit eine Richtung“ – ein Vorzeichen macht noch keinen Vektor. $\Delta x$, $v_x$ sind **Komponenten** (Skalare mit Vorzeichen), $\Delta t$ ist ein Skalar.
- [Z. 390](chapter_5-Kinematik.tex#L390), [632](chapter_5-Kinematik.tex#L632), [872](chapter_5-Kinematik.tex#L872): Aufgetragen ist der **Ort** $x(t)$, nicht der Weg (Weg ist nie negativ) → „Ort-Zeit-Diagramm“. Die Kurve im $(t,x)$-Diagramm ist der **Graph**, nicht die Bahnkurve. Beim freien Fall bewegt sich der Körper auf einer Geraden – nur der Graph ist eine Parabel.
- [Z. 460](chapter_5-Kinematik.tex#L460): „Verhältnis von zurückgelegtem **Weg** zu Zeit“ – hier ist die **Verschiebung** gemeint (Weg/Zeit = Durchschnittstempo). Diese Unterscheidung lohnt sich explizit.
- [Z. 764](chapter_5-Kinematik.tex#L764): Die 2. Ableitung ist nicht die Krümmung (Krümmung $\kappa = \lvert x''\rvert/(1+x'^2)^{3/2}$). → „hängt mit der Krümmung zusammen“.
- [Z. 824](chapter_5-Kinematik.tex#L824), [881](chapter_5-Kinematik.tex#L881): „ohne Luftwiderstand“ ergänzen (im Mathe-Anhang steht es).
- [Z. 834](chapter_5-Kinematik.tex#L834): „Geschwindigkeit ist negativ … und **steigt** linear“ – $v$ wird immer negativer; es steigt der **Betrag**.
- [Z. 1215](chapter_5-Kinematik.tex#L1215) und [Herleitungen:87](chapter_App-Herleitungen.tex#L87): $\lim\lvert\Delta\vec r\rvert = \Delta s$ ist trivial (beide → 0). Gemeint ist $\lim \lvert\Delta\vec r\rvert/\Delta s = 1$.
- [Z. 1285](chapter_5-Kinematik.tex#L1285): $\lvert\vec a_t\rvert = \lvert \dd v/\dd t\rvert$ (kann beim Bremsen negativ sein). Optional: $\lvert\vec a_n\rvert = v^2/\rho$ ergänzen.

**Kapitel 6 – Dynamik**
- [Z. 127](chapter_6-Dynamik.tex#L127): „Kraft … infolgedessen sich die Geschwindigkeit ändert“ – eine einzelne Kraft muss nichts beschleunigen (Gleichgewicht). → „Eine **resultierende** Kraft…“; Verformung als Wirkung erwähnen.
- [Z. 153-155](chapter_6-Dynamik.tex#L153): $\vec F = m\vec a + \dot m\vec v$ ist für die Rakete irreführend (hängt vom Bezugssystem ab). Korrekt: $m\,\dd\vec v/\dd t = \vec F + \vec u_\text{rel}\,\dd m/\dd t$. Vorschlag: Raketenbeispiel streichen oder richtig aufschreiben.
- [Z. 216](chapter_6-Dynamik.tex#L216): „relativistische Masse“ gilt heute als veraltet – ein Satz Hinweis reicht.
- [Z. 299](chapter_6-Dynamik.tex#L299): „3. Axiom ist direkte Folge der Impulserhaltung“ – Zirkelschluss, denn $\dd\vec P/\dd t = \vec F_\text{ext}$ setzt bereits voraus, dass sich innere Kräfte paarweise aufheben (3. Axiom). Besser: „…sind gleichwertig“.
- [Z. 461](chapter_6-Dynamik.tex#L461): $\Delta x \ll 1$ – eine Länge kann nicht „klein gegen 1“ sein. → „klein gegen die Federlänge“.
- [Z. 468](chapter_6-Dynamik.tex#L468): Federkonstante ist keine Materialeigenschaft (hängt auch von Drahtdicke, Windungszahl, Durchmesser ab).
- [Z. 570](chapter_6-Dynamik.tex#L570), [581](chapter_6-Dynamik.tex#L581) und [Rotation:329/332](chapter_9-RotationStarrerKoerper.tex#L332): Die Normal**komponente der Gewichtskraft** heißt hier $\vec F_N$ (Normalkraft), und $\vec F_N'$ ist die Kraft der Unterlage – bei der Statue (Z. 435) ist $\vec F_N'$ dagegen die Kraft auf den Tisch. Vorschlag: $\vec F_{G,\perp}$ für die Komponente, $\vec F_N$ nur für die Kraft der Unterlage.
- [Z. 677](chapter_6-Dynamik.tex#L677) vs. [679](chapter_6-Dynamik.tex#L679): Bildunterschrift „kleine Zugkraft → Reibung in $-x$“, Text „Reibung zeigt die Ebene hinauf“ – bitte mit der Achsenrichtung im Bild abgleichen.

**Kapitel 7–9**
- [chapter_7:160](chapter_7-Gravitation.tex#L160): Begründung „nach dem 3. Axiom proportional zu beiden Massen“ ist zu knapp: $F \propto m$ folgt aus $a$ unabhängig von $m$, das 3. Axiom macht es dann symmetrisch ⇒ $\propto M$.
- [chapter_7:255](chapter_7-Gravitation.tex#L255): „…ohne jemals auf die Oberfläche zu treffen“ – nur ohne Atmosphäre und Hindernisse.
- [chapter_8:8-11](chapter_8-Arbeit-Energie.tex#L8): Die Vorzeichenregel ist schwer lesbar („An A wird eine Arbeit verrichtet W<0“). Vorschlag: „$W_{A\to B} > 0$: A gibt Energie an B ab. $W_{A\to B} < 0$: A nimmt Energie von B auf.“
- [chapter_8:257](chapter_8-Arbeit-Energie.tex#L257): Bei konstanter Geschwindigkeit ändert sich die kinetische Energie **nicht**. Umgewandelt wird die chemische Energie des Treibstoffs. Rollreibung ([Z. 253](chapter_8-Arbeit-Energie.tex#L253)) entsteht hauptsächlich durch Verformung des Reifens (Walkarbeit).
- [chapter_8:261](chapter_8-Arbeit-Energie.tex#L261): „resultierende Kraft an einem **freien** Körper“ – in [Kap. 6, Z. 116](chapter_6-Dynamik.tex#L116) ist „frei“ als „resultierende Kraft = 0“ definiert.
- [chapter_8:242](chapter_8-Arbeit-Energie.tex#L242): „Energie = Fähigkeit, Arbeit zu verrichten“ – ok als Einstieg, aber nach dem 2. Hauptsatz nicht ganz richtig (Wärme ist nicht vollständig nutzbar). Ein Halbsatz Hinweis genügt.
- [chapter_9:344](chapter_9-RotationStarrerKoerper.tex#L344): Mit $J_S$ braucht man Steiner **nicht**; Steiner braucht man, wenn man um den Kontaktpunkt rechnet ($J_A = J_S + Mr^2$, siehe Z. 332). Ergänzen: Rollen ohne Gleiten braucht Haftreibung, die keine Arbeit verrichtet.
- [chapter_9:408](chapter_9-RotationStarrerKoerper.tex#L408): Mit $\vec r_\perp$ statt $\vec r$ erhält man nur die Komponente von $\vec L$ entlang der Achse – passt nicht ganz zum Hinweis auf Hauptträgheitsachsen in Z. 414.

**Kapitel 10 – Wärmelehre**
- [Z. 22](chapter_10-Waermelehre.tex#L22), [25](chapter_10-Waermelehre.tex#L25): Thermoelement misst die **Thermospannung** (Seebeck-Effekt) zwischen zwei Lötstellen unterschiedlicher Temperatur, nicht die Kontaktspannung.
- [Z. 57](chapter_10-Waermelehre.tex#L57), [1408](chapter_10-Waermelehre.tex#L1408): Tripelpunkt „per Definition exakt 273,16 K“ gilt seit 2019 nicht mehr (Kelvin über $k_B$, siehe Kap. 3). Heute ist 273,16 K ein Messwert.
- [Z. 151](chapter_10-Waermelehre.tex#L151): 7,56 % ist das Verhältnis zum **linearen** Anteil; an der Gesamtausdehnung sind es ≈ 7 %. Temperaturdifferenz besser in K.
- [Z. 155](chapter_10-Waermelehre.tex#L155): „…biegt sich so, dass das Material mit größerem α länger wird“ – beide werden länger; gemeint: es liegt **außen** (auf der gewölbten Seite).
- Anomalie der Dichte von Wasser (Maximum bei 4 °C, γ < 0 unter 4 °C) fehlt bei der Volumenausdehnung – wäre eine gute Ergänzung zur Tabelle.
- [Z. 744](chapter_10-Waermelehre.tex#L744): He-Durchmesser ≈ 0,26 nm (0,05 nm ist etwa der Atomradius). Das Fazit bleibt gleich.
- [Z. 977](chapter_10-Waermelehre.tex#L977): „$v_x = 0$ ist Stillstand“ – das Teilchen kann sich in $y$/$z$ bewegen. → „Die häufigste $x$-Komponente ist null.“
- [Z. 1052](chapter_10-Waermelehre.tex#L1052): „Die meisten Teilchen besitzen eine Geschwindigkeit nahe $v_W$“ → „Die Verteilung hat bei $v_W$ ihr Maximum.“
- [Z. 1097](chapter_10-Waermelehre.tex#L1097): Die 15-°C-Kalorie beträgt 4,1855 J; 4,1868 J ist die „internationale“ Kalorie.
- [Z. 1111](chapter_10-Waermelehre.tex#L1111): alte Mol-Definition (12 g C-12) – widerspricht Kap. 3 (seit 2019 über $N_A$).
- [Z. 1221](chapter_10-Waermelehre.tex#L1221): „geschlossenes Gefäß“ – dort steigt der Druck, und das Plateau bei 100 °C gibt es nicht. → „offenes Gefäß bei Normaldruck“.
- [Z. 1363](chapter_10-Waermelehre.tex#L1363): „wahrer thermodynamischer Druck“ – der gemessene Druck **ist** der thermodynamische. Gemeint: der Druck, den das Gas ohne Anziehung hätte.
- [Z. 1475](chapter_10-Waermelehre.tex#L1475): „Dissoziationsarbeit“ bedeutet das Aufspalten von Molekülen. Hier: „innere Verdampfungsarbeit“ / „Trennarbeit“.

**Kapitel 11 – Hauptsätze**
- [Z. 132](chapter_11-HauptsaetzeThermodynamik.tex#L132): „abgeschlossen (adiabatisch)“ – adiabatisch heißt nur „kein Wärmeaustausch“; abgeschlossen heißt „gar kein Austausch“.
- [Z. 168](chapter_11-HauptsaetzeThermodynamik.tex#L168): Erklärung der Freien Energie ist unklar. Einfacher: „Bei konstanter Temperatur ist $-\Delta F$ die maximal gewinnbare Arbeit.“
- [Z. 188](chapter_11-HauptsaetzeThermodynamik.tex#L188): „in beide Richtungen ablaufen“ → „…so umkehrbar, dass System **und Umgebung** wieder im Ausgangszustand sind“.
- [Z. 200](chapter_11-HauptsaetzeThermodynamik.tex#L200): „$p\cdot V$ ist eine Arbeit“ → „hat die Einheit einer Energie“.

---

## C – Konsistenz zwischen den Kapiteln

| Thema | Wo | Vorschlag |
|---|---|---|
| Drehmoment | $\vec M$ (Kap. 1, 9) vs. $\vec D$ (Kap. 6) | einheitlich $\vec M$ |
| $M$ doppelt belegt | Kap. 9: $M$ = Masse **und** Drehmoment im selben Abschnitt (Z. 332: $\vec F_G = M\vec g$ und $\vec M = \vec r\times\vec F$) | Masse $m$ oder Drehmoment $\vec\tau$ |
| Trägheitsmoment | $I$ (Kap. 1, 6) vs. $J$ (Kap. 9) | einheitlich |
| $n$ / $\nu$ | Stoffmenge $n$ (Kap. 3) vs. $\nu$ (Kap. 10/11); $n$ zusätzlich Teilchendichte (Kap. 10) und Anzahl Messungen (Kap. 4) | Stoffmenge einheitlich $n$ oder $\nu$ |
| Celsius-Temperatur | $\vartheta$ (Gay-Lussac) vs. $T[°\text{C}]$ (Gasthermometer); $T_0 = 273{,}15$ K bzw. $T_0 = 0$ °C | Celsius immer $\vartheta$ |
| Statistisches Gewicht | $\Omega$ (Kap. 11, Z. 146) vs. $W$ (Z. 457) – $W$ ist auch Arbeit | einheitlich $\Omega$ |
| Länge als Vektor | Tabelle Kap. 1 und Kap. 3, Z. 38: Länge = $\vec s$ | $l$ bzw. $s$ (Skalar) |
| Lichtstärke | $I_V$ (Z. 43) vs. $I_v$ (Z. 107) | $I_\text{v}$ |
| Prozessgrößen | Kap. 11, Z. 26 empfiehlt $\delta Q$; danach $\Delta Q_1$, $\dd Q$ | $Q_1$, $\delta Q$ |
| SI-Neudefinition 2019 | Kap. 3 neu, Kap. 10 (Mol, Tripelpunkt) alt | Kap. 10 anpassen |
| Signifikante Stellen | Kap. 4 erklärt die Regeln, Beispiele später nutzen sie nicht (z. B. 441,45 J, 0,08 €/km statt 0,081) | optional angleichen |

---

## D – Tippfehler und Kleinigkeiten

- [chapter_1:45](chapter_1-Allgemeines.tex#L45): `$\Sigma$` → `$\sum$`
- [chapter_2:143](chapter_2-Grundlagen.tex#L143): Komma vor „die“; „Großer Fermatscher Satz“
- [chapter_2:153](chapter_2-Grundlagen.tex#L153): „Ohm'sche Gesetz“ → „Ohm'sches Gesetz“
- [chapter_3:84](chapter_3-MaßeinheitenMessverfahren.tex#L84): „n Mole“ → „n Mol“; [Z. 111](chapter_3-MaßeinheitenMessverfahren.tex#L111): „Das Steradiant“ → „Der Steradiant“; Z. 115 „deren Verwendungen hat sich … durchgesetzt, dass“ → „deren Verwendung hat sich so … durchgesetzt, dass“
- [chapter_5:870](chapter_5-Kinematik.tex#L870): „erreicht **den** Massenpunkt den Boden [$z(t_E = 0$)]“ → „erreicht der Massenpunkt den Boden [$z(t_E) = 0$]“; Z. 961: $v_{x,0}$ vs. $v_{0,x}$
- [chapter_6:419](chapter_6-Dynamik.tex#L419): `\ivec{F}{1\rightarrow 2}` → `\ivecS{F}{1\rightarrow 2}`; [Z. 929](chapter_6-Dynamik.tex#L929): `+ \cdot (`; [Z. 942](chapter_6-Dynamik.tex#L942): „ab:=0“; [Z. 621](chapter_6-Dynamik.tex#L621): „den den“; [Z. 679](chapter_6-Dynamik.tex#L679): „…wird die Zugkraft groß **und** die Haftreibungskraft…“; Z. 1008: „Zentrifugalkraft ist für die Fliehkraft verantwortlich“ (sind dasselbe)
- [chapter_7:16](chapter_7-Gravitation.tex#L16): Satz „Im Kontext der Planetenbahnen ist diese Ellipse dargestellt in … befindet sich“ ist verunglückt
- [chapter_8:257](chapter_8-Arbeit-Energie.tex#L257): „…abgegeben mitberücksichtigt“ → „…abgeben, mitberücksichtigt“
- [chapter_10:893](chapter_10-Waermelehre.tex#L893): „Jedes Freiheitsgrad“; [Z. 1174](chapter_10-Waermelehre.tex#L1174): „von Gases“, „die die“; [Z. 1351](chapter_10-Waermelehre.tex#L1351): „entwickelten“ → „entwickelte“; [Z. 1394](chapter_10-Waermelehre.tex#L1394): Klammer in der Quellenangabe; Z. 900: $N_A$ ist keine Teilchenzahl
- [chapter_11:86](chapter_11-HauptsaetzeThermodynamik.tex#L86): „das Adiabatenexponent“ → „der“; Z. 90: „erlässt“ → „liefert“
- [chapter_App-Herleitungen:118](chapter_App-Herleitungen.tex#L118): „Winddicke“ → „Wanddicke“
- [chapter_App-Mathematische:1176](chapter_App-MathematischeEinschübe.tex#L1176): $\int\log x$ → $\int\log_a x$; Z. 963/986: $f:(x,y)\to\mathbb R$ → $f:\mathbb R^2\to\mathbb R$; Z. 1329: „über den **Rand** des Rechtecks“ → „über das Rechteck“

---

## Hinweise zur Sprache

Die Sprache passt größtenteils gut. Drei Stellen sind für Erstsemester unnötig abstrakt:
- [chapter_6:305](chapter_6-Dynamik.tex#L305) Superpositionsprinzip („Nettoreaktion … Stimuli“) – einfacher: „Wirken mehrere Kräfte gleichzeitig, addiert man sie wie Vektoren. Jede Kraft wirkt so, als wären die anderen nicht da.“
- Mathe-Anhang: Norm-Axiome, „positiv definite symmetrische Bilinearform“ – als optionalen Exkurs kennzeichnen.
- [chapter_2](chapter_2-Grundlagen.tex#L119) Einleitung „Bausteine der wissenschaftlichen Erkenntnis“ – sehr lange Sätze; ließe sich in 3–4 kurze Sätze teilen.
