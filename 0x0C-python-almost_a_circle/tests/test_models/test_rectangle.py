import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        r = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 10)

    def test_area(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n" \
                          "###\n"
        with unittest.mock.patch('sys.stdout', new=unittest.mock.StringIO()) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        r = Rectangle(4, 5)
        r.update(10, 2, 3, 1, 2)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_to_dictionary(self):
        r = Rectangle(4, 5, 1, 2, 10)
        expected_dict = {
            "id": 10,
            "width": 4,
            "height": 5,
            "x": 1,
            "y": 2
        }
        self.assertDictEqual(r.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
