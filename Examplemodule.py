def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract the second number from the first."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide the first number by the second.

    Raises:
        ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
