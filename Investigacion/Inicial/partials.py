import numpy as np

def parcial_coeficients_obs_row(XA, XB, LAB):
    """
    Calcula una fila de la matriz A para la ecuación de distancia linearizada entre dos puntos.

    Parámetros:
    XA : array_like
        Coordenadas iniciales del punto A (aproximaciones iniciales).
    XB : array_like
        Coordenadas iniciales del punto B (aproximaciones iniciales).
    LAB : float
        Distancia medida entre los puntos A y B.

    Devuelve:
    A_row : list
        Fila de la matriz A con las derivadas parciales.
    W : float
        Vector de observaciones (diferencia entre distancia medida y distancia calculada).
    """

    if len(XA) == 2 or len(XB) == 2:
        # Diferencias de coordenadas en 2D
        dX = XB[0] - XA[0]
        dY = XB[1] - XA[1]

        # Distancia calculada entre los puntos A y B en 2D
        AB0 = np.sqrt(dX**2 + dY**2)

        # Derivadas parciales en 2D
        dX_A = -dX / AB0
        dY_A = -dY / AB0
        dX_B = dX / AB0
        dY_B = dY / AB0

        # Fila de la matriz A en 2D
        partial_pt1 = [dX_A, dY_A]
        partial_pt2 = [dX_B, dY_B]

    else:
        # Diferencias de coordenadas en 3D
        dX = XB[0] - XA[0]
        dY = XB[1] - XA[1]
        dZ = XB[2] - XA[2]

        # Distancia calculada entre los puntos A y B en 3D
        AB0 = np.sqrt(dX**2 + dY**2 + dZ**2)

        # Derivadas parciales en 3D
        dX_A = -dX / AB0
        dY_A = -dY / AB0
        dZ_A = -dZ / AB0
        dX_B = dX / AB0
        dY_B = dY / AB0
        dZ_B = dZ / AB0

        # Fila de la matriz A en 3D
        partial_pt1 = [dX_A, dY_A, dZ_A]
        partial_pt2 = [dX_B, dY_B, dZ_B]

    # Vector de observaciones W (diferencia entre distancia medida y distancia calculada)
    W = AB0 - LAB

    return partial_pt1, partial_pt2, W