#!/usr/bin/env python3
import sys
import copy
import task1

program = []

with open("input", "r") as input_file:
    program = [int(x) for x in input_file.read().split(",")]

for noun in range(100):
    for verb in range(100):
        copy_of_program = copy.deepcopy(program)
        copy_of_program[1] = noun
        copy_of_program[2] = verb
        result = task1.do_intcode(copy_of_program)
        if result[0] == 19690720:
            print("noun: %s" % noun)
            print("verb: %s" % verb)
            print("100 * noun + verb: %s" % (100 * int(noun) + int(verb)))
            sys.exit(0)

assert False, "Program reached end without finding what it was looking for!"

