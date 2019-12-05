#!/usr/bin/env python3
import sys


def add(params, code, method):
    x = params[0]
    y = params[1]
    z = params[2]

    x = code[x] if not int(method[0]) else x
    y = code[y] if not int(method[1]) else y
    sum = x + y
    # print("%s + %s = %s" % (x, y, sum))
    code[z] = sum


def multiply(params, code, method):
    x = params[0]
    y = params[1]
    z = params[2]

    x = code[x] if not int(method[0]) else x
    y = code[y] if not int(method[1]) else y
    sum = x * y
    # print("%s * %s = %s" % (x, y, sum))
    code[z] = sum


def take_input(params, code, method):
    del method
    x = params[0]
    code[x] = int(sys.argv[2])


OUTPUTS = []


def output(params, code, method):
    del method
    x = params[0]
    OUTPUTS.append(code[x])


def exit(params, code, method):
    del params, method
    print(OUTPUTS)
    sys.exit()

opt_codes = {
    1: {"name": "add", "parameters": 3, "func": add},
    2: {"name": "multiply", "parameters": 3, "func": multiply},
    3: {"name": "input", "parameters": 1, "func": take_input},
    4: {"name": "output", "parameters": 1, "func": output},
    99: {"name": "halt", "parameters": 0, "func": exit},
}


def main():
    assert len(sys.argv) == 3, "usage: <instructions> <input>"
    codes = [int(x) for x in sys.argv[1].split(",")]

    i = 0
    last_i = -1

    while i != last_i:
        last_i = i
        print("%s/%s" % (i, len(codes)))
        code = int(codes[i])
        methods = str(code)[:-2]
        code = int(str(code)[-2:])

        assert code in opt_codes, code

        instruction = opt_codes[code]
        instruction_count = instruction["parameters"]
        params = [x for x in codes[i + 1 : i + instruction_count + 1]]
        methods = (
            "".join(["0" for x in range(len(params) - len(methods))]) + methods
        )
        methods = methods[::-1]
        i = i + instruction_count + 1
        try:
            instruction["func"](params, codes, methods)
        except IndexError:
            print(codes[:i])
            sys.exit(-1)

if __name__ == "__main__":
    main()
