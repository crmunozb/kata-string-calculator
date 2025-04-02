def sumar(cadena):
    # Si no hay nada en la cadena, retornamos 0
    if cadena == "":
        return 0
    
    #por defecto usaremos la coma como separador

    delimitador = ","
    #Si parte con // usaremos un delimitador personalizado

    if cadena.startswith("//"):
        partes_delim = cadena.split("\n", 1)  # Separamos delimitador del resto
        delimitador = partes_delim[0][2:]     # Tomamos solo el delimitador
        cadena = partes_delim[1]              # Ahora cadena solo tiene los números


    # Cambiamos los saltos de línea por comas
    cadena = cadena.replace("\n", delimitador)

    # Partimos la cadena usando el delimitador que se este usando
    partes = cadena.split( delimitador)

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
