class kendaraan:
    def __init__(self, kemudi, kursi):
        self.kemudi = kemudi
        self.kursi = kursi

    def bunyiKlakson(self):
        print("Klakson Berbunyi")


class Motor(kendaraan):
    def bunyiKlakson(self):
        print("Klakson Berbunyi wadaww..wadaww..")


class Bus(kendaraan):
    def bunyiKlakson(self):
        print("Klakson Berbunyi uhuyyy.. uhuyy..")


class sepeda(kendaraan):
    def bunyiklakson(self):
        print("Bunyi Klakson kuw....kew...kuw...!")


supra = Motor("Stang", "Satu")
supra.bunyiKlakson()
citra = Bus("setir", "100")
citra.bunyiKlakson()
bmx = sepeda("Stanggapit", "1")
bmx.bunyiklakson()
herley = Motor("stang", "satu")
herley.bunyiKlakson()
