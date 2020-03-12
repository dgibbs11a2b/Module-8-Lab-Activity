#----------------------------------------
#David Gibbs
#March 8, 2020
#
#This program contains a function that takes two input
#from a user and prints whether the numbers are equal or not.
#----------------------------------------

x = int(input("What is your first number?: "))

y = int(input("What is your second number?: "))
#Requests input from the user

if x >= y:
#change this to:  if x == y    it doesn't matter if it is greater or not.
    print("Your first number",x, "is equal to your second number",y,)
elif x != y:
    print("Your first number",x, "is not equal to your second number",y,)
#This last statement never gets executed.
else:
    print("Come back to me when you are ready to compare two numbers")


