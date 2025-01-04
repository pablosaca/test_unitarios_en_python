
# ****************************************************************************
# ************ FUNCIONES PARA ILUSTRAR EL USO DE TEST UNITARIOS **************
# ****************************************************************************

import math


def euclidean_distance(values_dict):

    input_check(values_dict)  # chequeo de valores de entrada

    # calculo de la distancia euclíedea
    x0 = values_dict["first_point"][0]
    y0 = values_dict["first_point"][1]
    x1 = values_dict["second_point"][0]
    y1 = values_dict["second_point"][1]

    distance = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    return distance


def input_check(values_dict):

    if not isinstance(values_dict, dict):
        raise TypeError("La entrada de la función debe ser un diccionario")

    required_keys = ["first_point", "second_point"]
    input_keys = list(values_dict.keys())
    input_values = list(values_dict.values())

    if len(input_keys) != len(required_keys):
        raise ValueError(
            f"El diccionario debe tener 2 claves. Has instroducido un diccionario con {len(input_keys)} claves"
        )

    for ckey, ikey in zip(required_keys, input_keys):
        if ckey != ikey:
            raise ValueError(f"Revisa los valores de entrada de las claves. Solo disponible {list(required_keys)}")

    for value in input_values:
        if not isinstance(value, tuple) or len(value) != 2:
            raise ValueError(f"El valor {value} debe ser una tupla de 2 elementos")

        for i in value:
            if not isinstance(i, (int, float)):
                raise ValueError(
                    f"Incorrecto valor en la tupla {value} que representa la posición de la coordenada. "
                    "Solo se admiten números enteros o float"
                )
