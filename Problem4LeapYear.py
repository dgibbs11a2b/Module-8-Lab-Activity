#----------------------------------------
#David Gibbs
#March 8, 2020
#
#This program will take the user’s input
#in the form of a 4-digit year
#and will return True if it is a leap year,
#and False if it is not a leap year.
#----------------------------------------


year = int(input("Please Enter the four digit Year : "))

if (( year % 400 == 0) or (( year % 4 == 0 ) and ( year % 100 != 0))):
    print("%d is a Leap Year" %year)
#Divisible by 400, remainder 0, divisible by 4, remainder 0,
#not divisble by 100...etc.
else:
    print("%d is not a Leap Year" %year)
