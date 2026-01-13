import uuid
from task import Task

class Project:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4()) 
        self.name = name
        self.task_list = []

    def add_task(self, title: str, description: str = "") -> Task:
        """Crea una task, la aggiunge e conferma l'operazione"""
        new_task = Task(title, description)
        self.task_list.append(new_task)
        print("Operazione completata: Task aggiunta con successo.")
        return new_task

    def set_project_name(self, new_name: str) -> None:
        """Cambia il nome e conferma l'operazione"""
        self.name = new_name
        print(f"Operazione completata: Progetto rinominato in '{new_name}'.")

    def get_project_id(self) -> str:
        return self.id
    
    def get_tasks_lenght(self) -> int:
        return len(self.task_list)

    def get_project_name(self) -> str:
        return self.name