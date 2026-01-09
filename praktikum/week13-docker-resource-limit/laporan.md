# Tugas Praktikum Minggu 13  
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : April Triadi
- **NIM**   : 250202930
- **Kelas** : 1IKRB

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa mempelajari konsep **containerization** menggunakan Docker, serta bagaimana sistem operasi membatasi pemakaian sumber daya proses melalui mekanisme isolasi dan kontrol resource (mis. *cgroups* pada Linux).

Fokus praktikum adalah:
1. Membuat **Dockerfile sederhana** untuk menjalankan aplikasi/skrip.
2. Menjalankan container dengan **pembatasan resource** (CPU dan memori).
3. Mengamati dampak pembatasan resource melalui output program dan monitoring sederhana.

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.

---

## Petunjuk dan Ketentuan
- Sistem operasi host bebas (Windows/macOS/Linux). Disarankan memakai **Docker Desktop** (atau Docker Engine di Linux).
- Program berbasis **terminal**.
- Fokus penilaian pada **keberhasilan build & run container**, **penerapan resource limit**, serta **kualitas analisis**.

Struktur folder (sesuaikan dengan template repo):
```
praktikum/week13-docker-resource-limit/
├─ code/
│  ├─ Dockerfile
│  └─ app.*
├─ screenshots/
│  └─ hasil_limit.png
└─ laporan.md
```

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```
   
---
   
## Hasil Eksekusi
1. xxxx
![xxxx](screenshot/week13.1.png)
2.xxxx
![xxxx](screenshot/week13.2.png)
3.xxxx
![xxxx](screenshot/week13.3.png)
4.xxxx
![xxxx](screenshot/week13.4.png
5.xxxc
![xxxx](screenshot/week13.5.png)

---

## Analisis
Pengujian menunjukkan bahwa container yang dijalankan tanpa limit dapat menggunakan CPU dan memori secara bebas sesuai kemampuan sistem host. Proses berjalan lebih cepat dan alokasi memori tidak dibatasi.
Saat container dijalankan dengan limit CPU dan memori, performa aplikasi menurun. Pembatasan CPU menyebabkan proses komputasi menjadi lebih lambat, sedangkan pembatasan memori dapat menyebabkan aplikasi gagal berjalan jika melebihi batas yang ditentukan. Monitoring menggunakan docker stats memperlihatkan penggunaan resource yang lebih terkontrol.

---

## Kesimpulan
Docker mendukung pembatasan penggunaan CPU dan memori pada container.
Container tanpa limit memiliki performa lebih cepat namun berpotensi mengganggu sistem.
Pembatasan resource membuat penggunaan CPU dan RAM lebih terkendali.
Resource limit penting untuk menjaga kestabilan dan efisiensi sistem.

---

## Tugas & Quiz
### Tugas
1. Buat Dockerfile sederhana dan program uji di folder `code/`.
2. Build image dan jalankan container **tanpa limit**.
3. Jalankan container dengan limit **CPU** dan **memori**.
4. Sajikan hasil pengamatan dalam tabel/uraian singkat di `laporan.md`.

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Mengapa container perlu dibatasi CPU dan memori?
2. Apa perbedaan VM dan container dalam konteks isolasi resource?
3. Apa dampak limit memori terhadap aplikasi yang boros memori?

---

*Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_.

