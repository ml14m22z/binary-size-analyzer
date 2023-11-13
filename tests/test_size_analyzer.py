import unittest
from src.analyzer.size_analyzer import SizeAnalyzer


class TestSizeAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = SizeAnalyzer()

    def test_analyze_size(self):
        # Test with a binary file
        result = self.analyzer.analyze_size('/usr/bin/python')
        self.assertIsInstance(result, tuple)
        # self.assertIsInstance(result, dict)
        # self.assertIn('program_size', result)
        # self.assertIn('dependencies_size', result)

        # Test with a non-binary file
        with self.assertRaises(ValueError):
            self.analyzer.analyze_size('/etc/passwd')

        # Test with a non-existing file
        with self.assertRaises(FileNotFoundError):
            self.analyzer.analyze_size('/')


if __name__ == '__main__':
    unittest.main()
