import unittest
from platillo import Platillo, Ingrediente

class TestPlatillo(unittest.TestCase):
    def testAddIngrediente(self):
        testCases = [
            {
                'name':'Agregar 1 elemento',
                'input' : [Ingrediente('papa', 'gr', '500'), 200], #entrada
                'list_final' : [ #salida esperada
                    {'ingrediente': Ingrediente('papa','gr','500'), 'cantidad': 200},
                ],
            },
            {
                'name' : 'Agregar 2 elementos',
                'input' : (
                    [Ingrediente('papa', 'gr', '500'), 200],
                    [Ingrediente('tomate', 'gr', '250'), 545]
                    ),
                'list_final' : [
                    {'ingrediente' : Ingrediente('papa', 'gr', '500'), 'cantidad': 200},
                    {'ingrediente' : Ingrediente('tomate', 'gr', '250'), 'cantidad' : 545}
                ],
            },
        ]
        
        for tc in testCases:
            plat = Platillo()
            plat.addIngrediente(tc['input'][0], tc['input'][1])
            
            for ing in tc['list_final']:
                inResult = False
                for ingResult in plat.ingredientes:
                    if ingResult['ingrediente'].nombre == ing['ingrediente'].nombre:
                        inResult = True
                        self.assertEqual(ing['cantidad'], ingResult['cantidad'])
                if not inResult:
                        self.fail('No se encontro el ingrediente {}'.format(ing.name))
        
        
if __name__=='__main__':
    unittest.main()