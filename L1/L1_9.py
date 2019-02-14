symbols = {
    "M":1000, 
    "CM":900,
    "D":500,
    "CD":400,
    "C":100,
    "XC":90,
    "L":50,
    "XL":40, 
    "X":10,
    "IX":9,
    "V":5,
    "IV":4,
    "I":1
}

def askInput(message):
    userInput = input(message)
    
    if userInput == "exit":
        quit()

    try:
        val = int(userInput)
        
    except ValueError:
        return askInput("*Value must be a numeric integer value\n")

    if (val < 0):
        return askInput("No negatives in ancient Rome, enter a positive number\n")

    return val

def toRoman(number):
    roman = ""
    for symbol in symbols:
        while number > 0 and symbols[symbol]<=number:
            if number >= symbols[symbol]:                
                roman+=symbol
                number-=symbols[symbol]
    return roman

def main():
    decimal = askInput("Enter a decimal number to conver to roman numeral, 'exit' to exit program\n")
    print (toRoman(decimal))
    main()

main()