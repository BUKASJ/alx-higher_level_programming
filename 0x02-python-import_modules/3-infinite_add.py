#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    arguments = argv[1:]
    result = sum(map(int, arguments))
    print(result)
