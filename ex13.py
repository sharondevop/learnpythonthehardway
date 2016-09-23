from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

dream = raw_input("What is you'r dream? ")
name = raw_input("What is you'r name? ")
music = raw_input("What music do you like? ")

print "So, you'r dream is %s, and you'r name is %s, you love to lession to %s. " % (
dream, name, music)