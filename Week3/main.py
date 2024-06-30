# main.py

import sys
import os

# Add the parent directory of 'mymath' to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import specific functions from the mymath package
from mymath.addition import add
from mymath.subtraction import subtract
from mymath.multiplication import multiply
from mymath.division import divide
from mymath.modulus import modulus
from mymath.exponentiation import power
from mymath.square_root import square_root
from mymath.trigonometry import sine, cosine, tangent

def main():
    a = 10
    b = 5

    # Basic arithmetic operations
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    try:
        print(f"{a} / {b} = {divide(a, b)}")
    except ValueError as e:
        print(e)
    print(f"{a} % {b} = {modulus(a, b)}")

    # Advanced mathematical operations
    print(f"{a} ** {b} = {power(a, b)}")
    try:
        print(f"Square root of {a} = {square_root(a)}")
    except ValueError as e:
        print(e)

    # Trigonometric functions
    import math
    angle = math.pi / 4  # 45 degrees in radians
    print(f"sin({angle}) = {sine(angle)}")
    print(f"cos({angle}) = {cosine(angle)}")
    print(f"tan({angle}) = {tangent(angle)}")

if __name__ == "__main__":
    main()
