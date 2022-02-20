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