from .menu import Menu
from ciphers.handlers.buffer import Buffer
from .factory import CipherFactory
from ciphers.handlers.file_handler import FileHandler
from .models.text import Text

class Manager:
    def __init__(self, buffer: Buffer, menu: Menu):
        self.buffer = buffer
        self.menu = menu

    def run(self) -> None:
        while True:
            choice = self.menu.get_choice()
            match choice:
                case "Load_file":
                    self.load_from_file()
                case "Encrypt_text":
                    self.encrypt_flow()
                case "Decrypt_text":
                    self.decrypt_flow()
                case "Show_buffer":
                    self.show_buffer()
                case "Save_file":
                    self.save_to_file()
                case "Exit":
                    print(f"Goodbye")
                    break
                case _:
                    raise ValueError(f"Podano błędną opcję")

    def encrypt_flow(self) -> None:
        text = input("Wprowadź tekst do zakodowania: ").strip()

        rot_type = self.menu.choose_cipher()
        cipher = CipherFactory.get_cipher(rot_type)

        encrypted = cipher.encrypt(text)

        obj = Text(txt=encrypted, rot_type=rot_type, status="encrypted")
        self.buffer.add(obj)

        print(f"Zakodowano: {encrypted}")

    def decrypt_flow(self) -> None:
        text = input("Wprowadź tekst do dekodowania: ").strip()

        rot_type = self.menu.choose_cipher()
        cipher = CipherFactory.get_cipher(rot_type)

        decrypted = cipher.decrypt(text)

        obj = Text(txt=decrypted, rot_type=rot_type, status="decrypted")
        self.buffer.add(obj)

        print(f"Dekodowano: {decrypted}")

    def load_from_file(self) -> None:
        filename = input("Plik do wczytania: ").strip()
        items = FileHandler.read_file(filename)

        if not items:
            print("Plik jest pusty")
            return

        self.buffer.add_bulk(items)

        print(f"Wczytano plik!")

    def save_to_file(self) -> None:
        filename = input("Plik do zapisania: ").strip()
        FileHandler.write_file(filename, self.buffer.all())

    def show_buffer(self) -> None:
        print("Zawartość Buffera")
        for item in self.buffer.all():
            print(item)











