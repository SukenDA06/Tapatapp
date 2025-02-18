class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return "Id: " + str(self.id) + " Username: " + self.username


listUsers = [
    User(1, "usuari1", "12345", "prova@gmail.com"),
    User(2, "user2", "123", "user2@proven.cat"),
    User(3, "admin", "12", "admin@proven.cat"),
    User(4, "admin2", "12", "admin2@proven.cat")
]


class DAOUsers:
    def __init__(self):
        self.users = listUsers

    def getUserByUsername(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None


daoUser = DAOUsers()

print(daoUser.getUserByUsername("usuari1"))
u = daoUser.getUserByUsername("notrobat")
if u:
    print(u)
else:
    print("No trobat")