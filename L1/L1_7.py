import random
symbolList = []

for c in range(48, 58):
    symbolList.append(chr(c))

for c in range(65, 91):
    symbolList.append(chr(c))

for c in range(97, 123):
    symbolList.append(chr(c))

for c in range(35, 39):
    symbolList.append(chr(c))

#print (symbolList)

def generatePassword(length):
    password=""
    for i in range(length):
        index = random.randint(0, len(symbolList)-1)
        password+=str(symbolList[index])
    return password

print (generatePassword(10))
