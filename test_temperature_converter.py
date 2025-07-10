import pytest

from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert round(celsius_to_fahrenheit(-40), 2) == -40.0


def test_fahrenheit_to_celsius():
    assert round(fahrenheit_to_celsius(32), 2) == 0
    assert round(fahrenheit_to_celsius(212), 2) == 100
    assert round(fahrenheit_to_celsius(-40), 2) == -40.0