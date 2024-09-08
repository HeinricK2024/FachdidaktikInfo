# Definition der Klasse 'Auto' mit Attributen und einer Methode
class Auto:
    # Konstruktor-Methode zum Initialisieren der Attribute
    def __init__(self, marke, modell):
        self.marke = marke  # Attribut 'marke' für die Klasse 'Auto'
        self.modell = modell  # Attribut 'modell' für die Klasse 'Auto'

    # Methode, um Informationen über das Auto auszugeben
    def zeige_info(self):
        print("Auto Marke:", self.marke)  # Zugriff auf das Attribut 'marke'
        print("Auto Modell:", self.modell)  # Zugriff auf das Attribut 'modell'

# Erstellung eines Auto-Objekts mit spezifischen Attributwerten
mein_auto = Auto("Toyota", "Corolla")

# Aufruf der Methode 'zeige_info' für das Objekt 'mein_auto'
mein_auto.zeige_info()


# Aufgaben zur Objektorientierten Programmierung in Python
# Aufgabe 1: Grundlegende Klasse erstellen
# Erstellen Sie eine Klasse namens Person mit zwei Attributen: name und alter. Initialisieren Sie diese Attribute in der __init__-Methode.
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter


# Aufgabe 2: Methode hinzufügen
# Erweitern Sie die Klasse Person um eine Methode namens zeige_info, die den Namen und das Alter der Person ausgibt.
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def zeige_info(self):
        print(f"Name: {self.name}, Alter: {self.alter}")


# Aufgabe 3: Objekt erstellen
# Erstellen Sie ein Objekt der Klasse Person mit Ihrem Namen und Ihrem Alter als Attribute. Rufen Sie anschließend die Methode zeige_info für dieses Objekt auf.
# Erstellen eines Objekts der Klasse Person
person1 = Person("Max Mustermann", 30)

# Aufruf der Methode zeige_info
person1.zeige_info()

# Aufgabe 4: Liste von Objekten
# Erstellen Sie eine Liste mit drei verschiedenen Personenobjekten. Gehen Sie durch die Liste und rufen Sie für jedes Objekt die Methode zeige_info auf.
# Erstellen von drei verschiedenen Personenobjekten
person1 = Person("Max Mustermann", 30)
person2 = Person("Erika Mustermann", 25)
person3 = Person("Hans Müller", 40)

# Hinzufügen der Personenobjekte zu einer Liste
personen_liste = [person1, person2, person3]

# Schleife, um durch die Liste zu iterieren und die zeige_info Methode aufzurufen
for person in personen_liste:
    person.zeige_info()

# Um die Liste zu erstellen, definieren Sie zunächst drei Instanzen der Klasse Person mit unterschiedlichen Werten für name und alter. Fügen Sie diese Instanzen dann einer Liste hinzu. Nutzen Sie eine Schleife, um durch die Liste zu iterieren und für jedes Objekt die zeige_info-Methode aufzurufen, um die Eigenschaften jeder Person auszugeben.

# Aufgabe 5: Attribute ändern
# Wählen Sie eines der Objekte aus Ihrer Personenliste aus und ändern Sie das Alter dieser Person. Geben Sie anschließend die aktualisierten Informationen aus.
# Ändern des Alters eines Objekts in der Liste
personen_liste[1].alter = 26  # Erika Mustermann wird ein Jahr älter

# Aktualisierte Informationen ausgeben
personen_liste[1].zeige_info()

# Aufgabe 6: Erstellung und Verwendung einer neuen Klasse
# Definieren Sie eine neue Klasse namens Buch. Diese Klasse soll zwei Attribute haben: titel und autor.
# Fügen Sie der Klasse Buch eine Methode zeige_info hinzu, die Titel und Autor des Buches ausgibt.
# Erstellen Sie drei Objekte der Klasse Buch mit unterschiedlichen Titeln und Autoren.
# Speichern Sie diese Buchobjekte in einer Liste namens buecherListe.
# Gehen Sie mit einer Schleife durch die buecherListe und rufen Sie für jedes Buchobjekt die Methode zeige_info auf.
# Ändern Sie den Autor eines der Bücher in der Liste und geben Sie die aktualisierten Informationen aus.
class Buch:
    def __init__(self, titel, autor):
        self.titel = titel
        self.autor = autor
    
    def zeige_info(self):
        print(f"Buchtitel: {self.titel}, Autor: {self.autor}")

# Erstellen von drei Buchobjekten
buch1 = Buch("Im Westen nichts Neues", "Erich Maria Remarque")
buch2 = Buch("Das Kapital", "Karl Marx")
buch3 = Buch("Andorra", "Max Frisch")

# Hinzufügen der Buchobjekte zu einer Liste
buecher_liste = [buch1, buch2, buch3]

# Schleife, um durch die Liste zu iterieren und die zeige_info Methode aufzurufen
for buch in buecher_liste:
    buch.zeige_info()

# Ändern des Autors eines der Bücher
buecher_liste[2].autor = "Max Mustermann"

# Aktualisierte Informationen ausgeben
buecher_liste[2].zeige_info()
