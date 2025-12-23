# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU  

---

# Identitas
- **Nama**  : April Triadi
- **NIM**   : 250202930
- **Kelas** : 1IKRB
- 
---

## A. Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan **mengimplementasikan program simulasi sederhana algoritma penjadwalan CPU**, khususnya **FCFS dan SJF**.  
Berbeda dengan Minggu 5–6 yang berfokus pada perhitungan manual, pada minggu ini mahasiswa mulai **mengotomatisasi perhitungan menggunakan program**, menjalankan dataset uji, serta menyajikan hasil dalam bentuk tabel atau grafik.

Praktikum ini menjadi jembatan antara **pemahaman konseptual** dan **implementasi komputasional** algoritma sistem operasi.

---

## B. Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## C. Ketentuan Teknis
- Bahasa pemrograman **bebas** (Python / C / Java / lainnya).  
- Tidak wajib GUI, cukup **program berbasis terminal**.  
- Fokus penilaian pada **logika algoritma dan keakuratan hasil**, bukan kompleksitas bahasa.

Struktur folder (sesuaikan dengan template repo):
```
praktikum/week9-sim-scheduling/
├─ code/
│  ├─ scheduling_simulation.*
│  └─ dataset.csv
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
```

---

## D. Langkah Pengerjaan
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```

---

## E. Tugas & Quiz
### Tugas
1. Buat program simulasi FCFS atau SJF.  
2. Jalankan program dengan dataset uji.  
3. Sajikan output dalam tabel atau grafik.  
4. Tulis laporan praktikum pada `laporan.md`.

### Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?
Simulasi diperlukan karena memungkinkan pengujian algoritma scheduling dalam kondisi yang mendekati situasi nyata tanpa harus diterapkan langsung pada sistem sebenarnya. Dengan simulasi, berbagai skenario beban kerja, jumlah proses, dan waktu kedatangan dapat diuji secara aman dan efisien. Selain itu, simulasi membantu mengevaluasi kinerja algoritma seperti waktu tunggu, waktu respon, dan utilisasi CPU secara lebih objektif.
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
Pada dataset besar, perhitungan manual sangat rentan terhadap kesalahan dan membutuhkan waktu yang lama. Sebaliknya, simulasi mampu memproses data dalam jumlah besar dengan cepat dan konsisten. Hasil simulasi biasanya lebih akurat dan detail, serta dapat menampilkan statistik kinerja secara menyeluruh, sedangkan perhitungan manual cenderung terbatas dan kurang praktis.
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.
Algoritma First Come First Serve (FCFS) merupakan algoritma yang paling mudah diimplementasikan. Hal ini karena FCFS hanya menjalankan proses berdasarkan urutan kedatangan tanpa perlu perhitungan prioritas atau waktu proses yang kompleks. Struktur logikanya sederhana dan tidak memerlukan mekanisme tambahan, sehingga cocok untuk pembelajaran dasar algoritma scheduling.

---

## F. Output yang Diharapkan
- Kode program simulasi di folder `code/`.  
- Dataset uji di `code/dataset.csv`.  
- Screenshot hasil eksekusi di `screenshots/`.  
- Laporan lengkap di `laporan.md`.  
- Semua hasil telah di-*commit* ke GitHub.

---

## G. Referensi
1. Silberschatz, A., Galvin, P., Gagne, G. *Operating System Concepts*, 10th Ed.  
2. Tanenbaum, A. *Modern Operating Systems*, 4th Ed.  
3. OSTEP – Scheduling.
