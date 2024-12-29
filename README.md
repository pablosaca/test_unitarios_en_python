# test_unitarios_en_Python

Ejemplos de test unitarios en Python usando los paquetes `unittest` y `pytest`

Para ejecutar los tests es necesario tener la estructura de carpetas en modo proyecto (desde la carpeta raíz)

El proyecto contiene dos carpetas (y scripts):

## functions/functions.py

Se dispone de una serie de funciones que realizan varias tares como:

Recibir un vector de palabras y devuelvor el número de veces que cada palabra se repite en el vector de entrada así como el número de caracteres que tiene cada palabra

Calcular la suma de los números impares proporcionados en una lista o vector de números

Recibir un vector de números enteros y devuelvor una serie de cadenas de texto aleatorias según los valores del vector

Imprimir aquellas palabras provenientes de una lista que empiecen por un carácter determinado

## tests/tests.py
Aplicación de los tests unitarios para las diferentes funciones

## Entorno de trabajo y dependencias

Se recomienda el uso de entorno de anaconda para crearse el proyecto de python:

```
conda create --name test_unitarios python=3.11
```
Para activar el entorno utiliza:
```
conda activate test_unitarios
```

Como puede verse, se ha trabajado con python==3.11 y las siguientes librerías en el entorno:

```
numpy==1.24.3
pandas==2.2.0
pytest==7.3.1
```
Para instalar los requerimientos del proyecto:

```
pip install -r requirements.txt
```


