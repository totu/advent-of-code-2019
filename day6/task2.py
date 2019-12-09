#!/usr/bin/env python3
import sys

def find_parent(orbits, orbitter):
    for orbit in orbits:
        orbit = orbit.split(")")
        if orbitter == orbit[1]:
            return orbit[0]

def main(orbits):
    data = set()
    for orbit in orbits:
        parent, slave = orbit.split(")")

        end = False
        string = slave
        while(not end):
            grand_parent = find_parent(orbits, parent)
            if grand_parent is None:
                end = True
            else:
                string = "%s.%s" % (grand_parent, string)
                parent = grand_parent

        data.add(string)


    my_location = [d for d in data if "YOU" in d][0].split(".")
    santas_location = [d for d in data if "SAN" in d][0].split(".")
    for hop in my_location:
        for hop_to in santas_location:
            if hop == hop_to:
                common_planet = my_location.index(hop)
                break

    me_to_hop = len(my_location) - common_planet
    santa_to_hop = len(santas_location) - santas_location.index(my_location[common_planet])
    print(my_location)
    print(santas_location)
    distance_to_santa = int(me_to_hop + santa_to_hop)
    print(distance_to_santa - 2)



if __name__ == "__main__":
    assert len(sys.argv) > 1, "usage: <input of orbits>"
    main(set(sys.argv[1:]))
