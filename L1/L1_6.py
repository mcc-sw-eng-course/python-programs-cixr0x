inputSequence = input("Please input a comma separated sequence, I'll tell you if its fibonacci\n")

sequence = inputSequence.split(",")

def checkFib(sequence):
    last = 0
    count = 1
    for x in sequence:  
        if (int(x)!=count):
            return False
        new = last+count
        last = count
        count =  new
    return True

if (checkFib(sequence)):
    print ("It is Fibonacci!")
else:
    print ("Not Fibonacci")