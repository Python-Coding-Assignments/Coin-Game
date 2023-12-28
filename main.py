import Constants.constant as constant

#declarations and initializations of variables
charInput = "null"
matchAmount = totalInput = 0
numHalves = numQuarters = numDimes = numNickels = numPennies = 0

#welcoming the user to the coin game
print("Welcome to the coin game!")
charInput = input("Would you like to play? (y/n): ")

#conditional statement if the user wants to play the game
if charInput == "Y" or charInput == "y":
    #getting user to enter how much money he/she would like to match
    matchAmount = float(input("What amount of money would you like to match? --> "))
    print("Okay! You need to match the value of $" + str("{:.2f}".format(matchAmount)))

    print("Enter the number of:")
    numHalves = int(input("\tHalf Dollars: "))
    numQuarters = int(input("\tQuarters: "))
    numDimes = int(input("\tDimes: "))
    numNickels = int(input("\tNickels: "))
    numPennies = int(input("\tPennies: "))

    if numHalves < 0 or numQuarters < 0 or numDimes < 0 or numNickels < 0 or numPennies < 0:
        print("You cannot enter a negative number of coins. Aborting game.")

    else:
        totalInput = (numHalves * constant.half) + (numQuarters * constant.quarter) + (numDimes * constant.dime) + (numNickels * constant.nickel) + (numPennies * constant.penny)

        if totalInput == matchAmount:
            print("You WIN!")
        elif totalInput > matchAmount:
            print("You LOST by: $" + str("{:.2f}".format((totalInput - matchAmount), 2)))
        else:
            print("You LOST by: $" + str("{:.2f}".format((matchAmount - totalInput), 2))) 

        print("Thanks for playing!")

elif charInput == "N" or charInput == "n":
    print("Guess you are scared! Come back when you are ready to play")

else:
    print("Invalid entry, aborting program.")