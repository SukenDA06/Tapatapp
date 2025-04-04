from flask import Flask, request, jsonify

class User:
    def __init__(self, id, username, password, email=""):
        self.id=id
        self.username=username
        self.password=password
        self.email=email

    def __str__(self):
        return "Id:" + str(self.id) + " Username:" + self.username

listUsers= [
    User(1,"usuari1", "12345", "prova@gmail.com"),
    User(2,"user2", "123", "user2@proven.cat"),
    User(3,"admin","12","admin@proven.cat"),
    User(4,"admin2","12")
]

class DAOUsers:
    def __init__(self):
        self.users=listUsers
    
    def getUserByUsername(self,username):
        for u in self.users:
            if u.username == username:
                return u
        return None

daoUser = DAOUsers()

u=daoUser.getUserByUsername("usuari1")
if(u):
    print(u)
else:
    print("No trobat")

#definir End-Point (http://<ip>:port/proto1/user?username=...)
# http://localhost:5000/tapatapp/getuser
# Method (GET/POST) -> GET  

app = Flask(__name__)

@app.route('/prototip1/getuser', methods=['GET'])
def get_User():
    username = request.args.get('username')
    user = daoUser.getUserByUsername(username)
    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "password": user.password,
            "email": user.email
        }), 200
    else:
        return jsonify({"error": "User not found"}), 400


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="10050")

# Parametres -> username
# Resposta (HTTP Codes 200 OK - 400 No trobat)