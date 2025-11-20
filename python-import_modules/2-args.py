#!/usr/bin/python3

if __name__ == "__main__":
    import sys


    argument_length = len(sys.argv) - 1

    if argument_length == 0:
        print("0 arguments.")
    elif argument_length > 0:
        print("{} arguments:".format(argument_length))
        for i in range(1,len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))

