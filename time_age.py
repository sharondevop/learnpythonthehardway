#!/usr/bin/python
import time; # This is include time module.
import datetime; # Include datetome module
import os; # Include os module

script_name = os.path.basename(__file__) # Get script name & store in variable

today = datetime.date.today() # initlize module
current_year = today.year # get the current year
current_month = today.month # get the curent month

# Function definition is here
def age_calculator( arg, arg2):
    my_month_birth = arg
    my_year_birth = arg2
    years_calc = (today.year - my_year_birth) # Callculte the year age
    #condition check for month number, to avoid nagtive numbers.
    if (my_month_birth < current_month): # Callculte the birth month
        month_calc = (current_month - my_month_birth) # # Callculte the birth month and store sum
    else:
        month_calc = (my_month_birth - today.month) # Callculte the birth month and store sum
    print "Your age is %d.%d young\n" % (years_calc, month_calc) # Print the age
    return;


print "I'm calling 'age_calculator' with variables from our script: %s " % script_name # print script name
my_year_birth = 1983 #set year birth
my_month_birth = 1 #set month birth
age_calculator(my_month_birth, my_year_birth)

print "I'm calling 'age_calculator' with numbers directly"
age_calculator(07, 1949)


# Function definition is here
def your_age():
    print "I am 'your_age' funcation and I'm calling 'age_calculator' print your age, HHHH!!! "
    age_calculator(my_month_birth, my_year_birth)
    return;

your_age()
