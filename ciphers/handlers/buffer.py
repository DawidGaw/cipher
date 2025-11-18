from dataclasses import asdict
from typing import List, Dict
from ciphers.models.text import Text

class Buffer:
    def __init__(self) -> None:
        self._data: List[Text] = []

    def add(self, text: Text) -> None:
        if isinstance(text, Text):
            self._data.append(text)

    def add_bulk(self, texts: List[Text]) -> None:
        for text in texts:
            self.add(text)


    def all(self) -> List[Text]:
        return self._data

    def data_as_list_of_dicts(self) -> List[Dict]:
        return [asdict(item) for item in self._data]

    def __repr__(self):
        return f"Buffer(data={self._data})"

    def __str__(self):
        return "\n".join(str(item) for item in self._data)

