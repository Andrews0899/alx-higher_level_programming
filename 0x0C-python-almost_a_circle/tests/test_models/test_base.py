import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_constructor_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_constructor_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_to_json_string(self):
        b = Base()
        self.assertEqual(b.to_json_string([]), "[]")
        self.assertEqual(b.to_json_string(None), "[]")
        self.assertEqual(b.to_json_string([{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]),
                         '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]')

    def test_from_json_string(self):
        b = Base()
        self.assertEqual(b.from_json_string(""), [])
        self.assertEqual(b.from_json_string("[]"), [])
        self.assertEqual(b.from_json_string('[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'),
                         [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}])

    def test_save_to_file(self):
        b = Base()
        b.save_to_file([])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_load_from_file(self):
        b = Base()
        result = b.load_from_file()
        self.assertEqual(result, [])

    def test_create(self):
        b = Base()
        self.assertIsNone(b.create())

    def test_save_to_file_csv(self):
        b = Base()
        b.save_to_file_csv([])
        with open("Base.csv", "r") as file:
            content = file.read()
            self.assertEqual(content, "")

    def test_load_from_file_csv(self):
        b = Base()
        result = b.load_from_file_csv()
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
