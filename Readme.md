# Heizungssteuerung mit ESPHome - Generierung der yaml Konfigurationsdatei

Die Fußbodenheizung besteht aus mehreren Verteilerkreisen, die - eventuell in
Gruppen zusammengefaßt - mit dem "Climate PID Regler" aus ESPHome geregelt werden.
Im oberen Stockwerk sind 7 Verteilerkreise vorhanden; im unteren sind es 8.

Um Fehler und Aufwand bei der Erstellung überwiegend identischer Konfigurationselemente (yaml Segmente) zu vermeinden, werden die regelungsspezifischen yaml-Konfigurationselemente automatisch generiert und über den ```packages```-Mechanismus in die ESPHome Konfiguration eingebunden (via GitHub).

Für die Generierung wird Python und ein Jinja2 Template verendet.

## Links

- [ESPHome - Packages](https://esphome.io/components/packages.html)
- [Medium - Automatic yaml Generation with Jinja2](https://medium.com/@muazzem.mamun/automating-yaml-file-generation-with-jinja2-b42bfb8bacaa)
- [Jinja2 - Whitespace control](https://jinja.palletsprojects.com/en/stable/templates/#whitespace-control)
- [yaml spec - merge](https://yaml.org/type/merge.html)
- [blog - Wiederverwertbare ESPHome Codeblöcke in eigene yaml Datei auslagern.](https://smarthomeyourself.de/wiki/esphome/wiederverwertbare-esphome-codebloecke-in-eigene-yaml-datei-auslagern/)

## Development Environment

### Python Setup

```shell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Install Python Modules

```shell
pip install jinja2
```

### Script Execution

```shell
python ./generate.py
```

## Jinja2 Template

## ESPHome Configuration

Snippet in ESPHome's yaml configuration

```yaml
packages:
  heizung:
    url: https://github.com/cvstebut/heizung-automation
    file: heating.yaml
    refresh: 1s
```

Notes

- During development, the configuration should always use the downloaded template from github. Thats why the ```refresh``` interval is kept very low.