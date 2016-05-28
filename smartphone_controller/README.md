# Fernsteuerung mit Blynk
[Blynk](http://www.blynk.cc/) ist eine Smartphone-App, mit der man User-Interfaces für Arduino, RasPi, etc. bauen kann. Hier eine kurze Anleitung, wie man damit den Roboter fernsteuern kann.


### 1. Blynk am Smartphone installieren
1. Download für [iOS](https://itunes.apple.com/us/app/blynk-control-arduino-raspberry/id808760481?ls=1&mt=8) oder [Android](https://play.google.com/store/apps/details?id=cc.blynk)
2. Registrieren / Anmelden
3. "Create New Project"
4. Bei "Hardware Model" **Raspberry Pi 2/A+/B+** auswählen
4. *Auth-Token* notieren für später oder schicke dir eine E-mail mit dem *Auth-Token*


### 2. Blynk auf dem RasPi einrichten
**Der RasPi muss zur Installation von Blynk und zur Steuerung des Roboters mit dem Internet verbunden sein!**

Die ganze Anleitung findest du auch hier: [https://github.com/blynkkk/blynk-library/blob/master/linux/README.md](https://github.com/blynkkk/blynk-library/blob/master/linux/README.md)

#### A. Voraussetzung: WiringPi installieren

Update: bevor du WiringPi installierst solltest du noch folgende Commands ausführen.

```
sudo apt-get install make
sudo apt-get install build-essential

```

Dann kannst du WiringPi installieren.

```bash
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
cd ..
```
Die ausführliche Anleitung gibt's auch nochmal hier: [http://wiringpi.com/download-and-install/](http://wiringpi.com/download-and-install/)

#### B. Blynk kompilieren

```bash
cd ..
git clone https://github.com/blynkkk/blynk-library.git
cd blynk-library/linux
make clean all target=raspberry
```

#### C. Blynk starten
Hier muss der vorher generierte *Auth-Token* eingesetzt werden, achte darauf, dass du dich nicht 

```bash
sudo ./blynk --token=AUTH-TOKEN
```


### 3. Interface designen in Blynk

1. Erstelle ein Interface mit vier Buttons und benenne sie LV, LH, RV, RH: Für jedes Rad zwei Buttons, einen für vorwärts, einen für rückwärts.
2. Weise jedem Button den entsprechenen digital GPIO Pin nach der unten stehenden Tabelle zu
3. Lass den 'Mode'-Schalter für jeden Button auf 'push'
4. Drücke rechts oben den "Play"-Button
5. Jetzt kannst du mit zwei Fingern deinen Roboter steuern

| Board | Links vorwärts | Links rückwärts | Rechts vorwärts | Rechts rückwärts |
|-------|----------------|-----------------|-----------------|------------------------|
| CamJam EduKit 3|gp8|gp7|gp10|gp9|
| Ryanteck RPi Motor Controller | gp18 | gp17 | gp23 | gp22 |
| Explorer Hat Pro | gp19 | gp20 | gp21 | gp26 |




![Screenshot 1](screenshot-1.png)

### 4. Teste ob deine Räder richtig rum fahren, wenn nicht vertausche einfach die Buttons


### 5. Autostart blynk script

Mache dein blynk script autorun mit [dieser Anleitung](https://github.com/erfindergarden/Roboter-Workshop/blob/master/Autostart.md).