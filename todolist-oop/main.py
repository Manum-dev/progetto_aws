from todolist import Todolist
from project import Project
from menu import Menu
from project import Project

def update_project_name(todolist: Todolist):
    """
    This function contains al the logic related to the update project name process
    """
    print("="*20)
    print("Lista dei progetti:")
    print("="*20)
    todolist.get_projects()

    id_progetto = input("Inserisci l'id del progetto da aggiornare: ")

    while True:

        new_name = input("Iserisci il nuovo nome del progetto: ")

        if todolist.is_project_name_already_exists(new_name):
            print(f"Un oggetto con il nome {new_name} esiste già")
            continue

        todolist.update_project_name(id_progetto, new_name)
        print(f"Update eseguito con successo per l'oggetto {id_progetto}")
        break

def main():
    todolist = Todolist()

    menu = Menu()

    while True: 

        menu.printMenu()

        i = input("Seleziona l'operazione da eseguire: ")

        match i:
            case "1": 
                print("Hai scelto aggiungi progetto")
                print("="*30)
                project_name = input("Inserisci nome del progetto: ")
                
                if todolist.is_project_name_already_exists(project_name):
                    print(f"Un oggetto con il nome {project_name} esiste già")
                    continue

                new_project = Project(project_name)
                todolist.add_project(new_project)
                print(f"il numero di progetti è: {todolist.get_projects_lenght()}")

                continue
            case "2": 
                print("Aggiungi task")
                continue
            case "3":
                print("Aggiungi tag")
                continue
            case "4":
                print("="*20)
                print("Lista dei progetti:")
                print("="*20)
                print(todolist.get_projects())

            case "5": 
                print("Lista i task")
                continue
            case "6":
                print("Lista i tags")
            case "7": 
                update_project_name(todolist)
                continue

            case "8":
                break
            case _: 
                print("Inserisci il valore corretto")
                continue
            case "9":
                break
            case _: 
                print("Inserisci il tag corretto")
                continue




if __name__ == "__main__":
    main()
from todolist import Todolist
from project import Project
from menu import Menu
from project import Project

def update_project_name(todolist: Todolist):
    """
    This function contains al the logic related to the update project name process
    """
    print("="*20)
    print("Lista dei progetti:")
    print("="*20)
    todolist.get_projects()

    id_progetto = input("Inserisci l'id del progetto da aggiornare: ")

    while True:

        new_name = input("Iserisci il nuovo nome del progetto: ")

        if todolist.is_project_name_already_exists(new_name):
            print(f"Un oggetto con il nome {new_name} esiste già")
            continue

        todolist.update_project_name(id_progetto, new_name)
        print(f"Update eseguito con successo per l'oggetto {id_progetto}")
        break

def main():
    todolist = Todolist()

    menu = Menu()

    while True: 

        menu.printMenu()

        i = input("Seleziona l'operazione da eseguire: ")

        match i:
            case "1": 
                print("Hai scelto aggiungi progetto")
                print("="*30)
                project_name = input("Inserisci nome del progetto: ")
                
                if todolist.is_project_name_already_exists(project_name):
                    print(f"Un oggetto con il nome {project_name} esiste già")
                    continue

                new_project = Project(project_name)
                todolist.add_project(new_project)
                print(f"il numero di progetti è: {todolist.get_projects_lenght()}")

                continue
            case "2": 
                print("Aggiungi task")
                continue
            case "3":
                print("Aggiungi tag")
                continue
            case "4":
                print("="*20)
                print("Lista dei progetti:")
                print("="*20)
                print(todolist.get_projects())

            case "5": 
                print("Lista i task")
                continue
            case "6":
                print("Lista i tags")
            case "7": 
                update_project_name(todolist)
                continue

            case "8":
                break
            case _: 
                print("Inserisci il valore corretto")
                continue



if __name__ == "__main__":
    main()