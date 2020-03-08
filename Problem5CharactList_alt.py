#----------------------------------------
#David Gibbs
#March 8, 2020
#
#This program will contains alternate code to Problem5Charactlist.py
#----------------------------------------

listOfItems = ["pan", "paper", "idea", "rope", "groceries"]
Items_Needed_1 = ["rope", "coat", "first aid kit"]
Items_Needed_2 = ["pan", "groceries"]
Items_Needed_3 = ["pen", "paper", "idea"]
debuffStatus = ["slow", "small", "confusion"]


print("\n Task 1: To Climb a mountain, your character has rope but still needs :" , Items_Needed_1)

print("\n")

if "rope" in listOfItems and "coat" and "first aid kit" and "slow" not in debuffStatus :
    print("\n Your character has all the items they need to complete Task 2 and they are not slow.")

else:
    print("Your character has",listOfItems,"Your character still needs a coat and first aid kit to climb a mountain and they can't be slow")

     
programPause = input("Ready to see the next task? Press the <ENTER> key to continue...")
#Pauses program and waits for user input

print("\n Task 2: To cook a meal, your character needs:", Items_Needed_2)

print("\n")

if "pan" and "groceries" in listOfItems and "small" not in debuffStatus :
    print("\n Your character has all the items they need to complete Task 2 and they are not small.")

else:
    print("Your character has",listOfItems,"Your character has a pan and groceries to cook a meal but they can't be small")


programPause = input("Ready to see the next task? Press the <ENTER> key to continue...")


print("\n Task 3: To write a book, your character needs:", Items_Needed_3)

print("\n")

if "pen" and "paper" and "idea" in listOfItems and "confusion" not in debuffStatus :
    print("Your character has",listOfItems,"Your character has all the items they need to write a book and they cannot have confusion.")

else:
    print("Your character still needs a pen and they can't have confusion.")









    
