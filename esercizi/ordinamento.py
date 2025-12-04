prezzi_lista: float = [45.5, 12.0, 78.3, 23.1, 56.7]
print("Prezzi originali", prezzi_lista)
numeri_ordinati = sorted(prezzi_lista)
print("Prezzi ordinati", numeri_ordinati)
print("Minimo", min(prezzi_lista))
print("Massimo",max(prezzi_lista))

check_item = 23.1
controllo: bool = check_item in prezzi_lista
print(check_item, controllo)

X=prezzi_lista
for X in prezzi_lista:
     if X > 50:
          print("Prezzi>50", X)