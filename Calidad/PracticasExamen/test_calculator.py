import unittest
from calculator import Calculator
from unittest.mock import patch

def mock(self, a, b):
    return self.a + self.b    

class testCalc(unittest.TestCase):
    #patch lleva el nombre del archivo, clase y la funcion que queremos simular
    @patch('calculator.Calculator.suma', expect = mock)        
    def testAdd(self, suma):
        #input = self.calc.sum(5, 90)
        self.assertEqual(15 + 85 , 100)
        
             
if __name__=='__main__':
    unittest.main()