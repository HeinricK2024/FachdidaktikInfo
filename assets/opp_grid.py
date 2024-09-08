# Aufgabe 1: Einzelne Auto-Bewegungen im Koordinatensystem
# Schreiben Sie einen Python-Code, in dem ein Auto von der Startposition (0,0) zuerst zu (5,0), dann zu (5,5), anschließend zu (0,5) und schließlich zurück zu (0,0) fährt. Nach jeder Bewegung soll die aktuelle Position des Autos ausgegeben werden.
class Car:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell
        self.x_position = 0
        self.y_position = 0
    
    def drive(self, x, y):
        self.x_position += x
        self.y_position += y
        print(f"{self.marke} {self.modell} ist jetzt bei Position ({self.x_position}, {self.y_position}).")

# Erzeugen einer Instanz der Car-Klasse für das erste Auto
auto1 = Car("Toyota", "Corolla")

# Bewegen des Autos zu den verschiedenen Positionen
auto1.drive(5, 0)  # Bewegt das Auto zu (5, 0)
auto1.drive(0, 5)  # Bewegt das Auto zu (5, 5)
auto1.drive(-5, 0) # Bewegt das Auto zu (0, 5)
auto1.drive(0, -5) # Bewegt das Auto zurück zu (0, 0)


# Aufgabe 2: Bewegung eines zweiten Autos im Koordinatensystem
# Ergänzen Sie den Code aus Aufgabe 1, indem Sie ein zweites Auto hinzufügen, das eine andere Route abfährt. Dieses Auto soll von (1,1) starten und dann einzeln zu den Punkten (1,4), (4,4), (4,1) und schließlich zurück zu (1,1) fahren. Jede Bewegung soll einzeln angegeben werden, um das Verständnis zu erleichtern.
class Car:
    def __init__(self, marke, modell, start_x=0, start_y=0):
        self.marke = marke
        self.modell = modell
        self.x_position = start_x
        self.y_position = start_y
    
    def drive(self, x, y):
        self.x_position += x
        self.y_position += y
        print(f"{self.marke} {self.modell} ist jetzt bei Position ({self.x_position}, {self.y_position}).")

# Erzeugen einer Instanz der Car-Klasse für das erste Auto
auto1 = Car("Toyota", "Corolla")

# Bewegen des ersten Autos zu den verschiedenen Positionen
auto1.drive(5, 0)  # Bewegt das Auto zu (5, 0)
auto1.drive(0, 5)  # Bewegt das Auto zu (5, 5)
auto1.drive(-5, 0) # Bewegt das Auto zu (0, 5)
auto1.drive(0, -5) # Bewegt das Auto zurück zu (0, 0)

# Erzeugen einer Instanz der Car-Klasse für das zweite Auto, das bei (1, 1) startet
auto2 = Car("Honda", "Civic", start_x=1, start_y=1)

# Bewegen des zweiten Autos zu den verschiedenen Positionen
auto2.drive(0, 3)  # Bewegt das Auto zu (1, 4)
auto2.drive(3, 0)  # Bewegt das Auto zu (4, 4)
auto2.drive(0, -3) # Bewegt das Auto zu (4, 1)
auto2.drive(-3, 0) # Bewegt das Auto zurück zu (1, 1)
