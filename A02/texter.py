#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Texter script for Assignment A02
Author: Valerie Bizova
Description:
    Reads a text file and reports:
        a) total number of lines
        b) number of lines containing the word 'sed' (case-insensitive)
Usage:
    python texter.py <filename>
"""

import sys


class Texter:
    """Class for processing text files."""

    def __init__(self, filename=None):
        """Initialize with the given filename."""
        self.filename = filename

    def run(self):
        """Analyze the text file and print the required results."""
        if not self.filename:
            print("Usage: python texter.py <filename>")
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            total_lines = len(lines)
            sed_lines = sum(1 for line in lines if 'sed' in line.lower())

            print(f"Total number of lines: {total_lines}")
            print(f"Number of lines containing 'sed': {sed_lines}")

        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python texter.py <filename>")
    else:
        filename = sys.argv[1]
        texter = Texter(filename)
        texter.run()
