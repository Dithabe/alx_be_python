import unittest 
from simple_calculator import SimpleCalculator

class testing(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5,8), 13) 

    def test_subtraction(self):   
        self.assertEqual(self.calc.subtract(15,5), 13) 
        
    def test_division(self):
        self.assertEqual(self.calc.divide(6,3), 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(8,2), 16)

    




