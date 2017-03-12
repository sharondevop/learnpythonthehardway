def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

first = 24.0
second = 34.0

adding = add(first,second)
subtracting = subtract(100.0,1023.0)
dividing = divide(adding, subtracting)
print "Result %f " % dividing
