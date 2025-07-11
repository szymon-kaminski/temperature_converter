import pytest

from temperature_converter import (
    celsius_to_fahrenheit, 
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
)

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