#!/usr/bin/env python3
import sys

def main():
    assert len(sys.argv) == 3, "give <start> and <end> values"

    candidates = []
    for i in range(111111, 1000000):
        x = str(i)
        if x[0] <= x[1] <= x[2] <= x[3] <= x[4] <= x[5]:
            # Check for matching pair
            matching_pair = []
            for j in range(5):
                if int(x[j]) == int(x[j+1]):
                    matching_pair.append(x[j])

            # Check that no three match in a row
            three_matching = []
            for j in range(4):
                if int(x[j]) == int(x[j+1]) == int(x[j+2]):
                    three_matching.append(x[j])

            three_matching = set(three_matching)
            matching_pair = set(matching_pair)
            can_append = len(matching_pair) > 0

            if len(matching_pair) <= len(three_matching):
                for t in three_matching:
                    if t in matching_pair:
                        can_append = False

            if can_append:
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
