# Input Nama Kendaraan
nama_kendaraan = input("Nama kendaraan? (contoh: mobil, motor): ")
# Input Jenis Bensin
jenis_bensin = input("Jenis bensin? (Pertalite, Pertamax, Pertamax Turbo): ")
# Input Kota Tujuan
kota_tujuan = input("Kota yang dituju?: ")

# Menentukan Harga per Liter dan Jarak Tempuh per Liter sesuai jenis bensin
if jenis_bensin == "Pertalite":
    harga_per_liter = 10000
    jarak_tempuh_per_liter = 12
elif jenis_bensin == "Pertamax":
    harga_per_liter = 14000
    jarak_tempuh_per_liter = 13
elif jenis_bensin == "Pertamax Turbo":
    harga_per_liter = 17000
    jarak_tempuh_per_liter = 13.5

# Menentukan Jarak ke Kota Tujuan
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

# Menghitung Pemakaian Bensin dan Total Harga Bensin
pemakaian_bensin = jarak_kota / jarak_tempuh_per_liter
total_harga_bensin = pemakaian_bensin * harga_per_liter

# Output Informasi
print("Nama Kendaraan:", nama_kendaraan)
print("Jenis Bensin:", jenis_bensin)
print("Kota Tujuan:", kota_tujuan)
print("Pemakaian Bensin:", pemakaian_bensin, "liter")
print("Total Harga Bensin:", total_harga_bensin, "rupiah") 


#Input Nama Pembeli
nama_pembeli = input("Masukkan Nama Pembeli: ")
# Input No Hp Pembeli
no_hp_pembeli = input("Masukkan No Hp Pembeli: ")
# Input Pesan Menu (makanan atau minuman)
pesan_menu = input("Pesan Menu Apa? (makanan atau minuman): ")

if pesan_menu == "makanan":
    print("Menu Makanan:")
    print("1. Nasi Goreng - Rp. 15,000")
    print("2. Mie Goreng - Rp. 12,000")
    print("3. Ayam Geprek - Rp. 18,000")
    pesanan = input("Masukkan pesanan (e.g., Nasi Goreng): ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
    
    if pesanan == "Nasi Goreng":
        harga_makanan = 15000
    elif pesanan == "Mie Goreng":
        harga_makanan = 12000
    elif pesanan == "Ayam Geprek":
        harga_makanan = 18000
    
    total_harga = harga_makanan * jumlah_pesanan
else:
    print("Menu Minuman:")
    print("1. Aneka Jus - Rp. 15,000")
    print("2. Soft Drink - Rp. 10,000")
    print("3. Sweet Ice Tea - Rp. 5,000")
    pesanan = input("Masukkan pesanan (e.g., Aneka Jus): ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
    
    if pesanan == "Aneka Jus":
        harga_minuman = 15000
    elif pesanan == "Soft Drink":
        harga_minuman = 10000
    elif pesanan == "Sweet Ice Tea":
        harga_minuman = 5000
    
    total_harga = harga_minuman * jumlah_pesanan

# Output Informasi
print("Nama Pembeli:", nama_pembeli)
print("No Hp Pembeli:", no_hp_pembeli)
print("Menu yang di Pesan:", pesanan)
print("Jumlah pesanan:", jumlah_pesanan)
print("Harga yang harus di bayarkan:", total_harga, "rupiah")


#tugas3
for i in range(1, 21):
    if i % 3 == 0:
        print("STT Nurul Fikri")
    else: print(i)





