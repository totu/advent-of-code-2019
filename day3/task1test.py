#!/usr/bin/env python3
import unittest
import task1

class TestDay1(unittest.TestCase):

    def test_shortest_distance_1(self):
        wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
        wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"

        wire1_coords = task1.get_wire_coords(wire1)
        wire2_coords = task1.get_wire_coords(wire2)
        shared_coords = task1.find_where_wires_cross(wire1_coords, wire2_coords)

        self.assertEqual(task1.find_shortest_distance(shared_coords), 159)

    def test_shortest_distance_2(self):
        wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
        wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

        wire1_coords = task1.get_wire_coords(wire1)
        wire2_coords = task1.get_wire_coords(wire2)
        shared_coords = task1.find_where_wires_cross(wire1_coords, wire2_coords)

        self.assertEqual(task1.find_shortest_distance(shared_coords), 135)


if __name__ == '__main__':
    unittest.main()



