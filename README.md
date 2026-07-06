# README und TO-DOS

## Wie notebooks starten

Aus der Kommandozeile, vorher

```bash
cd Dropbox/stuff/for-others/teaching/HFH/GKI/05-gki-website/
```

Danach eins von beidem:

### Erste Variante: `.venv`

```bash
source .venv/bin/activate
jupyter lab
jupyter lab include/03_00_plots_allgemein.ipynb
```

### Zweite Variante: `uv`

```bash
uv run jupyter lab
uv run jupyter lab include/03_00_plots_allgemein.ipynb
```

### Wie stoppe ich den Jupyter server ?

In dem terminal Fenster, `Ctrl+c`, danach mit `y` bestätigen.

## To-Do's

1. Update der Notebooks mit mehr comments und Text, Bezug SB 03 komplett
2. Füge ein Notebook zur Hyperparameteroptimierung hinzu (Bezug erster
Teil SB 04 bis einschließlich 4.2)
