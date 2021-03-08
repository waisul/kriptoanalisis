import re
import os.path
from collections import Counter

dokumen_file = input('Masukkan Nama Dokumen : ')
if(dokumen_file.find('.txt') == -1):
    dokumen_file = dokumen_file+'.txt'
if (os.path.exists(dokumen_file)):
    a = bool(1)
else:
    print('EROR! File Yang Diinginkan Tidak Tersedia!')
    exit()
if (os.path.exists(dokumen_file)):
    file = open(dokumen_file, 'r+')
string = ((' ').join(line.strip() for line in file))
mystring = string.lower()
cek_kata = re.compile('[^a-zA-Z]')
mystring = cek_kata.sub('', mystring)
n = int(input('Masukkan Jumlah Karakter : '))
frekuensi = {}
array = [(mystring[i:i + n]) for i in range(0, len(mystring), n)]
frekuensi = Counter(array)
print('\n\nHasil Analisis:')
counter=0
for i in sorted(frekuensi):
    counter += 1
    print('Karakter: ' + i + ',\t| Karakter Yang Sama: ' + str(frekuensi[i]) + ',\t| Frekuensi : ' + str(1/int(frekuensi[i])))
print('Total Karakter Keseluruhan: ' + str(counter))
