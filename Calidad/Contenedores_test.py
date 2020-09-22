import unittest
from Contenedores import *

class TestContenedores(unittest.TestCase):
    
    def test_cont(self):
        tests = (
            {'input' : 3, 'expect_out' : 27},
            {'input' : 5,'expect_out' : 125}
        )
