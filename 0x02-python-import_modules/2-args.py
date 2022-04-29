#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    print("{} arguments.".format(n))
    for i in range(1, n):
        print(i, ":", end="")
        print(sys.argv[i])
