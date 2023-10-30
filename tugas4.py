#Mari Berbelanja
pelanggan = "Fadlan Ipul"
totalbelanja = 50000

if(totalbelanja > 100000):
    keteragan ="Selamat Anda dapat hadiah"
else:
    keteragan ="terimakasih sudah belanja"

    #cetak data
print("Pelanggan",pelanggan, "\nTotal Belanja Anda Rp.",totalbelanja, "\n",keteragan)


#Mahasiswa diyatakan lulus jika nilai di atas 60
nama = "SI KONTOL GAROX"
matkul = "matematika"
nilai = 90.00
#termary
keteragan = "lulus" if nilai >= 60 else "Gagal"

#cetak data
print ("nama siswa \t:",nama,
"\nMata Kuliah \t:",matkul,
"\nNilai \t\t:",nilai,
"\nKeterangan \t:",keteragan)


nama = "Budi Anto"
makul = "Matematika"
nilai = 90.00
#uji grade dengan IF Multi Kondisi
if(nilai >= 85 and nilai<=100):
    grade = "A"
elif(nilai >= 75 and nilai<=85):
    grade = "B"
elif(nilai >= 60 and nilai<=75):
    grade = "C"
elif(nilai >= 30 and nilai<=60):
    grade = "D"
else:
    grade = "E"

print ("nama siswa \t:",nama,
"\nMata Kuliah \t:",matkul,
"\nNilai \t\t:",nilai,
"\nKeterangan \t:",grade)