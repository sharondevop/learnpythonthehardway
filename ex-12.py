from sys import argv

age = raw_input("How old are you? ")  # print to stdut How old are you ? , and assign the input to age variable
height = raw_input("How tall are you? ") # print to stdut How tall are you?  , and assign the input to height variable
weight = raw_input("How much do you weigh? ") # print to stdut How much do you weigh?  , and assign the input to weight variable

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight) # print the string and format the given variable as row data.
