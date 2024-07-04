import numpy as np 
import partials

def calcular_columnas_matrix_a(puntos, distancias, condiciones = False):
    """
    Calcula el número de columnas de la matriz A basada en los puntos y las distancias.

    :param puntos: ndarray de puntos con sus coordenadas.
    :param distancias: Lista de tuplas con los puntos y la distancia entre ellos.
    :return: Número de columnas de la matriz A.
    """
    num_puntos = puntos.shape[0]
    pt = puntos[0]
    dim_punto = len(pt[1]) if num_puntos > 0 else 0

    if condiciones:
        return num_puntos * dim_punto + len(distancias)
    else:
        return num_puntos * dim_punto

def crear_matriz(puntos, distancias, condiciones = False):
    """
    Crea una matriz inicializada con ceros basada en los puntos y distancias.

    :param puntos: ndarray de puntos con sus coordenadas.
    :param distancias: Lista de tuplas con los puntos y la distancia entre ellos.
    :return: Matriz inicializada con ceros.
    """
    columnas = calcular_columnas_matrix_a(puntos, distancias, condiciones)
    filas = len(distancias)
    return np.zeros((filas, columnas))

def obtener_indices_puntos(puntos):
    """
    Obtiene los índices correspondientes a cada punto en la matriz A.

    :param puntos: ndarray de puntos con sus coordenadas.
    :return: Diccionario con los índices de los puntos.
    """
    indices_puntos = {}
    dim_punto = len(puntos[0, 1])
    for i, punto in enumerate(puntos[:, 0]):
        indices_puntos[punto] = range(i * dim_punto, (i + 1) * dim_punto)
    return indices_puntos

def llenar_matriz(puntos, distancias, condiciones = False):
    """
    Llena la matriz A con los coeficientes parciales y las observaciones.

    :param puntos: ndarray de puntos con sus coordenadas.
    :param distancias: Lista de tuplas con los puntos y la distancia entre ellos.
    :return: Matriz A llena y lista W de coeficientes parciales.
    """
    # Crear la matriz inicializada
    matriz = crear_matriz(puntos, distancias, condiciones)
    
    
    # Obtener los índices de los puntos
    indices_puntos = obtener_indices_puntos(puntos)
    
    # Crear un diccionario para acceder rápidamente a las coordenadas por nombre
    coord_dict = {punto: np.array(coords) for punto, coords in puntos}

    W = []
    for i, (p1, p2, dist) in enumerate(distancias):
        try:
            coord_p1 = coord_dict[p1]
            coord_p2 = coord_dict[p2]
        except KeyError as e:
            raise KeyError(f"Punto {e} no encontrado en 'puntos'. Verifica que todos los identificadores en 'distancias' están presentes en 'puntos'.")
        
        partial1, partial2, w = partials.parcial_coeficients_obs_row(coord_p1, coord_p2, dist)


        # Llenar la matriz con las coordenadas de los puntos
        matriz[i, indices_puntos[p1]] = partial1  # Coordenadas del primer punto
        matriz[i, indices_puntos[p2]] = partial2  # Coordenadas del segundo punto

        if condiciones:
            # Añadir -1 en la posición correspondiente a la distancia
            matriz[i, -len(distancias) + i] = -1

        # Agregar w a la lista W
        W.append(w)

    return matriz, W
