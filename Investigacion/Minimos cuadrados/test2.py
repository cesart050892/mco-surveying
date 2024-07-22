import numpy as np

# Correcciones proporcionadas
correcciones_proporcionadas = np.array([
    2.11987279e-02, -6.96285618e-03, -9.51555920e-03,
    5.33993082e-02, 6.13708362e-03, 4.26807156e-02,
    1.85773756e-01, -1.01331564e-01, -1.83485649e-01,
    -1.29942393e-03, -1.63575923e-02, -4.30369150e-02,
    -5.20537364e-02, 2.53128683e-03, -1.76915706e-02,
    -2.07018631e-01, 1.15983642e-01, 2.11048978e-01
])

# Correcciones calculadas para los puntos
vector_correcciones = np.array([
    2.11987274e-02, -6.96285604e-03, -9.51555901e-03,
    5.33993100e-02, 6.13708288e-03, 4.26807144e-02,
    1.85773757e-01, -1.01331565e-01, -1.83485651e-01,
    -1.29942396e-03, -1.63575925e-02, -4.30369157e-02,
    -5.20537373e-02, 2.53128687e-03, -1.76915709e-02,
    -2.07018633e-01, 1.15983644e-01, 2.11048982e-01
])

# Índices correspondientes a los puntos
indices_puntos = np.array([
    0, 1, 2,
    3, 4, 5,
    6, 7, 8,
    9, 10, 11,
    12, 13, 14,
    15, 16, 17
])

# Extraer las correcciones para los puntos
correcciones_puntos = vector_correcciones[indices_puntos]

# Comparar correcciones proporcionadas con las calculadas
diferencias = correcciones_proporcionadas - correcciones_puntos

# Crear un diccionario para mostrar las diferencias
diferencias_diccionario = {
    "Proporcionadas": correcciones_proporcionadas.tolist(),
    "Calculadas": correcciones_puntos.tolist(),
    "Diferencias": diferencias.tolist()
}

# Verificar si hay diferencias significativas
diferencias_significativas = np.isclose(correcciones_proporcionadas, correcciones_puntos, rtol=1e-17)

# Mostrar el resultado de la verificación
for i, igual in enumerate(diferencias_significativas):
    if not igual:
        print(f"Diferencia encontrada en el índice {i}:")
        print(f"  Proporcionada: {correcciones_proporcionadas[i]}")
        print(f"  Calculada: {correcciones_puntos[i]}")
        print(f"  Diferencia: {diferencias[i]}")

print("\nTodas las correcciones son iguales:", np.all(diferencias_significativas))
