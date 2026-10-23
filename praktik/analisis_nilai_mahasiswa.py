
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []
    for x in data:
        if x >= batas:
            lulus.append(x)
    return lulus


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Menghitung statistik
jumlah_data = len(nilai)
total = sum(nilai)
rata = rata_rata(nilai)
minimum = min(nilai) if jumlah_data > 0 else 0
maksimum = max(nilai) if jumlah_data > 0 else 0

# Menghitung kelulusan
lulus = nilai_lulus(nilai, batas=60)
jumlah_lulus = len(lulus)
jumlah_tidak_lulus = jumlah_data - jumlah_lulus

# Menampilkan ringkasan
print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Seluruh nilai       : {nilai}")
print(f"Banyak data         : {jumlah_data}")
print(f"Total nilai         : {total}")
print(f"Rata-rata           : {rata:.2f}")
print(f"Nilai minimum       : {minimum}")
print(f"Nilai maksimum      : {maksimum}")
print(f"Batas kelulusan     : 60")
print(f"Daftar nilai lulus  : {lulus}")
print(f"Jumlah mahasiswa lulus       : {jumlah_lulus}")
print(f"Jumlah mahasiswa belum lulus : {jumlah_tidak_lulus}")

print("\n=== PENGUJIAN TEST CASE ===")

print("Rata-rata [60, 70, 80]:", f"{rata_rata([60, 70, 80]):.2f}")
print("Minimum [60, 70, 80]:", min([60, 70, 80]))
print("Maksimum [60, 70, 80]:", max([60, 70, 80]))
print("Jumlah lulus [60, 70, 80]:", len(nilai_lulus([60, 70, 80])))

print("Jumlah lulus [59, 60, 61]:", len(nilai_lulus([59, 60, 61])))
print("Rata-rata data kosong:", rata_rata([]))

