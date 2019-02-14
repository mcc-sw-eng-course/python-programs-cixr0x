class MyPowerList:

    def __init__(self, initialList=[]):
        if type(initialList) is list:
            self.pList = initialList
        else:
            print("Constuctor parameter is not a list")

    def addItem(self, item):
        self.pList.append(item)

    def removeItem(self, index):
        try:
            del(self.pList[index])
        except Exception as e:
            print("Couldn't delete item: "+str(e))

    def sort(self):
        for x in range(len(self.pList)):
            current = self.pList[x]
            index = x
            while index > 0 and self.pList[index - 1] > current:
                self.pList[index] = self.pList[index - 1]
                index = index-1
            self.pList[index] = current

    def lMerge(self, mergeList):
        self.pList = mergeList+self.pList

    def rMerge(self, mergeList):
        self.pList = self.pList+mergeList

    def writeToFile(self, path):
        with open(path, 'w') as f:
            for item in self.pList:
                f.write("%s " % item)

    def readFromFile(self, path):
        with open(path, 'r') as f:
            self.pList = list(map(lambda x: int(x), f.read().split()))

    def printList(self):
        print(self.pList)


myList = MyPowerList()
print("Adding items 1, 3, 5")
myList.addItem(1)
myList.addItem(3)
myList.addItem(5)
print("Printing list")
myList.printList()
print("Removing item at index 1")
myList.removeItem(1)
print("Printing list")
myList.printList()
print("Adding  random items 12, 4, 99, 7")
myList.addItem(12)
myList.addItem(4)
myList.addItem(99)
myList.addItem(7)
print("Printing list")
myList.printList()
print("Sort and print")
myList.sort()
myList.printList()
print("left merging with list [-5, -4, -3] and print")
myList.lMerge([-5, -4, -3])
myList.printList()
print("right merging with list [100, 102, 104] and print")
myList.rMerge([100, 102, 104])
myList.printList()
print("Saving to file 'mylist.txt'")
myList.writeToFile('mylist.txt')
print("Reading from 'mylist.txt' and print")
myNewList = MyPowerList()
myNewList.readFromFile('mylist.txt')
myNewList.printList()
