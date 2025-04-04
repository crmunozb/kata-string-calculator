import re  # Lo usamos para poder dividir la cadena con delimitadores largos o múltiples usando expresiones regulares

def sumar(cadena):
    # Si no hay nada en la cadena, retornamos 0
    if cadena == "":
        return 0
    
    #por defecto usaremos la coma o el salto de linea como separador
    delimitador_regex = ",|\n"

    #Si parte con // usaremos un delimitador personalizado
    if cadena.startswith("//"):
        partes_delim = cadena.split("\n", 1)  # Separamos delimitador del resto
        encabezado = partes_delim[0]
        cadena = partes_delim[1]              # Ahora cadena solo tiene los números

        if encabezado.startswith("//["):
            # Si hay uno o varios delimitadores entre corchetes
            delimitadores = re.findall(r"\[(.*?)\]", encabezado)
            delimitador_regex = "|".join(map(re.escape, delimitadores))  # para que funcione con regex
        else:
            # Tomamos solo el delimitador de un caracter
            delimitador = encabezado[2:]
            delimitador_regex = re.escape(delimitador)

    # Cambiamos los saltos de línea por comas (ya no es necesario si usamos regex, pero lo dejamos por compatibilidad)
    cadena = cadena.replace("\n", ",")

    # Partimos la cadena usando el delimitador que se este usando
    partes = re.split(delimitador_regex, cadena)

    # Convertimos todas las partes a enteros
    numeros = list(map(int, partes))

    # Revisamos si hay algún número negativo
    negativos = [n for n in numeros if n < 0]
    if negativos:
        # Si hay negativos, lanzamos error porque no están permitidos
        raise ValueError("No se permiten números negativos")
    
    numeros_filtrados = [n for n in numeros if n <= 1000] #Se ignoraran numeros mayores a 1000

    # Si todo bien, devolvemos la suma
    return sum(numeros_filtrados)
