# Search for a key word in a file in a dir and sub dirs
# Then print the file, line number and line

import os
import sys
import re

def search_file(file, key):
    """Search for a key word in a file and print the file, line number and line"""
    with open(file, "r", encoding="utf8") as f:
        try:
            for i, line in enumerate(f, 1):
                if key in line:
                    print(f'{file}, line {i}: {line.rstrip()}')
        
        except UnicodeDecodeError:
            pass

def search_dir(dir, key):
    """Search for a key word in a dir and sub dirs"""
    for root, dirs, files in os.walk(dir):
        for file in files:
            search_file(os.path.join(root, file), key)

search_dir(".\\tcl8.6.13", "TclCmd")


