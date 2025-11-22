import json
import os
from dataclasses import asdict
from typing import List

from ciphers.models.text import Text


class FileHandler:
    @staticmethod
    def read_file(filename: str) -> List[Text]:
        if not FileHandler.file_exists(filename):
            print(f"Plik {filename} nie istnieje")
            return []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Text(**item) for item in data]
        except json.JSONDecodeError:
            print(f"Plik '{filename}' ma błędny format JSON.")
            return []
        except Exception as e:
            print(f"Błąd podczas odczytu pliku: {e}")
            return []

    @staticmethod
    def write_file(filename: str, data: List[Text], append: bool = False) -> None:
        existing_data = []
        if append and FileHandler.file_exists(filename):
            existing_data = FileHandler.read_file(filename)
        all_data = existing_data + data

        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump([asdict(item) for item in all_data], file, indent=4)
                print(f"Dane zapisano do pliku '{filename}'.")
        except Exception as e:
            print(f"Błąd podczas zapisu: {e}")

    @staticmethod
    def file_exists(filename: str) -> bool:
        return os.path.exists(filename)
