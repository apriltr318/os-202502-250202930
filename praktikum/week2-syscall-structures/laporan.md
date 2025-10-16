
# Laporan Praktikum Minggu 2
 Topik: Struktur System Call dan Fungsi Kernel
---

## Identitas
- **Nama**  : April Triadi
- **NIM**   : 250202930 
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan perintah `strace` dan `man` sudah terinstal.
   - Konfigurasikan Git (jika belum dilakukan di minggu sebelumnya).

2. **Eksperimen 1 – Analisis System Call**
   Jalankan perintah berikut:
   ```bash
   strace ls
   ```
   > Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.  
   Simpan hasil analisis ke `results/syscall_ls.txt`.

3. **Eksperimen 2 – Menelusuri System Call File I/O**
   Jalankan:
   ```bash
   strace -e trace=open,read,write,close cat /etc/passwd
   ```
   > Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.

4. **Eksperimen 3 – Mode User vs Kernel**
   Jalankan:
   ```bash
   dmesg | tail -n 10
   ```
   > Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

5. **Diagram Alur System Call**
   - Buat diagram yang menggambarkan alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode.
   - Gunakan draw.io / mermaid.
   - Simpan di:
     ```
     praktikum/week2-syscall-structure/screenshots/syscall-diagram.png
     ```

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```
strace ls
```
```
strace -e trace=open,read,write,close cat /etc/passwd
```
```
dmesg | tail -n 10
```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
- >[Screenshot hasil](screenshots/Week2.1.png)
- >[Screenshot hasil](screenshots/Week2.2.png)
- >[Screenshot hasil](screenshots/Week2.3.png)
---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
Jawab pertanyaan berikut di bagian **Quiz** laporan:
1. Apa fungsi utama system call dalam sistem operasi?

   **Jawaban**
 
  - Fungsi utama system call dalam sistem operasi adalah sebagai jembatan antara program (user mode) dengan sistem operasi (kernel mode).
2. Sebutkan 4 kategori system call yang umum digunakan.

    **Jawaban**
    
   | System Call | Keterangan | Fungsi |
    | :--- | :--- | :--- |
    | `open()/openat()` | Membuka atau membuat file dan mengembalikan **File Desciptor (FD)**, yaitu bilangan bulat yang merujuk pada file tersebut dalam kernel. | Menginisiasi operasi I/O file (membaca dan menulis). |
    | `read()` | Membaca sebuah _byte_ data dari sumber yang diwakili oleh **File Descriptor** tertentu (misanya, file,_socket_, atau pipe) ke dalam _buffer_ didalam memori program. | Mengambil data dari perangkat I/O atau file. |
    | `write()` | Menulis sejumalah _byte_ data dari _buffer_ di memori progtam ke tujuan yang diwakili oleh **File Descriptor** (mmisalnya, file, _socket_, atau stdout). | Mengirim data ke perangkat I/O atau file. |
    | `fork()` | Membuat proses baru (**proses child**) yang merupakan salinan identik dari proses yang memanggilnya (**proses parent**). Proses _parent_ dan _child_ akan terus berjalan dari titi kembalinya ```fork()```. | Menciptakan proses baru (multitasking). |
   
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
   
   **Jawaban**
   
   Alasan utama mengapa system call tidak bisa dipanggil langsung oleh user program adalah karena pemisahan antara dua dunia di komputer:
- User mode (mode pengguna) — tempat program biasa berjalan, seperti browser, editor teks, atau game.
- Kernel mode (mode inti) — tempat sistem operasi menjalankan fungsi-fungsi paling sensitif, seperti mengelola memori, CPU, dan perangkat keras

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
