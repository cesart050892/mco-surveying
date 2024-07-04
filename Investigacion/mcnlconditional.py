import numpy as np

def delta_x_condicional(A, W, f):
    """
    Calcula Δx para la ecuación Δx = (A^T W A)^-1 A^T W f

    Parámetros:
    A (numpy.ndarray): Matriz de coeficientes A
    W (numpy.ndarray): Matriz de pesos W (diagonal)
    f (numpy.ndarray): Vector de términos independientes f

    Retorna:
    numpy.ndarray: Vector Δx
    """

    print(f"Matrix de diseño {A.shape}: \n{A}")
    print(f"Matrix de Pesos {W.shape}: \n{W}")
    print(f"Vector de residuos (1, {len(f)}): \n{f}")

    M = np.linalg.inv(np.dot(A,np.dot(W, A.T)))
    K = np.dot(M,f)

    return K