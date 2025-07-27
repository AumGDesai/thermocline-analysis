"""
Aum Desai
Fall 2022
CS152B Lab 03

This program is for Lab 03. It explores the basics of using sys.argv
"""

import sys

print(sys.argv)

print("Running program", sys.argv[0])
print("I'm going to open file", sys.argv[1])
print("I'm going to extract column", int(sys.argv[2]))

