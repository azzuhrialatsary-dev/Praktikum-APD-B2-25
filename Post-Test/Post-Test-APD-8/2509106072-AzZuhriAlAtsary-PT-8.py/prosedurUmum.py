import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def hitung_total(harga, jumlah):
    return harga * jumlah
