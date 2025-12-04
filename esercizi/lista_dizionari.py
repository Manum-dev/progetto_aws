# 1. Creare la lista di dizionari prodotti
prodotti: list[dict[str, str | int | float]]= [
    {"nome": "Laptop", "prezzo": 899.99, "quantita": 5},
    {"nome": "Mouse", "prezzo": 25.50, "quantita": 50},
    {"nome": "Tastiera", "prezzo": 75.00, "quantita": 30},
    {"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
]

# 2. Stampare prodotti con prezzo > 100
print("Prodotti con prezzo superiore a 100€:")
for prodotto in prodotti:
    if prodotto["prezzo"] > 100:
        print(f"{prodotto['nome']}: €{prodotto['prezzo']}")

# 3. Calcolare il valore totale dell'inventario
valore_totale = 0
for prodotto in prodotti:
    valore_prodotto = prodotto["prezzo"] * prodotto["quantita"]
    valore_totale += valore_prodotto

print(f"\nValore totale inventario: €{valore_totale:.2f}")