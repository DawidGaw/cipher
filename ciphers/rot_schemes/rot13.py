from .rot import Rot


class Rot13(Rot):
    @staticmethod
    def _cipher(text: str) -> list[str]:
        result = []
        for char in text:
            if "A" <= char <= "Z":
                result.append(chr((ord(char) - 65 + 13) % 26 + 65))
            elif "a" <= char <= "z":
                result.append(chr((ord(char) - 97 + 13) % 26 + 97))
            else:
                result.append(char)
        return result

    @staticmethod
    def encrypt(text: str) -> str:
        return str(Rot13._cipher(text))

    @staticmethod
    def decrypt(text: str) -> str:
        return str(Rot13._cipher(text))
