from prettytable import PrettyTable
from prosedurUmum import hitung_total, clear_screen
from data import Mainan_anak

def daftar_mainan():
    clear_screen()
    table = PrettyTable()
    table.title = "DAFTAR MAINAN"
    table.field_names = ["ID", "Nama Mainan", "Harga", "Stok"]
    for id_mainan, data in Mainan_anak.items():
        table.add_row([id_mainan, data["nama"], f"Rp{data['harga']:,}", data["stok"]])
    print(table)

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
        print("Mainan berhasil ditambah!")
    except ValueError:
        print("Input harga dan stok harus berupa angka")

def update_mainan():
    global Mainan_anak
    try:
        daftar_mainan()
        ID_diperbarui = int(input("ID mainan yang diupdate: "))
        if ID_diperbarui in Mainan_anak:
            Data_mainan = Mainan_anak[ID_diperbarui]
            print(f"Data lama: {Data_mainan}")
            Nama_baru = input("Nama baru (kosongkan jika tidak diubah): ")
            Harga_baru = input("Harga baru (kosongkan jika tidak diubah): ")
            Stok_baru = input("Stok baru (kosongkan jika tidak diubah): ")

            if Nama_baru != "":
                Data_mainan["nama"] = Nama_baru
            if Harga_baru != "":
                Data_mainan["harga"] = int(Harga_baru)
            if Stok_baru != "":
                Data_mainan["stok"] = int(Stok_baru)

            print("Data mainan berhasil diperbarui!")
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
            print("Mainan berhasil dihapus!")
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
