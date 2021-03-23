import re
import os.path
from collections import Counter

def menu():
    print("MENU :")
    print("1. Cek Dokumen")
    print("2. Cek Statistik Karakter Pada Dokumen")
    print("3. Mengganti Karakter Pada Dokumen")
    print("0. Keluar")

def pilihmenu():
    menu = int(input("\nPilih Menu: "))
    if menu == 1:
        cek_dokumen()
    elif menu == 2:
        cek_statistik()
    elif menu == 3:
        ganti_karakter()
    elif menu == 0:
        keluar()
    else:
        print("SILAHKAN PILIH MENU DENGAN SESUAI !!1")
        pilihmenu()

def cek_dokumen():
    dokumen_file = input("\nMasukkan Nama Dokumen : ")
    if (dokumen_file.find(".txt") == -1):
        dokumen_file = dokumen_file + ".txt"
    if (os.path.exists(dokumen_file)):
        a = bool(1)
    else:
        print("\nEROR! Dokumen Tidak Ditemukan!")
        cek_dokumen()
    if (os.path.exists(dokumen_file)):
        file = open(dokumen_file, 'r')
        teks = file.read()
        print("\nIsi Dokumen:")
        print(teks)
        file.close()
        backmenu()

def cek_statistik():
    dokumen_file = input("\nMasukkan Nama Dokumen : ")
    if (dokumen_file.find(".txt") == -1):
        dokumen_file = dokumen_file + ".txt"
    if (os.path.exists(dokumen_file)):
        a = bool(1)
    else:
        print("\nEROR! Dokumen Tidak Ada!")
        cek_statistik()
    if (os.path.exists(dokumen_file)):
        file = open(dokumen_file, 'r')
    string = ((' ').join(line.strip() for line in file))
    mystring = string.lower()
    cek_kata = re.compile('^.')
    mystring = cek_kata.sub('', mystring)
    n = 1
    array = [(mystring[i:i + n]) for i in range(0, len(mystring), n)]
    frekuensi = Counter(array)
    print('\nHasil Statistik:')
    counter = 0
    for i in sorted(frekuensi):
        counter += 1
        print('Karakter: ' + i + ',\t| Frekuensi: ' + str(frekuensi[i]) + ',\t| Peluang : ' + str(
            1 / int(frekuensi[i])))
    print('Total Karakter: ' + str(counter))
    file.close()
    backmenu()

def ganti_karakter():
    dokumen_file = input("\nMasukkan Nama Dokumen : ")
    if (dokumen_file.find(".txt") == -1):
        dokumen_file = dokumen_file + ".txt"
    if (os.path.exists(dokumen_file)):
        a = bool(1)
    else:
        print("\nEROR! Dokumen Tidak ditemukan!")
        ganti_karakter()
    if (os.path.exists(dokumen_file)):
        with open(dokumen_file) as carikarakter:
            karaktersebelum = input("\nKarakter Yang Diganti : ")
            if karaktersebelum in carikarakter.read():
                karaktersesudah = input("\nKarakter (" + karaktersebelum + ") Diganti Dengan : ")
                with open(dokumen_file, 'r+') as karakter:
                    file = karakter.read()
                    file = re.sub(karaktersebelum, karaktersesudah, file)
                    karakter.seek(0)
                    karakter.write(file)
                    karakter.truncate()
            else:
                print("\nEROR! Karakter Tidak Ditemukan!")
                ganti_karakter()
        backmenu()

def backmenu():
    pil = input("\nKembali Ke Menu (y/n) ? ")
    if pil == "y" or "Y" or "ya" or "Ya" or "Yes" or "yes" or "lanjut pak eko":
        menu()
        pilihmenu()
    elif pil == "n" or "N" or "tidak" or "Tidak" or "no" or "No" or "skip bosq":
        keluar()
    else:
        print("\nEROR! Pilihan Tidak Ada")
        backmenu()

def keluar():
    exit()

menu()
pilihmenu()
