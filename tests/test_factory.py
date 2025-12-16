import pytest

from ciphers.factory import CipherFactory
from ciphers.rot_schemes.rot13 import Rot13
from ciphers.rot_schemes.rot47 import Rot47


class TestCipherFactory:
    def test_get_cipher_rot13(self):
        cipher = CipherFactory.get_cipher("rot13")
        assert cipher is Rot13

    def test_get_cipher_rot47(self):
        cipher = CipherFactory.get_cipher("rot47")
        assert cipher is Rot47

    def test_get_cipher_case_insensitive(self):
        assert CipherFactory.get_cipher("Rot13") is Rot13
        assert CipherFactory.get_cipher("Rot47") is Rot47

    def test_get_cipher_invalid_number(self):
        with pytest.raises(ValueError) as exc:
            CipherFactory.get_cipher("rot99")
        assert "Podany szyfr: rot99 nie istnieje" in str(exc.value)
        assert "rot13" in str(exc.value)
        assert "rot47" in str(exc.value)
