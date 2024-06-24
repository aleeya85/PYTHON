import random

def pilih_kata():
    kata_kata = ['python', 'programming', 'hangman', 'developer', 'algorithm', 'function', 'variable', 'loop', 'condition', 'dictionary']
    return random.choice(kata_kata)

def tampilkan_tebakan(kata, tebakan):
    tampilan = ''
    for huruf in kata:
        if huruf in tebakan:
            tampilan += huruf
        else:
            tampilan += '_'
    return tampilan

def hangman():
    kata_rahasia = pilih_kata()
    tebakan = []
    salah = 0
    batas_salah = 6
    selesai = False

    print("Selamat datang di permainan Hangman!")
    print("Cuba untuk menebak kata yang telah saya pilih.")

    while not selesai and salah < batas_salah:
        print(f"\nKata yang harus ditebak: {tampilkan_tebakan(kata_rahasia, tebakan)}")
        print(f"Tebakan yang salah: {salah} dari {batas_salah}")
        huruf = input("Masukkan satu huruf: ").lower()

        if huruf in tebakan:
            print("Anda sudah menebak huruf ini. Cuba huruf lain.")
        elif huruf in kata_rahasia:
            tebakan.append(huruf)
            print("Betul!")
        else:
            tebakan.append(huruf)
            salah += 1
            print("Salah!")

        if '_' not in tampilkan_tebakan(kata_rahasia, tebakan):
            selesai = True

    if selesai:
        print(f"\nSelamat! Anda berhasil menebak kata '{kata_rahasia}' dengan {salah} kesalahan.")
    else:
        print(f"\nMaaf, anda kalah. Kata yang benar adalah '{kata_rahasia}'.")

if __name__ == "__main__":
    hangman()