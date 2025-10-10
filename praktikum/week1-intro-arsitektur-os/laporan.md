
# Laporan Praktikum Minggu Ke-1
"Arsitektur Sistem Operasi dan Kernel"

---

## Identitas
- **Nama**  : April Triadi
- **NIM**   : 250202930 
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

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
1. Sebutkan tiga fungsi utama sitem operasi pada komputer !
   **Jawaban:** Mengelola sumber daya komputer seperti CPU, memori, dan perangkat input-output.
Menyediakan antarmuka pengguna untuk berinteraksi dengan perangkat komputer.
Menjalankan aplikasi dan program yang diinstal oleh pengguna
2. Jelaskan perbedaan kernel mode dan user mode !
   **Jawaban:** Kernel mode adalah mode di mana sistem operasi bekerja dengan hak akses penuh terhadap seluruh sumber daya komputer, seperti memori, perangkat keras, dan CPU. Dalam mode ini, sistem dapat menjalankan instruksi yang bersifat kritis dan sensitif. Sebaliknya, user mode adalah mode di mana program atau aplikasi pengguna dijalankan dengan hak akses terbatas. Program di user mode tidak bisa langsung mengakses perangkat keras atau memori sistem, dan jika terjadi kesalahan, hanya program tersebut yang akan berhenti tanpa memengaruhi keseluruhan sistem.
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel !
   **Jawaban: Pada arsitektur monolithic ada Linux, MS-DOS dan UNIX
Pada microkernel ada MINIX, QNX dan Mach**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya? 
