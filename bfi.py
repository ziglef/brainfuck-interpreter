import sys

if( sys.argv.__len__() != 2 ):
    print("Usage: python bfi.py <brainfuck_filename>")

"""
    A brainfuck interpreter written in Python.
    It implements some extensions to the language which can be enabled by their
    repective command line flags.

    -x1 -> Adds extended functionality level 1
    -x2 -> Adds extended functionality level 2 (includes level 1)
    -x3 -> Adds extended functionality level 3 (invludes both level 1 and 2)

    The program (given level 3 extension) looks like this:
     ______________
    |              |
    |     Code     |
    |______________|
     ________________________________________________________________
    |           |                           |                        |
    |  Storage  |          Program          |          Data          |
    |___________|___________________________|________________________|

    The program is first read from the user inputed file into memory and then
    interpreted and executed.
"""

# Global values (Will be configurable)
MAX_FILE_SIZE = 30000
MAX_DATA_SIZE = 30000
MAX_CODE_SIZE = 30000

# "Static" values
code_ptr = 0                    # Current location of the code pointer
program_ptr = 0                 # Current location of the program pointer
code = []                       # Memory map where the code will be stored
storage = 0                     # The variable that will serve as storage
program = [0] * MAX_FILE_SIZE   # The memory that will be edited by the code
data = [0] * MAX_DATA_SIZE      # Where the input is with extended brainfuck

# Auxiliary stuff
bracer_ptr = 0                       # Current location of the stack pointer
bracer_stack = []                    # Locations of unmatched '[' and ']'
bracer_target = [0] * MAX_CODE_SIZE  # Locations of matching '[' and ']'

# Load the code to memory
with open(sys.argv[1]) as bf_file:
    code = bf_file.read()

# Interpretation:
# First find the pairs of '[' and ']' in the code
for char in code:
    if char is '[':  # If we locate a starting '[' we store its position
        bracer_stack.append(code_ptr)
    if char is ']':  # If we locate a ending ']' we will check if its unmatched
        if len(bracer_stack) is 0:
            print("Unmatched ']' in your code. Exiting...")
            exit()
        else:  # If everything is ok
            bracer_target[code_ptr] = bracer_stack.pop()
            bracer_target[bracer_target[code_ptr]] = code_ptr
    code_ptr += 1

# Check if any open '[' remained unmatched
if len(bracer_stack) > 0:
    print("Unmatched '[' in your code. Exiting...")
    exit()

# Then 'run' the program
code_ptr = 0
while code_ptr < len(code):
    if code[code_ptr] is '>':
        program_ptr += 1
    elif code[code_ptr] is '<' and program_ptr > 0:
        program_ptr -= 1
    elif code[code_ptr] is '+':
        program[program_ptr] += 1
    elif code[code_ptr] is '-' and program[program_ptr] > 0:
        program[program_ptr] -= 1
    elif code[code_ptr] is '.':
        print(chr(program[program_ptr]), end='')
    elif code[code_ptr] is ',':
        program[program_ptr] = sys.stdin.read(1)
    elif code[code_ptr] is '[' and program[program_ptr] is 0:
        code_ptr = bracer_target[code_ptr]
    elif code[code_ptr] is ']' and program[program_ptr] is not 0:
        code_ptr = bracer_target[code_ptr]

    code_ptr += 1
