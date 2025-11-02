from multiprocessing import Process, Value

counter = Value('i', 0)  # 'i' = inteiro

def increment(n):
    for _ in range(n):
        counter.value += 1  # não é thread/process-safe

processes = [Process(target=increment, args=(100000,)) for _ in range(5)]
for p in processes: p.start()
for p in processes: p.join()

print(counter.value)  # normalmente < 500000 devido a race condition
