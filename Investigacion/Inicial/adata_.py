import numpy as np

# Data de prueb de un pentagono

puntos = np.array(
   [
 ['A', [8, 10]],
 ['B', [12, 14]],
 ['C', [18, 8]],
 ['D', [20, 16]],
 ['E', [30, 10]]
   ], dtype=object
)

observaciones = np.array(
    [['A', 'B', 5.682],
 ['B', 'A', 5.675],
 ['C', 'B', 8.501],
 ['C', 'D', 8.259],
 ['D', 'C', 8.265],
 ['D', 'E', 11.663],
 ['E', 'D', 11.679],
 ['E', 'A', 22.017]], dtype=object
)

errores = np.array([0.0248054, 0.01817214, 0.01525741, 0.01248285, 0.01864619, 0.00092981
, 0.01741808, 0.01734771])