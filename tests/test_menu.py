from unittest.mock import patch

from ciphers.menu import Menu


@patch("builtins.input", side_effect=["1"])
@patch("builtins.print")
def test_get_choice_valid_number(mock_print, mock_input):
    choice = Menu.get_choice()
    assert choice == "Load_file"


@patch("builtins.input", side_effect=["invalid", "1"])
@patch("builtins.print")
def test_get_choice_invalid_number(mock_print, mock_input):
    choice = Menu.get_choice()
    assert choice == "Load_file"
    mock_print.assert_any_call("Niepoprawna opcja. Spróbuj jeszcze raz")


@patch("builtins.input", side_effect=["1"])
@patch("builtins.print")
def test_choose_cipher_rot13(mock_print, mock_input):
    rot_type = Menu.choose_cipher()
    assert rot_type == "rot13"


@patch("builtins.input", side_effect=["2"])
@patch("builtins.print")
def test_choose_cipher_rot47(mock_print, mock_input):
    rot_type = Menu.choose_cipher()
    assert rot_type == "rot47"


@patch("builtins.input", side_effect=["invalid", "1"])
@patch("builtins.print")
def test_choose_cipher_invalid_then_valid(mock_print, mock_input):
    rot_type = Menu.choose_cipher()
    # Po błędnym wyborze metoda powinna poprosić ponownie
    assert rot_type == "rot13"
    mock_print.assert_any_call("Podany szyfr: invalid nie istnieje")
