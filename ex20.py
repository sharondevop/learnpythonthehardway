from sys import argv

script, input_file = argv

# Create a function to print the contant of a file.
def print_all(f):
    print f.read()

# Create a function to postion the read a head to the start of a file.
def rewind(f):
    f.seek(0)

# Create a function to print one line.
def print_a_line(line_count, f):
    print line_count, f.readline()

# create a variable pointing to a file.
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# Create a variable with value 1 , print the number 1
# read one line from the file.
current_line = 1
print_a_line(current_line, current_file)

# Add right operand to the left operand and assign the result to the left operand
# print the number 2 and read one line from the file.
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

