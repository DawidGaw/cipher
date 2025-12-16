from ciphers.rot_schemes.rot47 import Rot47


class TestRot47:
    def test_rot13_uppercase(self):
        text = "He"
        result = Rot47()._cipher(text)
        assert result == "w6"

    def test_rot13_lowercase(self):
        text = "he"
        result = Rot47()._cipher(text)
        assert result == "96"

    def test_rot13_mixed_case(self):
        text = "Hej"
        result = Rot47()._cipher(text)
        assert result == "w6;"

    def test_rot13_encrypt(self):
        text = "Hej"
        result = Rot47().encrypt(text)
        assert result == "w6;"

    def test_rot13_decrypt(self):
        text = "ECj"
        result = Rot47().decrypt(text)
        assert result == "tr;"
