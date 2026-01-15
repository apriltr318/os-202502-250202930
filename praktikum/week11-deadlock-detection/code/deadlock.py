# Data: Alokasi [R1, R2] dan Request [R1, R2]
proses = ["P1", "P2", "P3"]

alloc = [[1, 0], [0, 1], [0, 0]]
req = [[0, 1], [1, 0], [1, 1]]

work = [0, 0]  # Resource tersedia
fin = [False, False, False]

# Cek setiap proses
for _ in range(3):
    for i in range(3):
        if not fin[i] and req[i][0] <= work[0] and req[i][1] <= work[1]:
            work[0] += alloc[i][0]
            work[1] += alloc[i][1]
            fin[i] = True

# Hasil
macet = [proses[i] for i in range(3) if not fin[i]]

print("Hasil Deteksi:")
if macet:
    print("DEADLOCK pada:", macet)
else:
    print("Sistem Aman")