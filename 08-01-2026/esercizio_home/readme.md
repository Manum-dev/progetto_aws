# 📡 SiteCheck JSON - Monitoraggio Web & Network

**SiteCheck** è uno strumento da riga di comando (CLI) scritto in Python per monitorare lo stato di salute di siti web e server. Verifica la raggiungibilità, misura i tempi di risposta (latenza) e salva automaticamente un report dettagliato in formato JSON.

È progettato per essere **leggero**, **veloce** e **senza dipendenze esterne**.

---

## ✨ Funzionalità

* **🚦 Controllo Stato:** Rileva se un sito è Online (200 OK), irraggiungibile o restituisce errori (404, 500, ecc.).
* **⏱️ Misurazione Latenza:** Calcola il tempo di risposta del server in secondi.
* **💾 Export JSON:** Salva automaticamente tutti i risultati in un file strutturato per analisi successive.
* **🎨 Output Colorato:** Feedback visivo immediato nel terminale (Verde=OK, Rosso=Errore, Giallo=Warning).
* **🔄 Modalità Interattiva:** Se lanciato senza argomenti, chiede all'utente i siti da controllare in un ciclo continuo.
* **⚡ Zero Dipendenze:** Funziona con le librerie standard di Python (`urllib`, `json`, `argparse`). Non serve `pip install`.

---

## 🚀 Requisiti

* Python 3.5 o superiore.

---

## 💻 Utilizzo

Apri il terminale ed esegui lo script in uno dei seguenti modi:
### 1. Controllo Rapido (Argomenti)
Passa uno o più URL direttamente nel comando:
```bash
python sitecheck_json.py google.com wikipedia.org

