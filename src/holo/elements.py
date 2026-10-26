import numpy as np
from .field import field

def aperture(field, r=1e-3):
    x = (np.arange(field.shape[1]) - (field.shape[1]-1)/2)*field.dx
    y = (np.arange(field.shape[0]) - (field.shape[0]-1)/2)*field.dy

    X,Y = np.meshgrid(x,y)

    mask = X**2+Y**2 <=r**2

    field.data *=mask
    return field