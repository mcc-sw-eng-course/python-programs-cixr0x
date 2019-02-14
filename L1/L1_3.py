
userInput = input("Enter a list of values, separated by coma: \n")

originalList = userInput.split(",")

#clean values from whitespaces
for index, val in enumerate(originalList):
    originalList[index]  = val.strip()

def removeDupsList(originalList):
    newList=[]
    for val in originalList:
        if not (val in newList):
            newList.append(val)
    return newList

def removeDupsSet(originalList):
    return list(set(originalList))

print (removeDupsList(originalList))
print (removeDupsSet(originalList))
