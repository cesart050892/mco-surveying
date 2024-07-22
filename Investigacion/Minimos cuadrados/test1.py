import numpy as np

# Datos iniciales y vectores corregidos
vector_parametros = np.array([
    -9.24347778e+05, -5.95230843e+06, 2.09662912e+06,
    -9.24151683e+05, -5.95237284e+06, 2.09654110e+06,
    -9.21992375e+05, -5.95222316e+06, 2.09796421e+06,
    -9.21980799e+05, -5.95207743e+06, 2.09834763e+06,
    -9.22886727e+05, -5.95156912e+06, 2.09928186e+06,
    -9.23608042e+05, -5.95153404e+06, 2.09903670e+06,
    2.68819950e+03, 2.59043490e+03, 2.05744570e+03,
    7.62566000e+02, 4.10188000e+02, 2.24384000e+02
])

indices_diccionario = {
    3: 0,
    4: 3,
    8: 6,
    9: 9,
    10: 12,
    11: 15,
    "obs(11-4)": 18,
    "obs(8-4)": 19,
    "obs(8-11)": 20,
    "obs(10-11)": 21,
    "obs(8-9)": 22,
    "obs(4-3)": 23
}

vector_correcciones = np.array([
    2.11987274e-02, -6.96285604e-03, -9.51555901e-03,
    5.33993100e-02, 6.13708288e-03, 4.26807144e-02,
    1.85773757e-01, -1.01331565e-01, -1.83485651e-01,
    -1.29942396e-03, -1.63575925e-02, -4.30369157e-02,
    -5.20537373e-02, 2.53128687e-03, -1.76915709e-02,
    -2.07018633e-01, 1.15983644e-01, 2.11048982e-01,
    -1.60991798e-04, 7.54988406e-04, -2.68151995e-03,
    4.40290134e-04, 3.68472345e-04, 1.94057851e-04
])

# Crear el vector de parámetros corregido
vector_parametros_corregido = vector_parametros + vector_correcciones

# Crear el diccionario de verificación
verificacion_diccionario = {}

for punto in [3, 4, 8, 9, 10, 11]:
    idx = indices_diccionario[punto]
    verificacion_diccionario[punto] = {
        "Inicial": vector_parametros[idx:idx+3].tolist(),
        "Corrección": vector_correcciones[idx:idx+3].tolist(),
        "Corregido": vector_parametros_corregido[idx:idx+3].tolist()
    }

# Agregar las observaciones de distancias
observaciones_indices = [
    "obs(11-4)", "obs(8-4)", "obs(8-11)", "obs(10-11)", "obs(8-9)", "obs(4-3)"
]

for obs in observaciones_indices:
    idx = indices_diccionario[obs]
    verificacion_diccionario[obs] = {
        "Inicial": vector_parametros[idx],
        "Corrección": vector_correcciones[idx],
        "Corregido": vector_parametros_corregido[idx]
    }

# Mostrar el diccionario de verificación
import json
print(json.dumps(verificacion_diccionario, indent=2))
