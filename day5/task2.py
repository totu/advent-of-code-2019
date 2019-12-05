#!/usr/bin/env python3
import sys

POINTER = 0

def add(params, code, method):
    x = params[0]
    y = params[1]
    z = params[2]

    x = code[x] if not int(method[0]) else x
    y = code[y] if not int(method[1]) else y
    sum = x + y
    # print("%s + %s = %s" % (x, y, sum))
    code[z] = sum
    global POINTER
    POINTER = POINTER + len(params) + 1


def multiply(params, code, method):
    x = params[0]
    y = params[1]
    z = params[2]

    x = code[x] if not int(method[0]) else x
    y = code[y] if not int(method[1]) else y
    sum = x * y
    # print("%s * %s = %s" % (x, y, sum))
    code[z] = sum
    global POINTER
    POINTER = POINTER + len(params) + 1


def take_input(params, code, method):
    del method
    x = params[0]
    code[x] = int(sys.argv[2])
    global POINTER
    POINTER = POINTER + len(params) + 1


OUTPUTS = []


def output(params, code, method):
    x = params[0]
    x = code[x] if not int(method[0]) else x
    OUTPUTS.append(x)
    global POINTER
    POINTER = POINTER + len(params) + 1

def exit(params, code, method):
    del params, method
    print(OUTPUTS)
    sys.exit()

def jump_if_true(params, code, method):
    x = params[0]
    y = params[1]

    x = code[x] if not int(method[0]) else x
    y = code[y] if not int(method[1]) else y

    global POINTER
    if x != 0:
        POINTER = y
    else:
        POINTER = POINTER + len(params) + 1

def jump_if_false(params, code, method):
    x = params[0]
    y = params[1]

    x = code[x] if not int(method[0]) else x
    y = code[y] if not int(method[1]) else y

    global POINTER
    if x == 0:
        POINTER = y
    else:
        POINTER = POINTER + len(params) + 1

def less_than(params, code, method):
    x = params[0]
    y = params[1]
    z = params[2]

    x = code[x] if not int(method[0]) else x
    y = code[y] if not int(method[1]) else y

    if x < y:
        code[z] = 1
    else:
        code[z] = 0

    global POINTER
    POINTER = POINTER + len(params) + 1

def equals(params, code, method):
    x = params[0]
    y = params[1]
    z = params[2]

    x = code[x] if not int(method[0]) else x
    y = code[y] if not int(method[1]) else y

    if x == y:
        code[z] = 1
    else:
        code[z] = 0

    global POINTER
    POINTER = POINTER + len(params) + 1

opt_codes = {
    1: {"name": "add", "parameters": 3, "func": add},
    2: {"name": "multiply", "parameters": 3, "func": multiply},
    3: {"name": "input", "parameters": 1, "func": take_input},
    4: {"name": "output", "parameters": 1, "func": output},
    5: {"name": "jump-if-true", "parameters": 2, "func": jump_if_true},
    6: {"name": "jump-if-false", "parameters": 2, "func": jump_if_false},
    7: {"name": "less-than", "parameters": 3, "func": less_than},
    8: {"name": "equals", "parameters": 3, "func": equals},
    99: {"name": "halt", "parameters": 0, "func": exit},
}


def main():
    global POINTER
    assert len(sys.argv) == 3, "usage: <instructions> <input>"
    codes = [int(x) for x in sys.argv[1].split(",")]

    last_pointer = -1

    while POINTER != last_pointer:
        last_pointer = POINTER
        print("%s/%s" % (POINTER, len(codes)))
        code = int(codes[POINTER])
        methods = str(code)[:-2]
        code = int(str(code)[-2:])

        assert code in opt_codes, "%s : %s" % (codes, code)

        instruction = opt_codes[code]
        instruction_count = instruction["parameters"]
        params = [x for x in codes[POINTER + 1 : POINTER + instruction_count + 1]]
        methods = (
            "".join(["0" for x in range(len(params) - len(methods))]) + methods
        )
        methods = methods[::-1]
        try:
            instruction["func"](params, codes, methods)
        except IndexError:
            print("INDEX ERROR!")
            print(codes[:POINTER+len(params)+1])
            sys.exit(-1)
    print(code, params, methods)
    print(codes[:POINTER+len(params)+1])

if __name__ == "__main__":
    main()
