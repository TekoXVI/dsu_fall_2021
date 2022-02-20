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
