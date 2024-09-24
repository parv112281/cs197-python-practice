import unittest
import number_of_ways


class TestNumberOfWay(unittest.TestCase):
    def test_number_of_ways_3(self):
        self.assertEqual(number_of_ways.number_of_ways(1, 2, 3), 3)