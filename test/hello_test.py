import unittest
from src import hello


class NamesTestCases(unittest.TestCase):
    def test_canary(self):
        self.assertEqual(True, True)

    def test_add(self):
        self.assertEqual(hello.add(1, 2), 3)


if __name__ == '__main__':
        unittest.main()
