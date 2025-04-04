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
        resultado = sumar ("1,2,3") # Debe sumar los numeros 1,2 y 3 
        self.assertEqual(resultado, 6) #Verificamos que el valor de la suma sea 6

    def test_soporta_saltos_de_linea(self):
        resultado = sumar("1\n2,3")  # Usa salto de línea \n y la coma "," como separadores
        self.assertEqual(resultado, 6)  # 1 + 2 + 3

    def test_no_se_permiten_numeros_negativos(self): # Si se incluye un número negativo, debe lanzar ValueError
        with self.assertRaises(ValueError): # con "With self.assertRaises (..)" le dice a python que esperamos recibir un error. Si no lanza el error, el test falla
            sumar("-1,-2,3")

    def test_ignorar_numeros_mayores_a_1000(self):
        #Ej: Si esta el numero 1001 , este será ignorado
         resultado = sumar("2,1001")
         self.assertEqual(resultado,2) #Como ignorará el 1001, solamente va a mostrar el numero 2
    
    def test_delimitador_personalizado(self):
        resultado = sumar("//;\n1;2")
        self.assertEqual(resultado,3) # 1 + 2 = 3 con ; como separador
    
    def test_delimitador_largo_personalizado(self):
        #Para este caso , el delimitador seria "***"
        resultado = sumar("//[***]\n1***2***3")
        self.assertEqual(resultado,6)# suma de 1+2+3

if __name__ == '__main__': # Permite correr los test directamente al ejecutar este archivo
    unittest.main()
