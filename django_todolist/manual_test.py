import requests
import json
import uuid

BASE_URL = "http://localhost:8000"

def test_flow():
    print("--- Inizio Test ---")
    
    # 1. Crea Progetto
    print("\n1. Creazione Progetto...")
    project_payload = {
        "name": f"Test Project {uuid.uuid4()}",
        "notes": "Note di test"
    }
    response = requests.post(f"{BASE_URL}/projects/", json=project_payload)
    if response.status_code == 201:
        project_data = response.json()
        project_id = project_data['id']
        print(f"✅ Progetto creato: {project_id}")
    else:
        print(f"❌ Errore creazione progetto: {response.text}")
        return

    # 2. Crea Task
    print("\n2. Creazione Task...")
    task_payload = {
        "title": f"Test Task {uuid.uuid4()}",
        "project_id": project_id
    }
    response = requests.post(f"{BASE_URL}/task/create", json=task_payload)
    if response.status_code == 201:
        task_data = response.json()
        task_id = task_data['id']
        print(f"✅ Task creato: {task_id}")
    else:
        print(f"❌ Errore creazione task: {response.text}")
        # Non ritorno qui, provo a pulire il progetto
    
    # 3. Update Task
    if 'task_id' in locals():
        print("\n3. Aggiornamento Task...")
        update_payload = {
            "is_complete": True,
            "title": "Task Aggiornato"
        }
        response = requests.patch(f"{BASE_URL}/task/update/{task_id}", json=update_payload)
        if response.status_code == 200:
            print("✅ Task aggiornato con successo")
        else:
            print(f"❌ Errore aggiornamento task: {response.text}")

    # 4. Delete Task
    if 'task_id' in locals():
        print("\n4. Eliminazione Task...")
        response = requests.delete(f"{BASE_URL}/task/delete/{task_id}")
        if response.status_code == 200:
            print("✅ Task eliminato con successo")
        else:
            print(f"❌ Errore eliminazione task: {response.text}")

    # 5. Delete Project
    print("\n5. Eliminazione Progetto...")
    response = requests.delete(f"{BASE_URL}/projects/{project_id}/")
    if response.status_code == 200:
        print("✅ Progetto eliminato con successo")
    else:
        print(f"❌ Errore eliminazione progetto: {response.text}")

    print("\n--- Test Completato ---")

if __name__ == "__main__":
    try:
        test_flow()
    except requests.exceptions.ConnectionError:
        print("❌ Errore: Impossibile connettersi al server. Assicurati che il server sia avviato su http://localhost:8000")
