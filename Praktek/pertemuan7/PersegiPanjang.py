def keliling(La, Lb):
    keliling = 2*(La+Lb)
    return keliling


La = (input("Massukan Panjang Persegi = "))
Lb = (input("Massukan Lebar Persegi = "))

k = keliling(La, Lb)
print("Luas Persegi", (k))
