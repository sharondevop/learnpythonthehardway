cars = 100 # will define cars as a 100
space_in_a_car = 4.0 # define space_in_a_car as 4.0
drivers = 30 # define drivers as 30
passengers = 90 # define passengers as 90
cars_not_driven = cars - drivers # calculating variables and define result.
cars_driven = drivers # define cars_driven as drivers
carpool_capacity = cars_driven * space_in_a_car # calculating variables and define result.
average_passengers_per_car = passengers / cars_driven # calculating variable and define result.

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."