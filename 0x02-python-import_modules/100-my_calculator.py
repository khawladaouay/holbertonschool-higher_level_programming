#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    n = len(argv) - 1
    operations = {'+': add, '-': sub, '*': mul, '/': div}
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        for key in operations:
            if key == argv[2]:
                operation = operations.get(key)
                print(f'{a} {argv[2]} {b} = {operation(a, b)}')
                exit(0)
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
