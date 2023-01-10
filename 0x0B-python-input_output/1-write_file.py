#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    write_file - writes a string to a text file (UTF8),
                and returns the number of characters written:
    Args:
        filename: name of the file
        text: text to be written
    Return: number of bytes written.
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return (f.write(text))
