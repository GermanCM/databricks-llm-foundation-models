import unittest

# Define una clase para tus pruebas
class MiPrueba(unittest.TestCase):

    # Define métodos de prueba que comienzan con "test_"
    def test_suma(self):
        resultado = 2 + 2
        self.assertEqual(resultado, 4)  # Verifica si el resultado es igual a 4

    def test_resta(self):
        resultado = 5 - 3
        self.assertEqual(resultado, 2)  # Verifica si el resultado es igual a 2

# Ejecuta las pruebas
if __name__ == '__main__':
    unittest.main()