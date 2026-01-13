from project import Project

class Todolist:
    def __init__(self):
        self.projects: list[Project] = []

    def add_project(self, project: Project) -> None:
        """Add single project to a to project list"""
        self.projects.append(project)
    
    def get_projects_lenght(self) -> int:
        """Return the number of projects inside the project list"""
        return len(self.projects)

    def get_projects(self):
        """Return the project formatted with <id - project name>"""
        for p in self.projects:
            print(f"{p.id} - {p.name}")

    def is_project_name_already_exists(self, new_name: str) -> bool:
        """Return True if project name already exists, instead return False""" 
        for p in self.projects:
            if p.get_project_name() == new_name.strip():
                return True
            else:
                return False

    def get_project_by_id(self, id: str) -> Project | None:
        return next((project for project in self.projects if project.get_project_id() == id), None)

        
    def update_project_name(self, id: str, new_name: str) -> None:
        """Update the project name based on his id"""
        project = self.get_project_by_id(id)

        if project is None:
            print("Il projetto con questo ID non esiste.")

        project.set_project_name(new_name)
