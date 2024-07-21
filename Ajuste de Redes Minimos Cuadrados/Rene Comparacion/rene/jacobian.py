import numpy as np

def getPartials(data):
    # print(f"vector gradiente derivada parcial de {data[0]} - {data[1]}")
    dX = np.float64(data[3][0]) - np.float64(data[2][0])
    dY = np.float64(data[3][1]) - np.float64(data[2][1])
    dZ = np.float64(data[3][2]) - np.float64(data[2][2])

    dCalc = np.float64(data[4])

    # Derivadas parciales en 3D
    dpX = dX / dCalc  
    dpY = dY / dCalc  
    dpZ = dZ / dCalc
    return np.array([dpX, dpY, dpZ], dtype=np.float64)

def getGradient(data, zeros, index, pa_index, pb_index):
    # Obtener las derivadas parciales
    dP = getPartials(data)
    dPn = -dP

    # Crear un vector de ceros con precisión flotante
    gradient = np.zeros(zeros, dtype=np.float64)

    # Colocar -1 en la posición especificada
    gradient[index] = -1

    # Colocar -dpX, -dpY, -dpZ en las posiciones especificadas comenzando en pa_index
    gradient[pa_index:pa_index+3] = dPn

    # Colocar dpX, dpY, dpZ en las posiciones especificadas comenzando en pb_index
    gradient[pb_index:pb_index+3] = dP

    return gradient

def getJacobian(data, lenght):

    # Orden base 
    # obs2 = getGradient(data[1], lenght, 18, 0, 3) # observacion 2 - 4-3
    # obs5 = getGradient(data[4], lenght, 19, 9, 6) # observacion 5 - 8-9
    # obs1 = getGradient(data[0], lenght, 20, 15, 12) # observacion 1 - 10-11
    # obs4 = getGradient(data[3], lenght, 21, 3, 6) # observacion 4 - 8-4
    # obs3 = getGradient(data[2], lenght, 22, 3, 15) # observacion 3 - 11-4
    # obs6 = getGradient(data[5], lenght, 23, 15, 6) # observacion 6 - 8-11

    # Orden nuevo 
    obs2 = getGradient(data[1], lenght, 18, 3, 0) # observacion 2 - 4-3
    obs5 = getGradient(data[4], lenght, 19, 6, 9) # observacion 5 - 8-9
    obs1 = getGradient(data[0], lenght, 20, 12, 15) # observacion 1 - 10-11
    obs4 = getGradient(data[3], lenght, 21, 6, 3) # observacion 4 - 8-4
    obs3 = getGradient(data[2], lenght, 22, 15, 3) # observacion 3 - 11-4
    obs6 = getGradient(data[5], lenght, 23, 6, 15) # observacion 6 - 8-11

    # Configurar opciones de impresión de NumPy para mostrar todos los decimales
    # np.set_printoptions(precision=17)
    # print(f"gradient:\n{eN6}\n")

    B = np.asarray([obs2,obs5,obs1,obs4,obs3,obs6])
    return B