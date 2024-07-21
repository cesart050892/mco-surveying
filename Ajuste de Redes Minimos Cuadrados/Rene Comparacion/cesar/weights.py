import numpy as np
from jacobian import calcular_columnas_matrix_a

def weight(sigma, puntos, distancias, condiciones = False):
    if condiciones:
        length = calcular_columnas_matrix_a(puntos, distancias, condiciones)
    else: 
        length = len(distancias)
    return np.diag(np.full(length, 1/(sigma)**2))