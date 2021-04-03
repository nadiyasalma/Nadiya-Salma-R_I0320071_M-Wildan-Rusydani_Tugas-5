# membuat program grading nilai

print('masukkan nama anda!')
x = input('nama: ')
print('masukkan nilai anda!')
y = int(input('nilai: '))
niali = 'halo, ', str(x), '!', 'nilai anda setelah di konversi adalah'
if y >= 85:
    print('nilai' + 'A')
elif y >= 80:
    print('nilai' + 'A-')
elif y >= 75:
    print('nilai' + 'B+')
elif y >= 70:
    print('nilai' + 'B')
elif y >= 65:
    print('nilai' + 'C+')
elif y >= 60:
    print('nilai' + 'C')
else:
    print('nilai' + 'E')