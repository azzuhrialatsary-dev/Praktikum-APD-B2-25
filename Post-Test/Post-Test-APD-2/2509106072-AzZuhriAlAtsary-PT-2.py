#25009106072-AzZuhriAlAtsary-PT-2

nama = input("Masukkan Nama Lengkap : ")
nim = input("Masukkan Nim : ")

harga = int(input("Masukkan Harga Makanan : Rp "))

menu = {
    1: ("Pecel Lele" , 5),
    2: ("Mie Ayam" , 8),
    3: ("Nasi Padang" , 10)
    }

print("\n================================== Hasil =======================================")
print(f"{nama} dengan Nim {nim} ingin membeli makanan Rp {harga:,}")
print("=" * 80)

print(f"{'No':<5}{'Menu':<15}{'Pajak':<12}{'Total Bayar':<20}")
print("-" * 80)

for key, (nama_menu, persen_pajak) in menu.items():
    pajak = harga * (persen_pajak / 100)
    total = harga + pajak
    print(f"{key:<5}{nama_menu:<15}{persen_pajak}%{' ':<10}Rp {total:>10,.0f}")

print("=" * 80)

pilihan = int(input("\nPilih Menu (1-3): "))

nama_menu, persen_pajak = menu[pilihan]
pajak = harga * (persen_pajak / 100)
total = harga + pajak

print("\n=============================== Detail Pesanan =================================")
print(f"{nama} dengan Nim {nim} memilih {nama_menu}")
print(f"Harga makanan : Rp {harga:,}")
print(f"Pajak ({persen_pajak}%) : Rp {pajak:,.0f}")
print(f"Total yang harus dibayar : Rp {total:,.0f}")
print("=" * 80)