#----------------------------------------
#David Gibbs
#March 8, 2020
#
#This program contains a function which takes two inputs
#from the user, calculates the sum, and then prints to
#the screen whether the value is less than, greater than,
#or equal to 10.
#----------------------------------------

x = int(input("Enter your first number?: "))
y = int(input("Enter your first number?: "))

def sum(x, y):
    return x + y
#Sets the definition of x and y and returns x + y in order to get the sum
    
if sum(x,y) > 10:
    print("The sum of the two given numbers is:",sum(x,y),"and this number is greater than 10")   
elif sum(x,y) < 10:
    print("The sum of the two given numbers is:",sum(x,y),"and this number is less than 10")
elif sum(x,y) == 10:
    print("The sum of the two given numbers is:",sum(x,y),"and this number is equal to 10")    
else:
    print("I'm sorry, I cannot help you!")

    
    
