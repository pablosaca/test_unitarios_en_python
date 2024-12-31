
# ****************************************************************************
# ************ FUNCIONES PARA ILUSTRAR EL USO DE TEST UNITARIOS **************
# ****************************************************************************

import random
import string
import pandas as pd


def count_word_details(word_vec):

    if not isinstance(word_vec, list):
        raise TypeError("La entrada de la función de debe ser una lista")

    # con la función set nos quedamos con los valores únicos de frecuencias
    # podemos iterar sobre él para contar las veces que un elemento/palabra se repite
    word_count = {word: word_vec.count(word) for word in set(word_vec)}

    # Se generan diccionarios para ir incorporando las longitude de las palabras y concurrencias
    letter_reporting_dict = {}
    concurrence_reporting_dict = {}
    for word, count in word_count.items():
        letter_reporting_dict[word] = len(word)  # cuenta longitud de cada palabra
        concurrence_reporting_dict[word] = count  # se añade al diccionario el número de veces que aparece la palabra en la secuencia a analizar

    # finalmente, se crea un dataframe como formato de salida
    reporting_df = pd.DataFrame({
        'n_cocurrencia_palabra': concurrence_reporting_dict,
        'n_caracteres_palabra': letter_reporting_dict
    })

    return reporting_df


def impar_number(n):

    # chequea si el valor no es numérico
    if not isinstance(n, (int, float)):
        raise TypeError("El valor introducido no es un número. Prueba otra vez.")

    # chequea si el valor no es un número entero
    if n != int(n):
        raise TypeError(f"El valor introducido no es un número entero: {n}. Prueba otra vez.")

    if int(n) % 2 != 0:
        return int(n)  # devuelve el número que se le pasa a la función
    else:
        return 0  # devuelve siempre 0


def cummulative_impar_number(input_):

    if not isinstance(input_, list):
        raise TypeError("La entrada de la función debe ser una lista")

    cum_number_list = []  # lista donde se va a obtener la suma acumulada
    # Iteramos sobre los elementos de la lista
    for value in input_:
        result = impar_number(value)  # chequea si el número es par o impar
        cum_number_list.append(result)  # incluimos los valores en la lista acumulada

    return sum(cum_number_list)  # suma de los vectores


def number_to_string(n):

    # chequea si el valor no es numérico
    if not isinstance(n, (int, float)):
        raise TypeError("El valor introducido no es un número. Prueba otra vez.")

    # chequea si el valor no es un número entero
    if n != int(n):
        raise TypeError(f"El valor introducido no es un número entero: {n}. Prueba otra vez.")

    # la función interna ascii_lowercase del paquete string proporciona un vector de caracteres con las letras del abecedario
    random_string = ''.join(random.choices(string.ascii_lowercase, k=int(n)))
    return random_string.upper()


def cummulative_string(input_):

    if not isinstance(input_, list):
        raise TypeError("La entrada de la función debe ser una lista")

    cum_vec = []  # lista donde se va a obtener la suma acumulada
    for n in input_:
        string = number_to_string(n)
        cum_vec.append(string)

    return pd.DataFrame({
        'numero_entrada': input_,
        'string': cum_vec
    })


def check_user_character(character):

    if not isinstance(character, str):
        raise TypeError("El input determinado para analizar la palabra debe ser un string")

    # comprueba si se ha indicado un string vacío
    if len(character) == 0:
        raise ValueError("El string debe tener un carácter. El input es un string vacío")

    # comprueba si el string contiene más de un carácter
    if len(character) > 1:
        raise ValueError(f"Debes devolver una sola letra. Has devuelto: {character}")

    return character


def word_starts_with_character(word, character):

    if not isinstance(word, str):
        raise TypeError("La entrada debe ser un string")

    if not isinstance(character, str):
        raise TypeError("El input determinado para analizar la palabra debe ser un string")

    word = word.strip().lower()   # elimina espacios en blanco al principio y al final
    character = character.strip().lower()  # convierte la palabra a minúsculas

    # se extrae la primera letra de la palabra y se compara con la letra indicada
    return word if word.startswith(character) else ""


def filter_words_by_starting_character(input_, character):

    character = check_user_character(character)

    word_list = []  # inicialización un vector vacío para almacenar las palabras
    # se recorre la lista de palabras y se incluyen aquellas que cumplan la condición
    for word in input_:
        output = word_starts_with_character(word, character)
        if len(output) > 0:
            word_list.append(word)

    # si no hay palabras, se indica
    if len(word_list) == 0:
        return f"No hay ninguna palabra que comience por {character}"
    else:
        return f"Hay {len(word_list)} palabras que comienzan por {character}: {', '.join(word_list)}"
