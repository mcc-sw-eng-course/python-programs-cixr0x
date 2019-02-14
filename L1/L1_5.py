def askInput(message):
    userInput = input(message)
    
    if userInput == "exit":
        quit()

    try:
        val = int(userInput)
        
    except ValueError:
        return askInput("*Value must be a numeric integer value\n")

    if (val < 0):
        return askInput("I cant generate '"+str(val)+"' numbers... please be serious\n")

    if (val > 2000):
        return askInput("Thats a big number... please try a smaller one\n")
    return val

def printFib(qty):
    last = 0
    count = 1
    outputString = ""
    for x in range(0, qty):        
        new = last+count
        outputString+=str(count)
        if (x!=qty-1): outputString+=","
        last = count
        count =  new
    print (outputString)

qty = askInput("How many fibonacci numbers should we generate?\n")
printFib(qty)
