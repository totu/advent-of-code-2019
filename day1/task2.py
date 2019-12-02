#!/usr/bin/env python3
"""Same as task 1, but now fuel also has a weight"""

import sys
import math


def print_help():
    """Print help for the user and exit with -1"""
    print("usage: %s <int>" % sys.argv[0])
    sys.exit(-1)


def get_input():
    """Check that we got an integer from CLI

    If arg is missing or not int tell the user

    Expect mass to be given as the first argument for the program
    """

    # check that we just got one int
    if len(sys.argv) != 2:
        print_help()

    try:
        # convert CLI arg to int
        mass = int(sys.argv[1])
    except TypeError:
        print_help()

    return mass


def calculate_fuel_consumption(mass):
    """Calculate fuel needed based on the mass of the Elves

    Formula: mass / 3 (rounded down) - 2

    Recurse until fuel needed for the fuel is 0 or less (this is done by wishing)
    """
    total_fuel_needed = 0
    fuel_needed = math.floor(mass / 3 - 2)
    if fuel_needed > 0:
        total_fuel_needed = fuel_needed
        total_fuel_needed += calculate_fuel_consumption(fuel_needed)
    return total_fuel_needed


def main():
    mass = get_input()
    fuel_needed = calculate_fuel_consumption(mass)
    print(fuel_needed)


if __name__ == "__main__":
    main()
