import math
import re

def add(a, b):
    """
    Add two numbers and return the result.
    """
    return a + b

def subtract(a, b):
    """
    Subtract the second number from the first and return the result.
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers and return the result.
    """
    return a * b

def divide(a, b):
    """
    Divide the first number by the second and return the result.
    Handle division by zero by returning "Error: Division by zero".
    """
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

def sqrt(a):
    """
    Return the square root of a number.
    Handle negative inputs by returning "Error: Negative input".
    """
    if a < 0:
        return "Error: Negative input"
    result = math.sqrt(a)
    return result


def modulus(a, b):
    """
    Return the remainder of the division of the first number by the second.
    Handle division by zero by returning "Error: Division by zero".
    """
    if b == 0:
        return "Error: Division by zero"
    else:
        return a % b

def exponent(a, b):
    """
    Return the result of raising the first number to the power of the second.
    """
    result = a ** b
    return result

def factorial(a):
    """
    Return the factorial of a number.
    Handle negative inputs by returning "Error: Negative input".
    """
    if a < 0:
        return "Error: Negative input"
    elif a == 0:
        return 1

    factorial = 1
    for i in range(1, a + 1):
        factorial *= i

    return factorial

         


def log(a, base):
    """
    Return the logarithm of a number with a specified base.
    Handle invalid inputs by returning "Error: Invalid input".
    """
    if a <= 0 or base <= 0 or base == 1:
        return "Error: Invalid input"
     
    count = 0
    
    
    while a >= base:
        a /= base
        count += 1
    
    return count


def sin(a):
    """
    Return the sine of a number (in radians).
    """
    return math.sin(a)

def cos(a):
    """
    Return the cosine of a number (in radians).
    """
    return math.cos(a)

def tan(a):
    """
    Return the tangent of a number (in radians).
    Handle undefined cases by returning "Error: Undefined".
    """

    cos_value = cos(a)
    if abs(cos_value) < 1e-10:  # Check if the cosine is close to zero
        return "Error: Undefined"
    
    # Tangent is sine divided by cosine
    sin_value = sin(a)
    return sin_value / cos_value


def degrees_to_radians(degrees):
    """
    Convert degrees to radians.
    """
    return degrees * (3.141592653589793 / 180)

def radians_to_degrees(radians):
    """
    Convert radians to degrees.
    """
    return radians * (180 / 3.141592653589793)

def evaluate_expression(expression):
    """
    Evaluate a mathematical expression using PEMDAS/BODMAS rules.
    The expression is a string, e.g., "3 / 7 * 8 % 3".
    This function will call other calculator functions in the correct order.
    """
    
      
    try:
        # Use eval to evaluate the expression
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except NameError:
        return "Error: Invalid expression"  # Catch undefined variables or invalid input
    except Exception as e:
        return f"Error: {str(e)}"
    


