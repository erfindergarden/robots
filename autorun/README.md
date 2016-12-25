# Autorun

Hier wird erklärt, wie ein Python- oder Bash-Script beim Systemstart automatisch ausgeführt werden kann.

Damit mehrere Programme einfach gleichzeitig gestartet werden können, und um den Autostart einfach zu deaktivieren verwenden wir das Script `autorun.sh` in diesem Ordner. Es startet automatisch alle anderen Programme im Autostart-Ordner, die den richtigen Dateinamen haben. Das wird noch genauer unter Schritt 3 erklärt.


## 1. Anlegen des Autostart-Ordners

Kopiere diesen gesamten Ordner (`autorun`) in dein Home-Verzeichnis (`/home/<benutzername>`, z.B. `/home/pi`).


## 2. rc.local updaten

Jetzt stellen wir ein, dass bei jedem Systemstart das Script `autorun.sh` in diesem Ordner ausgeführt wird.

Bearbeite dazu die Datei `/etc/rc.local` indem du den folgenden Befehl ausführst:

```bash
sudo nano /etc/rc.local
```

Füge unten die folgende Zeile an. Ersetze im Pfad `<benutzername>` mit deinem Benutzernamen. Es sollte sich der Pfad ergeben, an den du vorher den `autorun`-Ordner kopiert hast.

Navigiere dazu mit den Pfeiltasten (du kannst hier keine Maus benutzen) zur letzten Zeile und drücke , dann füge die folgende Zeile ein (*Rechtsklick → Einfügen* oder *CTRL+SHIFT+V*):

```
/home/<benutzermame>/autorun/autorun.sh &&
```

Drücke *CTRL+X*, gefolgt von *ENTER* um zu speichern und den Editor zu schließen.


## 3. Füge Autostart-Programme hinzu

Jetzt kannst du alle Scripte, die du automatisch starten willst ebenfalls in den `autostart`-Order kopieren. Es werden alle Scripte gestartet, die mit einer Ziffer beginnen und mit `.py` oder `.sh` enden, z.B. `01-line-follower.py`.

Im Falle eines Bash-Scripts muss die Datei noch ausführbar gemacht werden mit

```bash
chmod +x <dateiname>.sh
```


## 4. Autostart deaktivieren

Um ein Programm wieder vom Autostart auszuschließen, entferne einfach die Zahl am Anfang oder verändere die Dateiendung, z.B. `line-follower.py` oder `01-line-follower.py_`.
