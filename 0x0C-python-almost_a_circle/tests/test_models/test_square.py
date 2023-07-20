import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_create_square(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_update_square(self):
        square = Square(5)
        square.update(10, 8, 2, 3)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 10)

    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 10)
        dictionary = square.to_dictionary()
        expected_dict = {'id': 10, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(dictionary, expected_dict)

if __name__ == '__main__':
    unittest.main()
