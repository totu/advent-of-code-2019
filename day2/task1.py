#!/usr/bin/env python3
import sys

def print_help_and_exit():
    """Print out usage help for the user and exit with -1"""
    print("usage: %s <comma separated list of ints>" % sys.argv[0])
    sys.exit(-1)


def verify_input(args):
    """Verify that input is indeed list of ints"""
    try:
        code = [int(x) for x in args.split(',')]
    except TypeError:
        print_help_and_exit()

    return code


def main():
    # Rudamentary check on input
    if len(sys.argv) != 2:
        print_help_and_exit()

    code = verify_input(sys.argv[1])
    code = do_intcode(code)
    print(",".join([str(x) for x in code]))


def do_intcode(code):
    """take in list of ints and performs Intcode arithmetic on it

    opcodes:
    - 1: add
    - 2: multiply
    - 99: halt
    """
    current_position = 0
    while(current_position < len(code)):
        opt = code[current_position]
        assert opt in [1, 2, 99], "optcode (%s) not in expected values" % opt
        if opt == 99:
            break
        else:
            pos1, pos2, pos3 = code[current_position+1:current_position+4]
            if opt == 1:
                val = code[pos1] + code[pos2]
            elif opt == 2:
                val = code[pos1] * code[pos2]
            code[pos3] = val
        current_position = current_position + 4

    return code

if __name__ == '__main__':
    main()
