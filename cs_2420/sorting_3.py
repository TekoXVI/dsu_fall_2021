import sys, random, math

def bubble(A, compares):

    sorted = False
    while not sorted:
        sorted = True

        
        
        for i in range(len(A)-1):
            compares[0] += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i] 
                sorted = False
    return A

def shaker(A, compares):

    sorted = False
    while not sorted:
        sorted = True
        
        for i in range(len(A)-1):
            compares[0] += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

        

        for i in range(len(A)-1, 0, -1):
            compares[0] += 1
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                sorted = False
    return A

def counting(A, compares):
    compares[0] = len(A)
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

def merge(A, compares):
    if len(A) <= 1:
        return
    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]

    merge(L, compares)
    merge(R, compares)

    k = 0
    i = 0
    j = 0
    
    while i < len(L) and j < len(R):
        compares[0] += 1
        if L[i] > R[j]:
            A[k] = R[j]
            k += 1
            j += 1

        else:
            A[k] = L[i]
            k += 1
            i += 1

    while i < len(L):
        compares[0] += 1
        A[k] = L[i]
        k += 1
        i += 1

    while j < len(R):
        compares[0] += 1
        A[k] = R[j]
        k += 1
        j += 1
    
    return A


def quick(A, compares):
    quickR(A, 0, len(A)-1, compares)
    return A

def quickR(A, low, high, compares):
    if high - low <= 0:
        return
    pivot = low
    lmgt = low + 1
    for i in range(low+1, high+1):
        compares[0] += 1
        if A[i] < A[pivot]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[low], A[pivot] = A[pivot], A[low]
    
    quickR(A, low, pivot-1, compares)
    quickR(A, pivot+1, high, compares)

    return A


def quick_mod(A, compares):
    quickR_mod(A, 0, len(A)-1, compares)
    return A

def quickR_mod(A, low, high, compares):
    if high - low <= 0:
        return
        
    mid = (low + high) // 2
    A[low], A[mid] = A[mid], A[low]
        
    pivot = low
    lmgt = low + 1
    for i in range(low+1, high+1):
        compares[0] += 1
        if A[i] < A[pivot]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[low], A[pivot] = A[pivot], A[low]
    
    quickR_mod(A, low, pivot-1, compares)
    quickR_mod(A, pivot+1, high, compares)

    return A


def make_list(n):
    list = []
    for i in range(n):
        list.append(random.randrange(0, n))
    return list

def make_ms_list(n):
    list = []
    for i in range(n):
        list.append(random.randrange(0, n))
    list.sort()
    list[0], list[-1] = list[-1], list[0]
    return list

def format(x):
    if x != 0:
        x = math.log(x)/math.log(2)
    return x

def main():
    sys.setrecursionlimit(5000)
    # print 2 title lines by hand
    print("Compares with Random Data\n")
    names = ["Bubble", "Shaker", "Counting", "Merge", "Quick", "M_Quick"]

    print("   ", end=" ")
    for name in names:
        print(name.ljust(10, " "), end="")
    print()

    sorts = [bubble, shaker, counting, merge, quick, quick_mod]

    for s in range(3, 13):
        size = 2 ** s
        # print s as a formatted int, supressing return
        print("{:02d}".format(s), end="  ")
        
        for sort in sorts:
            A = make_list(size)
            compares = [0]
            sort(A, compares)
            # print log of compares, formatted, supressing return
            c = format(compares[0])
            print("{:<10.2f}".format(c), end="")
        print()
    # Test on random data and on mostly sorted data.
    # (Make a new function to create mostly sorted data.
    # Have it first call the MakeRandomData function,
    # have Python sort it,
    # then swap the first and last elements.)
    print("\n")
    print("Compares with Mostly Sorted Data\n")
    print("   ", end=" ")
    for name in names:
        print(name.ljust(10, " "), end="")
    print()
    for s in range(3, 13):
        size = 2 ** s
        # print s as a formatted int, supressing return
        # print("%02d" % (s), end=" ")
        print("{:02d}".format(s), end="  ")
        for sort in sorts:
            A = make_ms_list(size)
            compares = [0]
            sort(A, compares)
            # print log of compares, formatted, supressing return   
            c = format(compares[0])
            # print("%06.2f" % (c), end=" ")
            print("{:<10.2f}".format(c), end="")
        print()


main()


























#