import unittest
from main import Calculator


class TestMath(unittest.TestCase):

    def test_add(self):
        calc = Calculator()
        calc.add(2)
        self.assertEqual(calc.current, 2, "Wrong")

    def test_subtract(self):
        calc = Calculator()
        calc.add(3)
        calc.subtract(3)
        self.assertEqual(calc.current, 0, "Wrong")

    def test_multiply(self):
        calc = Calculator()
        calc.add(2)
        calc.multiply(2)
        self.assertEqual(calc.current, 4, "Wrong")

    def test_divide(self):
        calc = Calculator()
        calc.add(4)
        calc.divide(2)
        self.assertEqual(calc.current, 2, "Wrong")

    def test_exponentiate(self):
        calc = Calculator()
        calc.add(7)
        calc.exponentiate(2)
        self.assertEqual(calc.current, 49, "Wrong")

    def test_sqrt(self):
        calc = Calculator()
        calc.add(49)
        calc.sqrt()
        self.assertEqual(calc.current, 7.0, "Wrong")

    def test_reset(self):
        calc = Calculator()
        calc.add(10)
        calc.reset()
        self.assertEqual(calc.current, 0, "Wrong")


if __name__ == "__main__":
    unittest.main()