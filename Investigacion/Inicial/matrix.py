import numpy as np 
import partials

def calcular_columnas_matrix_a(puntos, distancias):
    num_puntos = len(puntos)
    dim_punto = len(next(iter(puntos.values()))) if num_puntos > 0 else 0
    return num_puntos * dim_punto + len(distancias)

def crear_matriz(puntos, distancias):
    columnas = calcular_columnas_matrix_a(puntos, distancias)
    filas = len(distancias)

    # Inicializar matriz con ceros
    matriz = np.zeros((filas, columnas))
    return matriz

def obtener_indices_puntos(puntos):
    indices_puntos = {}
    dim_punto = len(next(iter(puntos.values())))
    for i, punto in enumerate(puntos.keys()):
        indices_puntos[punto] = range(i * dim_punto, (i + 1) * dim_punto)
    return indices_puntos

def llenar_matriz(puntos, distancias):
    dim_punto = len(next(iter(puntos.values())))  # Dimensión de un punto
    matriz = crear_matriz(puntos, distancias)
    indices_puntos = obtener_indices_puntos(puntos)
    W = []
    for i, (p1, p2, dist) in enumerate(distancias):
        coord_p1 = np.array(puntos[p1])
        coord_p2 = np.array(puntos[p2])
        coord_p1, coord_p2, w = partials.parcial_coeficients_obs_row(coord_p1, coord_p2, dist)

        # Llenar la matriz con las coordenadas de los puntos
        matriz[i, indices_puntos[p1]] = coord_p1  # Coordenadas del primer punto
        matriz[i, indices_puntos[p2]] = coord_p2  # Coordenadas del segundo punto

        # Añadir -1 en la posición correspondiente a la distancia
        matriz[i, -len(distancias) + i] = -1

        # Agregar w a la lista W
        W.append(w)

    return matriz, W