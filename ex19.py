# Function definition is here
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count # print string and the given argument inside a variable cheese_count and performs string formatting as a decimal integer.
    print "You have %d boxes of crackers!" % boxes_of_crackers # print string and the given argument variable boxes_of_crackers and performs string formatting as as a decimal integer.
    print "Man that's enough for a party!" # print a string
    print "Get a blanket.\n" # print a string and print a linebreak.


print "We can just give the function numbers directly:" # print string
cheese_and_crackers(20, 30) #input  arguments  for the function


print "OR, we can use variables from our script:" # print string
amount_of_cheese = 10 # define a new variable
amount_of_crackers = 50 # define a new variable

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # input variable as argument to function


print "We can even do math inside too:" # print string
cheese_and_crackers(10 + 20, 5 + 6) # input argument to the function as math


print "And we can combine the two, variables and math:" # print string
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #input argument to the funcation variable and math
