
import numpy as np
import math

def calc_dist(PA, PB, LAB):
    """
    Calcula la distancia entre dos puntos y la diferencia con la distancia medida.

    Parámetros:
    PA (np.array): Coordenadas del punto A (x, y).
    PB (np.array): Coordenadas del punto B (x, y).
    LAB (float): Distancia medida entre A y B.

    Retorna:
    distancia (float): Distancia calculada entre A y B.
    diferencia (float): Diferencia entre la distancia calculada y la medida.
    """
    distancia = np.sqrt((PB[0] - PA[0])**2 + (PB[1] - PA[1])**2)
    diferencia = distancia - LAB
    return distancia, diferencia

def deg_to_rad(deg, min, sec):
    return deg + min/60 + sec/3600

def calc_ang(PC, PI, PT, ANG_CIT):
    """
    Calcula el ángulo entre tres puntos y la diferencia con el ángulo medido.

    Parámetros:
    PC (np.array): Coordenadas del punto C (x, y).
    PI (np.array): Coordenadas del punto I (x, y).
    PT (np.array): Coordenadas del punto T (x, y).
    ANG_CIT (tuple): Ángulo medido (grados, minutos, segundos).

    Retorna:
    angulo (float): Ángulo calculado entre I, C y T en grados.
    diferencia (float): Diferencia entre el ángulo calculado y el medido.
    """
    # Calcular los ángulos
    ang_IC = math.atan2(PT[1] - PI[1], PT[0] - PI[0])
    ang_CT = math.atan2(PC[1] - PI[1], PC[0] - PI[0])

    # Calcular el ángulo entre los vectores
    angulo = math.degrees(ang_CT - ang_IC)

    # Convertir ángulo medido a grados decimales
    ang_medido = deg_to_rad(*ANG_CIT)

    # Normalizar el ángulo calculado
    if angulo < 0:
        angulo += 360

    diferencia = angulo - ang_medido
    return angulo, diferencia

def calc_acim(PA, PB, AZ_AB):
    """
    Calcula el azimut entre dos puntos y la diferencia con el azimut medido.
    Se usa math.atan2(delta_x, delta_y) para asegurar que el ángulo se mida respecto al eje Y,
    que es considerado como el norte (0°).
    PT = [X, Y]

    Parámetros:
    PA (np.array): Coordenadas del punto A (x, y).
    PB (np.array): Coordenadas del punto B (x, y).
    AZ_AB (tuple): Azimut medido (grados, minutos, segundos).

    Retorna:
    azimut (float): Azimut calculado entre A y B en grados.
    diferencia (float): Diferencia entre el azimut calculado y el medido.
    """
    delta_x = PB[0] - PA[0]
    delta_y = PB[1] - PA[1]
    azimut = math.degrees(math.atan2(delta_x, delta_y))

    # Convertir azimut medido a grados decimales
    azimut_medido = deg_to_rad(*AZ_AB)

    # Normalizar el azimut calculado
    if azimut < 0:
        azimut += 360

    diferencia = azimut - azimut_medido
    return azimut, diferencia
    
# Escalar las coordenadas por factor
def scalar_coordinates(coordinates, scale_factor):
    scaled_coordinates = coordinates.copy()
    scaled_coordinates[:, 1:] = scaled_coordinates[:, 1:].astype(float) * scale_factor
    return scaled_coordinates