from .field import field
from .sources import Gaussian_illumination, Custom_illumination

from .elements import grid, aperture, aperture_inverse, lens, Sphere
from .propagation import propagate, H_prop

__version__ = "0.1.0"

__all__ = [
    'field',
    'Gaussian_illumination'
]