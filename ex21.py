# Exercise 21: Functions Can Return Something

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"


age = add(25, 25)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(200, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it iin anyway.
print "Here is a puzzle."

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
new = subtract(3,subtract(divide(add(2,multiply(3,4)),7),-1))
print "That becomes: ", new, "Can you do it by hand?"
