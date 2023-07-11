#!/usr/bin/python3
# 1-write_file.py
"""Defines a text file line-counting function."""


def write_file(filename="", text=""):
    """Return the number of lines in a text file."""
    lines = 0
    with open(filename) as fn:
        for line in fn:
            lines += 1
        return lines
