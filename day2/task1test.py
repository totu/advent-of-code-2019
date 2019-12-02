#!/usr/bin/env python3
import sys
import unittest
import task1 

class TestDay1(unittest.TestCase):

    def test_calculate_fuel_consumption(self):
        test_values = [("1,0,0,0,99", "2,0,0,0,99"), ("2,3,0,3,99", "2,3,0,6,99"), ("2,4,4,5,99,0", "2,4,4,5,99,9801"), ("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99")]
        for input_value, expected_value in test_values:
            input_value = task1.verify_input(input_value)
            expected_value = task1.verify_input(expected_value)
            self.assertEqual(task1.do_intcode(input_value), expected_value)

if __name__ == '__main__':
    unittest.main()

    
