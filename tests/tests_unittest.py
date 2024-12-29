
# **************************************************************
# ************** APLICACIÓN DE LOS TEST UNITARIOS **************
# ***************** USO DEL PAQUETE UNITTEST *******************
# **************************************************************

import unittest
import numpy as np
import pandas as pd
from functions.functions import (
    count_word_details,
    impar_number,
    cummulative_impar_number,
    number_to_string,
    cummulative_string,
    check_user_character,
    word_starts_with_character,
    filter_words_by_starting_character
)


class TestFunctions(unittest.TestCase):

    def tests_function_count_word_details(self):
        """Tests Unitarios de la función count_word_details"""

        word_list = ["master", "formacion", "datos", "analitica", "aprendizaje", "estadistica"]

        word_vec = np.array(word_list)  # conversión a vector de numpy
        self.assertRaisesRegex(
            TypeError, "La entrada de la función debe ser una lista", count_word_details, word_vec
        )

        output = count_word_details(word_list)  # salida de la función
        self.assertIsInstance(output, pd.DataFrame)  # chequeo la salida es un dataframe
        self.assertEqual(output.shape[1], 2)  # chequeamos el número de columnas
        self.assertEqual(output.shape[0], 6)  # chequeamos el número de filas
        self.assertListEqual(list(output.columns), ["n_cocurrencia_palabra", "n_caracteres_palabra"])  # chequeamos el nombre de las columnas del dataframe

    def tests_function_impar_number(self):
        """Tests Unitarios de la función impar-par"""

        self.assertRaisesRegex(
            TypeError, "El valor introducido no es un número. Prueba otra vez.", impar_number, np.array(["hola"])
        )
        self.assertRaisesRegex(
            TypeError, "El valor introducido no es un número entero: 5.5. Prueba otra vez.", impar_number, 5.5
        )

        self.assertEqual(impar_number(5), 5)  # chequeamos que el número sea impar
        self.assertEqual(impar_number(6), 0)  # chequeamos que el número sea par

    def tests_function_cummulative_impar_number(self):
        """Tests Unitarios de la función cummulative_impar_number"""

        self.assertRaisesRegex(
            TypeError, "La entrada de la función debe ser una lista",
            cummulative_impar_number,
            np.array([15, 3, 10])
        )
        self.assertRaisesRegex(
            TypeError, "La entrada de la función debe ser una lista", cummulative_impar_number, 10
        )

        self.assertRaisesRegex(
            TypeError, "El valor introducido no es un número. Prueba otra vez.",
            cummulative_impar_number,
            [10, 5, 2, "uned"]
        )  # realmente está chequeando la función impar_number

        self.assertEqual(cummulative_impar_number([6, 4, 2]), 0)  # chequeamos resultado de la suma (igualdad)
        self.assertEqual(cummulative_impar_number([3, 2, 5, 10]), 8)  # chequeamos resultado de la suma (igualdad)
        self.assertGreater(cummulative_impar_number([15]), 0)  # chequeamos resultado de la suma (mayor que cero)
        self.assertLessEqual(cummulative_impar_number([15, 2, 5, 10, 5]), 30)  # chequeamos resultado de la suma (menor o igual)
        self.assertIsInstance(cummulative_impar_number([15, 2, 5, 10, 5]), (int, float))

    def tests_function_number_to_string(self):
        """Tests Unitarios de la función number_to_string"""

        self.assertRaisesRegex(
            TypeError, "El valor introducido no es un número. Prueba otra vez.", number_to_string, "hola"
        )
        self.assertRaisesRegex(
            TypeError, "El valor introducido no es un número entero: 5.5. Prueba otra vez.", number_to_string, 5.5
        )

        self.assertIsInstance(number_to_string(5), str)  # chequeamos la salida es un string
        self.assertEqual(len(number_to_string(5)), 5)  # chequeamos la longitud de la cadena de caracteres

    def tests_function_cummulative_string(self):
        """Tests Unitarios de la función cummulative_string"""

        self.assertRaisesRegex(
            TypeError, "La entrada de la función debe ser una lista",
            cummulative_string,
            np.array([10, 3])
        )

        output = cummulative_string([5, 2])
        self.assertIsInstance(output, pd.DataFrame)  # chequeo la salida es un dataframe
        self.assertEqual(output.shape[1], 2)  # chequeamos el número de columnas
        self.assertEqual(output.shape[0], 2)  # chequeamos el número de filas
        self.assertListEqual(list(output.columns), ["numero_entrada", "string"])  # chequeamos el nombre del dataframe

    def tests_function_check_user_character(self):
        """Tests Unitarios de la función check_user_character"""

        self.assertRaisesRegex(
            TypeError, "El input determinado para analizar la palabra debe ser un string",
            check_user_character,
            5
        )
        self.assertRaisesRegex(
            ValueError, "El string debe tener un carácter. El input es un string vacío",
            check_user_character,
            ""
        )
        self.assertRaisesRegex(
            ValueError, "Debes devolver una sola letra. Has devuelto: pablo",
            check_user_character,
            "pablo"
        )

        self.assertIsInstance(check_user_character("a"), str)  # chequeo la salida es un string
        self.assertTrue(check_user_character("p") == "p")
        self.assertFalse(check_user_character("p") == "P")  # esto solo es igual si le pasamos el tolower

    def tests_function_word_starts_with_character(self):
        """Tests Unitarios de la función word_starts_with_character"""

        self.assertRaisesRegex(
            TypeError, "La entrada debe ser un string",
            word_starts_with_character,
            50,
            50
        )  # la primera comparación es la de la palabra
        self.assertRaisesRegex(
            TypeError, "La entrada debe ser un string",
            word_starts_with_character,
            ["palabra"],
            50
        )  # la primera comparación es la de la palabra
        self.assertRaisesRegex(
            TypeError, "El input determinado para analizar la palabra debe ser un string",
            word_starts_with_character,
            "palabra",
            50
        )

        self.assertIsInstance(word_starts_with_character("palabra", "M"), str)  # chequeo la salida es un string
        self.assertTrue(word_starts_with_character("palabra", "P") == "palabra")  # coincide inicio de palabra con letra (output -> true)
        self.assertTrue(word_starts_with_character("datos", "P") == "")  # no coincide inicio de palabra con letra -> string vacío (output -> true)
        self.assertFalse(word_starts_with_character("datos", "P") == "datos")  # no coincide inicio de palabra con letra -> string vacío (output -> false)

    def tests_function_filter_words_by_starting_character(self):
        """Tests Unitarios de la función filter_words_by_starting_character"""

        words_list = ["master", "formacion", "uned", "analisis", "datos", "analitica"]

        self.assertIsInstance(filter_words_by_starting_character(words_list, "a"), str)  # chequeo la salida es un string
        self.assertTrue(filter_words_by_starting_character(words_list, "p") == "No hay ninguna palabra que comience por p")  # no hay palabras que empiecen por p
        self.assertTrue(filter_words_by_starting_character(words_list, "A") == "Hay 2 palabras que comienzan por A: analisis, analitica")
