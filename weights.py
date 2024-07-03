import numpy as np
import matrix2 as m

def weight(sigma, puntos, distancias, condiciones = False):
    if condiciones:
        length = m.calcular_columnas_matrix_a(puntos, distancias, condiciones)
    else: 
        length = len(distancias)
    return np.diag(np.full(length, 1/(sigma)**2))