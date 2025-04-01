import unittest # Framework de testing estandar en Python
from string_calculator import sumar # importar funcion sumar que se va a testear

class TestStringCalculator(unittest.TestCase): #Clase que contiene los test para la funcion Sumar
    def test_suma_dos_numeros(self):
        resultado = sumar("1,2") # Debe sumar los numeros 1 y 2
        self.assertEqual(resultado, 3) # Verificamos que el resultado sea 3

    def test_cadena_vacia_devuelve_cero(self): #Llamos la funcion sumar con una cadena vacia de entrada
        resultado = sumar("")
        self.assertEqual(resultado, 0) #Verificamos que el resultado es 0 , ya que no existen numeros para sumar

    def test_multiples_numeros(self):
        resultado = sumar ("4,5,6") # Debe sumar los numeros 4,5 y 6 
        self.assertEqual(resultado, 15) #Verificamos que el valor de la suma sea 15


if __name__ == '__main__': # Permite correr los test directamente al ejecutar este archivo
    unittest.main()
