#!/usr/bin/python3
import sys
n = len(sys.argv)
print("{} arguments.".format(n))
for i in range(1, n):
    print(i, ":", end="")
    print(sys.argv[i])
