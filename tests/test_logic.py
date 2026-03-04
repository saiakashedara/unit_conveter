from logic import *

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32


def test_fahrenheit_to_celsius():
    assert round(fahrenheit_to_celsius(32), 2) == 0


def test_km_to_miles():
    assert round(km_to_miles(1), 5) == 0.62137


def test_miles_to_km():
    assert round(miles_to_km(1), 5) == 1.60934


def test_kg_to_pounds():
    assert round(kg_to_pounds(1), 5) == 2.20462


def test_pounds_to_kg():
    assert round(pounds_to_kg(2.20462), 2) == 1