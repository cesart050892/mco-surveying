import numpy as np
import data as d
import matrix2 as m
import weights as wg
import mco as le
import mcnlconditional as lec

condiciones = True

A, f = m.llenar_matriz(d.puntos, d.observaciones, condiciones)
# W = wg.weight(0.003, d.puntos, d.observaciones, condiciones)
W = np.diag([.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.000004,.000004,.000004,.000004,.000004,.000004])

# print(f"Matrix de diseño {A.shape}: \n{A}")
# print(f"\nMatrix de Pesos {W.shape}: \n{W}")
# print(f"\nVector de residuos (1, {len(f)}): \n{f}")

M = np.linalg.inv(np.dot(A,np.dot(W,A.T)))
# print(f"M: \n{M}")

K = np.dot(M,f)
# print(f"K: \n{K}")

V = np.dot(np.dot(W,A.T),K)
print(f"V: \n{V}")

