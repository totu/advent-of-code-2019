#!/usr/bin/env python3
import sys
sys.path.append("..")
import unittest
import task2

class TestDay1Task2(unittest.TestCase):

    def test_calculate_fuel_consumption(self):
        test_values = [(12, 2), (1969, 966), (100756, 50346)]
        for input_value, expected_value in test_values:
            self.assertEqual(task2.calculate_fuel_consumption(input_value), expected_value)

if __name__ == '__main__':
    unittest.main()

    
