import unittest
from math import sqrt
from qr import get_roots

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(set(get_roots(1, 2 ,3)), set())
    def test2(self):
        self.assertEqual(set(get_roots(1, -5, 6)), {-sqrt(3), -sqrt(2), sqrt(2), sqrt(3)})
    def test3(self):
        self.assertEqual(get_roots(0, 0, 0), 'infinity')
    def test4(self):
        self.assertEqual(set(get_roots(0, 1, -4)), set([-2, 2]))
    def test5(self):
        self.assertEqual(set(get_roots(1, 0, -81)), set([-3, 3]))


if __name__ == '__main__':
    unittest.main()