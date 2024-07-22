# Datos de pruebas
# Rene Manzano

import numpy as np

# Coordenadas iniciales (aproximaciones iniciales)
puntos = np.array([
    ['10', [-922886.72715334, -5951569.11657866, 2099281.85726845]],
    ['11', [-923608.04171829, -5951534.04024824, 2099036.70315641]],
    ['4', [-924151.68281468, -5952372.84075829, 2096541.10163531]],
    ['3', [-924347.7783152, -5952308.43195145, 2096629.12382028]],
    ['8', [-921992.37525752, -5952223.15849636, 2097964.20772335]],
    ['9', [-921980.7985837, -5952077.42737261, 2098347.62710959]],
],dtype=object)

# Distancias medidas
observaciones = np.array([
    ['10', '11', 762.566],  # Distancia medida entre 10 y 11
    ['4', '3', 224.384],    # Distancia medida entre 4 y 3
    ['11', '4', 2688.1995], # Distancia medida entre 11 y 4
    ['8', '4', 2590.4349],  # Distancia medida entre 8 y 4
    ['8', '9', 410.188],    # Distancia medida entre 8 y 9
    ['8', '11', 2057.4457],  # Distancia medida entre 8 y 11
], dtype=object)