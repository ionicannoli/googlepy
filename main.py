class Catalog:
    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.materii = {}
        self.absente = 0

    def __str__(self):
        return f"Nume: {self.nume}\nPrenume: {self.prenume}\nAbsente: {self.absente}"

    def incrementare_absente(self, nr_absente=1):
        self.absente += nr_absente

    def stergere_absente(self, nr_absente):
        if self.absente >= nr_absente:
            self.absente -= nr_absente

class Extensie1(Catalog):
    def adauga_materie(self, materia, note):
        self.materii[materia] = note

    def afisare_materii(self):
        for materia in self.materii:
            print(materia)

    def afisare_medii(self):
        for materia, note in self.materii.items():
            suma_note = 0
            numar_note = 0
            for nota in note:
                if isinstance(nota, (int, float)):
                    suma_note += nota
                    numar_note += 1
            if numar_note > 0:
                media = suma_note / numar_note
                print(f"Materia: {materia}, Media: {media}")


# Crearea studentilor si efectuarea operatiilor specifice
student1 = Extensie1("Ion", "Roata")
student1.incrementare_absente(3)
student1.stergere_absente(2)

student2 = Extensie1("George", "Cerc")
student2.incrementare_absente(4)
student2.stergere_absente(2)

print(f"Absentele studentului {student1.nume} {student1.prenume}: {student1.absente}")
print(f"Absentele studentului {student2.nume} {student2.prenume}: {student2.absente}")

student1.adauga_materie("Python", [8, 9, 7])
student1.adauga_materie("Romana", [9, 9, 10])

student2.adauga_materie("Python", [7, 6, 8])
student2.adauga_materie("Matematica", [9, 8, 9])

print("Materiile studentului Ion Roata:")
student1.afisare_materii()

print("Materiile studentului George Cerc:")
student2.afisare_materii()

print("Mediile studentului Ion Roata:")
student1.afisare_medii()

print("Mediile studentului George Cerc:")
student2.afisare_medii()
