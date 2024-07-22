import numpy as np

# # Coordenadas iniciales (aproximaciones iniciales)
# puntos = np.array([
#     [10, [-922886.72715334, -5951569.11657866, 2099281.85726845]],
#     [11, [-923608.04171829, -5951534.04024824, 2099036.70315641]],
#     [4, [-924151.68281468, -5952372.84075829, 2096541.10163531]],
#     [3, [-924347.7783152, -5952308.43195145, 2096629.12382028]],
#     [8, [-921992.37525752, -5952223.15849636, 2097964.20772335]],
#     [9, [-921980.7985837, -5952077.42737261, 2098347.62710959]],
# ], dtype=object)

# # Distancias medidas
# observaciones = np.array([
#     [10, 11, 762.566],    # Distancia medida entre 10 y 11
#     [4, 3, 224.384],      # Distancia medida entre 4 y 3
#     [11, 4, 2688.1995],   # Distancia medida entre 11 y 4
#     [8, 4, 2590.4349],    # Distancia medida entre 8 y 4
#     [8, 9, 410.188],      # Distancia medida entre 8 y 9
#     [8, 11, 2057.4457],   # Distancia medida entre 8 y 11
# ], dtype=object)

def crear_vector_parametros(puntos, observaciones):
    puntos_ordenados = sorted(puntos, key=lambda x: int(x[0]))

    vector_parametros = []
    indices_diccionario = {}

    for i, punto in enumerate(puntos_ordenados):
        idx = len(vector_parametros)
        indices_diccionario[punto[0]] = idx
        vector_parametros.extend(punto[1])

    observaciones_ordenadas = sorted(observaciones, key=lambda x: x[2], reverse=True)

    for i, obs in enumerate(observaciones_ordenadas):
        idx = len(vector_parametros)
        indices_diccionario[f"obs({int(obs[0])}-{int(obs[1])})"] = idx
        vector_parametros.append(obs[2])

    return np.array(vector_parametros), indices_diccionario, observaciones_ordenadas

def calcular_longitudes(indices_diccionario):
    length_diccionario = {}
    for key, value in indices_diccionario.items():
        if isinstance(key, int):  
            length_diccionario[key] = 3  
        else:  
            length_diccionario[key] = 1  

    longitud_total = sum(length_diccionario.values())
    return length_diccionario, longitud_total

def parcial_coeficients_obs_row(XA, XB, LAB):
    dX = XB[0] - XA[0]
    dY = XB[1] - XA[1]

    if len(XA) == 2 or len(XB) == 2:
        AB0 = np.sqrt(dX**2 + dY**2)
        partial_pt1 = [-dX / AB0, -dY / AB0]
        partial_pt2 = [dX / AB0, dY / AB0]
    else:
        dZ = XB[2] - XA[2]
        AB0 = np.sqrt(dX**2 + dY**2 + dZ**2)
        partial_pt1 = [-dX / AB0, -dY / AB0, -dZ / AB0]
        partial_pt2 = [dX / AB0, dY / AB0, dZ / AB0]

    W = AB0 - LAB
    return partial_pt1, partial_pt2, W

def crear_matrices(observaciones, indices_diccionario, vector_parametros):
    matriz_A = []
    hipermatriz = []
    W = []
    for obs in observaciones:
        idx_a = indices_diccionario[int(obs[0])]
        idx_b = indices_diccionario[int(obs[1])]
        idx_obs = indices_diccionario[f"obs({int(obs[0])}-{int(obs[1])})"]
        XA = vector_parametros[idx_a:idx_a+3]
        XB = vector_parametros[idx_b:idx_b+3]
        LAB = obs[2]
        
        partial_pt1, partial_pt2, w = parcial_coeficients_obs_row(XA, XB, LAB)
        
        row_A = np.zeros_like(vector_parametros)
        row_hiper = ['0'] * len(vector_parametros)
        for i in range(3):
            row_A[idx_a + i] = partial_pt1[i]
            row_A[idx_b + i] = partial_pt2[i]
            row_hiper[idx_a + i] = f"derv_parcial_{'xyz'[i]}_{obs[0]}"
            row_hiper[idx_b + i] = f"derv_parcial_{'xyz'[i]}_{obs[1]}"
        
        row_A[idx_obs] = -1  
        row_hiper[idx_obs] = f"dist_obs_{int(obs[0])}-{int(obs[1])}"
        
        matriz_A.append(row_A)
        hipermatriz.append(row_hiper)
        W.append(w)
    
    return np.array(matriz_A), hipermatriz, np.array(W)

# # Uso de las funciones modulares
# vector_parametros, indices_diccionario, observaciones_ordenadas = crear_vector_parametros(puntos, observaciones)
# length_diccionario, longitud_total = calcular_longitudes(indices_diccionario)
# matriz_A, hipermatriz, W = crear_matrices(observaciones_ordenadas, indices_diccionario, vector_parametros)

# # Impresión de resultados
# print("Vector de parámetros:")
# print(vector_parametros)

# print("\nDiccionario de índices del vector de parámetros:")
# for key, value in indices_diccionario.items():
#     print(f"{key}: {value}")

# print("\nLongitudes de los elementos del vector de parámetros:")
# for key, value in length_diccionario.items():
#     print(f"{key}: {value}")

# print(f"\nLongitud total del vector de parámetros: {longitud_total}")

# print("\nMatriz A (Jacobiana):")
# print(matriz_A)

# print("\nHipermatriz:")
# for row in hipermatriz:
#     print(row)

# print("\nVector de observaciones W:")
# print(W)
