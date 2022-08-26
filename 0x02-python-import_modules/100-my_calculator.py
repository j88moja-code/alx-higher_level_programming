#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in list(ops.keys()):
        print("Unkown operator. Available operators    : +, -, * and /")
        quit(1)
    print("{} {} {} = {}".format(a, argv[2], b, ops[argv[2]](a, b)))
