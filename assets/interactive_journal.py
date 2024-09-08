# Aufgabe 8: Funktionen und Objektorientierung
# Ziel: Das Programm durch Funktionen und Klassenstruktur organisieren.
class Tagebuch:
    def __init__(self):
        self.eintraege = []

    def eintrag_hinzufuegen(self, eintrag):
        self.eintraege.append(eintrag)

    def alle_eintraege_anzeigen(self):
        for eintrag in self.eintraege:
            print(eintrag)
            
# Aufgabe 9: Erweiterung: PinCode Eingabe
# Ziel: Eine PIN-Code-Abfrage integrieren, um den Zugriff auf das Tagebuch zu schützen.
def pin_eingabe():
    pin = "1234"
    versuch = input("Bitte gib deinen 4-stelligen PIN-Code ein: ")

    if versuch == pin:
        print("PIN korrekt. Zugriff gewährt.")
        return True
    else:
        print("Falscher PIN. Zugriff verweigert.")
        return False
    
# Aufgabe 1: Erstes Programm und Print-Befehl
# Ziel: Schreiben Sie ein Programm, das "Willkommen zum interaktiven Tagebuch!" auf dem Bildschirm ausgibt.
def start():
    print("Willkommen zum interaktiven Tagebuch!")

# Aufgabe 2: Verwendung von Strings
# Ziel: Erweitern Sie das Programm, sodass es den Benutzer nach seinem Namen fragt und ihn dann personalisiert begrüßt (z.B. "Hallo, [Name]!"). Nutzen Sie hierfür Variablen.
    name = input("Wie heißt du? ")
    print(f"Hallo, {name}!")

# Aufgabe 3: Datentypen und einfache Berechnungen
# Ziel: Fragen Sie den Benutzer nach seinem Geburtsjahr und berechnen Sie sein aktuelles Alter.
    geburtsjahr = int(input("In welchem Jahr bist du geboren? "))
    aktuelles_jahr = 2024
    alter = aktuelles_jahr - geburtsjahr
    print(f"Du bist {alter} Jahre alt.")

# Aufgabe 4: Entscheidungsstrukturen
# Ziel: Entscheiden Sie, ob der Benutzer volljährig ist, basierend auf dem berechneten Alter. Geben Sie einen entsprechenden Text via Print aus, je nachdem, ob der Benutzer volljährig oder minderjährig ist.   
    if alter >= 18:
        print("Du bist volljährig.")
    else:
        print("Du bist minderjährig.")
    
# Aufgabe 5: Logische Operatoren
# Ziel: Fragen Sie den Benutzer, ob er heute einen Tagebucheintrag machen möchte. Nutzen Sie logische Operatoren, um zu entscheiden, ob das Programm fortgesetzt oder beendet wird.
    eintrag_machen = input("Möchtest du heute einen Tagebucheintrag machen? (ja/nein) ")
    
    if eintrag_machen.lower() == "ja":
        tagebuch = Tagebuch()
# Aufgabe 6: Listen und Schleifen - Vorbereitung
# Ziel: Erstellen Sie eine vordefinierte Liste von Tagebucheinträgen und geben Sie alle Einträge mit einer Schleife aus. 
# Aufgabe 7: Listen und Schleifen - Erweiterung
# Ziel: Erlauben Sie dem Benutzer, weitere Tagebucheinträge zu machen, die der Liste hinzugefügt werden. Verwenden Sie hierfür eine while-Schleife.       
        while True:
            neuer_eintrag = input("Füge einen neuen Tagebucheintrag hinzu (oder 'stop' zum Beenden): ")
            if neuer_eintrag.lower() == "stop":
                break
            tagebuch.eintrag_hinzufuegen(neuer_eintrag)
        
        print("Aktualisierte Tagebucheinträge:")
        tagebuch.alle_eintraege_anzeigen()
    else:
        print("Vielleicht ein anderes Mal.")

if pin_eingabe():
    start()