# Projekt 5: Egge Quest

![image](05-screenshot.png)

Versucht, das abgebildete Programm selbst zu bauen. Der **weiße** Text ist die Ausgabe des Programms. Der **grüne** Text wird vom Benutzer eingegeben.

Die Aufgabe ist sehr umfangreich, deswegen gehen wir in einzelnen Schritten vor:

## Schritt 1:

Erstellt eine Datei `program.py` für euer Programm.

**Game Loop**

Der Kern des Spiels sind zwei Zeilen (`Du siehst...` und `Sprichst...`), die wiederholt werden.
Schreibe den Code für diesen *Game Loop*. Die Funktionen für `ansprechen()`, `ignorieren()` und `umsehen()` folgen dann in den nächsten Schritten.


## Schritt 2:

Wir möchten bei jedem Neustart des Spiels eine Liste zufällig generierter Gegner haben, die mit `umsehen()` angezeigt werden.
Wir verwenden dafür eine Klasse mit der mehrere verschiedene Gegnerobjekte erzeugt werden können.

**Objektorientierte Programmierung**

Die "objektorientierte Programmierung" (OOP) ist ein wichtiges Programmierkonzept.
Wir können mit `class` einen Bauplan erstellen, mit dem man dann eine beliebige Anzahl Objekte generieren kann.
Jedes Objekt (man sagt auch: jede Instanz der Klasse) hat dann die gleichen Attribute und Methoden.

Erstelle eine neue Klasse `Creatures` mit dem folgenden Code:

    class Creature:
        def __init__(self, name, level):
            self.name = name
            self.level = level

        def attack(self):
            pass

        def runaway(self):
            pass

So kannst du ein neues Objekt mit dem Bauplan erzeugen *(ein Objekt der Klasse instanzieren)*:

    Creature("Schüler", 5)

Versuche jetzt eine Liste mit fünf Schülern oder Schülerinnen mit zufälligem Level zu generieren.
Diese sollen im Game Loop angezeigt werden, wenn die Aktion `umsehen()` aufgerufen wird.

Das wechselnde Geschlecht (Schüler/Schülerin) im Beispiel oben kann noch ignoriert werden.
