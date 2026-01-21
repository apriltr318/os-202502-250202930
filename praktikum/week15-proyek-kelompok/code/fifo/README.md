#  Potato-OS: Laptop Kentang Simulator (RAM 4GB)

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