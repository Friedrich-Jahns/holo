import numpy as np
from .field import field

def grid(field):
    x = (np.arange(field.shape[1]) - (field.shape[1]-1)/2)*field.dx
    y = (np.arange(field.shape[0]) - (field.shape[0]-1)/2)*field.dy

    X,Y = np.meshgrid(x,y)
    return X,Y


def aperture(field, r=1e-3):
    X,Y = grid(field)

    mask = X**2+Y**2 <=r**2

    field.data *=mask
    return field

def aperture_inverse(field, r=1e-3):
    X,Y = grid(field)

    mask = X**2+Y**2 >=r**2

    field.data *=mask
    return field


def lens(field, focal_length=53.2e-3):
    X,Y = grid(field)

    wavelength = field.wavelength
    
    k = 2*np.pi/wavelength
    lens = np.exp(-1j*k*(X**2+Y**2)/(2*focal_length))
    field.data *= lens
    return field
    
def Sphere(field,z_c,x_c=0,y_c=0, r=1e-3):
    
    X,Y = grid(field)

    a_square = r**2-(field.z-z_c)**2
    mask = (X-x_c)**2+(Y-y_c)**2 >=a_square

    field.data *=mask
    return field,mask

