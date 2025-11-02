from prosedurUmum import clear_screen
from data import Data_user

def login():
    clear_screen()
    print("========== LOGIN ==========")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    print("===========================")

    if username in Data_user and Data_user[username]["password"] == password:
        print("Login berhasil!")
        return username, Data_user[username]["role"]
    else:
        print("Login gagal!")
        input("Enter untuk lanjut...")
        return None, None


def register():
    clear_screen()
    print("=============== REGISTER ===============")
    Username_baru = input("Masukkan Username Baru: ")
    Password_baru = input("Masukkan Password: ")
    print("========================================")

    if Username_baru not in Data_user:
        Data_user[Username_baru] = {"password": Password_baru, "role": "user"}
        print("Registrasi berhasil!")
    else:
        print("Username sudah ada!")
    input("Enter untuk lanjut...")
