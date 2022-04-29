#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print(n, "argument:")
        print(n,":", sys.argv[1])
    else:
        print(n, "argument:")
        for i in range(1, n):
            print(i, ":", end="")
            print(sys.argv[i])
