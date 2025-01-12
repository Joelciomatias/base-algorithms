import random

arr = [random.randint(-10000,10000) for _ in range(10000)]

arr.sort()

print(arr[0], arr[-1])

def bs(arr, n):

    print(f'procurando o {n}')
    start = 0
    end = len(arr)
    count = 0
    while start <= end:
        count+=1
        middle = (start+end) // 2

        if arr[middle] == n:
            return middle, count
        
        if arr[middle] > n:
            end = middle - 1
        else:
            start = middle + 1

    return -1, count

print(bs(arr,arr[random.randint(0,10000-1)]))


    
