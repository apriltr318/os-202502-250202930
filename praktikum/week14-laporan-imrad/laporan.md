# Tugas Praktikum Minggu 14  
Topik: Penyusunan Laporan Praktikum Format IMRAD

---

## Abstrak

Laporan ini membahas simulasi algoritma page replacement pada sistem operasi, yaitu FIFO, LRU, dan Optimal. Simulasi dilakukan menggunakan bahasa pemrograman Python untuk menghitung jumlah page fault berdasarkan variasi jumlah frame memori. Hasil simulasi menunjukkan bahwa algoritma Optimal menghasilkan jumlah page fault paling sedikit, diikuti oleh LRU dan FIFO.

---

## 1. Pendahuluan

Sistem operasi modern menggunakan memori virtual untuk menjalankan proses secara efisien. Salah satu masalah yang sering terjadi pada memori virtual adalah page fault, yaitu kondisi ketika halaman yang dibutuhkan tidak tersedia di memori utama sehingga harus diambil dari penyimpanan sekunder. Hal ini dapat menurunkan kinerja sistem.

Untuk mengatasi masalah tersebut, sistem operasi menerapkan algoritma page replacement. Algoritma ini menentukan halaman mana yang harus diganti ketika memori penuh. Beberapa algoritma yang umum digunakan adalah FIFO (First In First Out), LRU (Least Recently Used), dan Optimal.

Tujuan dari laporan ini adalah melakukan simulasi dan membandingkan performa ketiga algoritma page replacement berdasarkan jumlah page fault.


---

## 2. Metode

### 2.1 Alat dan Lingkungan

Bahasa pemrograman: Python

Library: matplotlib

Sistem operasi: Windows / Linux

---

### 2.2 Data Uji

Reference string yang digunakan dalam simulasi adalah:
```bash
1 2 3 2 1 5 6 2 1 2 3 7 6 3 2 1 2 3 6
```
Jumlah frame memori yang diuji adalah 1 sampai dengan 7 frame.

---

### 2.3 Algoritma

Algoritma yang digunakan dalam simulasi:

FIFO (First In First Out)

LRU (Least Recently Used)

Optimal

---

### 2.4 Kode Program
```bash
import matplotlib.pyplot as plt

# Reference string
reference_string = [1,2,3,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]

# FIFO Algorithm
def fifo(refs, frames):
    memory = []
    faults = 0
    index = 0
    for page in refs:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory[index] = page
                index = (index + 1) % frames
    return faults

# LRU Algorithm
def lru(refs, frames):
    memory = []
    faults = 0
    for page in refs:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        else:
            memory.remove(page)
            memory.append(page)
    return faults

# Optimal Algorithm
def optimal(refs, frames):
    memory = []
    faults = 0
    for i, page in enumerate(refs):
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                future = []
                for p in memory:
                    if p in refs[i+1:]:
                        future.append(refs[i+1:].index(p))
                    else:
                        future.append(float('inf'))
                memory[future.index(max(future))] = page
    return faults

# Simulasi
frames = range(1, 8)
fifo_faults = [fifo(reference_string, f) for f in frames]
lru_faults = [lru(reference_string, f) for f in frames]
opt_faults = [optimal(reference_string, f) for f in frames]

# Grafik
plt.plot(frames, fifo_faults, marker='o', label='FIFO')
plt.plot(frames, lru_faults, marker='o', label='LRU')
plt.plot(frames, opt_faults, marker='o', label='Optimal')
plt.xlabel('Jumlah Frame')
plt.ylabel('Page Fault')
plt.title('Perbandingan Algoritma Page Replacement')
plt.legend()
plt.grid(True)
plt.show()
```

---

## 3. Hasil

## 3.1 Hasil Simulasi

![hasil simulasi](week14.1.png)

### 3.2 Tabel Hasil Simulasi

Jumlah Frame	| FIFO |	LRU |	Optimal
|:---:|:---:|:---:|:---:|
| 1	| 19	| 19 | 19 |
| 2 |	17 |	15 |	13 |
| 3 |	15 | 12 |	9 |
| 4 | 13 | 10	| 8 |
| 5 |	11	| 8	|  7 |
| 6	| 10 |	7	| 6 |
| 7 |  9 | 6 | 6 |

Grafik hasil simulasi menunjukkan bahwa jumlah page fault menurun seiring bertambahnya jumlah frame memori.

---

## 4. Pembahasan

Algoritma FIFO memiliki performa paling rendah karena tidak mempertimbangkan pola penggunaan halaman. Halaman yang masih sering digunakan dapat tergantikan hanya karena lebih dulu masuk ke memori.

Algoritma LRU memberikan hasil yang lebih baik karena mengganti halaman yang paling lama tidak digunakan. Algoritma Optimal menghasilkan jumlah page fault paling sedikit karena mempertimbangkan penggunaan halaman di masa depan, namun sulit diterapkan secara nyata.

---

## 5. Kesimpulan

Berdasarkan simulasi yang dilakukan, algoritma Optimal memiliki performa terbaik dengan jumlah page fault paling sedikit. Algoritma LRU memberikan hasil mendekati Optimal dan lebih realistis untuk diterapkan, sedangkan FIFO memiliki performa paling rendah.

---

## Daftar Pustaka

1. Silberschatz, A., Galvin, P. B., & Gagne, G. Operating System Concepts.


2. Modul Praktikum Sistem Operasi – Page Replacement


