import sys

if( sys.argv.__len__() != 2 ):
    print("Usage: python bfi.py <brainfuck_filename>")

CODE_SIZE = 30000  # maximum size of the memory for the program
index = 0  # index of the current location in the data_map
data_map = [0] * CODE_SIZE  # memory map where the brainfuck program will write

# Open the file and process a single character at a time
with open(sys.argv[1]) as bf_file:
    for line in bf_file:
        for char in line:
            if char is '>':
                index += 1
            elif char is '<' and index > 0:
                index -= 1
            elif char is '+':
                data_map[index] += 1
            elif char is '-' and data_map[index] > 0:
                data_map[index] -= 1
            elif char is '.':
                print(chr(data_map[index]), end='')
            elif char is ',':
                data_map[index] = sys.stdin.read(1)
            elif char is '[' or char is ']':
                print("Loops are not yet supported.")
