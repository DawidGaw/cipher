from ciphers.rot_schemes.rot13 import Rot13


class TestRot13:
    def test_rot13_uppercase(self):
        text = "HE"
        result = Rot13()._cipher(text)
        assert result == "UR"

    def test_rot13_lowercase(self):
        text = "he"
        result = Rot13()._cipher(text)
        assert result == "ur"

    def test_rot13_mixed_case(self):
        text = "Hej"
        result = Rot13()._cipher(text)
        assert result == "Urw"

    def test_rot13_encrypt(self):
        text = "Hej"
        result = Rot13().encrypt(text)
        assert result == "Urw"

    def test_rot13_decrypt(self):
        text = "Urw"
        result = Rot13().decrypt(text)
        assert result == "Hej"
