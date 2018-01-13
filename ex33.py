# Assignment 0 to variable i
i = 0
numbers = [] # Create empty list

def append_to_numbers_and_count(limit, increment):
    i = 0
    numbers = []

    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

append_to_numbers_and_count(6,2)

#print "The numbers: "
#x = append_to_numbers_and_count(6,2)
#print x


