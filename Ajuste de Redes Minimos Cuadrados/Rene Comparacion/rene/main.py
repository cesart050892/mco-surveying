import numpy as np
from geographic import getArrayData
from jacobian import getJacobian
from residuals import getResiduals
from conditional import getVectorCorrections
from init import getInitData

npdata = getArrayData()
v = getInitData(npdata, 24)
# print(f"Datos iniciales: {npdata}\n\nVector formado a partir de los datos iniciales:{v}")

B = getJacobian(npdata)
print(f"Matriz B Desarrollada por la tabla de la imagen (Matrix Jacobiana aumentada): \n{B}")

W = getResiduals(npdata)
C = np.diag([.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.000004,.000004,.000004,.000004,.000004,.000004])

V = getVectorCorrections(B, C, W)
# print(f"Vector de correciones al vector parametro: \n{V}")