from sys import argv 					# import the module argv from sys

script, filename = argv 				# define the variable  to get the filename

txt = open(filename) 					# set the functions open with the filename variable to new variable name "txt"

print "Here's your file: " , txt.name 	# prints a little message with the name of the filename
print txt.read() 						# we call a function on txt to read.

txt.close() 							# Close opened file
print "Closed or not : ", txt.closed
print "Opening mode : ", txt.mode

print "Type the filename again:" 		# prints a little message
file_again = raw_input("> ") 			# get input from stdin from user and save it to a variable.

txt_again = open(file_again) 			# set the function open with the file_again variable to new variable named "txt_again"

print txt_again.read() 				   # we call a function on txt_again to read.
print "Closed or not : ", txt_again.closed
txt_again.close()
print "Closed or not after I run the close Method : ", txt_again.closed

