import pytest
from backend import add, subtract, multiply, divide, sqrt, modulus, exponent

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(0, 5) == 0
    assert divide(5, 0) == "Error: Division by zero"

def test_sqrt():
    assert sqrt(9) == 3
    assert sqrt(0) == 0
    assert sqrt(-1) == "Error: Negative input"

def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(0, 5) == 0
    assert modulus(5, 0) == "Error: Division by zero"

def test_exponent():
    assert exponent(2, 3) == 8
    assert exponent(5, 0) == 1
    assert exponent(0, 5) == 0
