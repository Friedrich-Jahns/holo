from .field import field
from .sources import Gaussian_illumination

from .elements import grid, aperture, lens
from .propagation import propagate, H_prop

__version__ = "0.1.0"

__all__ = [
    'field',
    'Gaussian_illumination'
]