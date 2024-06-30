# mymath/__init__.py

from .addition import add
from .subtraction import subtract
from .multiplication import multiply
from .division import divide
from .modulus import modulus
from .exponentiation import power
from .square_root import square_root
from .trigonometry import sine, cosine, tangent

__all__ = [
    'add',
    'subtract',
    'multiply',
    'divide',
    'modulus',
    'power',
    'square_root',
    'sine',
    'cosine',
    'tangent'
]
