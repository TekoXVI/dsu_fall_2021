import random, time

def main():
    n = int(input('List length? '))
    list = make_list(n)
    B = list
    B.sort
    
    t1 = time.time()
    print('Bubble Sort:  ', bubble(list))
    t2 = time.time()
    speed1 = str(round((t2 - t1) * 1000, 4)) +  ' ms'
    print('Speed:        ', speed1)

    t1 = time.time()
    print('Shaker Sort:  ', shaker(list))
    t2 = time.time()
    speed2 = str(round((t2 - t1) * 1000, 4)) +  ' ms'
    print('Speed:        ', speed2)
    
    
    t1 = time.time()
    print('Counting Sort:', counting(list))
    t2 = time.time()
    speed3 = str(round((t2 - t1) * 1000, 4)) +  ' ms'
    print('Speed:        ', speed3)
    
    
    t1 = time.time()
    print('Verification: ', B)
    t2 = time.time()
    speed4 = str(round((t2 - t1) * 1000, 4)) +  ' ms'
    print('Speed:        ', speed4)
    
    o = input('Want to see speeds only? (y/n) ')
    if o == 'y':
        print(' Bubble:', speed1, '\n',
        'Shaker:', speed2, '\n',
        'Count: ', speed3, '\n',
        'Python:', speed4)
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

main()





























