#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = len(sys.argv) - 1
    print("{} argument{}{}".format(args, "" if args == 1 else "s", "." if args == 0 else ":"))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
