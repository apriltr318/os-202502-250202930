import csv

def simulasi_kasir_detail():
    data_pelanggan = []
    
    # 1. Membaca data dari CSV
    try:
        with open('dataset.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_pelanggan.append({
                    'nama': row['pelanggan'],
                    'datang': int(row['kedatangan']),
                    'layanan': int(row['pelayanan']),
                    'info': row['deskripsi']
                })
    except FileNotFoundError:
        print("File dataset.csv tidak ditemukan!")
        return

    # 2. Inisialisasi variabel
    n = len(data_pelanggan)
    waktu_selesai = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    waktu_mulai = [0] * n

    # 3. Perhitungan Algoritma FCFS
    for i in range(n):
        if i == 0:
            waktu_mulai[i] = data_pelanggan[i]['datang']
        else:
            # Mulai saat datang atau saat orang sebelumnya selesai
            waktu_mulai[i] = max(data_pelanggan[i]['datang'], waktu_selesai[i-1])
        
        waktu_selesai[i] = waktu_mulai[i] + data_pelanggan[i]['layanan']
        turnaround_time[i] = waktu_selesai[i] - data_pelanggan[i]['datang']
        waiting_time[i] = waktu_mulai[i] - data_pelanggan[i]['datang']

    # 4. Cetak Hasil Tabel
    print("\n" + "="*95)
    print(f"{'ID':<4} | {'Datang':<6} | {'Layanan':<7} | {'Mulai':<6} | {'Selesai':<7} | {'Wait':<4} | {'TAT':<4} | {'Deskripsi Belanja'}")
    print("-" * 95)

    for i in range(n):
        print(f"{data_pelanggan[i]['nama']:<4} | "
              f"{data_pelanggan[i]['datang']:<6} | "
              f"{data_pelanggan[i]['layanan']:<7} | "
              f"{waktu_mulai[i]:<6} | "
              f"{waktu_selesai[i]:<7} | "
              f"{waiting_time[i]:<4} | "
              f"{turnaround_time[i]:<4} | "
              f"{data_pelanggan[i]['info']}")

    # 5. Ringkasan Statistik
    print("-" * 95)
    print(f"Rata-rata Waiting Time    : {sum(waiting_time)/n:.2f}")
    print(f"Rata-rata Turnaround Time : {sum(turnaround_time)/n:.2f}")
    print("="*95 + "\n")

if __name__ == "__main__":
    simulasi_kasir_detail()