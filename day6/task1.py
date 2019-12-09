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

    print(data)
    count = 0
    for d in data:
        count += len(d.split("."))

    print(count)



if __name__ == "__main__":
    assert len(sys.argv) > 1, "usage: <input of orbits>"
    main(set(sys.argv[1:]))
