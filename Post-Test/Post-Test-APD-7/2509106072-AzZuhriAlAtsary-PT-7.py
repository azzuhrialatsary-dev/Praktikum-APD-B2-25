import os

Data_user = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
    "zuhrihengker": {"password": "hengker123", "role": "admin"}
}

Mainan_anak = {
    1: {"nama": "Mobil Remote", "harga": 120000, "stok": 10},
    2: {"nama": "Boneka Barbie", "harga": 95000, "stok": 8},
    3: {"nama": "Puzzle 1000 pcs", "harga": 75000, "stok": 15}
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def daftar_mainan():
    clear_screen()
    print("===================== DAFTAR MAINAN =====================")
    print(f"{'ID':<4} {'Nama Mainan':<25} {'Harga':<15} {'Stok':<10}")
    print("---------------------------------------------------------")
    for id_mainan, data_mainan in Mainan_anak.items():
        print(f"{id_mainan:<4} {data_mainan['nama']:<25} Rp{data_mainan['harga']:>10,} {data_mainan['stok']:>5}")
    print("=========================================================")

def hitung_total(harga, jumlah):
    return harga * jumlah

def tambah_mainan():
    global Mainan_anak
    try:
        Nama_mainan = input("Nama mainan: ")
        Harga_mainan = int(input("Harga: "))
        Stok_mainan = int(input("Stok: "))

        if Nama_mainan == "":
            print("Nama mainan tidak boleh kosong")
            return

        ID_baru = 1
        while ID_baru in Mainan_anak:
            ID_baru += 1

        Mainan_anak[ID_baru] = {
            "nama": Nama_mainan,
            "harga": Harga_mainan,
            "stok": Stok_mainan
        }
        print("Mainan berhasil ditambah")
    except ValueError:
        print("Input harga dan stok harus berupa angka")

def update_mainan():
    global Mainan_anak
    try:
        daftar_mainan()
        ID_diperbarui = int(input("ID mainan yang diupdate: "))
        if ID_diperbarui in Mainan_anak:
            Data_mainan = Mainan_anak[ID_diperbarui]
            print("Data lama:", Data_mainan)
            Nama_baru = input("Nama baru (kosongkan jika tidak diubah): ")
            Harga_baru = input("Harga baru (kosongkan jika tidak diubah): ")
            Stok_baru = input("Stok baru (kosongkan jika tidak diubah): ")

            if Nama_baru != "":
                Data_mainan["nama"] = Nama_baru
            if Harga_baru != "":
                Data_mainan["harga"] = int(Harga_baru)
            if Stok_baru != "":
                Data_mainan["stok"] = int(Stok_baru)

            print("Data mainan berhasil diperbarui")
        else:
            print("ID mainan tidak ditemukan")
    except ValueError:
        print("Input ID dan harga/stok harus angka")

def hapus_mainan():
    global Mainan_anak
    try:
        daftar_mainan()
        ID_hapus = int(input("ID mainan yang dihapus: "))
        if ID_hapus in Mainan_anak:
            del Mainan_anak[ID_hapus]
            print("Mainan berhasil dihapus")
        else:
            print("ID tidak ditemukan")
    except ValueError:
        print("Input harus berupa angka")

def beli_mainan():
    global Mainan_anak
    try:
        daftar_mainan()
        ID_beli = int(input("Masukkan ID mainan: "))
        Jumlah_beli = int(input("Jumlah beli: "))
        if ID_beli in Mainan_anak:
            Data_mainan = Mainan_anak[ID_beli]
            if Jumlah_beli <= Data_mainan["stok"]:
                Total_harga = hitung_total(Data_mainan["harga"], Jumlah_beli)
                Data_mainan["stok"] -= Jumlah_beli
                print(f"Total bayar: Rp{Total_harga:,}")
            else:
                print("Stok tidak cukup")
        else:
            print("Mainan tidak ditemukan")
    except ValueError:
        print("Input harus berupa angka")

while True:
    clear_screen()
    print("========== TOKO MAINAN ANAK ==========")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("======================================")
    menu = input("Pilih menu (1-3): ")

    if menu == "1":
        clear_screen()
        print("========== LOGIN ==========")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print("===========================")

        login = False
        role = ""

        if username in Data_user and Data_user[username]["password"] == password:
            login = True
            role = Data_user[username]["role"]

        if not login:
            print("Login gagal")
            input("Enter untuk lanjut...")
        else:
            if role == "admin":
                while True:
                    clear_screen()
                    print("============ MENU ADMIN ============")
                    print("1. Lihat mainan")
                    print("2. Tambah mainan")
                    print("3. Update mainan")
                    print("4. Hapus mainan")
                    print("5. Logout")
                    print("====================================")
                    Pilihan_admin = input("Pilih menu (1-5): ")

                    if Pilihan_admin == "1":
                        daftar_mainan()
                    elif Pilihan_admin == "2":
                        tambah_mainan()
                    elif Pilihan_admin == "3":
                        update_mainan()
                    elif Pilihan_admin == "4":
                        hapus_mainan()
                    elif Pilihan_admin == "5":
                        break
                    else:
                        print("Pilihan salah")
                    input("Enter untuk kembali...")

            else:
                while True:
                    clear_screen()
                    print("=========== MENU USER ============")
                    print("1. Lihat mainan")
                    print("2. Beli mainan")
                    print("3. Logout")
                    print("==================================")

                    Pilihan_user = input("Pilih (1-3): ")

                    if Pilihan_user == "1":
                        daftar_mainan()
                    elif Pilihan_user == "2":
                        beli_mainan()
                    elif Pilihan_user == "3":
                        break
                    else:
                        print("Pilihan tidak valid")
                    input("Enter untuk kembali...")

    elif menu == "2":
        clear_screen()
        print("=============== REGISTER ===============")
        Username_baru = input("Masukkan Username Baru: ")
        Password_baru = input("Masukkan Password: ")
        print("========================================")

        if Username_baru not in Data_user:
            Data_user[Username_baru] = {"password": Password_baru, "role": "user"}
            print("Registrasi berhasil")
        else:
            print("Username sudah ada!")
        input("Enter untuk lanjut...")

    elif menu == "3":
        print("Terima kasih sudah berkunjung!")
        break

    else:
        print("Pilihan tidak valid")
        input("Enter untuk lanjut...")
