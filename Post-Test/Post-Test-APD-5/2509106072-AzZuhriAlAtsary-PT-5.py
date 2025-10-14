import os

Data_user = [["admin", "admin123", "admin"], ["user", "user123", "user"], ["zuhrihengker", "hengker123", "admin"]]
Mainan_anak = [[1, "Mobil Remote", 120000, 10], [2, "Boneka Barbie", 95000, 8], [3, "Puzzle 1000 pcs", 75000, 15]]

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
        for Data_pengguna in Data_user:
            if Data_pengguna[0] == username and Data_pengguna[1] == password:
                login = True
                role = Data_pengguna[2]
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
                        for data_mainan in Mainan_anak:
                            print(f"{data_mainan[0]:<4} {data_mainan[1]:<25} Rp{data_mainan[2]:>10,} {data_mainan[3]:<5}")
                        print("=========================================================")
                        input("Enter untuk kembali...")

                    elif Pilihan_admin == "2":
                        Nama_mainan = input("Nama mainan: ")
                        Harga_mainan = input("Harga: ")
                        Stok_mainan = input("Stok: ")

                        if Harga_mainan != "" and Stok_mainan != "":
                            ID_baru = Mainan_anak[-1][0] + 1
                            Mainan_anak.append([ID_baru, Nama_mainan, int(Harga_mainan), int(Stok_mainan)])
                            print("Mainan berhasil ditambah!")
                        else:
                            print("Harga dan stok tidak boleh kosong!")
                        input("Enter untuk kembali...")

                    elif Pilihan_admin == "3":
                        ID_diperbarui = input("ID mainan: ")
                        if ID_diperbarui != "":
                            ID_diperbarui = int(ID_diperbarui)
                            Data_ketemu = False
                            for Data_mainan in Mainan_anak:
                                if Data_mainan[0] == ID_diperbarui:
                                    Data_ketemu = True
                                    print("Data lama:", Data_mainan)
                                    Nama_baru = input("Nama baru: ")
                                    Harga_baru = input("Harga baru: ")
                                    Stok_baru = input("Stok baru: ")
                                    if Nama_baru != "":
                                        Data_mainan[1] = Nama_baru
                                    if Harga_baru != "":
                                        Data_mainan[2] = int(Harga_baru)
                                    if Stok_baru != "":
                                        Data_mainan[3] = int(Stok_baru)
                                    print("Data diperbarui!")
                            if Data_ketemu == False:
                                print("ID tidak ditemukan!")
                        else:
                            print("ID tidak boleh kosong!")
                        input("Enter untuk kembali...")

                    elif Pilihan_admin == "4":
                        ID_hapus = input("ID mainan yang dihapus: ")
                        if ID_hapus != "":
                            ID_hapus = int(ID_hapus)
                            Indeks_hapus = -1
                            for i in range(len(Mainan_anak)):
                                if Mainan_anak[i][0] == ID_hapus:
                                    Indeks_hapus = i
                            if Indeks_hapus != -1:
                                del Mainan_anak[Indeks_hapus]
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
                        print("=========== DAFTAR MAINAN ============")
                        for Data_mainan in Mainan_anak:
                            print(Data_mainan)
                            print("===================================")
                        input("Enter untuk kembali...")

                    elif Pilihan_user == "2":
                        ID_beli = input("Masukkan ID mainan: ")
                        Jumlah_dibeli = input("Jumlah beli: ")
                        if ID_beli != "" and Jumlah_beli != "":
                            ID_beli = int(ID_beli)
                            Jumlah_beli = int(Jumlah_beli)
                            Data_ketemu = False
                            for Data_mainan in Mainan_anak:
                                if Data_mainan[0] == ID_beli:
                                    Data_ketemu = True
                                    if Jumlah_beli <= Data_mainan[3]:
                                        Total_harga = Jumlah_beli * Data_mainan[2]
                                        Data_mainan[3] = Data_mainan[3] - Jumlah_beli
                                        print("Total bayar:", Total_harga)
                                    else:
                                        print("Stok tidak cukup")
                            if Data_ketemu == False:
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
        print("======== REGISTER ========")
        Username_baru = input("Masukkan Username Baru: ")
        Password_baru = input("Masukkan Password: ")
        print("==========================")
        Username_sama = False
        for Data_pengguna in Data_user:
            if Data_pengguna[0] == Username_baru:
                Username_sama = True
        if Username_sama == False:
            Data_user.append([Username_baru, Password_baru, "user"])
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
