#----------------------------------------
#David Gibbs
#March 8, 2020
#
#This program will take the existing list
#and print to the screen if the value 5 exists
#in that list.
#----------------------------------------
num_list = [ 1, 5, 4, 3, 7, 9, 2, 8, 0, 2 ] 
  
for i in num_list: 
    if(i == 5) : 
#the line below gets printed whether five is or is not in the list.  It is a bit confusing.
        print ("The number 5 exists in this list") 
  
#or another way could be...

def numbers(list_of_numbers):
    value = ['5']
    for i in list_of_numbers:
        if i in value:
            return True
    else:
        return False
print(numbers(['1','5','4','3','7','9','2','8','0','2']))


#def listCheck(numbers):
#    for x in numbers:
#       if x == 5:
#           print("Five is in the list")
#          return
#    

#numbers = [1, 2, 3, 4, 6, 7, 15]

#listCheck(numbers)
