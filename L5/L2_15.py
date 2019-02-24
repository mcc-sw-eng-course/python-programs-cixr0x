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
