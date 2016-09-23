formatter = "%r %r %r %r" # define variable as a format characters. 

print formatter % (1, 2, 3, 4) # print 1 2 3 4
print formatter % ("one", "two", "three", "four") # print one two three four
print formatter % (True, False, False, True) # print True false false true
print formatter % (formatter, formatter, formatter, formatter) 
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

