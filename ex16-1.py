from sys import argv

script, filename = argv

open_file = open(filename)

print "We're going to read the content of this txt: %r. " % filename
print "Here's the content: \n \n" , open_file.read()
print open_file.read()

print "The txt is closed? " , open_file.closed
open_file.close()
print "The txt is closed now ? ", open_file.closed

