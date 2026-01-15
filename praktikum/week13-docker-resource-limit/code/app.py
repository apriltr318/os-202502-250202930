import os

def create_huge_file(filename, size_in_mb):
    # Menghitung ukuran dalam bytes (1 MB = 1024 * 1024 bytes)
    size_in_bytes = size_in_mb * 1024 * 1024
    
    print(f"Sedang membuat file {filename} sebesar {size_in_mb} MB...")
    
    with open(filename, "wb") as f:
        # Menulis data kosong (null bytes) sebesar ukuran yang ditentukan
        f.write(b"\0" * size_in_bytes)
        
    print("Selesai! File berhasil dibuat.")

# Eksekusi pembuat file 500 MB
create_huge_file("file_raksasa.dat", 500)