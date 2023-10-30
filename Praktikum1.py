umur = input("masukan umur anda :")
if int(umur) <17:
    keterangan = "masih anak"
elif int(umur) <45:
    keterangan = "sudah dewasa"
elif int(umur) <65:
    keterangan = "sudah tua"
else:
    keterangan = "sudah tua"
print('umur anda',umur , 'artinya',keterangan)


a = int(input('masukan nilai a: '))
b = int(input('masukan nilai b: '))
c = int(input('masukan nilai c: '))

if a > b and a> c:
    print('A yang trebesar')
elif b > a and b > c:
    print('B yang trebesar')
else:
    print('C yang trebesar')