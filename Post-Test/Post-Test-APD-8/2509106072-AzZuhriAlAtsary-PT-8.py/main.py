from prosedurUmum import clear_screen
from pengelolaanMainan import daftar_mainan, tambah_mainan, update_mainan, hapus_mainan, beli_mainan
from autentikasi import login, register

while True:
    clear_screen()
    print("========== TOKO MAINAN ANAK ==========")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("======================================")
    menu = input("Pilih menu (1-3): ")

    if menu == "1":
        username, role = login()
        if not username:
            continue

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
                pilihan = input("Pilih menu (1-5): ")

                if pilihan == "1": daftar_mainan()
                elif pilihan == "2": tambah_mainan()
                elif pilihan == "3": update_mainan()
                elif pilihan == "4": hapus_mainan()
                elif pilihan == "5": break
                else: print("Pilihan salah")

                input("Enter untuk kembali...")

        else:
            while True:
                clear_screen()
                print("=========== MENU USER ============")
                print("1. Lihat mainan")
                print("2. Beli mainan")
                print("3. Logout")
                print("==================================")

                pilihan = input("Pilih (1-3): ")

                if pilihan == "1": daftar_mainan()
                elif pilihan == "2": beli_mainan()
                elif pilihan == "3": break
                else: print("Pilihan tidak valid")

                input("Enter untuk kembali...")

    elif menu == "2":
        register()

    elif menu == "3":
        print("Terima kasih sudah berkunjung!")
        break

    else:
        print("Pilihan tidak valid")
        input("Enter untuk lanjut...")
