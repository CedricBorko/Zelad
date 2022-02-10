import unittest
from Logic.Math.vector2D import Vector2D

class TestVector2DMethods(unittest.TestCase):

    def test_magnitude(self): 
        self.assertEqual(Vector2D(3, 4).magnitude, 5)
        self.assertEqual(Vector2D(0, 4).magnitude, 4)
        self.assertEqual(Vector2D(0, 0).magnitude, 0)
        self.assertAlmostEqual(Vector2D(1, 1).magnitude, 2**0.5)

    def test_add(self): 
        self.assertEqual(Vector2D(3, 4) + Vector2D(-1, 5), Vector2D(2, 9))
        self.assertEqual(Vector2D(0, 4) + Vector2D(2, 2), Vector2D(2, 6))
        self.assertEqual(Vector2D(0, 0) + Vector2D(9, -0), Vector2D(-9, 0))

    def test_sub(self): 
        self.assertEqual(Vector2D(3, 4) - Vector2D(-1, 5), Vector2D(4, -1))
        self.assertEqual(Vector2D(0, 4) - Vector2D(2, 2), Vector2D(-2, 2))
        self.assertEqual(Vector2D(0, 0) - Vector2D(0.5, -2.6), Vector2D(-0.5, 2.6))
    
    def test_dot(self): 
        self.assertEqual(Vector2D(3, 4).dot(Vector2D(0, 4)), 16)
        self.assertEqual(Vector2D(-12, 4).dot(Vector2D(2, 2)), -16)
        self.assertEqual(Vector2D(0.5, -1.5).dot(Vector2D(0.5, 2)), -2.75)
    
    def test_normalize(self):
        self.assertEqual(Vector2D(3, 4).normalize(), Vector2D(0.12, 0.16))
        self.assertEqual(Vector2D(-12, 4).normalize(), Vector2D(0.085, 0.025))
        self.assertEqual(Vector2D(0.5, -1.5).normalize(), Vector2D(0.2, -0.6))



if __name__ == "__main__":
    unittest.main()