name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.54
weight = 180 # lbs
weight_kg = weight * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's % inches tall." % height
print "He's %d centimeter tall." % round (height_cm)
print "He's %r pounds heavy." % weight
print "He's %d kilogram heavy." % round (weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffe." % teeth


# this line is tricky, try to get it exactly right
print "if I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)

#print "My height %d Inches and %d Centimeter. " % (height, round (height_cm))

#print "My weight %d Lbs and %d Kilogram. " % (weight, round (weight_kg))

