from unittest.mock import patch, mock_open

import pytest

from src.utils import read_json, create_list_from_json


@patch('builtins.open', new_callable=mock_open, read_data='[1, 2, 3]')
@patch('json.load')
def test_read_json(mock_json_load, mock_open):
    mock_json_load.return_value = [1, 2, 3]
    result = read_json('fake_file.json')
    assert result == [1, 2, 3]
    mock_json_load.assert_called_once()


@patch('builtins.open', new_callable=mock_open, read_data='[1, 2, 3]')
@patch('json.load')
def test_read_json_not_list(mock_json_load, mock_open):
    mock_json_load.return_value = {1, 2, 3}
    result = read_json('fake_file.json')
    assert result == []
    mock_json_load.assert_called_once()


def test_read_json_not():
    assert read_json('not_file.json') == []


def test_create_list_from_json(list_dicts):
    prod = create_list_from_json(list_dicts)[0].products_list[0]
    assert prod.name == "Samsung Galaxy C23 Ultra"
    assert prod.description == "256GB, Серый цвет, 200MP камера"


def test_create_list_from_json_1():
    with pytest.raises(TypeError):
        create_list_from_json({''}) == []
