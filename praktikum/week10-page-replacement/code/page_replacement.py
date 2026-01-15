pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3

def simulasi(algoritma):
    memory = []
    faults = 0
    print(f"\n--- Simulasi {algoritma.upper()} ---")
    print("Page | Memory State      | Status")
    print("-" * 32)
    
    for page in pages:
        status = "Hit"
        if page not in memory:
            status = "Fault"
            faults += 1
            if len(memory) >= capacity:
                memory.pop(0)
            memory.append(page)
        elif algoritma == "lru":
            # Logika LRU: Pindahkan yang baru diakses ke belakang
            memory.remove(page)
            memory.append(page)
            
        print(f" {page}   | {str(memory):<15} | {status}")
    
    print("-" * 32)
    print(f"Total Page Fault: {faults}")

# Menjalankan simulasi
simulasi("fifo")
simulasi("lru")

