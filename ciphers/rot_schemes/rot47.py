from .rot import Rot


class Rot47(Rot):
    @staticmethod
    def _cipher(text: str) -> str:
        result = []
        for char in text:
            ascii_code = ord(char)
            if 33 <= ascii_code <= 126:
                result.append(chr(33 + ((ord(char) + 14) % 94)))
            else:
                result.append(char)
        return "".join(result)

    @staticmethod
    def encrypt(text: str) -> str:
        return Rot47._cipher(text)

    @staticmethod
    def decrypt(text: str) -> str:
        return Rot47._cipher(text)
