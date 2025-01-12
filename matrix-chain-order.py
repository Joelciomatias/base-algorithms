def matrix_chain_order(p, acc=0, added=0):

    if added == 2:
        return acc
    if len(p) == 2 and added == 0:
        p.insert(0, 1)
        added += 1
    elif len(p) == 2 and added == 1:
        p.append(1)
        added += 1

    n = len(p) - 1 
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                print(f'{p[i]} * {p[k + 1]} * {p[j + 1]}')
                acc += (p[i] * p[k + 1] * p[j + 1])
                p.pop(k+1)
                return matrix_chain_order(p, acc, added)
    return 0

p = [3,1,5,8]

min_operations = matrix_chain_order(p)

print(f"Número mínimo de multiplicações necessárias: {min_operations}")
