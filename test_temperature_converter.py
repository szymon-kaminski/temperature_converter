import pytest

from temperature_converter import (
    celsius_to_fahrenheit, 
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
    convert_celsius_to_fahrenheit,
    convert_fahrenheit_to_celsius,
    convert_celsius_to_kelvin,
    convert_fahrenheit_to_kelvin,
    convert_kelvin_to_celsius,
    convert_kelvin_to_fahrenheit,
)

from unittest.mock import patch


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert round(celsius_to_fahrenheit(-40), 2) == -40.0


def test_fahrenheit_to_celsius():
    assert round(fahrenheit_to_celsius(32), 2) == 0
    assert round(fahrenheit_to_celsius(212), 2) == 100
    assert round(fahrenheit_to_celsius(-40), 2) == -40.0


def test_celsius_to_kelvin():
    assert round(celsius_to_kelvin(0), 2) == 273.15
    assert round(celsius_to_kelvin(100), 2) == 373.15


def test_kelvin_to_celsius():
    assert round(kelvin_to_celsius(273.15), 2) == 0
    assert round(kelvin_to_celsius(373.15), 2) == 100


def test_fahrenheit_to_kelvin():
    assert round(fahrenheit_to_kelvin(32), 2) == 273.15
    assert round(fahrenheit_to_kelvin(212), 2) == 373.15


def test_kelvin_to_fahrenheit():
    assert round(kelvin_to_fahrenheit(273.15), 2) == 32.0
    assert round(kelvin_to_fahrenheit(373.15), 2) == 212.0


@patch("builtins.input", return_value="0")
def test_convert_celsius_to_fahrenheit(mock_input, capsys):
    convert_celsius_to_fahrenheit()
    captured = capsys.readouterr()
    assert "0.0°C is 32.00°F" in captured.out


@patch("builtins.input", return_value="32")
def test_convert_fahrenheit_to_celsius(mock_input, capsys):
    convert_fahrenheit_to_celsius()
    captured = capsys.readouterr()
    assert "32.0°F is 0.00°C" in captured.out


@patch("builtins.input", return_value="0.0")
def test_convert_celsius_to_kelvin(mock_input, capsys):
    convert_celsius_to_kelvin()
    captured = capsys.readouterr()
    assert "0.0°C is 273.15 K" in captured.out


@patch("builtins.input", return_value="32")
def test_convert_fahrenheit_to_kelvin(mock_input, capsys):
    convert_fahrenheit_to_kelvin()
    captured = capsys.readouterr()
    assert "32.0°F is 273.15 K" in captured.out


@patch("builtins.input", return_value="273.15")
def test_convert_kelvin_to_celsius(mock_input, capsys):
    convert_kelvin_to_celsius()
    captured = capsys.readouterr()
    assert "273.15 K is 0.00°C" in captured.out


@patch("builtins.input", return_value="273.15")
def test_convert_kelvin_to_fahrenheit(mock_input, capsys):
    convert_kelvin_to_fahrenheit()
    captured = capsys.readouterr()
    assert "273.15 K is 32.00°F" in captured.out
