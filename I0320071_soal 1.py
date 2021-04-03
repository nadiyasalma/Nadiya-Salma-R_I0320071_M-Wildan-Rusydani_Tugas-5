# membuat program menyapa pengunjung

print('masukkan nama anda!')
x = input('nama: ')
print('masukkan jenis kelamin anda!')
y = input('jenis kelamin (p/l): ')

if x == 'l':
    print("halo selamat datang, tuan", x, "!")
else:
    print("halo selamat datang, nyonya", y, "!")