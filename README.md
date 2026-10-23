
# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Intan Muhafadoh
NIM: 2225250132
Kelas: ...

## Tujuan

Mengolah kumpulan data numerik dengan list Python, menghitung statistik nilai mahasiswa, dan menentukan kelulusan berdasarkan batas nilai 60.

## Struktur Program

Folder `latihan` berisi:
- `01_buat_list.py`: Membuat list.
- `02_indeks_slicing.py`: Mempelajari indeks dan slicing.
- `03_manipulasi_list.py`: Memanipulasi list.
- `04_agregasi_nilai.py`: Mengolah data nilai.
- `05_filter_kelulusan.py`: Menyaring nilai kelulusan.
- `06_fungsi_statistik.py`: Menggunakan fungsi statistik.

Folder `praktik` berisi:
- `analisis_nilai_mahasiswa.py`: Menghitung jumlah data, total, rata-rata, nilai minimum, maksimum, dan informasi kelulusan mahasiswa.

## Cara Menjalankan

Jalankan perintah berikut di terminal dari folder utama proyek:

```bash
python3 praktik/analisis_nilai_mahasiswa.py
```

## Test Case

| Data | Pengujian | Hasil Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Data utama | Total nilai | 695 | 695 | Berhasil |
| Data utama | Rata-rata | 69.50 | 69.50 | Berhasil |
| Data utama | Minimum dan maksimum | 45 dan 90 | 45 dan 90 | Berhasil |
| Data utama | Jumlah lulus | 7 | 7 | Berhasil |
| Data utama | Jumlah belum lulus | 3 | 3 | Berhasil |
| `[60, 70, 80]` | Rata-rata | 70.00 | 70.00 | Berhasil |
| `[60, 70, 80]` | Minimum dan maksimum | 60 dan 80 | 60 dan 80 | Berhasil |
| `[60, 70, 80]` | Jumlah lulus | 3 | 3 | Berhasil |
| `[59, 60, 61]` | Jumlah lulus | 2 | 2 | Berhasil |
| `[]` | Rata-rata data kosong | 0 tanpa error | 0 tanpa error | Berhasil |

## Refleksi

Saya memahami bahwa list dapat menyimpan banyak data dalam satu variabel dan setiap elemen memiliki indeks. Saya juga memahami penggunaan fungsi `len()`, `sum()`, `min()`, dan `max()` untuk mengolah data numerik.

Kesalahan yang berhasil diperbaiki adalah indentasi pada kode Python. Saya juga belajar menangani list kosong agar fungsi rata-rata tidak menghasilkan error.
