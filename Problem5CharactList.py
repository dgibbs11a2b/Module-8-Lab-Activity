#----------------------------------------
#David Gibbs
#March 8, 2020
#
#This program will execute a check on the
#character’s existing list of items needed
#against items already in their possession
#and will also check against current status debuffs.
#----------------------------------------

def pause():
    programPause = input("Ready to see the next task? Press the <ENTER> key to continue...")

def main():
    
    Items_Needed_1 = ['coat' , 'first aid kit']

    Items_Needed_2 = ['pan' , 'groceries']

    Items_Needed_3 = ['pen' , 'paper' , 'idea']
    
    listOfItems = ['pan' , 'paper', 'idea', 'rope', 'groceries']

    debuffStatus = ['slow' , 'small' , 'confusion']

    print("\n Task 1: To Climb a mountain, your character has rope but still needs :" , Items_Needed_1)

    if 'rope' in listOfItems :
        if 'coat' and 'first aid kit' in listOfItems :
            if 'slow' not in debuffStatus :
                print("\n Your character has all the items they need to climb a mountain and they are not slow : " , listOfItems)
        else: 
            print("\n Your characer still needs to collect these items", Items_Needed_1, "and your character needs to be faster in order to climb a mountain :")

    print("\n")
    pause()

    print("\n Task 2: To Cook a meal, your character has a pan and groceries needed for the meal but cannot have small :" , Items_Needed_2)

    if 'pan' and 'groceries' in listOfItems and 'small' in debuffStatus :
        print("\n Your character has all the items they need to complete Task 2 but they cannot have small. Here is the current list : " , listOfItems)

    if 'pan' and 'groceries' in listOfItems and 'small' not in debuffStatus :
        print("\n Your character has all the items they need to complete Task 2 and they aren't small. Here is the current list : " , listOfItems)

    if 'pan' and 'groceries' not in listOfItems and 'small' in debuffStatus :
        print("\n Your character still needs to collect these items", Items_Needed_2, "and your character cannot have small. Here is the current list : " , listOfItems)    

    if 'pan' and 'groceries' not in listOfItems and 'small' not in debuffStatus :
        print("\n Your characer still needs to collect", Items_Needed_2, "and your character cannot have small. Here is the current list : " , listOfItems)  

    print("\n")
    pause()


    if 'pen' not in listOfItems :
        if 'paper' and 'idea' in listOfItems :
            if 'confusion' in debuffStatus :
                print("\n Your character still needs a pen and they cannot have confusion. Here is the current list : " , listOfItems)
        else: 
            print("\n Your character has all the items they need to write a book, and they cannot have confusion. Here is the current list : " , listOfItems)



if __name__ == '__main__':
    main()
