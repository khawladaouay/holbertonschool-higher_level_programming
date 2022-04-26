#!/usr/bin/python3
def uppercase(str):
    Str1 = ""
    for i in range(len(str)):
        ASC = ord(str[i])
        if (ASC >= 97 and ASC <= 122):
            Str1 += chr(ASC - 32)
            continue
        Str1 += str[i]
    print('{}'.format(Str1))
