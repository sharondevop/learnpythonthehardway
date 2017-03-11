#!/usr/bin/python
import re # include directory


Regex_Pattern = r'hackerrank' # create variable with the pattren value
Test_string = raw_input('--->') # get data from stdinput

match = re.findall(Regex_Pattern, Test_string) # create variable with the regex match
print "Number of matches :", len(match)  # print the number of item found
