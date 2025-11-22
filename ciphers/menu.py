from typing import Literal

RotType = Literal['rot13', 'rot47']

class Menu:
    CIPHER_TYPES: dict[str, tuple[RotType, str]] = {
        "1": ("rot13", "ROT13"),
        "2": ("rot47", "ROT47"),
    }
    options = {
        "1": "Load_file",
        "2": "Encrypt_text",
        "3": "Decrypt_text",
        "4": "Show_buffer",
        "5": "Save_file",
        "6": "Exit"
    }

    @staticmethod
    def show() -> None:
        print("\n=== Witaj w Menu programu Cipher ===")
        print("1. Wczytaj dane z pliku")
        print("2. Zaszyfruj tekst")
        print("3. Odszyfruj tekst")
        print("4. Wyświetl bufor")
        print("5. Zapisz do pliku")
        print("6. Wyjście")

    @classmethod
    def get_choice(cls)-> str:
        cls.show()
        choice = input("\n Wybierz opcję: ").strip()
        if choice in cls.options:
            return cls.options[choice]
        print(f"Niepoprawna opcja. Spróbuj jeszcze raz")
        return cls.get_choice()

    @classmethod
    def choose_cipher(cls) -> RotType:
        print("\nWybierz szyfr:")

        for key, (_, display_name) in cls.CIPHER_TYPES.items():
            print(f"{key}. {display_name}")

        choice = input("Opcja: ").strip()

        if choice in Menu.CIPHER_TYPES:
            return Menu.CIPHER_TYPES[choice][0]
        else:
            print(f"Podany szyfr: {choice} nie istnieje")
            return Menu.choose_cipher()

