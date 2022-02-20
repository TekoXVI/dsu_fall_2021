import random, time

def main():
    n = int(input('List length? '))
    list = make_list(n)
    B = list
    B.sort
    
    t1 = time.time()
    print('Bubble Sort:    ', bubble(list))
    t2 = time.time()
    speed1 = str(round((t2 - t1) * 1000, 4)) +  ' ms'
    print('Speed:          ', speed1)

    t1 = time.time()
    print('Shaker Sort:    ', shaker(list))
    t2 = time.time()
    speed2 = str(round((t2 - t1) * 1000, 4)) +  ' ms'
    print('Speed:          ', speed2)
    
    t1 = time.time()
    print('Counting Sort:  ', counting(list))
    t2 = time.time()
    speed3 = str(round((t2 - t1) * 1000, 4)) +  ' ms'
    print('Speed:          ', speed3)
    

    t1 = time.time()
    print('Merge Sort:     ', merge(list))
    t2 = time.time()
    speed4 = str(round((t2 - t1) * 1000, 4)) +  ' ms'
    print('Speed:          ', speed4)

    t1 = time.time()
    print('Quick Sort:     ', quick(list))
    t2 = time.time()
    speed5 = str(round((t2 - t1) * 1000, 4)) +  ' ms'
    print('Speed:          ', speed5)

    t1 = time.time()
    print('Mod. Quick Sort:', quick_mod(list))
    t2 = time.time()
    speed6 = str(round((t2 - t1) * 1000, 4)) +  ' ms'
    print('Speed:          ', speed6)


    t1 = time.time()
    print('Verification:   ', B)
    t2 = time.time()
    speed7 = str(round((t2 - t1) * 1000, 4)) +  ' ms'
    print('Speed:          ', speed7)    
    
    o = input('Want to see speeds only? (y/n) ')
    if o == 'y':
        print(' Bubble: ', speed1, '\n',
        'Shaker: ', speed2, '\n',
        'Count:  ', speed3, '\n',
        'Merge:  ', speed4, '\n',
        'Quick:  ', speed5, '\n',
        'M.Quick:', speed6, '\n',
        'Python: ', speed7)
    else:
        pass

def bubble(A):

    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                sorted = False
    return A

def shaker(A):

    sorted = False
    while not sorted:
        sorted = True

        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

        for i in range(len(A)-1, 0, -1):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                sorted = False
    return A

def counting(A):
    F = [0] * (len(A) + 1)
    for v in A:
        F[v] += 1
    k = 0
    for i in range(len(F)):
        value = i
        count = F[i]
        for j in range(count):
            A[k] = value
            k += 1
    return A

def make_list(n):
    list = []
    for i in range(n):
        list.append(random.randrange(0, n))
    return list


def merge(A):
    if len(A) <= 1:
        return
    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]

    merge(L)
    merge(R)

    k = 0
    i = 0
    j = 0
    
    while i < len(L) and j < len(R):
        if L[i] > R[j]:
            A[k] = R[j]
            k += 1
            j += 1

        else:
            A[k] = L[i]
            k += 1
            i += 1

    while i < len(L):
        A[k] = L[i]
        k += 1
        i += 1

    while j < len(R):
        A[k] = R[j]
        k += 1
        j += 1
    
    return A


def quick(A):
    quickR(A, 0, len(A)-1)
    return A

def quickR(A, low, high):
    if high - low <= 0:
        return
    pivot = low
    lmgt = low + 1
    for i in range(low+1, high+1):
        if A[i] < A[pivot]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[low], A[pivot] = A[pivot], A[low]
    
    quickR(A, low, pivot-1)
    quickR(A, pivot+1, high)

    return A


def quick_mod(A):
    quickR_mod(A, 0, len(A)-1)
    return A

def quickR_mod(A, low, high):
    if high - low <= 0:
        return
        
    mid = (low + high) // 2
    A[low], A[mid] = A[mid], A[low]
        
    pivot = low
    lmgt = low + 1
    for i in range(low+1, high+1):
        if A[i] < A[pivot]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[low], A[pivot] = A[pivot], A[low]
    
    quickR_mod(A, low, pivot-1)
    quickR_mod(A, pivot+1, high)

    return A

main()





























