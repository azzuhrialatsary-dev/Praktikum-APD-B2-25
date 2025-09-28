nama = "Az Zuhri Al Atsary"
nim = "2509106072"

Biaya_Langganan = 1500000

Nama_Lengkap = input("Masukkan Nama Lengkap : ")
NIM_Lengkap = input("Masukkan NIM : ")

if Nama_Lengkap == nama and NIM_Lengkap == nim :
    print("\n" + "=" * 130)
    print(f"{'No':<10}{'Paket':<15}{'Biaya Administrasi':<25}{'Benefit':<20}")
    print("-" * 130)
    print(f"{'1':<10}{'Bronze':<15}{'1%':<25}{'Akses dasar ke lagu-lagu populer':<20}")
    print(f"{'2':<10}{'Silver':<15}{'3%':<25}{'Akses lagu premium dan playlist kustom':<20}")
    print(f"{'3':<10}{'Gold':<15}{'5%':<25}{'Akses lagu premium, playlist kustom, dan mode offline':<20}")
    print(f"{'4':<10}{'Platinum':<15}{'7%':<25}{'Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis':<20}")
    print("=" * 130)

    Pilihan_Paket = int(input("\nPilih paket (1-4) : "))

    if Pilihan_Paket == 1:
        Paket = "Bronze"
        Benefit = "Akses dasar ke lagu-lagu populer"
        Biaya_Administrasi = 0.01 * Biaya_Langganan
    elif Pilihan_Paket == 2:
        Paket = "Silver"
        Benefit = "Akses lagu premium dan playlist kustom"
        Biaya_Administrasi = 0.03 * Biaya_Langganan
    elif Pilihan_Paket == 3:
        Paket = "Gold"
        Benefit = "Akses lagu premium, playlist kustom, dan mode offline"
        Biaya_Administrasi = 0.05 * Biaya_Langganan
    elif Pilihan_Paket == 4:
        Paket = "Platinum"
        Benefit = "Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis"
        Biaya_Administrasi = 0.07 * Biaya_Langganan
    else:
        print("Pilihan paket tidak valid")
else:
    print("Tidak dapat menampilkan menu pilihan. Silakan periksa kembali Nama Lengkap dan NIM Lengkap Anda")
    exit()

Total_Bayar = Biaya_Langganan + Biaya_Administrasi

print("\n=================================================================================================")
print("Nama         :", Nama_Lengkap)
print("NIM          :", NIM_Lengkap)
print("Paket        :", Paket)
print("Benefit      :", Benefit)
print("Total Bayar  : Rp ",f"{Total_Bayar:,.0f}")
print("=================================================================================================")