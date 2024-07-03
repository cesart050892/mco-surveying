import numpy as np

# Datos proporcionados
data = np.array([
    [10.0, 11.0,
     np.array([-922886.72715334, -5951569.11657866, 2099281.85726845]),
     np.array([-923608.04171829, -5951534.04024824, 2099036.70315641]),
     762.6438154315333, 762.566, 0.0778154315332813],
    
    [4.0, 3.0,
     np.array([-924151.68281468, -5952372.84075829, 2096541.10163531]),
     np.array([-924347.7783152, -5952308.43195145, 2096629.12382028]),
     224.38771082294144, 224.384, 0.0037108229414570815],
    
    [11.0, 4.0,
     np.array([-923608.04171829, -5951534.04024824, 2099036.70315641]),
     np.array([-924151.68281468, -5952372.84075829, 2096541.10163531]),
     2688.3375698433133, 2688.1995, 0.13806984331313288],
    
    [8.0, 4.0,
     np.array([-921992.37525752, -5952223.15849636, 2097964.20772335]),
     np.array([-924151.68281468, -5952372.84075829, 2096541.10163531]),
     2590.4140294107874, 2590.4349, -0.020870589212790946],
    
    [8.0, 9.0,
     np.array([-921992.37525752, -5952223.15849636, 2097964.20772335]),
     np.array([-921980.7985837, -5952077.42737261, 2098347.62710959]),
     410.34376509154475, 410.188, 0.15576509154476526],
    
    [8.0, 11.0,
     np.array([-921992.37525752, -5952223.15849636, 2097964.20772335]),
     np.array([-923608.04171829, -5951534.04024824, 2099036.70315641]),
     2058.035112979308, 2057.4457, 0.5894129793077809]
], dtype=object)


# Cálculo de derivadas parciales para cada observación
dfX10 = -(data[0,3][0]-data[0,2][0])/data[0,4]
dfY10 = -(data[0,3][1]-data[0,2][1])/data[0,4]
dfZ10 = -(data[0,3][2]-data[0,2][2])/data[0,4]

dfX11 = (data[0,3][0]-data[0,2][0])/data[0,4]
dfY11 = (data[0,3][1]-data[0,2][1])/data[0,4]
dfZ11 = (data[0,3][2]-data[0,2][2])/data[0,4]

dfX04 = (data[1,3][0]-data[1,2][0])/data[1,4]
dfY04 = (data[1,3][1]-data[1,2][1])/data[1,4]
dfZ04 = (data[1,3][2]-data[1,2][2])/data[1,4]

dfX03 = -(data[1,3][0]-data[1,2][0])/data[1,4]
dfY03 = -(data[1,3][1]-data[1,2][1])/data[1,4]
dfZ03 = -(data[1,3][2]-data[1,2][2])/data[1,4]

dfX11A = (data[2,3][0]-data[2,2][0])/data[2,4]
dfY11A = (data[2,3][1]-data[2,2][1])/data[2,4]
dfZ11A = (data[2,3][2]-data[2,2][2])/data[2,4]

dfX04B = -(data[2,3][0]-data[2,2][0])/data[2,4]
dfY04B = -(data[2,3][1]-data[2,2][1])/data[2,4]
dfZ04B = -(data[2,3][2]-data[2,2][2])/data[2,4]

dfX08A = (data[3,3][0]-data[3,2][0])/data[3,4]
dfY08A = (data[3,3][1]-data[3,2][1])/data[3,4]
dfZ08A = (data[3,3][2]-data[3,2][2])/data[3,4]

dfX04A = -(data[3,3][0]-data[3,2][0])/data[3,4]
dfY04A = -(data[3,3][1]-data[3,2][1])/data[3,4]
dfZ04A = -(data[3,3][2]-data[3,2][2])/data[3,4]

dfX08 = (data[4,3][0]-data[4,2][0])/data[4,4]
dfY08 = (data[4,3][1]-data[4,2][1])/data[4,4]
dfZ08 = (data[4,3][2]-data[4,2][2])/data[4,4]

dfX09 = -(data[4,3][0]-data[4,2][0])/data[4,4]
dfY09 = -(data[4,3][1]-data[4,2][1])/data[4,4]
dfZ09 = -(data[4,3][2]-data[4,2][2])/data[4,4]

dfX08B = -(data[5,3][0]-data[5,2][0])/data[5,4]
dfY08B = -(data[5,3][1]-data[5,2][1])/data[5,4]
dfZ08B = -(data[5,3][2]-data[5,2][2])/data[5,4]

dfX11B = (data[5,3][0]-data[5,2][0])/data[5,4]
dfY11B = (data[5,3][1]-data[5,2][1])/data[5,4]
dfZ11B = (data[5,3][2]-data[5,2][2])/data[5,4]

# Construcción de las filas de la matriz de diseño
row_1 = [dfX04, dfY04, dfZ04, dfX03, dfY03, dfZ03, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0]  # 4 - 3
row_2 = [0, 0, 0, 0, 0, 0, dfX09, dfY09, dfZ09, dfX08, dfY08, dfZ08, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0]  # 9 - 8
row_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, dfX10, dfY10, dfZ10, dfX11, dfY11, dfZ11, 0, 0, -1, 0, 0, 0]  # 10 - 11
row_4 = [0, 0, 0, dfX08A, dfY08A, dfZ08A, dfX04A, dfY04A, dfZ04A, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0]  # 8 - 4
row_5 = [0, 0, 0, dfX11A, dfY11A, dfZ11A, 0, 0, 0, 0, 0, 0, 0, 0, 0, dfX04B, dfY04B, dfZ04B, 0, 0, 0, 0, -1, 0]  # 11 - 4
row_6 = [0, 0, 0, 0, 0, 0, dfX08B, dfY08B, dfZ08B, 0, 0, 0, 0, 0, 0, dfX11B, dfY11B, dfZ11B, 0, 0, 0, 0, 0, -1]  # 8 - 11

# Convertir las filas a una matriz numpy
B = np.asarray([row_1, row_2, row_3, row_4, row_5, row_6])

W = np.asarray([[data[1,6]],[data[4,6]],[data[0,6]],[data[3,6]],[data[2,6]],[data[5,6]]])

C = np.diag([.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.0005,.000004,.000004,.000004,.000004,.000004,.000004])

# Extracción de coordenadas y distancias
x03 = [data[1,3][0]]
y03 = [data[1,3][1]]
Z03 = [data[1,3][2]]

x04 = [data[1,2][0]]
y04 = [data[1,2][1]]
Z04 = [data[1,2][2]]

x08 = [data[4,2][0]]
y08 = [data[4,2][1]]
Z08 = [data[4,2][2]]

x09 = [data[4,3][0]]
y09 = [data[4,3][1]]
Z09 = [data[4,3][2]]

x10 = [data[0,2][0]]
y10 = [data[0,2][1]]
Z10 = [data[0,2][2]]

x11 = [data[0,3][0]]
y11 = [data[0,3][1]]
Z11 = [data[0,3][2]]

d1 = [data[1,5]]
d2 = [data[4,5]]
d3 = [data[0,5]]

d4 = [data[3,5]]
d5 = [data[2,5]]
d6 = [data[5,5]]

# Creación del vector v
v = np.asarray([x03, y03, Z03, x04, y04, Z04, x08, y08, Z08, x09, y09, Z09, 
                x10, y10, Z10, x11, y11, Z11, d1, d2, d3, d4, d5, d6])


# print(f"Matrix B: {B}")
# print(f"\nMatrix v: {v}")
# print(f"\nMatrix W: {W}")

M = np.linalg.inv(np.dot(B,np.dot(C,B.T)))
K = np.dot(M,W)
V = np.dot(np.dot(C,B.T),K)

print(f"Matrix M: {M}")
print(f"\nMatrix K: {K}")
print(f"\nMatrix V: {V}")
