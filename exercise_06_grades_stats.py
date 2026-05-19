# Ejercicio 6 - Estadísticas de notas por estudiante


def grades_stats(filename):
    """
    Lee un archivo donde cada línea tiene el formato:

        estudiante:nota1,nota2,nota3,...

    y retorna un diccionario donde la clave es el nombre del estudiante y
    el valor es una TUPLA (promedio, maximo, minimo) con los tres valores
    como float.

    Reglas:
    - El promedio se calcula con todas las notas de la línea.
    - Las líneas vacías se ignoran.
    - Se garantiza que todas las notas son números válidos.
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, tuple[float, float, float]] - estadísticas por estudiante.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "Ana:8,9,7\nBeto:5,5,10\nCami:10\n"
        grades_stats("notas.txt") -> {
            "Ana": (8.0, 9.0, 7.0),
            "Beto": (6.666666666666667, 10.0, 5.0),
            "Cami": (10.0, 10.0, 10.0),
        }
    """
    diccionario = {}


    with open(filename, "r") as archivo:
        for line in archivo:
            line = line.strip()
            if line != "":
                lista = line.strip().split(":")
                if len(lista) == 2:
                    notas = lista[1].strip().split(",")
                    for i in range(len(notas)):
                        notas[i] = float(notas[i])
                    promedio = sum(notas) / len(notas)
                    maximo = max(notas)
                    minimo = min(notas)
                    tupla = (promedio, maximo, minimo)
                    diccionario[lista[0]] = tupla
        
    return diccionario