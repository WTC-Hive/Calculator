import pytest
import math
from backend import (
    add, subtract, multiply, divide, modulus, exponent,
    sqrt, factorial, log, sin, cos, tan,
    degrees_to_radians, radians_to_degrees, evaluate_expression
)

def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(5, 5) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Error: Division by zero"

def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(10, 0) == "Error: Division by zero"

def test_exponent():
    assert exponent(2, 3) == 8
    assert exponent(5, 0) == 1

def test_sqrt():
    assert sqrt(16) == 4
    assert sqrt(-1) == "Error: Negative input"

def test_factorial():
    assert factorial(5) == 120
    assert factorial(-1) == "Error: Negative input"

def test_log():
    assert log(100, 10) == 2
    assert log(-1, 10) == "Error: Invalid input"
    assert log(100, 1) == "Error: Invalid input"

def test_sin():
    assert sin(math.pi / 2) == pytest.approx(1)

def test_cos():
    assert cos(math.pi) == pytest.approx(-1)

def test_tan():
    assert tan(math.pi / 4) == pytest.approx(1)
    assert tan(math.pi / 2) == "Error: Undefined"

def test_degrees_to_radians():
    assert degrees_to_radians(180) == pytest.approx(math.pi)

def test_radians_to_degrees():
    assert radians_to_degrees(math.pi) == pytest.approx(180)

def test_evaluate_expression():
    assert evaluate_expression("3 + 5 * 2") == 13
    assert evaluate_expression("(3 + 5) * 2") == 16
    assert evaluate_expression("10 / 0") == "Error: Division by zero"
    assert evaluate_expression("sqrt(16)") == 4
    assert evaluate_expression("factorial(5)") == 120
    assert evaluate_expression("log(100, 10)") == 2
    assert evaluate_expression("invalid") == "Error: Invalid expression"