#!/usr/bin/env python3
# Author ID: ocoji

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        result = float(number1) + float(number2)
        # If both can be converted to float, we can return int if result is whole
        if result.is_integer():
            result = int(result)
        return result
    except Exception:
        return 'error: could not add numbers'

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except Exception:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                # works
    print(add('10', 5))              # works
    print(add('abc', 5))             # exception
    print(read_file('seneca2.txt'))  # works
    print(read_file('file10000.txt'))# exception
