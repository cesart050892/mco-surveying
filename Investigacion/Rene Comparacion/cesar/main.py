from data import puntos, observaciones
from jacobian import llenar_matriz

condiciones = True
A, f = llenar_matriz(puntos, observaciones, condiciones)