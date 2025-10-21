# buah = {"apel", "jeruk", "mangga", "apel"}
# print(buah)

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print(angka)

# Daftar_buku = {
#     "Buku1" : "Bumi Manusia",
#     "Buku2" : "Laut Bercerita"
# }
# print(Daftar_buku["Buku1"])
# print(Daftar_buku)

# Biodata = {
#     "Nama" : "Ananda Daffa Harahap",
#     "NIM" : 2409106050,
#     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" : True,
#     "Social Media" : {
#         "Instagram" : "daffahrhap"
#     }
# }

# print(Biodata.get("KRS")[0:-1])

# Nilai = {
# "Matematika": 80,
# "B. Indonesia": 90,
# "B. Inggris": 81,
# "Kimia": 78,
# "Fisika": 80
# }
# # Tanpa menggunakan items()
# for i in Nilai:
#     print(i)
# print("") # pemisah
# # Menggunakan items()
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")

#setelah menggunakan setdefault
print(Nilai)