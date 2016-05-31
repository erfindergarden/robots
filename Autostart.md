# Autostart

Es gibt mehrere Möglichkeiten, ein Programm automatisch beim Einschalten des Raspberry Pi zu starten.

In unserem Beispiel wollen wir das Python-Script unter `/home/pi/robot.py` automatisch ausführen, sobald der Pi gestartet wird.

## Methode 1: Crontab

Cron ist ein Linux-Bestandteil, der es erlaubt, regelmäßige Tasks auszuführen. Man kann einen Zeitpunkt und einen Befehl angeben. Der Befehl wird dann immer zum angegebenen Zeitpunkt ausgeführt.

Ein Möglicher Zeitpunkt ist `@reboot`, das heißt bei jedem Start.

### Crontab öffnen

Zuerst öffnen wir die Cron-Konfiguration:

```bash
sudo crontab -e
```

### Zeile einfügen

Dann fügen wir am Ende eine Zeile an. Das bedeutet, blynk erst eine Minute nach dem reboot gestartet wird. 

insert code mit  ... 

```
i
```

für den Handycontroller ... 

```cron
@reboot sleep 1 && /home/deinbenutzermame/blynk-library/linux/blynk --token=XXXXXXXXXXXXX
```

oder für ein anderes Porgramm ... 

```cron
@reboot python /home/Roboter-WorkShop/deinprogramm.py
```


und schließe und speichere. 

````
:wq!
````


## Methode 2: rc.local

Editiere rc.local

```
sudo nano  /etc/rc.local
```

```
python /home/usr/deinprogramm.py &
```


## Methode 3: init.d

Die typische Methode, wie ein Linux-System Dienste beim Systemstart startet, geht über *init-Scripte*. Das sind Scripts, die im Ordner `/etc/init.d/` abgelegt sind und auf verschiendene Kommandos hören, z.B. `start` oder `stop`.

### Init-Script anlegen

Wir legen für unser Programm eine soche Datei an. Speichere den folgenden Inhalt in eine Datei unter `/etc/init.d/robot`

```bash
#!/bin/sh
### BEGIN INIT INFO
# Provides:			 robot
# Required-Start:    
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Set off our robot on boot.
# Description:       So he can save the world while we hack.
### END INIT INFO
 
case "$1" in
    start)
        # Befehl zum Starten unseres Scripts
        python /home/pi/robot.py &
        ;;
    stop)
        # (Optional) Befehl zum Stoppen unseres Scripts
        killall python & # Achtung! Beendet alle Python-Programme!
        ;;
    restart)
        # (Optional) Befehl zum Neustarten
        ;;
esac
 
exit 0
```

### Autostart einrichten

Jetzt müssen wir unser Init-Script noch *ausführbar* machen, und dem System mitteilen, dass es beim Einschalten gestartet werden soll:

```bash
sudo chmod +x /etc/init.d/robot  # ausführbar machen
sudo update-rc.d robot defaults  # automatischen start aktivieren
```

Um den Autostart des Scripts wieder zu deaktivieren, gib den folgenden Befehl ein:

```bash
sudo update-rc.d robot disable  # autostart deaktivieren
```


