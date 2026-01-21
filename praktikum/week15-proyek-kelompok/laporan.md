# Laporan Proyek Kelompok: Mini Simulasi Sistem Operasi
### Tugas Praktikum Minggu 15 

---

## 1. Pendahuluan

### A. Latar Belakang
Sistem Operasi berperan penting dalam mengatur bagaimana proses dijalankan serta bagaimana memori dialokasikan agar sistem dapat berjalan optimal. Konsep inti seperti penjadwalan CPU dan manajemen memori seringkali bersifat abstrak, sehingga diperlukan pendekatan praktis untuk mendemonstrasikannya melalui analogi kegiatan sehari-hari.

Dalam proyek ini, dilakukan simulasi algoritma **First Come First Serve (FCFS)** menggunakan studi kasus antrean kasir dan algoritma **Page Replacement FIFO** menggunakan studi kasus manajemen RAM pada ponsel. Simulasi ini dikembangkan menggunakan Python untuk memberikan visualisasi konkret mengenai waktu tunggu (*waiting time*) dan kesalahan halaman (*page fault*).

### B. Tujuan Proyek
Tujuan dari proyek kelompok ini adalah sebagai berikut:
* Memahami cara kerja algoritma FCFS dalam penjadwalan proses.
* Memahami mekanisme page replacement FIFO pada manajemen memori.
* Mengimplementasikan algoritma Sistem Operasi ke dalam bentuk program fungsional.
* Menganalisis hasil simulasi berdasarkan output tabel dan metrik performa yang dihasilkan.

---

## 2. Arsitektur Aplikasi

### A. Desain Arsitektur Umum
Aplikasi dibangun menggunakan arsitektur modular berbasis **Command Line Interface (CLI)**. Logika program dipisahkan antara pengontrol utama (`main.py`) dan manajemen data di direktori `data/`. Seluruh sistem dibungkus dalam **Docker** untuk menjamin portabilitas.

### B. Deskripsi Modul dan Dataset
1.  **Modul Penjadwalan Proses (FCFS)**:
    * **Deskripsi**: Mensimulasikan antrean kasir di mana pelanggan yang datang lebih awal dilayani terlebih dahulu.
    * **Dataset (`dataset.csv`)**: Berisi kolom `pelanggan` (ID), `kedatangan` (waktu tiba), `pelayanan` (durasi), dan `deskripsi` aktivitas belanja.
2.  **Modul Manajemen Memori (FIFO)**:
    * **Deskripsi**: Memodelkan RAM ponsel yang menutup aplikasi tertua (indeks pertama) saat kapasitas penuh untuk memberi ruang bagi aplikasi baru.
    * **Logika**: Sistem melacak status *Hit* (aplikasi sudah ada di RAM) dan *Fault* (aplikasi perlu dimuat baru/mengganti aplikasi lama).

### C. Alur Data (Data Flow)
* **Input**: Membaca data dari `dataset.csv` untuk FCFS dan riwayat akses aplikasi untuk FIFO.
* **Proses**: Skrip `main.py` menghitung *Waiting Time* (WT = Waktu Mulai - Waktu Kedatangan) dan *Turnaround Time* (TAT = Waktu Selesai - Waktu Kedatangan).
* **Output**: Visualisasi tabel status RAM dan ringkasan statistik rata-rata WT/TAT yang disimpan dalam `laporan_simulasi.txt`.

---

## 3. Konfigurasi Lingkungan (Docker)
Proyek ini menggunakan **Dockerfile** dengan spesifikasi sebagai berikut:
* **Base Image**: `python:3.14-alpine` untuk efisiensi ukuran.
* **Konfigurasi**:
    * Menetapkan direktori kerja di `/app`.
    * Menyalin file `main.py` dan folder `data/` ke dalam kontainer.
    * Menjalankan perintah `python main.py` saat kontainer diaktifkan.

---

## 4. Hasil dan Analisis

### A. Analisis Simulasi FCFS (Antrean Kasir)
Urutan kedatangan sangat memengaruhi waktu tunggu. Kelebihannya adalah kesederhanaan implementasi, namun berisiko mengalami **Convoy Effect**, di mana pelanggan dengan durasi pelayanan lama menghambat pelanggan di belakangnya yang mungkin hanya membutuhkan waktu singkat.
Algoritma ini memproses pelanggan berdasarkan urutan kedatangan di `dataset.csv`.

**Tabel Output Simulasi FCFS:**
| ID | Datang | Layanan | Mulai | Selesai | Wait | TAT | Deskripsi |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| P1 | 0 | 5 | 0 | 5 | 0 | 5 | Belanja Bulanan |
| P2 | 1 | 3 | 5 | 8 | 4 | 7 | Kebutuhan Dapur |
| P3 | 2 | 8 | 8 | 16 | 6 | 14 | Persiapan Pesta |
| P4 | 3 | 6 | 16 | 22 | 13 | 19 | Alat Tulis |
| P5 | 4 | 2 | 22 | 24 | 18 | 20 | Beli Minuman |

![Screenshot hasil](./screenshots/hasil_tabel_cpu_scheduling.png)

Dapat dilihat adanya kenaikan *Waiting Time* yang signifikan pada P4 dan P5 karena harus menunggu P3 yang memiliki waktu layanan lama (8 unit). Inilah yang disebut dengan *Convoy Effect*.

### B. Analisis Simulasi FIFO Page Replacement (laptop)
FIFO bekerja secara murni berdasarkan waktu masuk tanpa mempertimbangkan frekuensi penggunaan aplikasi. Hal ini sering menyebabkan aplikasi yang masih dibutuhkan terhapus dari memori jika aplikasi tersebut adalah yang paling lama berada di RAM, mengakibatkan jumlah *page fault* yang tinggi pada sistem dengan RAM terbatas.
Berdasarkan logika di `main.py`, sistem akan melakukan "Tutup Paksa" pada aplikasi tertua jika RAM penuh.

**Log Output Status RAM:**

![Screenshot hasil](./screenshots/demo_run_page_replacement.png)
![Screenshot hasil](./screenshots/hasil_tabel_page_replacement.png)

---

## 5. Identitas Kelompok dan Pembagian Tugas

| No | Nama Anggota | NIM | Peran / Tugas |
|:---:|:---|:---:|:---|
| 1 | **April Triadi** | 250202930 | Project Lead & Dockerization |
| 2 | **Mohammad Fatikh Mahsun** | 250202952 | Developer 1 (Logic FCFS & Dataset) |
| 3 | **Luthfi Aulia Rahman** | 250202948 | Developer 2 (Logic FIFO & UI) |
| 4 | **Syafi`iyah Ramadhani** | 250202968 | Dokumentasi & Quality Assurance |

---

## 6. Jawaban Quiz

1. Tantangan terbesar integrasi modul apa, dan bagaimana solusinya?

    - Tantangan Integrasi: Inkonsistensi format data antara CSV (untuk FCFS) dan TXT/string (untuk FIFO). 

    - Solusi: Standarisasi input melalui modularisasi fungsi baca file dan penggunaan kontrak data yang jelas sebelum diproses oleh algoritma.

2. Mengapa Docker membantu proses demo dan penilaian proyek?

     Manfaat Docker: Menjamin aplikasi berjalan sama di semua perangkat ("*It works on my machine*") dan menyederhanakan proses demo karena penguji cukup menjalankan `docker compose up` tanpa instalasi manual.

3. Jika dataset diperbesar 10x, modul mana yang paling terdampak performanya? Jelaskan.

    Dampak Dataset 10x: Dampak Perubahan Skala Dataset
    berdasarkan struktur sistem yang dikembangkan, jika dataset diperbesar 10x, maka analisis dampaknya adalah sebagai berikut:

    Alasan Utama:

      1. Akumulasi Convoy Effect

         Dalam algoritma FCFS, setiap proses harus menunggu seluruh proses sebelumnya selesai tanpa adanya interupsi (non-preemptive). Jika data bertambah 10x, risiko munculnya proses dengan durasi pelayanan yang sangat lama di awal antrean meningkat. Hal ini akan mengakibatkan "efek konvoi" yang memanjang, menyebabkan lonjakan Waiting Time (WT) secara kumulatif bagi ratusan data pelanggan di belakangnya.

    2. Beban Kalkulasi Statistik

        Alur data pada `main.py` menghitung WT dan TAT secara sekuensial (berurutan). Dengan dataset 10x lebih besar:

     * Sistem harus menghitung waktu mulai dan waktu selesai yang saling bergantung dari baris pertama hingga terakhir.
     * Beban komputasi untuk menghasilkan agregasi statistik rata-rata pada file `laporan_simulasi.txt` akan meningkat drastis karena dependensi data tersebut.

    3. Efisiensi Waktu Tunggu

         Berbeda dengan modul FIFO (Manajemen Memori) yang performanya dibatasi oleh kapasitas RAM yang statis, performa FCFS sangat bergantung pada volume baris data. Semakin banyak pelanggan dalam dataset, maka efisiensi waktu tunggu rata-rata akan memburuk secara signifikan jika durasi layanan antar pelanggan tidak seragam.


---

## 7. Kesimpulan dan Saran
Simulasi ini berhasil mendemonstrasikan bagaimana Sistem Operasi mengelola antrean proses dan memori secara efisien. Disarankan untuk menambahkan algoritma **Least Recently Used (LRU)** pada modul memori dan **Shortest Job First (SJF)** pada modul penjadwalan untuk perbandingan performa yang lebih mendalam.

---
**Pernyataan Akhir**: Laporan ini disusun sebagai tanggung jawab akademik mata kuliah Sistem Operasi berdasarkan hasil kerja kelompok yang sebenar-benarnya.
