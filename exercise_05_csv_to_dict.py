# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """

    diccionarios = []

    with open(filename, "r") as csvfile:
        lineas = csvfile.readlines()
        if len(lineas) != 0:
            lista = lineas[0].strip().split(",")
            for line in lineas[1:]:
                diccionario = {}
                nombres = line.strip().split(",")
                for i in nombres:
                    lugar = nombres.index(i)
                    if lugar == 1:
                        i = int(i)
                    diccionario[lista[lugar]] = i
                diccionarios.append(diccionario)
        return diccionarios



    pass  # Reemplazar con tu implementación
