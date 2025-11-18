from abc import abstractmethod, ABC


class Rot(ABC):
    @staticmethod
    @abstractmethod
    def encrypt(text: str) -> str:
        pass

    @staticmethod
    @abstractmethod
    def decrypt(text: str) -> str:
        pass
