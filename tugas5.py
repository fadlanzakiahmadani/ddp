kendaraan = ["honda civic","mobil","CC.46.900","silver","4" ]
kendaraan.append("Rp609.000.000")
kendaraan.append ("Honda")
print(kendaraan)

pilihan = input("Masukkan pilihan: ")
match pilihan:
    case "1":
        s = int(input("Masukkan luas Persegi: "))
        luas = s * s
        print(luas)
    case "2":
        s = int(input("Masukkan luas lingkugan: "))
        luas = s * s
        print(luas)
    case "3":
        s = int(input("Masukkan luas Segitiga: "))
        luas = s * s
        print(luas)
