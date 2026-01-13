"""class Formina:
    def __init__(self, nome_forma: str):
        self.forma = nome_forma
    
biscotto1= Formina("cuoricino")

print(biscotto1.forma)"""

class Persona:
    def __init__(self, nome: str, cognome: str, isEdgemonyPartecipant: bool):
        self.nome = nome
        self.cognome = cognome
        self.isEdgemonyPartecipant = isEdgemonyPartecipant

    def printisEdgemonyPartecipant(self) ->None:
        print(f"{self.nome} {self.cognome}: {self.isEdgemonyPartecipant}")

class Corso:
    def __init__(self, nome):
        self.nome = nome
        self.partecipants= []
    
    def addPartecipant(self, p:Persona) ->bool:
        if p.isEdgemonyPartecipant:
            self.partecipants.append(f"{p.nome} {p.cognome}")
            return True
        else:
            return False

persona1 = Persona("Claudia", "Nigro", True)
persona2 = Persona ("Valeria", "Anjoi", False)

corso1 = Corso("Edgemony")

print (corso1.addPartecipant(persona1)