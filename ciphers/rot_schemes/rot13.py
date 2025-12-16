from .rot import Rot


class Rot13(Rot):
    @staticmethod
    def _cipher(text: str) -> str:
        result = []
        for char in text:
            if "A" <= char <= "Z":
                result.append(chr((ord(char) - 65 + 13) % 26 + 65))
            elif "a" <= char <= "z":
                result.append(chr((ord(char) - 97 + 13) % 26 + 97))
            else:
                result.append(char)

        return "".join(result)

    @staticmethod
    def encrypt(text: str) -> str:
        return Rot13._cipher(text)

    @staticmethod
    def decrypt(text: str) -> str:
        return Rot13._cipher(text)
