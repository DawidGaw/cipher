import json
import os

from ciphers.handlers.file_handler import FileHandler
from ciphers.models.text import Text


def test_file_exists(tmp_path):
    file = tmp_path / "file.json"
    file.write_text("[]")
    assert FileHandler.file_exists(str(file)) is True

    nonexisting = tmp_path / "nonexisting_file.json"
    assert FileHandler.file_exists(str(nonexisting)) is False


def test_read_file_not_exist(tmp_path):
    filename = tmp_path / "file.json"
    result = FileHandler.read_file(str(filename))
    assert result == []


def test_read_file_valid_json(tmp_path):
    filename = tmp_path / "data.json"
    json_data = [{"txt": "hello", "rot_type": "rot13", "status": "encrypted"}]
    filename.write_text(json.dumps(json_data))

    result = FileHandler.read_file(str(filename))

    assert len(result) == 1
    assert isinstance(result[0], Text)
    assert result[0].txt == "hello"
    assert result[0].rot_type == "rot13"
    assert result[0].status == "encrypted"


def test_read_file_invalid_json(tmp_path):
    filename = tmp_path / "broken.json"
    filename.write_text("{ invalid json }")

    result = FileHandler.read_file(str(filename))

    assert result == []


def test_write_file_overwrite(tmp_path):
    filename = tmp_path / "save.json"
    data = [Text("abc", "rot13", "encrypted")]

    FileHandler.write_file(str(filename), data, append=False)

    saved = json.loads(filename.read_text())

    assert saved == [{"txt": "abc", "rot_type": "rot13", "status": "encrypted"}]


def test_write_file_append(tmp_path):
    filename = tmp_path / "save.json"

    FileHandler.write_file(str(filename), [Text("Hello", "rot13", "encrypted")])
    saved = json.loads(filename.read_text())

    FileHandler.write_file(
        str(filename), [Text("Bonjour", "rot47", "encrypted")], append=True
    )

    saved = json.loads(filename.read_text())

    assert len(saved) == 2
    assert saved[0]["txt"] == "Hello"
    assert saved[0]["rot_type"] == "rot13"
    assert saved[0]["status"] == "encrypted"
    assert saved[1]["txt"] == "Bonjour"
    assert saved[1]["rot_type"] == "rot47"
    assert saved[1]["status"] == "encrypted"


def test_write_file_invalid_path():
    filename = "/this/path/does/not/exist/test.json"
    FileHandler.write_file(filename, [Text("Hello", "rot13", "encrypted")])
    assert not os.path.exists(filename)
