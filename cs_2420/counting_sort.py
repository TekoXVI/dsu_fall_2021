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

    print(A)

counting([1,5,4,2,5])
counting([5,8,7,1,2,6,5,2,5,8,4,2,6])
