#   Nama : Alfan Jibal Akbar
#   NIM  : 24241150
class Mhs_alumni:
    def __init__(self, tahun_lulus=2025):
        self.tahun_lulus = tahun_lulus
    
    def info_alumni(self):
        return f"Lulus tahun {self.tahun_lulus}"


class Mhs_aktif:
    def __init__(self, tahun_masuk=2024):
        self.tahun_masuk = tahun_masuk
    
    def info_aktif(self):
        return f"Masuk tahun {self.tahun_masuk}"


class Mahasiswa(Mhs_alumni, Mhs_aktif):
    def __init__(self, nama, nim, prodi, angkatan):
        Mhs_alumni.__init__(self)
        Mhs_aktif.__init__(self)
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.angkatan = angkatan
    
    # atribut tambahan child
    def ktm(self):
        return f"KTM atas nama {self.nama} (NIM {self.nim})"

    def ijazah(self):
        return f"Ijazah akan diterbitkan setelah lulus tahun {self.tahun_lulus}"

    def beasiswa(self):
        return f"{self.nama} mendapatkan beasiswa"

    def info_mahasiswa(self):
        return (
            f"Nama    : {self.nama},"
            f"NIM     : {self.nim},"
            f"Prodi   : {self.prodi},"
            f"Angkatan: {self.angkatan},"
            f"{self.info_aktif()},"
            f"{self.info_alumni()},"
        )


class DataKampus(Mahasiswa):
    def __init__(self, nama, nim, prodi, angkatan, kampus="Universitas Pendidikan Mandalika"):
        super().__init__(nama, nim, prodi, angkatan)
        self.kampus = kampus

    def info_kampus(self):
        return f"{self.nama} terdaftar di {self.kampus}"


mhs = DataKampus(
    nama="Alfan Jibal Akbar",
    nim="24241150",
    prodi="Pendidikan Teknologi Informasi",
    angkatan=2024
)

print(mhs.info_mahasiswa())
print(mhs.info_kampus())
print(mhs.ktm())
print(mhs.beasiswa())