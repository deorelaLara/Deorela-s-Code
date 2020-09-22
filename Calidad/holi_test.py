import unittest
from holis import fib
#herencia
class TestFib(unittest.TestCase):
    def test_fib(self):
        entradas = [8, 3, 0] 
        salidas_esperadas = [21, 2, 0]
        for entradas, salidas_esperadas in zip(entradas, salidas_esperadas):
            salida_real = fib(entradas)
            self.assertEqual(salidas_esperadas, salida_real) #manda mensaje de error si falla (excepcion)
    

if __name__ == "__main__":
    unittest.main()
