print("==============================")
print("Contoh sederhana pembuatn list pada bahasa pemrograman python")

list1 = ['pemrograman dasar', 'arsitektur komputer', 1999, 2019]

list2 = [1, 2, 3, 4, 5]

list3 = ["a", "b", "c", "d"]

print(list1, list2, list3)

# Cara mengakses nilai di dalam list Python
print("==============================")
print("Cara mengakses nilai di dalam list Python")

list1 = ['pemrograman dasar', 'arsitektur komputer', 1999, 2019]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# Update Nilai Dalam List Python
print("==============================")
print("Update Nilai Dalam List Python")
List = ['pemrograman dasar', 'arsitektur komputer', 1999, 2019]
print("Nilai ada pada index 2: ", List[2])
List[2] = 2022
print("Nilai baru ada pada index 2", List[2])


print("Cara menghapus nilai pada list python")
List = ['matematika', 'bahasa inggris', 1999, 2022]

print(List)

del List[2]
print("Setelah dihapus nilai pada index 2: ", List)
print(List)

# Contoh cara membuat Dictionary pada Python
print("==============================")
print("Contoh cara membuat Dictionary pada Python")

dict = {'Name': 'Muhammad Fawwaz', 'Age': 9, 'Class': 'Third'}

print("dict['Name']: ", dict['Name'])

print("dict['Age']: ", dict['Age'])
# Update dictionary python
print("==============================")
print("Update dictionary python")

dict = {'Name': 'Uwais Alhanif', 'Age': 7, 'Class': 'First'}

print(dict)

dict['Age'] = 8  # Mengubah entri yang sudah ada
dict['School'] = "SDIT AS Sunnah "  # Menambah entri baru
print("dict['School']: ", dict['School'])


# contoh cara menghapus pada Dictionary Python
print("==============================")
print("Contoh cara menghapus pada Dictionary Python")
dict = {'Name': 'Andika', 'Age': 17, 'Class': 'First'}
print(dict)
del dict['Name']  # hapus entri dengan key 'Name'
print(dict)
dict.clear()  # hapus semua entri di dict
print(dict)
del dict  # hapus dictionary yang sudah ada

# Contoh sederhana pembuatan tuple pada bahasa pemrograman python
print("==============================")
print("Contoh sederhana pembuatan tuple pada bahasa pemrograman python")

tup1 = ('Bahasa Arab', 'Bahasa Indonesia', 1993, True)
tup2 = (10, 20, 30, 40, 50)
tup3 = "a", "b", "c", "d"
print(tup1, tup2, tup3)

# Cara mengakses nilai tuple
print("==============================")
print("Cara mengakses nilai tuple")

tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])

print("tup2[1:5]: ", tup2[1:5])

print(tup1)

# Update Nilai Dalam Tuple Python
print("==============================")
print("Update Nilai Dalam Tuple Python")
tup1 = (102, 304.506)

tup2 = ('Aabc', 'Xxyz')

tup3 = tup1 + tup2
print(tup3)

# Hapus Nilai Dalam Tuple Python
print("==============================")
print("Hapus Nilai Dalam Tuple Python")
tup = ('fisika', 'kimia', 1993, 2017)
print(tup)

# hapus tuple dengan statement del
del tup  # lalu buat kembali tuple yang baru dengan elemen yang diinginkan
tup = ('Bahasa', 'Literasi', 2020)
print("Setelah menghapus tuple :", tup)
