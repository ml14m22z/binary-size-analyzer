import unittest
from src.utils import helper

class TestHelper(unittest.TestCase):

    def setUp(self):
        self.binary_file = 'path_to_binary_file'

    def test_read_binary_file(self):
        content = helper.read_binary_file(self.binary_file)
        self.assertIsNotNone(content)

    def test_calculate_size(self):
        size = helper.calculate_size(self.binary_file)
        self.assertIsInstance(size, int)

    def test_find_dependencies(self):
        dependencies = helper.find_dependencies(self.binary_file)
        self.assertIsInstance(dependencies, list)

if __name__ == '__main__':
    unittest.main()