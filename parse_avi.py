#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

isVersionSet = None
filename = None

PROGRAM = "parse_avi"
VERSION = "0.0.1.SNAPSHOT"


def main():
    if not parse_args():
        sys.exit(1)

    if process_file(filename):
        sys.exit(0)
    else:
        sys.exit(1)


def parse_args():
    global filename

    parser = argparse.ArgumentParser("ParseAVI")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s " + VERSION)
    parser.add_argument("filename", help="choose file to parse")
    args = parser.parse_args()
    if not args.filename:
        parser.print_help()
        return False
    filename = args.filename
    return True


def process_file(filename):
    try:
        f = open(filename)
    except IOError:
        return False

    try:
        print f.read()
    finally:
        f.close()


if __name__ == "__main__":
    main()
