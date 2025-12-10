from data.services import (
    get_lista_domande_e_risposte, 
    valida_scelta, 
    is_risposta_esatta, 
    get_numero_domanda_corrente, 
    get_counter_aggiornato,
    genera_statistiche,
    calcola_percentuale,
    verifica_superamento,
    recupera_dati_domanda,
    aggiorna_lista_risultati
)
from ui.console import (
    mostra_feedback, 
    mostra_domanda, 
    print_numero_domanda, 
    print_gioco_terminato, 
    genera_feedback, 
    raccogli_risposta,
    mostra_risultati_finali,
    gestisci_menu_fine_gioco
)

def main():
    lista_domande = get_lista_domande_e_risposte("domande.txt")
    risultato_finale: list[dict[str, str | bool]] = []

    counter: int = 0
    totale_domande: int = len(lista_domande)

    while counter <= totale_domande:

        if counter == totale_domande:
            nuovo_indice = gestisci_menu_fine_gioco(counter, totale_domande, risultato_finale)
            if nuovo_indice is None: 
                break
            counter = nuovo_indice
            continue
        
        # recupero dei dati
        dati_correnti = recupera_dati_domanda(lista_domande[counter]) 

        # presentazione domande
        domanda_corrente: int = get_numero_domanda_corrente(counter)
        print_numero_domanda(domanda_corrente, totale_domande)
        mostra_domanda(dati_correnti["domanda"])

        # input dell'utente
        risposta_utente: str = raccogli_risposta()

        feedback: str = ""

        if valida_scelta(risposta_utente):
            esatta: bool = is_risposta_esatta(risposta_utente, dati_correnti["risposta"])
            mostra_feedback(genera_feedback(esatta))

            risultato_corrente = {
                "domanda" : lista_domande[counter],
                "risposta_corretta" : esatta,
                "scelta_utente" : risposta_utente.upper()
            }

            aggiorna_lista_risultati(risultato_finale, risultato_corrente, counter)


        else: 
            mostra_feedback("Inserisci solo la risposta tra le opzioni elencate")

        # navigazione domanda (successiva / precedente)
        if counter > 0:
            input_prev_next: str = input("Digita 'P' per andare alla domanda precedente oppure qualsiasi altro tasto per continuare: ")
            counter = get_counter_aggiornato(counter, input_prev_next)
        else:
            counter += 1 

    # statistiche finali
    print_gioco_terminato()

    statistiche: dict[str, int] = genera_statistiche(risultato_finale)
    esatte = statistiche["risposte_esatte"]
    errate = statistiche["risposte_non_esatte"]
    totale_domande_fatte = esatte + errate
    
    perc = calcola_percentuale(esatte, totale_domande_fatte)
    is_superato = verifica_superamento(perc)
    
    mostra_risultati_finali(esatte, errate, totale_domande_fatte, perc, is_superato)

if __name__ == "__main__": 
    main()