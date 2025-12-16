from ciphers.handlers.buffer import Buffer
from ciphers.models.text import Text


class TestBuffer:
    def setup_method(self):
        self.buffer = Buffer()

    def test_add_single_text(self):
        text = Text("hello", "rot13", "encrypted")

        self.buffer.add(text)

    def test_add_ignores_invalid_type(self):
        self.buffer.add("Something bla")
        assert len(self.buffer.all()) == 0

    def test_add_bulk_adds_multiple_items(self):
        text = [
            Text("hello", "rot13", "encrypted"),
            Text("Winter", "rot13", "encrypted"),
        ]
        self.buffer.add_bulk(text)
        assert self.buffer.all() == text
        assert len(self.buffer.all()) == 2

    def test_all_returns(self):
        text = Text("hello", "rot13", "encrypted")
        self.buffer.add(text)
        result = self.buffer.data_as_list_of_dicts()
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] == {"txt": "hello", "rot_type": "rot13", "status": "encrypted"}

    def test_repr(self):
        text = Text("hello", "rot13", "encrypted")
        self.buffer.add(text)
        r = repr(self.buffer)
        assert "Buffer" in r
        assert "hello" in r

    def test_str(self):
        text = Text("hello", "rot13", "encrypted")
        text1 = Text("popp", "rot13", "encrypted")
        self.buffer.add_bulk([text1, text])
        result = str(self.buffer)
        assert "hello" in result
        assert "popp" in result
        assert "\n" in result
