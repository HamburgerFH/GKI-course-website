# GKI-Notebooks in GitHub Codespaces

Diese Umgebung enthält Python, Jupyter und alle Pakete für die Notebooks
(pandas, matplotlib, scikit-learn, TensorFlow/Keras).

## Notebook ausführen

1. Links im Explorer den Ordner `include/` öffnen.
2. Ein Notebook anklicken, z. B. `03_01_weinplots.ipynb`.
3. Oben rechts **Run All** wählen. Falls nach einem Kernel gefragt wird:
   **Jupyter Kernel... -> gki-venv** auswählen.

Hinweise:

- Beim ersten Start installiert der Codespace die Pakete. Das dauert einige
  Minuten; erst danach steht der Kernel `gki-venv` zur Verfügung.
- Das MNIST-Notebook trainiert ein neuronales Netz auf der CPU und braucht
  einige Minuten.

## Codespace beenden

Kostenlose GitHub-Konten haben ein monatliches Kontingent an Rechenzeit.
Nach der Arbeit den Codespace stoppen: unten links auf **Codespaces** klicken
-> **Stop Current Codespace**. Inaktive Codespaces stoppen nach 30 Minuten
automatisch.

Eigene Änderungen bleiben im Codespace erhalten, bis er gelöscht wird
(spätestens nach 30 Tagen Inaktivität). Wichtige Dateien per Rechtsklick ->
**Download...** sichern.
