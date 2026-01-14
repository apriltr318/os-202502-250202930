# Tugas Praktikum Minggu 12  
Topik: Virtualisasi Menggunakan Virtual Machine  

---

## Identitas
| Nama | NIM | Kelas |
| :--- | :--- | :--- |
| APRIL TRIADI | 250202930 | 1IRB |
| LUTHFI AULIA RAHMAN | 250202948 | 1IKRB |
| MUHAMMAD FATIKH MAHSUN | 250202952 | 1IKRB |


---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari konsep **virtualisasi sistem operasi** dengan menggunakan **Virtual Machine (VM)**.  
Mahasiswa diarahkan untuk menginstal dan menjalankan sistem operasi guest di atas host OS menggunakan perangkat lunak virtualisasi seperti **VirtualBox** atau **VMware**.

Praktikum ini menekankan pemahaman hubungan antara **host OS**, **guest OS**, dan **hypervisor**, serta bagaimana konfigurasi resource (CPU, memori, dan storage) memengaruhi kinerja dan isolasi sistem.

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).  
2. Membuat dan menjalankan sistem operasi guest di dalam VM.  
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).  
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.  
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Ketentuan Teknis
- Virtualisasi dapat menggunakan **VirtualBox** atau **VMware**.  
- Sistem operasi guest bebas (Linux Ubuntu direkomendasikan).  
- Praktikum dapat dilakukan secara **kelompok kecil (2–3 orang)**.

Struktur folder (sesuaikan dengan template repo):
```
praktikum/week12-virtual-machine/
├─ code/
│  └─ catatan_konfigurasi.txt (opsional)
├─ screenshots/
│  ├─ instalasi_vm.png
│  ├─ konfigurasi_resource.png
│  └─ os_guest_running.png
└─ laporan.md
```

---

## Langkah Praktikum
1. **Instalasi Virtual Machine**
   - Instal VirtualBox atau VMware pada komputer host.  
   - Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

2. **Pembuatan OS Guest**
   - Buat VM baru dan pilih OS guest (misal: Ubuntu Linux).  
   - Atur resource awal:
     - CPU: 1–2 core  
     - RAM: 2–4 GB  
     - Storage: ≥ 20 GB

3. **Instalasi Sistem Operasi**
   - Jalankan proses instalasi OS guest sampai selesai.  
   - Pastikan OS guest dapat login dan berjalan normal.

4. **Konfigurasi Resource**
   - Ubah konfigurasi CPU dan RAM.  
   - Amati perbedaan performa sebelum dan sesudah perubahan resource.

5. **Analisis Proteksi OS**
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  
   - Kaitkan dengan konsep *sandboxing* dan *hardening* OS.

6. **Dokumentasi**
   - Ambil screenshot setiap tahap penting.  
   - Simpan di folder `screenshots/`.

7. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
   git push origin main
   ```
  
--- 

## Hasil Eksekusi
1. Instalasi VirtualBox
![instruksi](screenshot/instalasi_vm.png)
2.Konfigurasi Virtual Machine
![Konfigurasi](screenshot/konfigurasi_resource.png)
3.Guesst Running
![os_guest_running](screenshot/os_guest_running.png)
<img width="1920" height="1080" alt="Screenshot 2026-01-10 184134" src="https://github.com/user-attachments/assets/3b46b1db-3db3-4440-bb13-f6a8a7e8a5bc" />


---

​## Analisis

Berdasarkan praktikum yang dilakukan, virtualisasi terbukti efektif untuk menyediakan lingkungan yang terisolasi. Pengaturan resource (RAM & CPU) sangat krusial; pada pengujian saya, pemberian RAM 2GB membuat Ubuntu berjalan cukup stabil untuk tugas ringan, namun penggunaan CPU melonjak saat menjalankan update sistem. Hal ini menunjukkan peran Hypervisor dalam menjadwalkan instruksi antara hardware fisik dan mesin virtual. Dari sisi keamanan, mekanisme sandboxing memastikan bahwa kegagalan sistem pada Guest OS tidak mengganggu stabilitas Host OS.

---

​## Kesimpulan Praktikum

• ​Efisiensi Penggunaan Hardware: Virtualisasi memungkinkan satu perangkat keras fisik untuk menjalankan berbagai sistem operasi secara simultan. Hal ini membuktikan bahwa resource komputer (CPU, RAM, Storage) dapat dibagi dan dikelola secara optimal tanpa memerlukan perangkat fisik tambahan.

• ​Keamanan melalui Isolasi: Praktikum ini menunjukkan bahwa VM berfungsi sebagai lingkungan terisolasi (Sandboxing). Kegagalan sistem, serangan malware, atau kesalahan konfigurasi pada Guest OS tidak akan berdampak pada kestabilan Host OS karena adanya proteksi dari lapisan Hypervisor.

• ​Abstraksi Hardware: Hypervisor memegang peranan vital sebagai mediator yang mengelola instruksi antara sistem operasi tamu (Guest) dan hardware fisik (Host). Pengaturan resource yang tepat sangat menentukan keseimbangan performa antara kedua sistem tersebut.

• ​Fleksibilitas Pengembangan: Penggunaan Virtual Machine sangat efektif untuk kebutuhan pengujian software, pembelajaran sistem operasi baru (seperti Linux), dan pengembangan aplikasi dalam lingkungan yang aman dan dapat dikonfigurasi ulang dengan cepat (melalui fitur snapshot).

---

## Tugas & Quiz
### Tugas
1. Instal dan jalankan OS guest menggunakan VM.  
2. Konfigurasikan resource VM sesuai instruksi.  
3. Dokumentasikan proses instalasi dan konfigurasi.  
4. Tulis laporan praktikum pada `laporan.md`.

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Apa perbedaan antara host OS dan guest OS?
     
| Fitur| Host OS (Sistem Utama) | Guest OS (Sistem Tamu) |
|------|------------------------|------------------------|
| Lokasi Instalasi|Terpasang langsung pada perangkat keras (Hardware) fisik. | Terpasang di atas software virtualisasi (Virtual Machine). |
| Akses Hardware|Memiliki kendali penuh dan akses langsung ke CPU, RAM, dan Disk.|Hanya bisa mengakses resource yang "dipinjamkan" oleh Host melalui Hypervisor. |
| Jumlah|Hanya ada satu Host OS dalam satu komputer fisik.|Bisa ada banyak Guest OS yang berjalan bersamaan.|
| Kemandirian|Tetap berjalan meskipun Guest OS dimatikan atau rusak.|Sangat bergantung pada Host OS; jika Host mati, Guest ikut mati. |
| Tujuan Utama|Mengelola hardware dan menjalankan aplikasi sehari-hari.|Uji coba OS, menjalankan software lama, atau isolasi keamanan. |


2. Apa peran hypervisor dalam virtualisasi?
   
• ​Abstraksi Sumber Daya: Hypervisor memisahkan (mengabstraksi) perangkat keras fisik (CPU, RAM, Storage) dari sistem operasi. Ia membuat "hardware virtual" sehingga satu komputer fisik bisa terbaca sebagai beberapa komputer virtual.

• ​Alokasi & Penjadwalan: Ia bertugas sebagai manajer yang membagi resource hardware secara dinamis. Jika VM1 butuh 2GB RAM dan VM2 butuh 4GB, Hypervisor yang mengatur distribusinya agar tidak bentrok.

• ​Isolasi (Keamanan): Hypervisor memastikan setiap Guest OS berjalan di ruang terisolasi. Jika satu Guest OS crash atau terkena virus, sistem operasi lain dan Host OS tetap aman karena tidak ada akses langsung antar VM.

​Intinya: Hypervisor adalah "polisi lalu lintas" yang mengatur lalu lintas data antara hardware fisik dengan berbagai sistem operasi yang menumpang di atasnya.
  
3. Mengapa virtualisasi meningkatkan keamanan sistem?  
Virtualisasi meningkatkan keamanan sistem melalui konsep utama yang disebut Isolasi (Sandboxing).
Mengapa hal tersebut terjadi:

• ​Isolasi Lingkungan: Setiap Guest OS berjalan di dalam "wadah" virtual yang terpisah secara total dari Host OS. Jika sistem operasi virtual terkena virus atau malware, ancaman tersebut akan terkurung di dalam VM dan tidak dapat menyebar ke sistem utama (Host).

• ​Keamanan Pengujian (Testing): Virtualisasi memungkinkan pengguna untuk menjalankan aplikasi yang mencurigakan atau konfigurasi sistem yang berisiko tanpa membahayakan integritas data fisik di komputer utama.

• ​Snapshot dan Recovery: Virtualisasi memiliki fitur snapshot yang memungkinkan sistem kembali ke kondisi aman sebelumnya secara instan jika terjadi kegagalan sistem atau serangan siber.

---

## F. Output yang Diharapkan
- Screenshot instalasi dan konfigurasi VM.  
- Laporan lengkap instalasi dan analisis VM di `laporan.md`.  
- Semua hasil telah di-*commit* ke GitHub.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
