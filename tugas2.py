class Kendaraan:
    pemilik = "alfan jibal akbar"
    def __init__(self, jenis, merk, tahun):
        self.jenis = jenis
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"Jenis: {self.jenis}, Merk: {self.merk}, Tahun: {self.tahun}"

mobil = Kendaraan("Mobil", "avanza", 2020)
print(mobil.info())
motor = Kendaraan("Motor", "scoopy", 2019)
print(motor.info())
print(f"Pemilik Kendaraan: {Kendaraan.pemilik}")