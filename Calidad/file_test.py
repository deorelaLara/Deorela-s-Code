import unittest
from file import countChar

class TestFile(unittest.TestCase):
    def test_file(self):
        lectura =countChar('c:/Users/deore/OneDrive/Escritorio/Python/Calidad/test.txt')
        self.assertEqual(lectura, 16) #manda mensaje de error si falla (excepcion)

if __name__=="__main__":
    unittest.main()
