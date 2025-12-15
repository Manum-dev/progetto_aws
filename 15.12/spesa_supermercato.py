"""
Obiettivo: Creare un programma che simuli una spesa al supermercato. 
Il programma deve gestire una Lista della Spesa (ciò che devi comprare) e un Carrello (ciò che stai prendendo).
Scenario: Siamo nel 2050. I carrelli del supermercato sono robotizzati. 
Per evitare sprechi, il carrello si rifiuta di aprirsi se cerchi di inserire un prodotto che non è nella tua lista della spesa digitale.
Cosa fare:
Analisi e definizione di tutto ciò che serve al nostro programma per funzionare e per terminare
Disegno del flusso (draw.io)
Implementazione del codice

lista spesa di 4 prodotti:
- cipolle,
- latte,
- lattughe,
- birra.

prodotti inseriti dall'utente nel carrello
input --> inserimento prodotti nel carello

if/else: 
- input è vuoto
- lower case
    - controllo che il prodotto sia nella lista della spesa
    - controllo che il prodotto non sia già stato inserito
    - se il prodotto passa il controllo apri il carrello
    - altrimenti il carello non si apre e poi di nuovo fai un nuovo input
- if / else
        - ingredienti sono quattro?
        - controllo con un ciclo quali prodotti mancano
    - altrimenti riproponi input con messaggio dei prodotti che mancano


"""""