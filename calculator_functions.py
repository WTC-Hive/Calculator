import math

def add(a, b):
    """
    Add two numbers and return the result.
    """
    results= sum(a,b)
    return results
    pass

def subtract(a, b):
    """
    Subtract the second number from the first and return the result.
    """
    results= a-b
    return results
    pass

def multiply(a, b):
    """
    Multiply two numbers and return the result.
    """
    results = a* b
    return results
    pass

def divide(a, b):
    """
    Divide the first number by the second and return the result.
    Handle division by zero by returning "Error: Division by zero".
    """
    
    if b == 0:
        return "Error: Division by zero"
    results= a /b
    return results
    pass

def sqrt(a):
    """
    Return the square root of a number.
    Handle negative inputs by returning "Error: Negative input".
    """
    if a < 0:
        return "Error: Negative input"
    else:
        return math.sqrt(a)
    
    pass

def modulus(a, b):
    """
    Return the remainder of the division of the first number by the second.
    Handle division by zero by returning "Error: Division by zero".
    """
    if b == 0:
        return "Error: Division by zero"
    return a % b

def exponent(a, b):
    """
    Return the result of raising the first number to the power of the second.
    """
    results = a **b
    return results
    pass
