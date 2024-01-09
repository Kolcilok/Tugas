# class PersegiPanjang:

#     counter = 5

#     def __init__(self, p, l):
#         self.panjang = p
#         self.lebar = l

#     def ubahPanjang(self, p):
#         self.panjang = p

#     def ubahLebar(self, l):
#         self.lebar = l

#     def hitungKeliling(self):
#         return 2*(self.panjang+self.lebar)

#     def hitungLuas(self):
#         return self.panjang*self.lebar

#     def cetakKeliling(self):
#         print("Keliling Persegi panjang = %.2f" % self.hitungKeliling())

#     def cetakLuas(self):
#         print("Luas Persegi Panjang %.2f" % self.hitungLuas())


# objek1 = PersegiPanjang(10, 5)
# objek2 = PersegiPanjang(4, 5)
# objek3 = PersegiPanjang(2, 6)

# objek1.counter
# objek2.counter
# objek3.counter

# print(objek1.counter)
# print(objek2.counter)
# print(objek3.counter)
# print(PersegiPanjang.counter)

# class Aritmatika:
#     @staticmethod
#     def tambah(a, b):
#         return a+b

#     @staticmethod
#     def kurang(a, b):
#         return a-b

#     @staticmethod
#     def kali(a, b):
#         return a*b

#     @staticmethod
#     def bagi(a, b):
#         return a/b


# print(Aritmatika.bagi(5, 2))
# objek1 = Aritmatika()
# print(objek1.tambah(4, 5))

# class StringList(list):
#     def __init__(self):
#         self.data = []

#     def __repr__(self):
#         return str(self.data)

#     def append(self, objek):
#         if not isinstance(objek, str):
#             raise TypeError("Objek harus bertipe string")
#         self.data.append(objek)

#     def insert(self, indeks, objek):
#         if indeks > len(self.data) or indeks < -len(self.data):
#             raise TypeError("objek di luar rentang")
#         if not isinstance(objek, str):
#             raise TypeError("Objek harus bertipe string (bag2)")
#             self.data.append(self.objek)


# slislt = StringList()
# slislt.append("Apel")
# slislt.append("Anggur")
# slislt.append("Duren")
# print(slislt)
# slislt.append(3)
# print(slislt)

from abc import ABCMeta, abstractmethod
# kelas abstrak


class DuaDimensi(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
        pass
# kelas SegiEmpat turunan dari kelas DuaDimensi


class SegiEmpat(DuaDimensi):
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l
    # membuat metode luas

    def luas(self):
        return self.panjang*self.lebar
# kelas SegiTiga turunan dari kelas DuaDimensi


class SegiTiga(DuaDimensi):
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t
    # membuat metode luas

    def luas(self):
        return 0.5 % (self.alas*self.tinggi)

# kelas Lingkaran turunan dari kelas DuaDimensi


class Lingkaran(DuaDimensi):
    def __init__(self, r):
        self.radius = r

    # membuat metode luas
    def luas(self):
        return 3.14 * self.radius * self.radius


# # obj = DuaDimensi()
# obj1 = SegiTiga(9, 3)
# print(obj1.luas())

# membuat list kosong
listku = []

# menambahkan objek Segiempat ke dalam listku
listku.append(SegiEmpat(2, 2))
listku.append(SegiTiga(3, 6))
listku.append(Lingkaran(7))

# menelusuri seluruh elemen listku
for obj in listku:
    if not issubclass(obj.__class__, DuaDimensi):
        raise TypeError('Objek harus turunan dari kelas DuaDimensi')
    if isinstance(obj, SegiEmpat):
        print("Luas segi empat = ", end=" ")
    elif isinstance(obj, SegiTiga):
        print("Luas segitiga = ", end=" ")
    else:
        print("Luas lingkaran = ", end=" ")
    print(obj.luas())
