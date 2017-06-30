#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys

isDirSet = False
directory = None


def main():
    if not parse_args():
        sys.exit(1)

    if process_dir(directory):
        sys.exit(0)
    else:
        sys.exit(1)


def parse_args():
    global isDirSet
    global directory

    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", help="choose directory to traverse")
    args = parser.parse_args()
    if not args.dir:
        parser.print_help()
        return False
    isDirSet = True
    directory = args.dir
    return True


def process_dir(directory):
    if directory is None or directory == "":
        return False
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file = os.path.join(dirpath, filename)
            print file
            process_file(file)
    return True


def process_file(file):
    try:
        f = open(file)
    except IOError:
        return False
    try:
        print f.read()
    finally:
        f.close()


if __name__ == "__main__":
    main()
