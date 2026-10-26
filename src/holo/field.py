import numpy as np

class field:
    def __init__(self,data,wavelength,dx,dy,z):
        self.data = np.array(data, dtype=complex)
        self.wavelength = wavelength
        self.dx = dx
        self.dy = dy
        self.z = z
        self.shape = self.data.shape
