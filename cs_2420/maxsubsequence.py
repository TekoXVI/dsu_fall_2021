def maxSubSequence(A):

    #Kayle's algorithm:
    bestS = 0
    bestE = 0
    bestT = A[0]
    for s in range(len(A)):
      for e in range(s, len(A)):
        total = 0
        for i in range(s, e+1):
          total += A[i]
        if total > bestT:
          bestS = s
          bestE = e
          bestT = total
    return bestS, bestE

A = [-1,2,3,-6,5,6,-5,2,4,-7,5,1,-18,1]

answer = maxSubSequence(A)
print(answer)
