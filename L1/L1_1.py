def askInput(message):
    userInput = input(message)
    
    if userInput == "exit":
        quit()

    try:
        val = int(userInput)
        return val
    except ValueError:
        return askInput("*Value must be a numeric integer value\n")

def checkMultiple(value, divideBy):
    return value % divideBy == 0


def main():
    value = askInput("Please enter a value ('exit' to exit program)\n")
    if checkMultiple(value, 4):
        print ("Your number is multple of 4")
    else:
        if checkMultiple(value, 2):
            print ("Your number is even")
        else:
            print ("Your number is odd")
    
    print ("For the next trick I need you to enter 2 values")
    num =  askInput("Please enter the first value\n")
    check =  askInput("Please enter the second value\n")

    if checkMultiple(num, check):
        print (str(num) +" divides evenly by "+ str(check))
    else:
        print (str(num) +" does not divide evenly by "+ str(check))


main()