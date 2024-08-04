class UserManager:
    def __init__(self):
        self.users = {}
        self.id_count = 1

    def addUser(self, name):
        id = self.id_count
        self.users[id] = name
        self.id_count += 1
        return id

    def getUser(self, id):
        return self.users.get(id, None)

    def deleteUser(self, id):
        if id in self.users:
            del self.users[id]
            return "true"
        return "false"

    def findUserByName(self, name):
        return [id for id, user_name in self.users.items() if user_name == name]

if __name__ == "__main__":
    userManager = UserManager()

