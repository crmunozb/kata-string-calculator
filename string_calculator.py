def sumar(cadena):
    # Si la cadena está vacía, no hay números para sumar y retorna 0
    if cadena == "":
        return 0
    
    # Usamos split(",") para separar 
    # Ej: "4,5,6" seria ['4', '5', '6']
    partes = cadena.split(",")
    
    # Usamos map(int, ...) para convertir cada parte a entero
    # Ej: ['4', '5', '6'] -> [4, 5, 6]
    numeros = map(int, partes)
    # Sumamos todos los números y retornamos el resultado
    return sum(numeros)
