# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import pandas
import glob
import os

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    # Lo haremos dos veces, uno para train y otro para test

    tipo_archivo = ["train", "test"]
    tipo_sentimiento = ["negative", "neutral", "positive"]

    # Creamos la carpeta
    directorio = "./files/output"
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    
    aux = 0

    for tipo in tipo_archivo:

        # Creamos las columnas
        columnas = ["phrase", "sentiment"]

        # Creamos el dataframe
        data_frame = pandas.DataFrame(columns =  columnas)

        # Creamos la lista
        lista_dataframes = []

        # Cargamos los datos
        for sentimiento in tipo_sentimiento:

            patron_sentimiento = "files/input/{0}/{1}/*.txt".format(tipo, sentimiento)

            # Cargamos los archivos
            archivos = glob.glob(patron_sentimiento)

            # Recorremos cada archivo y lo añadimos a la lista
            for archivo in archivos:

                # Cargamos la frase
                frase = open(archivo, "r").read()

                # Creamos un dataframe temporal
                df = pandas.DataFrame({"phrase": [frase], "sentiment": [sentimiento]})

                # Añadimos el sentimiento
                lista_dataframes.append(df)
        
        # Una vez tenemos todas las frases de un tipo: train o test
        # Guardamso todo en el dataframe
        data_frame = pandas.concat(lista_dataframes, ignore_index = True)

        # Guardamos el dataframe en formato csv
        direccion_guardado = "./files/output/{0}_dataset.csv".format(tipo)
        data_frame.to_csv(direccion_guardado)

    return 0