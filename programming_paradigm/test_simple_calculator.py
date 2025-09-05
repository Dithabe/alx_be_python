import unittest 
from simple_calculator import SimpleCalculator

class testing(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5,8), 13) 

    def test_subtraction(self):
        result = SimpleCalculator.subtract(15,5)   
        self.assertEqual(result, 13) 
        
    def test_divide(self):
        result = SimpleCalculator.divide(6,3)
        self.assertEqual(result, 2)

    def tes_multiply(self):
        result = SimpleCalculator.multiply(8,2)
        self.assertEqual(result, 16)

    

