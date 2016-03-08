import sys

if( sys.argv.__len__() != 2 ):
    print("Usage: python basdasdafi.py <brainfuck_filename>")

# index: index of the current location in the data_map
# data_map: "document" where the brainfuck program will write
index = 0
data_map = [0] * 30000

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
                print(data_map[index], end='')
            elif char is ',':
                data_map[index] = sys.stdin.read(1)
            elif char is '[' or char is ']':
                print("Loops are not yet supported.")
