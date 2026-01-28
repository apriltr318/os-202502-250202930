# Simulasi Antrian Kasir Supermarket (Algoritma FCFS)



Proyek ini adalah implementasi algoritma **First-Come, First-Served (FCFS)** untuk mensimulasikan antrian pada kasir supermarket. Program ini dirancang untuk menghitung efisiensi layanan berdasarkan waktu kedatangan dan durasi pelayanan pelanggan.



##  Deskripsi Studi Kasus

Dalam simulasi ini, terdapat 5 pelanggan dengan karakteristik belanja yang berbeda-beda. Algoritma FCFS menjamin bahwa pelanggan yang datang lebih awal akan dilayani terlebih dahulu.



### Dataset Pelanggan:

| ID  | Kedatangan | Pelayanan | Deskripsi Belanja          |

|-----|------------|-----------|----------------------------|

| P1  | 0          | 5         | Belanja Bulanan (Banyak)   |

| P2  | 1          | 3         | Kebutuhan Dapur (Sedikit)  |

| P3  | 2          | 8         | Persiapan Pesta (Sangat Banyak) |

| P4  | 3          | 6         | Alat Tulis (Sedang)        |

| P5  | 4          | 2         | Beli Minuman (Sangat Sedikit) |



---



##  Cara Menjalankan Program



### 1. Menjalankan Langsung dengan Python

Pastikan Anda memiliki Python 3.x terinstal. Jalankan perintah berikut di terminal:

```bash

python main.py




## Simulasi Laptop Kentang (RAM 4GB) Algoritma FIFO



Simulator manajemen memori menggunakan algoritma **FIFO (First-In-First-Out)** untuk memvisualisasikan bagaimana laptop spesifikasi rendah menangani beban aplikasi yang berlebihan.



##  Fitur Utama

* **Logika FIFO**: Simulasi nyata penggantian halaman (page replacement) memori.

* **Dataset CSV**: Mendukung input data eksternal via file `dataset.csv`.

* **Auto-Reporting**: Menghasilkan file `laporan_simulasi.txt` secara otomatis.

* **Docker Ready**: Sudah dilengkapi Dockerfile untuk dijalankan di lingkungan terisolasi.



## 🛠️ Persyaratan Sistem

* Python 3.10 atau versi lebih tinggi.

* Docker (Opsional, jika ingin dijalankan via Container).



##  Struktur Proyek

```text

├── main.py              # Script utama (Logika Program)

├── dataset.csv          # Daftar aplikasi yang akan dijalankan

├── Dockerfile           # Konfigurasi Containerization

└── laporan_simulasi.txt # Hasil diagnosa (Generated otomatis)















