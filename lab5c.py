#!/usr/bin/env python3
# Author ID: spaudel11

def add(number1, number2):
    try:
        result = int(number1) + int(number2)
        return result
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError):
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))     
    print(add('10', 5))                 
    print(add('abc', 5))                   
    print(read_file('seneca2.txt'))      
    print(read_file('file10000.txt'))   
