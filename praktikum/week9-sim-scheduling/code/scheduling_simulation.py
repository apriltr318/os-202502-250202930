   def hitung_penjadwalan(proses_list, tipe="FCFS"):
    # Urutkan berdasarkan Arrival Time dulu
    proses_list.sort(key=lambda x: x['at'])

    current_time = 0
    hasil = []
    antrian = list(proses_list)

    if tipe == "SJF":
        # Logika SJF Non-Preemptive
        while antrian:
            # Cari proses yang sudah tiba dan punya burst time terkecil
            tersedia = [p for p in antrian if p['at'] <= current_time]
            
            if not tersedia:
                current_time = antrian[0]['at']
                continue
            
            p = min(tersedia, key=lambda x: x['bt'])
            antrian.remove(p)

            p['ct'] = current_time + p['bt']
            p['tat'] = p['ct'] - p['at']
            p['wt'] = p['tat'] - p['bt']
            current_time = p['ct']
            hasil.append(p)
    else:
        # Logika FCFS
        for p in antrian:
            if current_time < p['at']:
                current_time = p['at']
            
            p['ct'] = current_time + p['bt']
            p['tat'] = p['ct'] - p['at']
            p['wt'] = p['tat'] - p['bt']
            current_time = p['ct']
            hasil.append(p)

    return hasil

# Data dari gambar: P1(0,6), P2(1,8), P3(2,7), P4(3,3)
dataset = [
    {'nama': 'P1', 'at': 0, 'bt': 6},
    {'nama': 'P2', 'at': 1, 'bt': 8},
    {'nama': 'P3', 'at': 2, 'bt': 7},
    {'nama': 'P4', 'at': 3, 'bt': 3}
]

def tampilkan(judul, data):
    print(f"\n=== {judul} ===")
    print("Proses | AT | BT | CT | WT | TAT")
    
    total_wt = 0
    total_tat = 0
    
    for p in data:
        print(f"{p['nama']:6} | {p['at']:2} | {p['bt']:2} | {p['ct']:2} | {p['wt']:2} | {p['tat']:3}")
        total_wt += p['wt']
        total_tat += p['tat']
        
    print(f"Rata-rata WT  : {total_wt/len(data):.2f}")
    print(f"Rata-rata TAT : {total_tat/len(data):.2f}")

# Eksekusi
hasil_fcfs = hitung_penjadwalan([p.copy() for p in dataset], "FCFS")
hasil_sjf = hitung_penjadwalan([p.copy() for p in dataset], "SJF")

tampilkan("HASIL FCFS", hasil_fcfs)
tampilkan("HASIL SJF (NON-PREEMPTIVE)", hasil_sjf)