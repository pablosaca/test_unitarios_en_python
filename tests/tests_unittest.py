
# **************************************************************
# ************** APLICACIÓN DE LOS TEST UNITARIOS **************
# ***************** USO DEL PAQUETE UNITTEST *******************
# **************************************************************

import unittest
from functions.functions import euclidean_distance


class TestFunctions(unittest.TestCase):

    def tests_functional_euclidean_distance(self):
        """Tests Unitarios resultados funcionales de la función euclidean_distance"""

        _input_1 = {
            "first_point": (2, 3),
            "second_point": (2, 3)
        }
        output_1 = euclidean_distance(_input_1)  # salida de la función
        self.assertIsInstance(output_1, (int, float))  # chequeo la salida es un número
        self.assertEqual(output_1, 0)  # chequeamos que la distancia entre el mismo punto debe ser 0

        _input_2 = {
            "first_point": (2, 0),
            "second_point": (0, 0)
        }
        self.assertEqual(euclidean_distance(_input_2), 2)
        # el resultado es 2 porque: sqrt((2-0)^2 + (0-0)^2) -> solo nos movemos por el eje X, el eje Y es 0

        _input_3 = {
            "first_point": (16, 5),
            "second_point": (11, 3)
        }
        output_3 = euclidean_distance(_input_3)  # resultado teórico -> 5.385164807134504
        self.assertEqual(round(output_3, 3), 5.385)  # comparamos 3 decimales

    def tests_errors_euclidean_distance(self):
        """Tests Unitarios gestión de errores input de la función euclidean_distance"""

        # comprobamos que pasa si le pasamos una lista como input -> debe saltar un error porque solo admite diccionario
        # puedes probar a pasarle un texto, lista, número, etc.
        _input_0 = (2, 3, 2, 3)
        self.assertRaisesRegex(
            TypeError, "La entrada de la función debe ser un diccionario", euclidean_distance, _input_0
        )

        # hay que escapar los corchetes (uso de \ con [)
        _input_00 = {
            "first_point": (2, 3),
            "second_point": (4, 9),
            "tird_point": (0, 0)
        }
        self.assertRaisesRegex(
            ValueError,
            "El diccionario debe tener 2 claves. Has instroducido un diccionario con 3 claves",
            euclidean_distance,
            _input_00
        )

        # comprobamos que las claves del diccionario sean las admitidas por la función
        _input_1 = {
            "primer_punto": (2, 3),
            "segundo_punto": (2, 3)
        }
        # hay que escapar los corchetes (uso de \) en el mensaje comparativo
        self.assertRaisesRegex(
            ValueError,
            "Revisa los valores de entrada de las claves. Solo disponible \['first_point', 'second_point'\]",
            euclidean_distance,
            _input_1
        )
        # también podemos usar assertRaises sin mensaje, si bien, como es de esperar, es menos restrictivo
        self.assertRaises(ValueError, euclidean_distance, _input_1)

        # comprobamos que los valores de las coordenadas (claves) sean tuplas
        _input_2 = {
            "first_point": (2, 3),
            "second_point": [4, 8]
        }
        self.assertRaisesRegex(
            TypeError,
            "La posición de las coordenadas debe venir como tupla de valores enteros o float",
            euclidean_distance,
            _input_2
        )

        # comprobamos que los valores de las coordenadas (tuplas) tienen siempre una longitud de 2 (x, e y)
        _input_3 = {
            "first_point": (2, 3),
            "second_point": (4, 8, 10)
        }
        self.assertRaisesRegex(
            ValueError,
            "El tamaño de la tupla solo puede tener 2 elementos, actualmente tiene 3",
            euclidean_distance,
            _input_3
        )

       # comprobamos que los valores de las coordenadas (tuplas) sean siempre valores numéricos
        _input_4 = {
            "first_point": (2, 3),
            "second_point": (4, "8")
        }
        # hay que escapar los paréntesis (uso de \) en el mensaje comparativo
        self.assertRaisesRegex(
            ValueError,
            "Incorrecto valor en la tupla \(4, '8'\) que representa la posición de la coordenada. "
            "Solo se admiten números enteros o flaot",
            euclidean_distance,
            _input_4
        )
