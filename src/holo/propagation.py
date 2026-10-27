import numpy as np
from .field import field

   


def H_prop(field, f_x, f_y, z):
    wavelength = field.wavelength
    
    kz_sq = (1 / wavelength)**2 - f_x**2 - f_y**2
    
    kz = np.sqrt(np.maximum(0, kz_sq))
    
    H = np.exp(1j * 2 * np.pi * z * kz)
    
    H[kz_sq < 0] = 0
    
    return H

def propagate(field,z):
    fft_data = np.fft.fftshift(np.fft.fft2(field.data))
    
    Ny, Nx = fft_data.shape

    fx = np.fft.fftshift(np.fft.fftfreq(Nx, d=field.dx))
    fy = np.fft.fftshift(np.fft.fftfreq(Ny, d=field.dy))

    FX, FY = np.meshgrid(fx, fy)

    H = H_prop(field, FX, FY, z)

    propagated = fft_data * H

    field.data = np.fft.ifft2(np.fft.ifftshift(propagated))
    field.z += z
    return field

