# README und TO-DOS

## Notebooks in GitHub Codespaces ausführen

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/HamburgerFH/GKI-course-website?quickstart=1)

Mit einem (kostenlosen) GitHub-Konto startet der Button eine fertige
Python-/Jupyter-Umgebung im Browser. Die Notebooks liegen in `include/`;
die Anleitung öffnet sich im Codespace automatisch
(`.devcontainer/README.md`).

## Passwortschutz

Die veröffentlichte GitHub-Pages-Site verschlüsselt beim CI-Build alle
generierten HTML-Dateien mit StatiCrypt. Das gemeinsame Passwort liegt nur im
GitHub-Actions-Secret `SITE_PASSWORD`. Das feste Salt in `.staticrypt.json`
ermöglicht, dass ein gemerktes Passwort auf allen Unterseiten und über mehrere
Deployments hinweg funktioniert.

Nur die Startseite ist ein Login-Einstieg. Nach erfolgreicher Eingabe wird die
Freigabe automatisch für fünf Tage gespeichert. Unterseiten entschlüsseln sich
danach ohne weitere Abfrage. Ein direkter Unterseitenaufruf ohne gültige
Freigabe wird zur Startseite umgeleitet; dort erscheint das einzige
Passwortformular.

Zum Ändern des Passworts:

```bash
gh secret set SITE_PASSWORD --repo HamburgerFH/GKI-course-website
```

Danach den Publish-Workflow erneut ausführen. Das Passwort darf weder in Git
noch in Workflow-Ausgaben stehen.

Der Schutz ist eine Zugangshürde für eine statische Website, aber kein
serverseitiger Zugriffsschutz. Das Quell-Repository, `search.json` und statische
Dateien wie Bilder bleiben öffentlich. Für vertrauliche Inhalte ist ein Hoster
mit serverseitiger Authentifizierung erforderlich.

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
