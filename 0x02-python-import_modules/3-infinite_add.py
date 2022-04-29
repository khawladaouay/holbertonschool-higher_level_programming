#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    i = 1
    sum = 0
    if argc == 1:
        print("0")
    else:
        while i < argc:
            sum += int(argv[i])
            i += 1
        print(sum)
