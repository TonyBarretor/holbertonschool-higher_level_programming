#!/usr/bin/python3
if __name__ == "__main__":
    a = 1
    b = 2
    exec(open("add_0.py").read())
    print("{} + {} = {}".format(a, b, add(a, b)))
