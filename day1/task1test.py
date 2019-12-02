#!/usr/bin/env python3
import sys
sys.path.append("..")
import unittest
import task1 

class TestDay1(unittest.TestCase):

    def test_calculate_fuel_consumption(self):
        test_values = [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
        for input_value, expected_value in test_values:
            self.assertEqual(task1.calculate_fuel_consumption(input_value), expected_value)

if __name__ == '__main__':
    unittest.main()

    
