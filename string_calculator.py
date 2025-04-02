def sumar(cadena):
    # Si no hay nada en la cadena, retornamos 0
    if cadena == "":
        return 0

    # Cambiamos los saltos de línea por comas
    cadena = cadena.replace("\n", ",")

    # Partimos la cadena usando la coma como separador
    partes = cadena.split(",")

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
