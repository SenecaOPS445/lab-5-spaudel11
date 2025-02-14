#!/usr/bin/env python3
# Author ID: spaudel11

def read_file_string(file_name):
    
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data

def read_file_list(file_name):
    
    f = open(file_name, 'r')
    data = f.readlines()
    f.close()

    list_of_lines = [] 
    for line in data:
        list_of_lines.append(line.strip())
    return list_of_lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))