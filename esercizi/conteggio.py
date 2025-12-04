# 1. Creare la lista voti
voti = ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]

# 2. Creare un dizionario vuoto
conteggio = {}

# 3. Iterare sulla lista e contare le occorrenze
for voto in voti:
    conteggio[voto] = conteggio.get(voto, 0) + 1

# 4. Stampare il dizionario finale
print("Conteggio voti:", conteggio)
