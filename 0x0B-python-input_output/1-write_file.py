#!/usr/bin/python3

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of
    characters written."""
    with open(filename, "w", encoding="utf8") as file:
        chars_written = file.write(text)
        return chars_written
