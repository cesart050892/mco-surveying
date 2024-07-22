import numpy as np
from geographic import getArrayData
from jacobian import getJacobian
from residuals import getResiduals
from conditional import getVectorCorrections
from parameters import getParameters
from weighting import getWeightingMatrix

npdata = getArrayData()

POINTS = 6
DIMESIONPOINTS = 3
OBS = 6

v = getParameters(npdata)
# print(f"Vector de parametros [{type(v)}]:{v}")

LENGTHVECTORPARAMETER = (POINTS * DIMESIONPOINTS) + OBS

W = getResiduals(npdata)
# print(f"Vector de diferencias (Matrix Jacobiana aumentada): \n{B}")

B = getJacobian(npdata, LENGTHVECTORPARAMETER)
# print(f"Matriz B (Matrix Jacobiana aumentada): \n{B}")

option_from_to = {'from_to': (18, 23, .003)}
C = getWeightingMatrix(LENGTHVECTORPARAMETER, default_dev=.02, option=option_from_to)
# print(f"Matriz de Pesos (Matrix Diagonal): \n{C}")

V = getVectorCorrections(B, C, W)
# print(f"Vector de correciones [{type(V)}]: \n{V}")

l = V.flatten() - v
print(f"Vector de parametros corregido: \n{l}")

PT1 = [l[0], l[1], l[2]]
PT2 = [l[3], l[4], l[5]]

# Diferencias de coordenadas en 3D
dX = PT2[0] - PT1[0]
dY = PT2[1] - PT1[1]
dZ = PT2[2] - PT1[2]

# Distancia calculada entre los puntos A y B en 3D
DIST =  np.sqrt(dX**2 + dY**2 + dZ**2)
DIFF = DIST + l[18]

print(f"Punto 3 corregido: \n{PT1}")
print(f"Punto 4 corregido: \n{PT2}")
print(f"Parametros 18 corregido: \n{l[18]}")
print(f"Distancia 3-4: \n{DIST}")
print(f"Error: \n{DIFF}")