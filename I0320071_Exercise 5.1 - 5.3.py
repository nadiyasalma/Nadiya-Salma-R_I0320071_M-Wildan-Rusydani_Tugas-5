# exercise 5.1

# penggunaan if untuk satu kasus
# inputkan bilangan
bilangan = int(input('masukkan bilangan bulat: '))
# memeriksa bilangan
if bilangan % 2 == 0:
    print('%d adalah bilangan genap' % bilangan)
print()

# exercise 5.2

# penggunaan if untuk dua kasus
# inputkan bilangan
bilangan = int(input('masukkan bilangan bulat: '))
#memeriksa bilangan
if bilangan % 2 == 0:
    print('%d adalah bilangan gebanp' % bilangan)
else:
    print('%d adalah bilangan ganjil' % bilangan)
print()

# exercise 5.3

# penggunaan if untuk tu=iga kasus selebihnya
# inputkan bilangan
print('masukkan koordinat')
x = int(input('masukkan nilai x: '))
y = int(input('masukkan nilai y: '))
info = 'koordinat (' + str(x) = ',' + str(y) + ') berada pada kuadran '
# memeriksa nilai x dan y
if x > 0 and y > 0:
    print(info + 'I')
elif x < 0 and y > 0:
    print(info + 'II')
elif x < 0 and y < 0:
    print(info + 'III')
elif x > 0 and y < 0:
    print(info + 'IV')
else:
    pass
print()
/