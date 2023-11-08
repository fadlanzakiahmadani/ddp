nama_kendaraan = input("Nama Kendaraan (contoh: mobil, motor): ")
jenis_bensin = input("Jenis Bensin (Pertalite/Pertamax/Pertamax Turbo): ")
kota_tujuan = input("Kota Tujuan: ")

jarak_tempuh = 0
harga_per_liter = 0
total_harga = 0

if jenis_bensin == "Pertalite":
    harga_per_liter = 10000
    jarak_tempuh = 12
elif jenis_bensin == "Pertamax":
    harga_per_liter = 14000
    jarak_tempuh = 13
elif jenis_bensin == "Pertamax Turbo":
    harga_per_liter = 17000
    jarak_tempuh = 13.5

if kota_tujuan == "Jakarta":
    jarak_kota = 20
elif kota_tujuan == "Bekasi":
    jarak_kota = 35.7
elif kota_tujuan == "Depok":
    jarak_kota = 5
elif kota_tujuan == "Tangerang":
    jarak_kota = 99
elif kota_tujuan == "Bogor":
    jarak_kota = 120.6

pemakaian_bensin = jarak_kota / jarak_tempuh
total_harga = pemakaian_bensin * harga_per_liter

print("Nama Kendaraan:", nama_kendaraan)
print("Jenis Bensin:", jenis_bensin)
print("Kota Tujuan:", kota_tujuan)
print("Pemakaian Bensin:", pemakaian_bensin)
print("Total Harga Bensin:",int(total_harga))



nama_pembeli = input("Masukkan Nama Pembeli: ")
no_hp_pembeli = input("Masukkan No Hp Pembeli: ")
pesan_menu = input("Pesan Menu Apa? (makanan atau minuman): ")

harga_menu = 0
jumlah_pesanan = 0
harga_total = 0

if pesan_menu == "makanan":
    print("Menu Makanan:")
    print("1. Nasi Goreng (Rp. 15.000)")
    print("2. Mie Goreng (Rp. 12.000)")
    print("3. Ayam Geprek (Rp. 18.000)")
    menu_makanan = input("Masukkan pesanan makanan: ")
    if menu_makanan == "1":
        harga_menu = 15000
    elif menu_makanan == "2":
        harga_menu = 12000
    elif menu_makanan == "3":
        harga_menu = 18000

elif pesan_menu == "minuman":
    print("Menu Minuman:")
    print("1. Aneka Jus (Rp. 15.000)")
    print("2. Soft Drink (Rp. 10.000)")
    print("3. Sweet Ice Tea (Rp. 5.000)")

    menu_minuman = input("Masukkan pesanan minuman: ")
    if menu_minuman == "1":
        harga_menu = 15000
    elif menu_minuman == "2":
        harga_menu = 10000
    elif menu_minuman == "3":
        harga_menu = 5000

i = 1
while i <= 20:
    if i % 3 == 0:
        print("STT Nurul Fikri")
    else:
        print(i)
    i += 1