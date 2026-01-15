import matplotlib.pyplot as plt

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

def optimal(refs, frames):
    memory = []
    faults = 0
    for i, page in enumerate(refs):
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                future = refs[i+1:]
                idx = []
                for m in memory:
                    if m in future:
                        idx.append(future.index(m))
                    else:
                        idx.append(float('inf'))
                memory[idx.index(max(idx))] = page
    return faults

reference_string = [1,2,3,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
frames = range(1, 8)

fifo_faults = [fifo(reference_string, f) for f in frames]
lru_faults = [lru(reference_string, f) for f in frames]
opt_faults = [optimal(reference_string, f) for f in frames]

plt.plot(frames, fifo_faults, marker='o', label='FIFO')
plt.plot(frames, lru_faults, marker='o', label='LRU')
plt.plot(frames, opt_faults, marker='o', label='Optimal')
plt.xlabel('Jumlah Frame')
plt.ylabel('Jumlah Page Fault')
plt.title('Perbandingan Algoritma Page Replacement')
plt.legend()
plt.grid()
plt.savefig('page_replacement.png')
plt.show()