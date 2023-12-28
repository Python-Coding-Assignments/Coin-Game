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

    #getting the user's inputs for number of coins
    print("Enter the number of:")
    numHalves = int(input("\tHalf Dollars: "))
    numQuarters = int(input("\tQuarters: "))
    numDimes = int(input("\tDimes: "))
    numNickels = int(input("\tNickels: "))
    numPennies = int(input("\tPennies: "))

    #conditional statement which runs if one of the user's inputs is less than zero
    if numHalves < 0 or numQuarters < 0 or numDimes < 0 or numNickels < 0 or numPennies < 0:
        print("You cannot enter a negative number of coins. Aborting game.")

    #conditional statement which runs if all of the user's inputs are positive
    else:
        #calculating the monetary value of all coins that the user input
        totalInput = (numHalves * constant.half) + (numQuarters * constant.quarter) + (numDimes * constant.dime) + (numNickels * constant.nickel) + (numPennies * constant.penny)

        #conditional statement which runs if total input equals the user's match amount
        if totalInput == matchAmount:
            print("You WIN!")

        #conditional statement which runs if total input is greater than the user's match amount    
        elif totalInput > matchAmount:
            print("You LOST by: $" + str("{:.2f}".format((totalInput - matchAmount), 2)))

        #conditional statement which runs if user's match amount is greater than the total input    
        else:
            print("You LOST by: $" + str("{:.2f}".format((matchAmount - totalInput), 2))) 

        print("Thanks for playing!")

#conditional statement which runs if user decides to not play the game
elif charInput == "N" or charInput == "n":
    print("Guess you are scared! Come back when you are ready to play")

#conditional statement which runs if the user enters an input other than Y, y, N, or n
else:
    print("Invalid entry, aborting program.")
