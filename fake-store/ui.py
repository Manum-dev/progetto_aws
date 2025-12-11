def print_prodotto(product: dict[str, any]) -> None:
    """Stampa i dettagli completi di un prodotto"""
    print("*" * 30)
    print(f"PRODOTTO")
    print("*" * 30)
    print(f"ID: {product['id']}")
    print(f"Titolo: {product['title']}")
    print(f"Category: {product['category']}")
    print(f"PRICE: {product['price']}")
    print(f"DESCRIPTION: {product['description']}")


def print_products_list(products: list[dict[str, any]]) -> None:
    """Stampa la lista di prodotti mostrando solo ID e titolo"""
    print("=" * 50)
    print("LISTA PRODOTTI")
    print("=" * 50)
    for product in products:
        print(f"ID: {product['id']:3} - {product['title']}")
    print("=" * 50)
    print(f"Totale prodotti: {len(products)}")


def show_menu() -> str:
    """Mostra il menu principale e restituisce la scelta dell'utente"""
    print("\n1. Visualizza tutti i prodotti")
    print("2. Cerca prodotto per ID")
    return input("\nScegli un'opzione (1 o 2): ")


def get_product_id_input() -> int:
    """Richiede e valida l'input dell'ID prodotto"""
    id_input = input("\nInserisci l'id del prodotto da visualizzare: ")
    
    if not id_input.strip():
        raise ValueError("L'ID non può essere vuoto!")
    
    product_id = int(id_input)
    if product_id < 0:
        raise ValueError("L'ID deve essere un numero positivo!")
    
    return product_id