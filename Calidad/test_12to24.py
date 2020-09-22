import unittest
from time_12to24 import time_to24

class testConvertor(unittest.TestCase):
    def testCase(self):
        tst = [
            {'input':'02:23 PM', 'expect_out':'14:23 PM'},
            {'input':'11:42 PM', 'expect_out':'23:42 PM'},
            {'input':'11:42 AM', 'expect_out':'11:42 AM'},
            {'input':'12:00 PM', 'expect_out':'12:00 PM'},
            {'input':'12:00 AM', 'expect_out':'00:00 AM'},
            {'input':'01:05 AM', 'expect_out':'01:05 AM'},
            {'input':'11:59 PM', 'expect_out':'23:59 PM'}     
        ]
        
        for hours in tst:
            self.assertEqual(time_to24(hours['input']), hours['expect_out'])

if __name__=='__main__':
    unittest.main()