#!/usr/bin/env python3
import sys

def main():
    assert len(sys.argv) == 3, "give <start> and <end> values"

    candidates = []
    for i in range(111111, 1000000):
        x = str(i)
        if x[0] <= x[1] <= x[2] <= x[3] <= x[4] <= x[5]:
            if x[0] == x[1] or x[1] == x[2] or x[2] == x[3] or x[3] == x[4] or x[4] == x[5]:
                candidates.append(i)


    start = int(sys.argv[1])
    end = int(sys.argv[2])

    possible_password = []
    for i in range(start, end+1):
        if i in candidates:
            possible_password.append(i)


    print(len(possible_password))


if __name__ == "__main__":
    main()
