"""
Generiert ein Histogramm von Messwerten aus einer Gaußverteilung
zur Illustration statistischer Fehler.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Deutsche Schriftarten und Layout
rcParams['font.family'] = 'sans-serif'
rcParams['font.size'] = 12
rcParams['axes.labelsize'] = 14
rcParams['axes.titlesize'] = 14

# Setze den Seed für Reproduzierbarkeit
np.random.seed(46)

# "Wahrer Wert" der Messgröße
x_true = 100.0

# Generiere Messwerte aus Normalverteilung mit Offset zum wahren Wert
# (simuliert systematischen + statistischen Fehler)
n_measurements = 100
std_dev = 8.0
mean_measured = 100.0  # Leicht verschoben vom wahren Wert

# Messwerte generieren
measurements = np.random.normal(loc=mean_measured, scale=std_dev, size=n_measurements)

# Berechne Mittelwert und Standardabweichung
x_mean = np.mean(measurements)
sigma = np.std(measurements, ddof=1)

# Erstelle Figure
fig, ax = plt.subplots(figsize=(10, 6))

# Standardabweichungsbereiche (optional als schwach eingefärbte Bereiche)
ax.axvspan(x_mean - sigma, x_mean + sigma, alpha=0.3, color='gray', 
           label=r'$\pm \sigma$')

# Histogramm erstellen (türkisfarben wie im Original)
n, bins, patches = ax.hist(measurements, bins=30, 
                           color='#87CEEB', 
                           edgecolor='#5DADE2', 
                           alpha=0.9,
                           linewidth=1.2)

# Vertikale Linien für Mittelwert und wahren Wert
ax.axvline(x_mean, color='black', linestyle='--', linewidth=2.5, 
           label=r'Mittelwert $\bar{x}$', zorder=5)
ax.axvline(x_true, color='red', linestyle='-', linewidth=2.5, 
           label=r'Wahrer Wert $x_\mathrm{W}$', zorder=5)


# Achsenbeschriftungen
ax.set_xlabel(r'Messwerte $x_i$', fontsize=14)
ax.set_ylabel(r'Häufigkeit $n_i$', fontsize=14)

# Legende
ax.legend(loc='upper left', fontsize=11, framealpha=0.95)

# Grid für bessere Lesbarkeit
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.7)
ax.set_axisbelow(True)

# Layout optimieren
plt.tight_layout()

# Speichern als PDF (vektorisiert, besser für LaTeX)
output_path_pdf = 'Bilder/Kapitel_Grundlagen/stat_Verteilung_messwerte.pdf'
plt.savefig(output_path_pdf, format='pdf', dpi=300, bbox_inches='tight')
print(f"PDF gespeichert: {output_path_pdf}")

# Zusätzlich als PNG (für schnelle Vorschau)
output_path_png = 'Bilder/Kapitel_Grundlagen/stat_Verteilung_messwerte.png'
plt.savefig(output_path_png, format='png', dpi=300, bbox_inches='tight')
print(f"PNG gespeichert: {output_path_png}")

plt.show()

# Ausgabe der Werte
print(f"\nStatistische Auswertung:")
print(f"Wahrer Wert x_W: {x_true:.2f}")
print(f"Mittelwert x̄: {x_mean:.2f}")
print(f"Standardabweichung σ: {sigma:.2f}")
print(f"Anzahl Messungen: {n_measurements}")
