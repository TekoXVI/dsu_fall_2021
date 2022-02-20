def shaker(list):

    sorted = False
    while not sorted:
        sorted = True

        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

        for i in range(len(list)-1, 0, -1):
            if list[i] < list[i-1]:
                list[i], list[i-1] = list[i-1], list[i]
                sorted = False

    print(list)

shaker([1,3,4,5,6,7,8,9,2])
shaker([4,5,8,3,1,5,7,6,8])
shaker([7,5,9,8,10,11,15,11,12])
