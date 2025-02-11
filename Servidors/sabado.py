class User:
    def _init_(self, id, username, password, email):
        self.id=id
        self.username=username
        self.password=password
        self.email=email

    def _str_(self):
        return "Id:" + str(self.id) + " Username:" + self.username

listUsers= [
    User(1, "usuari1", "12345", "prova@gmail.com"),
    User(2, "user2", "123", "user2@proven.cat"),
    User(3, "admin", "12", "admin@proven.cat")
    User(4, "admin2", "12")        
]

class DAOUsers:
    def _init_(self):
        self.users=listUsers

    def getUserByUsername(self, username):
        return None
    
daoUser = DAOUsers()

print(daoUser.getUserByUsername("usuari1"))
u=daoUser.getUserByUsername("notrobat")
if(u):
    print(u)
else:
    print("No trobat")