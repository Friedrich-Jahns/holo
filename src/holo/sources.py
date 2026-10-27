import numpy as np
from .field import field


def  Gaussian_illumination(shape=(512,512),U_0=1,sigma=3e-3,dx=1e-2/512,dy=1e-2/512,wavelength=532e-9,z=0):

    x = (np.arange(shape[1]) - (shape[1]-1)/2)*dx
    y = (np.arange(shape[0]) - (shape[0]-1)/2)*dy

    X,Y = np.meshgrid(x,y)
    
    data = U_0*np.exp(-(X**2+Y**2)/sigma**2)
    
    return field(
        data = data.astype(complex),
        wavelength = wavelength,
        dx = dx,
        dy = dy,
        z  =z
    )

def Custom_illumination(data, shape=(512,512),dx=1e-2/512,dy=1e-2/512,wavelength=532e-9,z=0,padding=False):
    data = np.array(data) / 255.0
    
    if padding:
        data = np.pad(
            data,
            pad_width=((data.shape[0]//2, data.shape[0]//2), (data.shape[1]//2, data.shape[1]//2)),
            mode="constant",
            constant_values=0
        )
    
    return field(
        data = data.astype(complex),
        wavelength = wavelength,
        dx = dx,
        dy = dy,
        z  =z
    )