

import math

def square_root(a):
    
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)
