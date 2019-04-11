# Belajar-Membuat-Fungsi-Python
# ungsi Binary Number
# buat fungsi def dengan nama bin dengan parameter n


def bin(n): #buat inisialisasi string bernama an, artinya kamu menginginkan eksekusi dari an berupa data string
    an = " " #N besar menyatakan inisialisasi ulang dari n
    N = n    #while untuk kejadian terus menerus sedangkan if untuk kejadian sekali saja, ketika kejadian N selalu lebih besar dari 0 maka perintah selanjutnya akan terus berulang
    while N > 0:
        # inisialisasi a digunakan untuk menyatakan N di modulo 2, jadi akan menghasilkan nilai sisa
        # nilai sisa dari N, jika genap akan bersisa 0, dan jika ganjil akan menyisakan angka 1. (baca lagi arti modulo)
        a = N % 2
        # fungsi // akan menghasilkan nilai hasil bagi yang hanya mengambil nilai integernya saja, misal : data float 3,05.             maka yang diambil hanya angka 3 nya saja
        N = N // 2
        # a di perintahkan dengan perintah str agar dapat dimasukkan dalam fungsi an, sedangan an tidak perlu karena sudah di           initialisasi dari awal
        an = str(a) + an
        # print an
    return an
print(bin(3))
