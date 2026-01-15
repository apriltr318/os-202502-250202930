# Reference string
reference_string = [1,2,3,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]

# FIFO
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

# LRU
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

# Optimal
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

# ===== OUTPUT TABEL =====
print("Jumlah Frame | FIFO | LRU | Optimal")
print("-----------------------------------")

for frame in range(1, 8):
    f_fifo = fifo(reference_string, frame)
    f_lru = lru(reference_string, frame)
    f_opt = optimal(reference_string, frame)
    print(f"{frame:^12}|{f_fifo:^6}|{f_lru:^5}|{f_opt:^8}")