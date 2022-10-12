import unittest
from homework_11.task2 import Mathematician


class MathematicianTestCase(unittest.TestCase):

    def setUp(self):
        self.mathematician = Mathematician()

    def test_remove_positives(self):
        self.assertEqual(self.mathematician.remove_positives([26, -11, -8, 13, -90]), [-11, -8, -90])

    def test_square_nums(self):
        self.assertEqual(self.mathematician.square_nums([7, 11, 5, 4]), [49, 121, 25, 16])

    def test_filter_leaps(self):
        self.assertEqual(self.mathematician.filter_leaps([2001, 1884, 1995, 2003, 2020]), [1884, 2020])


