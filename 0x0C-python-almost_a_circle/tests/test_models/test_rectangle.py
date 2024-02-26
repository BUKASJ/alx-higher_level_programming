import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        rectangle = Rectangle(10, 20, 5, 5, 1)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 5)

    def test_getters_setters(self):
        rectangle = Rectangle(10, 20, 5, 5, 1)

        rectangle.width = 15
        rectangle.height = 25
        rectangle.x = 10
        rectangle.y = 15

        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 25)
        self.assertEqual(rectangle.x, 10)
        self.assertEqual(rectangle.y, 15)


if __name__ == '__main__':
    unittest.main()
