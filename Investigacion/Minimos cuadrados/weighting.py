import numpy as np

def getWeightingMatrix(length, default_dev, custom_devs=None, option=None):
    """
    Crea una matriz de peso diagonal con desviaciones estándar definidas por el usuario.
    Las desviaciones estándar se pueden personalizar utilizando las siguientes opciones:
    - custom_devs: Diccionario con índices específicos como claves y desviaciones estándar como valores.
    - option: Diccionario con opciones 'all' o 'from_to' para personalizar las desviaciones estándar.
    
    Parameters:
    length (int): Longitud del vector de desviaciones estándar.
    default_dev (float): Desviación estándar predeterminada para todos los elementos.
    custom_devs (dict, optional): Diccionario con índices específicos como claves y desviaciones estándar como valores.
    option (dict, optional): Diccionario con opciones de configuración. Puede contener:
                             - 'all': Desviación estándar para todos los elementos.
                             - 'from_to': Tupla con el rango (start, end) y el valor de desviación estándar.
    
    Returns:
    np.ndarray: Matriz de pesos diagonal.
    """
    # Crear una lista de desviaciones estándar predeterminadas
    default_devs = [default_dev] * length
    
    if option:
        if 'all' in option:
            # Aplicar el mismo valor a todos los elementos
            default_devs = [option['all']] * length
        elif 'from_to' in option:
            start, end, value = option['from_to']
            if 0 <= start < length and 0 <= end < length:
                default_devs[start:end + 1] = [value] * (end - start + 1)
            else:
                raise IndexError("El rango está fuera del rango permitido.")
    
    # Si se proporcionan desviaciones estándar personalizadas, aplicarlas
    if custom_devs:
        for index, dev in custom_devs.items():
            if 0 <= index < length:
                default_devs[index] = dev
            else:
                raise IndexError("El índice está fuera del rango permitido.")
    
    # Crear la matriz de pesos diagonal
    weighting_matrix = np.diag(default_devs)
    
    return weighting_matrix

# # Ejemplo de uso con custom_devs
# custom_devs = {
#     18: .0001,
#     19: .0002,
#     20: .0003,
#     21: .0004,
#     22: .0005,
#     23: .0006
# }
# W1 = getWeightingMatrix(length=24, default_dev=.0005, custom_devs=custom_devs)
# print("Matriz con custom_devs:")
# print(W1)

# # Ejemplo de uso con opción 'all'
# option_all = {'all': .0002}
# W2 = getWeightingMatrix(length=24, default_dev=.0005, option=option_all)
# print("\nMatriz con opción 'all':")
# print(W2)

# # Ejemplo de uso con opción 'from_to'
# option_from_to = {'from_to': (18, 23, .0003)}
# W3 = getWeightingMatrix(length=24, default_dev=.0005, option=option_from_to)
# print("\nMatriz con opción 'from_to':")
# print(W3)
