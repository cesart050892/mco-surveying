import numpy as np
from jacobian import crear_vector_parametros,calcular_longitudes,crear_matrices
from data import puntos, observaciones
from weighting import getWeightingMatrix
from conditional import getVectorCorrections
import json

# Uso de las funciones modulares
vector_parametros, indices_diccionario, observaciones_ordenadas = crear_vector_parametros(puntos, observaciones)
length_diccionario, longitud_total = calcular_longitudes(indices_diccionario)
matriz_A, hipermatriz, W = crear_matrices(observaciones_ordenadas, indices_diccionario, vector_parametros)

option_from_to = {'from_to': (18, 23, .000004)}
C = getWeightingMatrix(longitud_total, default_dev=.0005, option=option_from_to)

# # Impresión de resultados
# print(f"Vector de parámetros:\n{vector_parametros}")

print("\nDiccionario de índices del vector de parámetros:")
for key, value in indices_diccionario.items():
    print(f"{key}: {value}")

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

# print(f"Matriz de Pesos (Matrix Diagonal): \n{C}")

vector_correcciones = getVectorCorrections(matriz_A, C, W)
# print(f"Vector de correciones [{type(vector_correcciones)}]: \n{vector_correcciones}")

vector_parametros_corregido = vector_correcciones.flatten() - vector_parametros
# print(f"Vector de parametros corregido: \n{vector_parametros_corregido}")

def calcDist3D(PT1, PT2):
    # Diferencias de coordenadas en 3D
    dX = PT2[0] - PT1[0]
    dY = PT2[1] - PT1[1]
    dZ = PT2[2] - PT1[2]

    # Distancia calculada entre los puntos A y B en 3D
    return  np.sqrt(dX**2 + dY**2 + dZ**2)

def crear_diccionario_verificacion(puntos, observaciones, vector_parametros, vector_parametros_corregido, vector_correcciones, indices_diccionario):
    verificacion_diccionario = {}

    # Verificación de puntos
    for punto in puntos:
        punto_id = punto[0]
        idx = indices_diccionario[punto_id]
        verificacion_diccionario[punto_id] = {
            "Inicial": vector_parametros[idx:idx+3].tolist(),
            "Corrección": vector_correcciones[idx:idx+3].tolist(),
            "Corregido": vector_parametros_corregido[idx:idx+3].tolist()
        }

    # Verificación de observaciones
    for obs in observaciones:
        obs_id = f"obs({int(obs[0])}-{int(obs[1])})"
        idx = indices_diccionario[obs_id]
        verificacion_diccionario[obs_id] = {
            "Inicial": vector_parametros[idx],
            "Corrección": vector_correcciones[idx],
            "Corregido": vector_parametros_corregido[idx]
        }

        # Calcular la distancia usando las coordenadas corregidas
        pt1_id = int(obs[0])
        pt2_id = int(obs[1])
        pt1_corregido = verificacion_diccionario[pt1_id]["Corregido"]
        pt2_corregido = verificacion_diccionario[pt2_id]["Corregido"]
        distancia_calculada = calcDist3D(pt1_corregido, pt2_corregido)
        distancia_observada = obs[2]

        verificacion_diccionario[obs_id]["Distancia calculada"] = distancia_calculada
        verificacion_diccionario[obs_id]["Distancia observada"] = distancia_observada
        verificacion_diccionario[obs_id]["Diferencia"] = distancia_calculada - distancia_observada

    return verificacion_diccionario

# Crear el diccionario de verificación
verificacion_diccionario = crear_diccionario_verificacion(
    puntos, observaciones, vector_parametros, vector_parametros_corregido, vector_correcciones, indices_diccionario
)

# Mostrar el diccionario de verificación
print(json.dumps(verificacion_diccionario, indent=2))