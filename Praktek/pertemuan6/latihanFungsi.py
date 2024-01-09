def salam(nama, asal):
    print(f"Assalamu'alaikum whai {nama} berasal dari {asal}")


salam("Ahmad", "Bumiayu")


def luasPP(panjang, lebar):
    luas = panjang * lebar
    return luas


"memanggil fungsi luaspp"
a = int(input("Massukan Panjang = "))
b = int(input("Massukan Panjang = "))

print("Luas persegi panjang ", str(luasPP(a, b)))


def luasLingkaran(jari2):
    luas = 3.14*jari2*jari2
    return luas


c = luasLingkaran(7)
print(c)


def kali(x, y):
    return x*y


print("perkalian luas", str(kali(luasLingkaran(7), luasPP(a, b))))
7
