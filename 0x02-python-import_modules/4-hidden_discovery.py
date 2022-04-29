#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    modules = dir(hidden_4)
    for i in modules:
        if i[0] != '_':
            print(i)
