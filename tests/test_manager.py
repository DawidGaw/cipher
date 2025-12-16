from unittest.mock import MagicMock, patch

from ciphers.factory import CipherFactory
from ciphers.handlers.file_handler import FileHandler
from ciphers.manager import Manager
from ciphers.models.text import Text


@patch("builtins.print")
@patch("builtins.input", return_value="hello")
def test_encrypt_flow(mock_input, mock_print):
    menu = MagicMock()
    menu.choose_cipher.return_value = "Rot13"

    buffer = MagicMock()
    manager = Manager(buffer, menu)

    cipher_mock = MagicMock()
    cipher_mock.encrypt.return_value = "uryyb"

    with patch.object(CipherFactory, "get_cipher", return_value=cipher_mock):
        manager.encrypt_flow()

    cipher_mock.encrypt.assert_called_once_with("hello")

    assert buffer.add.call_count == 1
    added_text = buffer.add.call_args[0][0]
    assert added_text.txt == "uryyb"
    assert added_text.rot_type == "Rot13"
    assert added_text.status == "encrypted"

    mock_print.assert_any_call("Zakodowano: uryyb")


@patch("builtins.print")
@patch("builtins.input", return_value="uryyb")
def test_decrypt_flow(mock_input, mock_print):
    menu = MagicMock()
    menu.choose_cipher.return_value = "Rot13"

    buffer = MagicMock()
    manager = Manager(buffer, menu)

    cipher_mock = MagicMock()
    cipher_mock.decrypt.return_value = "uryyb"

    with patch.object(CipherFactory, "get_cipher", return_value=cipher_mock):
        manager.decrypt_flow()

    cipher_mock.decrypt.assert_called_once_with("uryyb")
    assert buffer.add.call_count == 1
    added_text = buffer.add.call_args[0][0]
    assert added_text.txt == "uryyb"
    assert added_text.rot_type == "Rot13"
    assert added_text.status == "decrypted"
    mock_print.assert_any_call("Dekodowano: uryyb")


@patch("builtins.print")
@patch("builtins.input", return_value="data.txt")
def test_load_from_file_nonempty(mock_input, mock_print):
    menu = MagicMock()
    buffer = MagicMock()
    manager = Manager(buffer, menu)

    items = [Text("abc", "rot13", "encrypted")]

    with patch.object(FileHandler, "read_file", return_value=items):
        manager.load_from_file()

    buffer.add_bulk.assert_called_once_with(items)
    mock_print.assert_called_with("Wczytano plik!")


@patch("builtins.print")
@patch("builtins.input", return_value="data.txt")
def test_load_from_file_empty(mock_input, mock_print):
    menu = MagicMock()
    buffer = MagicMock()
    manager = Manager(buffer, menu)

    with patch.object(FileHandler, "read_file", return_value=[]):
        manager.load_from_file()

    buffer.add_bulk.assert_not_called()
    mock_print.assert_called_with("Plik jest pusty")


@patch("builtins.input", return_value="output.txt")
def test_save_to_file(mock_input):
    menu = MagicMock()
    buffer = MagicMock()
    buffer.all.return_value = ["item1", "item2"]

    manager = Manager(buffer, menu)
    with patch.object(FileHandler, "write_file") as mock_write:
        manager.save_to_file()

    mock_write.assert_called_once_with("output.txt", ["item1", "item2"])


@patch("builtins.print")
def test_show_buffer(mock_print):
    menu = MagicMock()
    buffer = MagicMock()
    buffer.all.return_value = ["X", "Y"]

    manager = Manager(buffer, menu)
    manager.show_buffer()

    mock_print.assert_any_call("Zawartość Buffera")
    mock_print.assert_any_call("X")
    mock_print.assert_any_call("Y")
