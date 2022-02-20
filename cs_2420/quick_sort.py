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
            print(A)
            lmgt += 1
    pivot = lmgt - 1
    A[low], A[pivot] = A[pivot], A[low]
    print(A)
    quickR(A, low, pivot-1)
    quickR(A, pivot+1, high)
    return A

quick([4,1,9,8,2,7,5,3,5,7])