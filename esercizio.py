def misura_temperatura(gradi: int)->int:
    if gradi<10:
        return "very cold"
    else:
       return "è alta"

temperatura = int(input("Inserisci la temperatura: "))

# Stampa il risultato usando return
print(misura_temperatura(temperatura))
