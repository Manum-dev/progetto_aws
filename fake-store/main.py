

from api import (
    
    BASE_URL, 
    get_lista_prodotti,
    get_prodotto,
    create_product,
    create_category,
    post_data,
    get_data,
    product_model,
    product_list_model,
    get_data,
    json
)

from ui import (
    print_prodotto, 
    print_product_list, 
    invia_prodotto_al_server,
) 

from funzioni import (
    mostra_categorie,
    richiedi_input,
    richiedi_immagini,
    crea_prodotto_interattivo,
    get_prodotto,
    conferma_invio)

def main() -> None:
    try:
      print_product_list(product_list_model(get_lista_prodotti(BASE_URL)))
        #id = input("Inserisci l'id del prdotto da visualizzare:")
        # product= product_model(get_prodotto(f"{BASE_URL}/{id}"))
        #print_prodotto(product)
        # print_prodotto(create_product(BASE_URL, prod))
    
 
    
    except ConnectionError as e:
        print(f"Errore di connessione: {e}")
    
    except ValueError as e:
        print(f"Errore: {e}")
    
    except KeyError as e:
        print(f"Errore nei dati: {e}")
    
    except TypeError as e:
        print(f"Errore di tipo: {e}")
    
    except KeyboardInterrupt:
        print("\nOperazione interrotta dall'utente.")
    
    except Exception as e:
        print(f"Errore imprevisto: {type(e).__name__} - {e}")

def main():
    print("\n" + "="*50)
    print("  INSERIMENTO PRODOTTO")
    print("="*50 + "\n")
    
    print("Categorie disponibili:")
    print("  1 = Clothes")
    print("  2 = Electronics")
    print("  3 = Furniture")
    print("  4 = Shoes")
    print("  5 = Others\n")
    
    # Input dati
    titolo = input("Titolo: ")
    prezzo = float(input("Prezzo (€): "))
    descrizione = input("Descrizione: ")
    categoria_id = int(input("ID Categoria (1-5): "))
    url_immagine = input("URL Immagine (opzionale, premi INVIO per skip): ").strip()
    
    # Crea prodotto
    prodotto = {
        "title": titolo,
        "price": prezzo,
        "description": descrizione,
        "categoryId": categoria_id,
        "images": [url_immagine] if url_immagine else ["https://i.imgur.com/ZANVnHE.jpeg"]
    }
    
    # Mostra riepilogo
    print("\n" + "-"*50)
    print("RIEPILOGO:")
    print(json.dumps(prodotto, indent=2, ensure_ascii=False))
    print("-"*50)
    
    # Conferma
    conferma = input("\nConfermi? (s/n): ").lower()
    
    if conferma in ['s', 'si', 'sì']:
        try:
            print("\nInvio in corso...")
            risultato = create_product(BASE_URL, prodotto)
            
            print("\n✅ PRODOTTO CREATO!")
            print(f"ID: {risultato['id']}")
            print(f"Titolo: {risultato['title']}")
            print(f"Prezzo: €{risultato['price']}")
        except Exception as e:
            print(f"\n❌ Errore HTTP {e.response.status_code}")
        except Exception as e:
            print(f"\n❌ Errore: {e}")
    else:
        print("\n❌ Annullato")


if __name__ == "__main__":
    main()
