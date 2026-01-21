# PRESENTASI PROYEK KELOMPOK: MINI SIMULASI OS
**Topik:** CPU Scheduling (FCFS) & Memory Management (FIFO)  
**Tugas Praktikum Minggu:** 15

---

## Nama Anggota Kelompok 
- **April Triadi** (250202930)
- **Mohammad Fatikh Mahsun** (250202952)
- **Luthfi Aulia Rahman** (250202948)
- **Syafi'iyah Ramadhani** (250202968)

---
  
## 1. PENDAHULUAN
### Latar Belakang
* Konsep inti Sistem Operasi seperti penjadwalan CPU dan manajemen memori seringkali bersifat abstrak.
* Diperlukan pendekatan praktis melalui analogi kegiatan sehari-hari untuk memberikan visualisasi konkret mengenai waktu tunggu dan kesalahan halaman.

### Studi Kasus
1.  **Simulasi Antrean Kasir (FCFS)**: 
    * Merepresentasikan pelanggan yang datang lebih awal akan dilayani terlebih dahulu.
    * Digunakan untuk memahami cara kerja algoritma *First Come First Serve* dalam penjadwalan proses.
2.  **Simulasi RAM HP (FIFO)**: 
    * Memodelkan RAM ponsel yang menutup aplikasi tertua saat kapasitas penuh untuk memberi ruang bagi aplikasi baru.
    * Digunakan untuk memahami mekanisme *page replacement* FIFO pada manajemen memori.

---

## 2. ARSITEKTUR APLIKASI
### Tech Stack
* **Bahasa:** Python (Berbasis CLI/Terminal).
* **Environment:** Docker menggunakan base image `python:3.14-alpine` untuk efisiensi dan portabilitas.
* **Struktur:** Arsitektur modular berbasis *Command Line Interface*.

### Desain Modular
* **Controller Utama (`main.py`):** Berfungsi sebagai pengontrol utama logika program.
* **Manajemen Data (`data/`):** Direktori khusus yang menyimpan dataset simulasi seperti `dataset.csv`.
* **Output:** Visualisasi tabel dan ringkasan statistik (WT/TAT) yang disimpan dalam `laporan_simulasi.txt`.

---

## 3. SKENARIO DEMO
1.  **Konfigurasi Docker**: Menetapkan direktori kerja di `/app` dan menyalin seluruh file modul ke dalam kontainer.
2.  **Jalankan Aplikasi**: Perintah `python main.py` mengeksekusi simulasi secara otomatis.
3.  **Proses Data**:
    * Membaca data kedatangan pelanggan dari `dataset.csv`.
    * Mensimulasikan akses aplikasi pada memori RAM ponsel.

---

## 4. HASIL & ANALISIS: CPU SCHEDULING (FCFS)

**Tabel Output Simulasi:**
| ID | Arrival time | Burst time | Start time | Finish time | WT | TAT |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 5 | 0 | 5 | 0 | 5 |
| P2 | 1 | 3 | 5 | 8 | 4 | 7 |
| P3 | 2 | 8 | 8 | 16 | 6 | 14 |
| P4 | 3 | 6 | 16 | 22 | 13 | 19 |
| P5 | 4 | 2 | 22 | 24 | 18 | 20 |

**Analisis:**

* Terjadinya Convoy Effect:

 Bukti Terjadinya Convoy Effect
Analisis mengenai P4 dan P5  itu Mari kita lihat lompatan angka pada kolom WT (Waiting Time):

P1 ke P2: WT naik 4 unit.

P2 ke P3: WT naik 2 unit.

P3 ke P4: WT melonjak 7 unit (dari 6 ke 13).

P4 ke P5: WT melonjak 5 unit (dari 13 ke 18).

Lompatan besar pada P4 terjadi tepat setelah P3 yang memiliki durasi Layanan: 8 (durasi terlama di dataset). Ini adalah bukti nyata Convoy Effect: satu proses besar menghambat semua proses kecil di belakangnya.Terjadi kenaikan *Waiting Time* signifikan pada P4 dan P5 karena harus menunggu P3 yang memiliki durasi pelayanan lama (8 unit).
* Urutan kedatangan sangat memengaruhi performa sistem meskipun implementasinya sederhana.

---

## 5. HASIL & ANALISIS: MEMORY (FIFO)

**Analisis Mekanisme:**
* Sistem melakukan "Tutup Paksa" pada aplikasi tertua jika RAM penuh berdasarkan urutan waktu masuk.
* **Kelemahan:** Aplikasi yang masih dibutuhkan dapat terhapus jika aplikasi tersebut adalah yang paling lama berada di RAM, mengakibatkan jumlah *page fault* yang tinggi.
* FIFO tidak mempertimbangkan frekuensi penggunaan, hanya fokus pada waktu muat aplikasi ke memori.

Implementasi algoritma FIFO pada modul manajemen memori memiliki kelemahan mendasar karena sistem hanya bekerja berdasarkan urutan waktu masuk tanpa memedulikan seberapa sering sebuah aplikasi digunakan oleh pengguna. Hal ini menyebabkan aplikasi yang sebenarnya masih sangat dibutuhkan atau sering diakses justru terhapus secara otomatis hanya karena aplikasi tersebut adalah yang paling lama berada di dalam RAM. Akibatnya, sistem sering kali mengalami page fault yang tinggi karena harus memuat ulang aplikasi yang baru saja dihapus, sehingga penggunaan memori menjadi tidak efisien terutama ketika menangani aplikasi penting yang seharusnya menetap di RAM dalam jangka waktu lama.

---

## 6. TIM & KONTRIBUSI

Berdasarkan riwayat repositori (*Git logs*), berikut adalah pembagian tugas kelompok:

| Nama Anggota | Peran Utama | Deskripsi Kontribusi |
| :--- | :--- | :--- |
| **April Triadi** | *Project Lead* | Koordinasi proyek dan Dockerization. |
| **Muhammad Fatikh Mahsun** | *Developer 1* | Logika FCFS, pembuatan dataset, dan penambahan file contoh via upload. |
| **Luthfi Aulia Rahman** | *Developer 2* | Logika FIFO, pengembangan UI, pembuatan data awal, dan update `README.md`. |
| **Syafiiyah Ramadhani** | *QA & Docs* | Dokumentasi, pembersihan direktori kode, serta update tugas praktikum minggu 11-13. |


---
**Terima Kasih**

*Laporan ini disusun sebagai tanggung jawab akademik mata kuliah Sistem Operasi.*
