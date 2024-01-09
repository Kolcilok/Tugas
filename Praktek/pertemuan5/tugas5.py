# li = [20, 30, 40, 50, 60]

# for el in li:
#     print(el, end=" ")


li = [20, 30, 40, 50, 60]
# mendapatkan objek iterator (itr) dari sebuah list
itr = li.__iter__()
# mendapatkan elemen pertama (el)
el = itr.__next__()

# while el:
#     print(el, end=' ')
#     try:
#         el = itr.__next__()
#     except StopIteration as e:
#         print()
#         break

# try:
#     a = int(input("Massukan Nilai a: "))
#     b = int(input("Massukan Nilai b: "))
#     c = a/b
#     print("%d/%d = %.2f" % (a, b, c))
# except ZeroDivisionError as e:
#     print("Error : Bro/Sist , Telah Terjadi pembagian dengan nol")

# try:
#     f = open("contoh.txt", "w")
#     f.write("Python\n")
#     f.write("Ruby\n")
#     f.write("PHP\n")
# finally:
#     f.close()

# try:
#     f = open("contoh.txt", "r")
#     lines = f.readlines()
#     for line in lines:
#         print(lines, end="")
# finally:
#     f.close()

# try:
#     f = open("contoh.txt", "r")
#     lines = f.readlines()
#     for line in lines:
#         print(lines, end="")
# except IOError as e:
#     print("ERROR: File tidak Ditemukan")
# finally:
#     if f:
#         f.close()


# def intdiv(a, b):
#     if not isinstance(a, int) or\
#             not isinstance(b, int):
#         raise TypeError("ERROR: a dan b harus bertipe bilangan bulat")
#     if b == 0:
#         raise ZeroDivisionError("Error : b tidak boleh noll")
#     c = a//b
#     return c
# print(intdiv(10, 7))


# def kali(a, b):
#     c = a*b
#     return c


# def cetak(s):
#     print(s)


# # memanggil fungsi kali()
# x = kali(3, 5)
# cetak(x)
# cetak("Belajar Pemrogramn Dekstop")
# print(__name__)

# def cetakBonus(daftar=[]):
#     def hitungBonus(gaji):
#         if gaji < 5000000:
#             bonus = 0.05*gaji
#         elif 5000000 <= gaji < 7000000:
#             bonus = 0.10*gaji
#         else:
#             bonus = 0.15*gaji
#         return bonus
#     hitungBonus(6000000)
#     for nama, gaji in daftar:
#         b = hitungBonus(gaji)
#         print("%s\t%d\t\t%.2f" % (nama, gaji, b))


# data = [("agus", 4000000), ("Andi", 6000000), ("Ali", 9000000)]
# cetakBonus(data)

# def minim(a, b):
#     if a < b:
#         return a
#     else:
#         return b


# m = minim(3, 7)
# print(m)

# class Titik(object):
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def pindah(self, x, y):
#         self.x = x
#         self.y = y

#     def cetak(self):
#         print("%d\t\t%d" % (self.x, self.y))


# t = Titik()
# t.pindah(3, 8)
# t.cetak()

def tulis(s, gantiBaris=True):
    if gantiBaris:
        print(s)
    else:
        print(s, end="")


tulis("Nur")
tulis("Wahyu")
tulis("Hidayat")

tulis("Nur", False)
tulis("Wahyu", False)
tulis("Hidayat")
