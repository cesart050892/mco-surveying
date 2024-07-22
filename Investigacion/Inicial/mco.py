import numpy as np

def calcular_delta_x_ponderado(A, W, f):
    """
    Calcula Δx para la ecuación Δx = (A^T W A)^-1 A^T W f

    Parámetros:
    A (numpy.ndarray): Matriz de coeficientes A
    W (numpy.ndarray): Matriz de pesos W (diagonal)
    f (numpy.ndarray): Vector de términos independientes f

    Retorna:
    numpy.ndarray: Vector Δx
    """

    # Transpuesta de A
    AT = np.transpose(A)
    
    # Calcular A^T W A
    ATWA = np.dot(AT, np.dot(W, A))
    
    # Calcular A^T W f
    ATWF = np.dot(AT, np.dot(W, f))
    
    # Calcular (A^T W A)^-1
    ATWA_inv = np.linalg.pinv(ATWA)
    
    # Calcular Δx
    delta_x = np.dot(ATWA_inv, ATWF)
    
    return delta_x