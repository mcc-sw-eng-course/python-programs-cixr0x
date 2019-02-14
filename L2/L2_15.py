import json


class Directory:

    def __init__(self):
        self.dir = []

    def new(self, name="", address="", phone="", email=""):
        user = {
            "name": name,
            "address": address,
            "phone": phone,
            "email": email
        }
        self.dir.append(user)

    def writeToFile(self, path):
        with open(path, 'w') as f:
            f.write(json.dumps(self.dir))

    def readFromFile(self, path):
        with open(path, 'r') as f:
            self.dir = json.loads(f.read())

    def findBy(self, key, value):
        for index in range(len(self.dir)):
            user = self.dir[index]
            if user[key] == value:
                return user
        print("Couldn't not find any record where '" +
              str(key)+"' is '"+str(value)+"'")

    def print(self):
        if (len(self.dir) == 0):
            print("Directory is empty")
            return
        for i in range(len(self.dir)):
            user = self.dir[i]
            info = ""
            for key, val in user.items():
                info = info+(f"{key}: {val}, ")
            print(info)


print("**Created directory")
myDir = Directory()
print("**Adding users to directory")
myDir.new("Juan", "Calle 13", "33225566", "eljuan@dominio.com")
myDir.new("Pedro", "Av Idayvuelta", "33492333", "elpedro@mismodominio.com")
myDir.new("Maria", "Av Siempreviva", "32435465", "maria@mainstream.com")
print("**Printing directory")
myDir.print()
print("**Writing directory to file")
myDir.writeToFile('dir.txt')

print("**Created new directory")
otherDir = Directory()
print("**Printing new directory")
otherDir.print()
print("**Loading file into new directory")
otherDir.readFromFile('dir.txt')
print("**Printing new directory again")
otherDir.print()

print("**Finding user with name 'Maria' and printing her email")
maria = myDir.findBy("name", "Maria")
print(maria["email"])
