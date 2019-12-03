#!/usr/bin/env python3
import sys
import math

def get_wire_coords(wire):
    """Plot out coordinates of given wire"""
    wire_coords = [(0,0)]
    x = 0
    y = 0
    for w in wire.split(","):
        length = int(w[1:])
        if w.startswith("U"):
            for l in range(length):
                y = y - 1
                wire_coords.append((x, y))
        if w.startswith("D"):
            for l in range(length):
                y = y + 1
                wire_coords.append((x, y))
        if w.startswith("L"):
            for l in range(length):
                x = x - 1
                wire_coords.append((x, y))
        if w.startswith("R"):
            for l in range(length):
                x = x + 1
                wire_coords.append((x, y))

    return wire_coords

def find_shortest_distance(coords):
    """Find shortest distance from 0,0 using 'Manhattan distance'"""
    shortest_distance = math.inf
    for coord in coords:

        # Skip start
        if coord[0] == coord[1] and coord[0] == 0:
            continue

        # Use absolute values since our coords go negative
        distance = abs(coord[0]) + abs(coord[1])
        if distance < shortest_distance:
            shortest_distance = distance

    return shortest_distance

def find_where_wires_cross(coords1, coords2):
    """Find and return intesections of the wires
    based on their coordinates
    """
    matches = []
    for coord in coords1:
        if coord in coords2:
            matches.append(coord)

    return matches

def main():
    #wire1 = "R8,U5,L5,D3"
    #wire2 = "U7,R6,D4,L4"
    wire1 = sys.argv[1]
    wire2 = sys.argv[2]

    wire1_coords = get_wire_coords(wire1)
    wire2_coords = get_wire_coords(wire2)
    shared_coords = find_where_wires_cross(wire1_coords, wire2_coords)

    shortest_distance = find_shortest_distance(shared_coords)

    print(shortest_distance)

if __name__ == '__main__':
    main()
