from typing import TextIO

def get_file(file_path: str ) -> TextIO:
    """Recupera un oggetto IO di tipo testuale dal un file specifico"""
    return open(file_path, "r")


def send_questions(file_path: str ) -> TextIO:
    return open(file_path, "r")

def get_file_content(file_path: str) -> str:
    if not file_path:
        raise ValueError("Il file path non può essere vuoto!")

    try:
        with open(file_path, "r") as f:
            return f.read()

    except FileNotFoundError:
        raise FileNotFoundError("Il file non esiste")

