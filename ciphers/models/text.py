from dataclasses import dataclass, asdict
from typing import Literal


@dataclass
class Text:
    txt: str
    rot_type: Literal ["rot13", "rot47"]
    status: Literal ["encrypted", "decrypted"]
