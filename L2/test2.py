
l1Read = open('list1.txt', 'r')
list1 = l1Read.read().split()

l2Read = open('list2.txt', 'r')
list2 = l2Read.read().split()

finalList = []

valueSet = set()

for x in list1:
    valueSet.add(x)

for y in list2:
    initialLength = len(valueSet)
    valueSet.add(y)
    newLength = len(valueSet)
    if (initialLength == newLength):
        finalList.append(y)

writer = open('Third.txt', 'w')
writer.write(finalList)
writer.close()
