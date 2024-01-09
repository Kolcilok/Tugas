class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def skripsi(self):
        print("Mahasiswa Sedang Mengerjakan Skipsi.")

    def skripsiA(self):
        print(f"{self.nama} Sedang Skipsi")


"Membuat object mahasiswa"
mhs1 = Mahasiswa("21.0.01.0034", "Abjul kodir", "Teknik Mesin")

print(mhs1.nama)
print(mhs1.jurusan)
mhs1.skripsi()
mhs1.skripsiA()
