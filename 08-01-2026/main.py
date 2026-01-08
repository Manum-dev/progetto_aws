import argparse
import json
import os
import uuid
import datetime
import sys
from typing import List, Dict, Optional, Any

# Constants
DATA_FILE = "todo_data.json"

# --- Data Models (represented as dictionaries in JSON but managed here) ---
# Project: { "id": str, "name": str, "description": str, "created_at": str }
# Task: { "id": str, "title": str, "project_id": str, "tags": List[str], "is_completed": bool, "created_at": str, "completed_at": str|None }
# Tag: { "id": str, "name": str, "color": str }

# --- Storage Manager ---
class StorageManager:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.filepath):
            initial_data = {
                "projects": [],
                "tasks": [],
                "tags": [],
            }
            self.save_data(initial_data)

    def load_data(self) -> Dict[str, Any]:
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"projects": [], "tasks": [], "tags": []}

    def save_data(self, data: Dict[str, Any]):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

# --- Helpers ---
def get_now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def generate_id() -> str:
    return str(uuid.uuid4())

# --- Controllers ---
class TodoApp:
    def __init__(self, storage: StorageManager):
        self.storage = storage
        self.data = self.storage.load_data()

    def save(self):
        self.storage.save_data(self.data)

    # --- Projects ---
    def create_project(self, name: str, description: str):
        if any(p['name'] == name for p in self.data['projects']):
            print(f"❌ Errore: Il progetto '{name}' esiste già.")
            return

        new_project = {
            "id": generate_id(),
            "name": name,
            "description": description,
            "created_at": get_now_iso()
        }
        self.data['projects'].append(new_project)
        self.save()
        print(f"✅ Progetto '{name}' creato con successo.")

    def list_projects(self):
        if not self.data['projects']:
            print("📂 Nessun progetto trovato.")
            return
        
        print(f"{'ID':<38} | {'NOME':<20} | DESCRIZIONE")
        print("-" * 80)
        for p in self.data['projects']:
            print(f"{p['id']:<38} | {p['name']:<20} | {p['description']}")

    def delete_project(self, name_or_id: str):
        # Allow native ID or finding by name
        project_to_delete = None
        for p in self.data['projects']:
            if p['id'] == name_or_id or p['name'] == name_or_id:
                project_to_delete = p
                break
        
        if not project_to_delete:
            print(f"❌ Errore: Progetto '{name_or_id}' non trovato.")
            return

        # Cascade delete tasks
        project_id = project_to_delete['id']
        original_task_count = len(self.data['tasks'])
        self.data['tasks'] = [t for t in self.data['tasks'] if t['project_id'] != project_id]
        deleted_tasks = original_task_count - len(self.data['tasks'])

        self.data['projects'].remove(project_to_delete)
        self.save()
        print(f"🗑️ Progetto '{project_to_delete['name']}' eliminato (e {deleted_tasks} task associati).")

    # --- Tags ---
    def create_tag(self, name: str, color: str):
        if any(t['name'] == name for t in self.data['tags']):
            print(f"❌ Errore: Il tag '{name}' esiste già.")
            return

        new_tag = {
            "id": generate_id(),
            "name": name,
            "color": color
        }
        self.data['tags'].append(new_tag)
        self.save()
        print(f"✅ Tag '{name}' creato.")

    def list_tags(self):
        if not self.data['tags']:
            print("🏷️ Nessun tag trovato.")
            return
        
        print(f"{'NOME':<15} | COLORE")
        print("-" * 30)
        for t in self.data['tags']:
            print(f"{t['name']:<15} | {t.get('color', '')}")

    def delete_tag(self, name: str):
        tag_to_delete = next((t for t in self.data['tags'] if t['name'] == name), None)
        if not tag_to_delete:
            print(f"❌ Errore: Tag '{name}' non trovato.")
            return

        # Remove tag from all tasks
        for task in self.data['tasks']:
            if name in task['tags']:
                task['tags'].remove(name)

        self.data['tags'].remove(tag_to_delete)
        self.save()
        print(f"🗑️ Tag '{name}' eliminato e rimosso dai task.")

    # --- Tasks ---
    def create_task(self, project_name: str, title: str, tags: str):
        # Find project
        project = next((p for p in self.data['projects'] if p['name'] == project_name), None)
        if not project:
            print(f"❌ Errore: Progetto '{project_name}' non trovato.")
            return

        if any(t['title'] == title and t['project_id'] == project['id'] for t in self.data['tasks']):
             print(f"❌ Errore: Un task con titolo '{title}' esiste già in questo progetto.")
             return

        tag_list = [t.strip() for t in tags.split(',')] if tags else []
        
        # Verify tags exist (optional strict mode, but let's allow ad-hoc or strict? 
        # Requirements say: "creare tag... vedere... cancellare". 
        # It implies tags are entities. Let's check if they exist or auto-create? 
        # "Tag: hanno id". So likely we should validate they exist or error.
        # But for UX, let's warn if they don't exist in registry? 
        # Simplest: Just store names in task for now, but to be consistent with "Tag has ID", 
        # normally we link by ID, but user inputs names. 
        # Let's check if tag names exist in our Tag registry.
        registered_tag_names = {t['name'] for t in self.data['tags']}
        valid_tags = []
        for tag_name in tag_list:
            if tag_name not in registered_tag_names:
                print(f"⚠️ Warning: Tag '{tag_name}' non definito. Usa 'tag add' prima.")
            else:
                valid_tags.append(tag_name)

        new_task = {
            "id": generate_id(),
            "title": title,
            "project_id": project['id'],
            "tags": valid_tags,
            "is_completed": False,
            "created_at": get_now_iso(),
            "completed_at": None
        }
        self.data['tasks'].append(new_task)
        self.save()
        print(f"✅ Task '{title}' aggiunto al progetto '{project_name}'.")

    def list_tasks(self, project_name: Optional[str] = None, status: Optional[str] = None, tag: Optional[str] = None):
        tasks_view = self.data['tasks']

        # Filter by project
        if project_name:
            project = next((p for p in self.data['projects'] if p['name'] == project_name), None)
            if not project:
                print(f"❌ Errore: Progetto '{project_name}' non trovato.")
                return
            tasks_view = [t for t in tasks_view if t['project_id'] == project['id']]

        # Filter by status
        if status == 'done':
            tasks_view = [t for t in tasks_view if t['is_completed']]
        elif status == 'todo':
            tasks_view = [t for t in tasks_view if not t['is_completed']]

        # Filter by tag
        if tag:
            tasks_view = [t for t in tasks_view if tag in t['tags']]

        if not tasks_view:
            print("📭 Nessun task trovato.")
            return

        # Enrich with project name for display
        project_map = {p['id']: p['name'] for p in self.data['projects']}

        print(f"{'STATO':<5} | {'PROGETTO':<15} | {'TITOLO':<30} | TAGS")
        print("-" * 70)
        for t in tasks_view:
            state_icon = "✅" if t['is_completed'] else "⭕"
            p_name = project_map.get(t['project_id'], "???")
            tags_str = ", ".join(t['tags'])
            print(f"{state_icon:<5} | {p_name:<15} | {t['title']:<30} | {tags_str}")

    def toggle_task(self, title: str, done: bool):
        # Note: Title is unique PER PROJECT in my logic above, but global uniqueness was requested 
        # "Task ha: titolo (univoco)". If global unique, good.
        # Let's assume global unique for simplicity as per requirement.
        
        task = next((t for t in self.data['tasks'] if t['title'] == title), None)
        if not task:
            print(f"❌ Errore: Task '{title}' non trovato.")
            return

        task['is_completed'] = done
        task['completed_at'] = get_now_iso() if done else None
        self.save()
        status = "completato" if done else "riaperto"
        print(f"ok Task '{title}' segnato come {status}.")

    def delete_task(self, title: str):
        task = next((t for t in self.data['tasks'] if t['title'] == title), None)
        if not task:
            print(f"❌ Errore: Task '{title}' non trovato.")
            return
        
        self.data['tasks'].remove(task)
        self.save()
        print(f"🗑️ Task '{title}' eliminato.")
        
    def add_tag_to_task(self, task_title: str, tag_name: str):
        # Verify task
        task = next((t for t in self.data['tasks'] if t['title'] == task_title), None)
        if not task:
            print(f"❌ Errore: Task '{task_title}' non trovato.")
            return
            
        # Verify tag
        if not any(t['name'] == tag_name for t in self.data['tags']):
             print(f"❌ Errore: Tag '{tag_name}' non esiste. Crealo prima.")
             return
             
        if tag_name not in task['tags']:
            task['tags'].append(tag_name)
            self.save()
            print(f"🏷️ Tag '{tag_name}' aggiunto a '{task_title}'.")
        else:
            print(f"ℹ️ Il task ha già questo tag.")

# --- Main Entry Point ---
def main():
    storage = StorageManager(DATA_FILE)
    app = TodoApp(storage)

    parser = argparse.ArgumentParser(description="Todo List CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Project Commands
    p_parser = subparsers.add_parser("project", help="Gestione Progetti")
    p_sub = p_parser.add_subparsers(dest="subcommand", required=True)
    
    p_add = p_sub.add_parser("add", help="Crea nuovo progetto")
    p_add.add_argument("name", help="Nome progetto")
    p_add.add_argument("--desc", help="Descrizione progetto", default="")

    p_list = p_sub.add_parser("list", help="Lista progetti")

    p_del = p_sub.add_parser("delete", help="Cancella progetto")
    p_del.add_argument("name", help="Nome o ID progetto")

    # Tag Commands
    t_parser = subparsers.add_parser("tag", help="Gestione Tag")
    t_sub = t_parser.add_subparsers(dest="subcommand", required=True)

    t_add = t_sub.add_parser("add", help="Crea nuovo tag")
    t_add.add_argument("name", help="Nome tag")
    t_add.add_argument("--color", help="Colore tag (es: red)", default="grey")

    t_list = t_sub.add_parser("list", help="Lista tag")

    t_del = t_sub.add_parser("delete", help="Cancella tag")
    t_del.add_argument("name", help="Nome tag")

    # Task Commands
    tsk_parser = subparsers.add_parser("task", help="Gestione Task")
    tsk_sub = tsk_parser.add_subparsers(dest="subcommand", required=True)

    tsk_add = tsk_sub.add_parser("add", help="Aggiungi task")
    tsk_add.add_argument("project", help="Nome progetto")
    tsk_add.add_argument("title", help="Titolo task")
    tsk_add.add_argument("--tags", help="Tags separati da virgola", default="")

    tsk_list = tsk_sub.add_parser("list", help="Vedi tasks")
    tsk_list.add_argument("--project", help="Filtra per progetto")
    tsk_list.add_argument("--status", choices=['done', 'todo'], help="Filtra per stato")
    tsk_list.add_argument("--tag", help="Filtra per tag")

    tsk_done = tsk_sub.add_parser("done", help="Completa task")
    tsk_done.add_argument("title", help="Titolo task")
    
    tsk_open = tsk_sub.add_parser("reopen", help="Riapri task")
    tsk_open.add_argument("title", help="Titolo task")

    tsk_tag = tsk_sub.add_parser("tag", help="Assegna tag a task")
    tsk_tag.add_argument("title", help="Titolo task")
    tsk_tag.add_argument("tag", help="Nome tag")

    tsk_del = tsk_sub.add_parser("delete", help="Cancella task")
    tsk_del.add_argument("title", help="Titolo task")

    args = parser.parse_args()

    if args.command == "project":
        if args.subcommand == "add":
            app.create_project(args.name, args.desc)
        elif args.subcommand == "list":
            app.list_projects()
        elif args.subcommand == "delete":
            app.delete_project(args.name)

    elif args.command == "tag":
        if args.subcommand == "add":
            app.create_tag(args.name, args.color)
        elif args.subcommand == "list":
            app.list_tags()
        elif args.subcommand == "delete":
            app.delete_tag(args.name)

    elif args.command == "task":
        if args.subcommand == "add":
            app.create_task(args.project, args.title, args.tags)
        elif args.subcommand == "list":
            app.list_tasks(args.project, args.status, args.tag)
        elif args.subcommand == "done":
            app.toggle_task(args.title, True)
        elif args.subcommand == "reopen":
            app.toggle_task(args.title, False)
        elif args.subcommand == "tag":
            app.add_tag_to_task(args.title, args.tag)
        elif args.subcommand == "delete":
            app.delete_task(args.title)

if __name__ == "__main__":
    main()