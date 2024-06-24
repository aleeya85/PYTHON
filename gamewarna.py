#!usr/bin/env python
import random

def teka_warna():
    warna = ['merah', 'biru', 'kuning', 'hijau', 'oren', 'ungu', 'hitam', 'putih', 'kelabu', 'coklat']
    warna_rahsia = random.choice(warna)
    percubaan = 0

    print("Selamat datang di permainan Teka Warna!")
    print("Saya telah memilih satu warna dari daftar berikut:")
    print(", ".join(warna))
    print("Cuba untuk meneka warna tersebut.\n")

    while True:
        teka_warna = input("Masukkan warna tekaan anda: ").lower()
        percubaan += 1

        if teka_warna not in warna:
            print("Warna yang anda masukkan tidak ada dalam daftar. Sila cuba lagi.\n")
        elif teka_warna < warna_rahsia:
            print("Tekaan anda salah! Warna yang anda pilih berada di urutan lebih rendah dalam daftar. Cuba lagi.\n")
        elif teka_warna > warna_rahsia:
            print("Tekaan anda salah! Warna yang anda pilih berada di urutan lebih tinggi dalam daftar. Cuba lagi.\n")
        else:
            print(f"YEAY! Tekaan anda betul {percubaan} percubaan.\n")
            break

if __name__ == "__main__":
    teka_warna()
