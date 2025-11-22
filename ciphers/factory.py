from typing import Type
from ciphers.rot_schemes.rot import Rot
from ciphers.rot_schemes.rot13 import Rot13
from ciphers.rot_schemes.rot47 import Rot47


class CipherFactory:
    _ciphers: dict[str, Type[Rot]] = {"rot13": Rot13, "rot47": Rot47}

    @staticmethod
    def get_cipher(rot_type: str )-> Type[Rot]:
        rot_type = rot_type.lower()
        if rot_type in CipherFactory._ciphers:
            return CipherFactory._ciphers[rot_type]
        else:
            raise ValueError(f"Podany szyfr: {rot_type} nie istnieje"
                             f"/n Dostępne są jedynie: {list(CipherFactory._ciphers.keys())}")






