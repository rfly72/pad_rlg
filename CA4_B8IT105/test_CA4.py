
from CA4 import add, subtract, multiply, divide, exponent, cube, square, squareroot, factorial, sine, cosine
import unittest
class TestCalculator(unittest.TestCase):

        

        def testAdd(self):
                self.assertEqual(4, add(2,2))
                self.assertEqual(6, add(2,4))
                self.assertEqual(6, add(4,2))
                self.assertEqual(3, add(4,-1))
                self.assertEqual(0, add(-2,2))
                self.assertEqual(round(5/6.0, 4),
                                round(add(2/4.0, 2/6.0), 4))
                                
        def testSubtract(self):
                self.assertEqual(0, subtract(2,2))
                self.assertEqual(3, subtract(2,-1))
                
        def testMultiply(self):
                self.assertEqual(0, multiply(2,0))

        def testDivide(self):
                self.assertEqual(1, divide(5,5))
                #self.assertEqual("Not a number", divide(5,0))
                
        def testExponent(self):
                self.assertEqual(256, exponent(2,8))
                self.assertEqual(1, exponent(13,0))
                self.assertEqual(9, exponent(-3,2))
                self.assertEqual(-27, exponent(-3,3))
                
        def testCube(self):
                self.assertEqual(8, cube(2))
                self.assertEqual(0, cube(0))
                self.assertEqual(-27, cube(-3))
                
                
        def testSquare(self):
                self.assertEqual(16, square(4))
                self.assertEqual(0, square(0))
                self.assertEqual(25, square(-5))

        def testSquareRoot(self):
                self.assertEqual(5, squareroot(25))
                self.assertEqual(0, squareroot(0))
                
                
        def testFactorial(self):

                self.assertEqual(120, factorial(5))

                self.assertEqual(720, factorial (6))

                self.assertEqual(3628800, factorial(10))
                
        def testSine(self):
                self.assertEqual(0, sine(0))
                self.assertEqual(0.5, round(sine(30), 1))
                self.assertEqual(-1, sine(270))
                self.assertEqual(1, sine(90))
                self.assertEqual(0.70, round(sine(45), 1))
                self.assertEqual(-0.5, round(sine(-30), 1))
                
        def testCosine(self):
                self.assertEqual(1, cosine(0))
                self.assertEqual(round(0.86), 1, round(cosine(30), 1))
                self.assertEqual(-1, cosine(180))
                self.assertEqual(round(0.5,), 1, cosine(60))
                self.assertEqual(0.7, round(cosine(-45), 1))
                self.assertEqual(0, round(cosine(270), 1))


if __name__ == '__main__':
    unittest.main()