import random

tries = 3

def askInput(message):
    userInput = input(message)
    
    if userInput == "exit":
        quit()

    try:
        val = int(userInput)
        return val
    except ValueError:
        return askInput("*Value must be a numeric integer value\n")

def main():
    rndNum = random.randint(1, 9)
    print ("You have "+str(tries)+" shots to guess the number... go!")
    for t in range(tries):
        val = askInput("")
        if (val == rndNum):
            print("You got it!")
            break
        else:
            if (val < rndNum):
                print("Too low!")
            else:
                print("Too high!")
                
    print("Wanna play again? Type 'exit' to finish, type anything else to go again")
    if (input() == 'exit'):
        quit()
    else:
        main()

main()