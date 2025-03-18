import requests

BASE_URL = "http://127.0.0.1:5000"

def get_all_accounts():
    response = requests.get(f"{BASE_URL}/accounts")
    if response.status_code == 200:
        return response.json()
    return None

def get_account_by_username(user_name):
    response = requests.get(f"{BASE_URL}/account/{user_name}")
    if response.status_code == 200:
        return response.json()
    return None

def get_all_infants():
    response = requests.get(f"{BASE_URL}/children")
    if response.status_code == 200:
        return response.json()
    return None

def get_infants_by_acc_id(acc_id):
    response = requests.get(f"{BASE_URL}/children/{acc_id}")
    if response.status_code == 200:
        return response.json()
    return None

if __name__ == "__main__":
    print("Obteniendo todas las cuentas:")
    accounts = get_all_accounts()
    print(accounts)
    
    user_name = input("Introduce el nombre de usuario para buscar la cuenta: ")
    account = get_account_by_username(user_name)
    print(account if account else "Usuario no encontrado")
    
    print("Obteniendo todos los infantes:")
    infants = get_all_infants()
    print(infants)
    
    acc_id = input("Introduce el ID de usuario para buscar infantes asociados: ")
    if acc_id.isdigit():
        user_infants = get_infants_by_acc_id(int(acc_id))
        print(user_infants if user_infants else "No se encontraron infantes para este usuario")
    else:
        print("ID de usuario no válido")