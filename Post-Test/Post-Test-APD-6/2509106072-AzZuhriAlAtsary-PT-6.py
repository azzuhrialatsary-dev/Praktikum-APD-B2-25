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

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("========== TOKO MAINAN ANAK ==========")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("======================================")
    menu = input("Pilih menu (1-3): ")

    if menu == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("========== LOGIN ==========")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print("===========================")

        login = False
        role = ""
        if username in Data_user and Data_user[username]["password"] == password:
            login = True
            role = Data_user[username]["role"]

        if login == False:
            print("Login gagal")
            input("Enter untuk lanjut...")
        else:
            if role == "admin":
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("============ MENU ADMIN ============")
                    print("1. Lihat mainan")
                    print("2. Tambah mainan")
                    print("3. Update mainan")
                    print("4. Hapus mainan")
                    print("5. Logout")
                    print("====================================")
                    Pilihan_admin = input("Pilih menu (1-5): ")

                    if Pilihan_admin == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("===================== DAFTAR MAINAN =====================")
                        print(f"{'ID':<4} {'Nama Mainan':<25} {'Harga':<15} {'Stok':<10}")
                        print("---------------------------------------------------------")
                        for id_mainan, data_mainan in Mainan_anak.items():
                            print(f"{id_mainan:<4} {data_mainan['nama']:<25} Rp{data_mainan['harga']:>10,} {data_mainan['stok']:>5}")
                        print("=========================================================")
                        input("Enter untuk kembali...")

                    elif Pilihan_admin == "2":
                        Nama_mainan = input("Nama mainan: ")
                        Harga_mainan = input("Harga: ")
                        Stok_mainan = input("Stok: ")

                        if Harga_mainan != "" and Stok_mainan != "":
                            ID_baru = 1
                            while ID_baru in Mainan_anak:
                                ID_baru += 1
                            Mainan_anak[ID_baru] = {
                                "nama": Nama_mainan,
                                "harga": int(Harga_mainan),
                                "stok": int(Stok_mainan)
                            }
                            print("Mainan berhasil ditambah!")
                        else:
                            print("Harga dan stok tidak boleh kosong!")
                        input("Enter untuk kembali...")

                    elif Pilihan_admin == "3":
                        ID_diperbarui = input("ID mainan: ")
                        if ID_diperbarui != "":
                            ID_diperbarui = int(ID_diperbarui)
                            if ID_diperbarui in Mainan_anak:
                                Data_mainan = Mainan_anak[ID_diperbarui]
                                print("Data lama:", Data_mainan)
                                Nama_baru = input("Nama baru: ")
                                Harga_baru = input("Harga baru: ")
                                Stok_baru = input("Stok baru: ")
                                if Nama_baru != "":
                                    Data_mainan["nama"] = Nama_baru
                                if Harga_baru != "":
                                    Data_mainan["harga"] = int(Harga_baru)
                                if Stok_baru != "":
                                    Data_mainan["stok"] = int(Stok_baru)
                                print("Data diperbarui!")
                            else:
                                print("ID tidak ditemukan!")
                        else:
                            print("ID tidak boleh kosong!")
                        input("Enter untuk kembali...")

                    elif Pilihan_admin == "4":
                        ID_hapus = input("ID mainan yang dihapus: ")
                        if ID_hapus != "":
                            ID_hapus = int(ID_hapus)
                            if ID_hapus in Mainan_anak:
                                del Mainan_anak[ID_hapus]
                                print("Mainan dihapus!")
                            else:
                                print("ID tidak ditemukan!")
                        else:
                            print("ID tidak boleh kosong!")
                        input("Enter untuk kembali...")

                    elif Pilihan_admin == "5":
                        break

                    else:
                        print("Pilihan salah!")
                        input("Enter untuk lanjut...")

            else:
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=========== MENU USER ============")
                    print("1. Lihat mainan")
                    print("2. Beli mainan")
                    print("3. Logout")
                    print("===================================")
                    Pilihan_user = input("Pilih (1-3): ")

                    if Pilihan_user == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("==================== DAFTAR MAINAN =====================")
                        print(f"{'ID':<4} {'Nama Mainan':<25} {'Harga':<15} {'Stok':<10}")
                        print("---------------------------------------------------------")
                        for id_mainan, data_mainan in Mainan_anak.items():
                            print(f"{id_mainan:<4} {data_mainan['nama']:<25} Rp{data_mainan['harga']:>10,} {data_mainan['stok']:>5}")
                        print("=========================================================")
                        input("Enter untuk kembali...")

                    elif Pilihan_user == "2":
                        ID_beli = input("Masukkan ID mainan: ")
                        Jumlah_beli = input("Jumlah beli: ")
                        if ID_beli != "" and Jumlah_beli != "":
                            ID_beli = int(ID_beli)
                            Jumlah_beli = int(Jumlah_beli)
                            if ID_beli in Mainan_anak:
                                Data_mainan = Mainan_anak[ID_beli]
                                if Jumlah_beli <= Data_mainan["stok"]:
                                    Total_harga = Jumlah_beli * Data_mainan["harga"]
                                    Data_mainan["stok"] -= Jumlah_beli
                                    print("Total bayar:", Total_harga)
                                else:
                                    print("Stok tidak cukup")
                            else:
                                print("Mainan tidak ditemukan")
                        else:
                            print("Input tidak boleh kosong!")
                        input("Enter untuk kembali...")

                    elif Pilihan_user == "3":
                        break

                    else:
                        print("Pilihan salah")
                        input("Enter untuk lanjut...")

    elif menu == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=============== REGISTER ===============")
        Username_baru = input("Masukkan Username Baru: ")
        Password_baru = input("Masukkan Password: ")
        print("========================================")

        if Username_baru not in Data_user:
            Data_user[Username_baru] = {"password": Password_baru, "role": "user"}
            print("Registrasi berhasil")
        else:
            print("Username sudah ada")
        input("Enter untuk lanjut...")

    elif menu == "3":
        print("Terima kasih sudah berkunjung")
        break

    else:
        print("Pilihan tidak valid")
        input("Enter untuk lanjut...")
