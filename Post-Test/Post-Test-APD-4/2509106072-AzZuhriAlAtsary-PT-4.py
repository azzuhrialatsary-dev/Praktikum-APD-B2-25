nama = "Az Zuhri Al Atsary"
nim = "2509106072"

percobaan = 0
while percobaan < 3:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username == nama and password == nim:
        print("\nLogin berhasil")
        break
    else:
        print("\nLogin gagal")
        percobaan += 1

if percobaan == 3:
    print("Sudah 3 kali gagal. Program berhenti.")
else :
    while True:
        print("\n================ Opsi ===================")
        print("1. Tiket Reguler (Rp 50.000)")
        print("2. Tiket VIP (Rp 100.000)")
        print("3. Tiket VVIP (Rp 150.000)")
        print("4. Keluar")
        print("=========================================\n")

        opsi = int(input("Pilih opsi (1-4): "))

        if opsi == 1:
            jenis_tiket = "Reguler"
            harga_tiket = 50000
        elif opsi == 2:
            jenis_tiket = "VIP"
            harga_tiket = 100000
        elif opsi == 3:
            jenis_tiket = "VVIP"
            harga_tiket = 150000
        elif opsi == 4:
            print("\nKeluar dari program")
            break
        else:
            print("\nOpsi tidak valid")
            continue

        jumlah_tiket = int(input("Masukkan jumlah tiket: "))

        total = 0
        for i in range(jumlah_tiket):
            total += harga_tiket

            if total >= 300000:
                potongan_harga = total * 0.12
                total = total - potongan_harga
                bonus = "diskon 12%"
            elif total >= 200000:
                potongan_harga = total * 0.08
                total = total - potongan_harga
                bonus = "diskon 8%"
            elif total >= 150000:
                bonus = "poster film eksklusif"
            else:
                bonus = "tidak ada diskon/bonus"

        print("\n=========== Struk Pembelian ===========")
        print("Jenis Tiket  :", jenis_tiket)
        print("Jumlah Tiket :", jumlah_tiket)
        print(f"Total Bayar  : Rp {total:,.0f}")
        print("Diskon/Bonus :", bonus)
        print("=======================================\n")