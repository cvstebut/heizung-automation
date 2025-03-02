# Heizungssteuerung mit ESPHome - Generierung der yaml Konfigurationsdatei

Die Fußbodenheizung besteht aus mehreren Verteilerkreisen, die - eventuell in
Gruppen zusammengefaßt - mit dem "Climate PID Regler" aus ESPHome geregelt werden.
Im oberen Stockwerk sind 7 Verteilerkreise vorhanden; im unteren sind es 8.

Um Fehler und Aufwand bei der Erstellung überwiegend identischer Konfigurationselemente (yaml Segmente) zu vermeinden, werden die regelungsspezifischen yaml-Konfigurationselemente automatisch generiert und über den ```packages```-Mechanismus in die ESPHome Konfiguration eingebunden (via GitHub).

Für die Generierung wird Python und ein Jinja2 Template verendet.

## Python Umgebung

## Jinja2 Template

## Ablauf bei der Programmierung des ESP32 mittels ESPHome
