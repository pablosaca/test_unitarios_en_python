
# **************************************************************
# ************** APLICACIÓN DE LOS TEST UNITARIOS **************
# ****************** USO DEL PAQUETE PYTEST ********************
# **************************************************************

import pytest
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


def test_count_word_details():

    word_list = ["master", "formacion", "datos", "analitica", "aprendizaje", "estadistica"]
    word_vec = np.array(word_list)

    # error cuando la entrada no es una lista
    with pytest.raises(TypeError, match="La entrada de la función debe ser una lista"):
        count_word_details(word_vec)

    output = count_word_details(word_list)  # salida de la función
    assert isinstance(output, pd.DataFrame)  # chequeo la salida es un dataframe
    assert output.shape[1] == 2  # chequeamos el número de columnas
    assert output.shape[0] == 6  # chequeamos el número de filas
    assert list(output.columns) == ["n_cocurrencia_palabra", "n_caracteres_palabra"]  # chequeamos el nombre de las columnas del dataframe


def test_impar_number():

    with pytest.raises(TypeError, match="El valor introducido no es un número. Prueba otra vez."):
        impar_number(np.array(["hola"]))

    with pytest.raises(TypeError, match="El valor introducido no es un número entero: 5.5. Prueba otra vez."):
        impar_number(5.5)

    assert impar_number(5) == 5  # chequeamos que el número sea impar
    assert impar_number(6) == 0  # chequeamos que el número sea par


def test_cummulative_impar_number():

    with pytest.raises(TypeError, match="La entrada de la función debe ser una lista"):
        cummulative_impar_number(np.array([15, 3, 10]))

    with pytest.raises(TypeError, match="La entrada de la función debe ser una lista"):
        cummulative_impar_number(10)

    with pytest.raises(TypeError, match="El valor introducido no es un número. Prueba otra vez."):
        cummulative_impar_number([10, 5, 2, "uned"])

    # Verificamos la salida de la suma
    assert cummulative_impar_number([6, 4, 2]) == 0    # chequeamos resultado de la suma (igualdad)
    assert cummulative_impar_number([3, 2, 5, 10]) == 8  # chequeamos resultado de la suma (igualdad)
    assert cummulative_impar_number([15]) > 0  # chequeamos resultado de la suma (mayor que cero)
    assert cummulative_impar_number([15, 2, 5, 10, 5]) <= 30  # chequeamos resultado de la suma (menor o igual)
    assert isinstance(cummulative_impar_number([15, 2, 5, 10, 5]), (int, float))


def test_number_to_string():

    with pytest.raises(TypeError, match="El valor introducido no es un número. Prueba otra vez."):
        number_to_string("hola")

    with pytest.raises(TypeError, match="El valor introducido no es un número entero: 5.5. Prueba otra vez."):
        number_to_string(5.5)

    # Verificamos que la salida sea un string y la longitud del string
    result = number_to_string(5)
    assert isinstance(result, str)  # chequeamos la salida es un string
    assert len(result) == 5  # chequeamos la longitud de la cadena de caracteres


def test_cummulative_string():

    with pytest.raises(TypeError, match="La entrada de la función debe ser una lista"):
        cummulative_string(np.array([10, 3]))

    output = cummulative_string([5, 2])
    assert isinstance(output, pd.DataFrame)  # chequeo la salida es un dataframe
    assert output.shape[1] == 2  # chequeamos el número de columnas
    assert output.shape[0] == 2  # chequeamos el número de filas
    assert list(output.columns) == ["numero_entrada", "string"]  # chequeamos el nombre del dataframe


def test_check_user_character():

    with pytest.raises(TypeError, match="El input determinado para analizar la palabra debe ser un string"):
        check_user_character(5)

    with pytest.raises(ValueError, match="El string debe tener un carácter. El input es un string vacío"):
        check_user_character("")

    with pytest.raises(ValueError, match="Debes devolver una sola letra. Has devuelto: pablo"):
        check_user_character("pablo")

    assert isinstance(check_user_character("a"), str)  # chequeo la salida es un string
    assert check_user_character("p") == "p"
    assert check_user_character("p") != "P"  # esto solo es igual si le pasamos el tolower


def test_word_starts_with_character():

    with pytest.raises(TypeError, match="La entrada debe ser un string"):
        word_starts_with_character(50, 50)

    with pytest.raises(TypeError, match="La entrada debe ser un string"):
        word_starts_with_character(["palabra"], 50)

    with pytest.raises(TypeError, match="El input determinado para analizar la palabra debe ser un string"):
        word_starts_with_character("palabra", 50)

    assert isinstance(word_starts_with_character("palabra", "M"), str)  # chequeo la salida es un string
    assert word_starts_with_character("palabra", "P") == "palabra"  # coincide inicio de palabra con letra (output -> true)
    assert word_starts_with_character("datos", "P") == ""  # no coincide inicio de palabra con letra -> string vacío (output -> true)
    assert word_starts_with_character("datos", "P") != "datos"  # no coincide inicio de palabra con letra -> string vacío (output -> false)


def test_filter_words_by_starting_character():

    words_list = ["master", "formacion", "uned", "analisis", "datos", "analitica"]

    # Verificamos el comportamiento cuando no hay palabras que empiezan con el carácter
    result = filter_words_by_starting_character(words_list, "p")
    assert isinstance(result, str)  # chequeo la salida es un string
    assert result == "No hay ninguna palabra que comience por p"  # no hay palabras que empiecen por p

    # Verificamos el comportamiento cuando hay palabras que empiezan con el carácter
    result = filter_words_by_starting_character(words_list, "A")
    assert isinstance(result, str)  # chequeo la salida es un string
    assert result == "Hay 2 palabras que comienzan por A: analisis, analitica"
