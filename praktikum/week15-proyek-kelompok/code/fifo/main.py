import os
import time

def simulasi_laptop_kentang_direct():
    # DATASET LANGSUNG DI DALAM KODE
    # Simulasi user laptop kentang yang maksa buka banyak tab dan aplikasi berat
    riwayat_aplikasi = [
        "Chrome", "Word", "Spotify", "Chrome", 
        "Zoom", "PowerPoint", "Zoom", "Chrome", 
        "Valorant", "Word", "Excel", "WhatsApp"
    ]
    
    kapasitas = 3  # Batas RAM laptop kentang
    ram = []
    page_faults = 0
    log_hasil = []

    header = f"\n{'='*85}\n{' POTATO LAPTOP SIMULATOR - RAM 4GB EDITION ':^85}\n{'='*85}"
    print(header)
    
    tabel_head = f"{'Langkah':<8} | {'Buka':<15} | {'Isi RAM (Background)':<30} | {'Status'}"
    print(tabel_head)
    print("-" * 85)

    for i, aplikasi in enumerate(riwayat_aplikasi, 1):
        status_sistem = ""
        
        # Logika FIFO
        if aplikasi in ram:
            status_sistem = "LANCAR (Hit)  | Ready di Background"
        else:
            page_faults += 1
            if len(ram) < kapasitas:
                ram.append(aplikasi)
                status_sistem = "LOADING...    | Mengisi Slot Kosong"
            else:
                dihapus = ram.pop(0)
                ram.append(aplikasi)
                status_sistem = f"LAG! (Fault)  | Tutup Paksa {dihapus}"

        # Tampilkan Baris
        ram_display = str(ram)
        print(f"{i:<8} | {aplikasi:<15} | {ram_display:<30} | {status_sistem}")
        time.sleep(0.3) # Efek loading biar dramatis

    # Statistik Akhir
    total = len(riwayat_aplikasi)
    hit = total - page_faults
    skor = (hit / total) * 100
    
    footer = (
        f"{'-'*85}\n"
        f"HASIL DIAGNOSA SISTEM:\n"
        f"- Total Aplikasi Dibuka      : {total}\n"
        f"- Total RAM Macet (Fault)    : {page_faults}\n"
        f"- Skor Kesehatan Laptop      : {skor:.1f}%\n"
        f"{'='*85}"
    )
    print(footer)

    # Simpan ke file laporan otomatis
    with open("laporan_simulasi.txt", "w") as f:
        f.write("REKAM MEDIS LAPTOP KENTANG\n")
        f.write(f"Total Fault: {page_faults}\n")
        f.write(f"Skor Akhir: {skor:.1f}%")

if __name__ == "__main__":
    simulasi_laptop_kentang_direct()