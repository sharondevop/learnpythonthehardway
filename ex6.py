x = "There are %d types of people." % 10  # create variable, with embedded variable inside a string by using format characters.
binary = "binary" # create variable
do_not = "don't" # create variable
y = "Those who know %s and those who %s." % (binary, do_not) # create variable, with embedded multiple variable inside a string by using format characters.

print x # print the variable x
print y # print the variable y

print "I said: %r" % x # print the string with a variable x
print "I also said: '%s'" % y # print the string with a variable y

hilarious = False # create a variable
joke_evaluation = "Isn't that joke so funny?! %r" # create a variable, with embedded format characters.

print joke_evaluation % hilarious # print the variable and add the string inside hilarious variable.

w = "This is the left side of..." # create a variable
e = "a string with a right side." # create a variable

print w + e # print variable w and add variable e to the same line.

