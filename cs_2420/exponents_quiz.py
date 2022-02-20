import random, time

def quiz():

    exponents = {0: '1',   1: '2',   2: '4',   3: '8',   4: '16',   5: '32',   6: '64',   7: '128',   8: '256',   9: '512',
    			10: '1k', 11: '2k', 12: '4k', 13: '8k', 14: '16k', 15: '32k', 16: '64k', 17: '128k', 18: '256k', 19: '512k',
    			20: '1m', 21: '2m', 22: '4m', 23: '8m', 24: '16m', 25: '32m', 26: '64m', 27: '128m', 28: '256m', 29: '512m',
    			30: '1b', 31: '2b', 32: '4b', 33: '8b', 34: '16b', 35: '32b', 36: '64b', 37: '128b', 38: '256b', 39: '512b',
    			40: '1t', 41: '2t', 42: '4t', 43: '8t', 44: '16t', 45: '32t', 46: '64t', 47: '128t', 48: '256t', 49: '512t'}
    			
    		
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    	   10,11,12,13,14,15,16,17,18,19,
    	   20,21,22,23,24,25,26,27,28,29,
    	   30,31,32,33,34,35,36,37,38,39,
    	   40,41,42,43,44,45,46,47,48,49]
    
    t1 = time.time()
    
    for num in range(len(exponents)):
        num = random.choice(nums)
        correct = False
        while not correct:
            answer = input('2^' + str(num) + '? ')
            if exponents[num] == answer:
                nums.remove(num)
                correct = True
    
    t2 = time.time()
    t = round(t2-t1, 3)
    print("Your time is", t, "seconds.")

def short_quiz():

    exponents = {0: '1',   1: '2',   2: '4',   3: '8',   4: '16',   5: '32',   6: '64',   7: '128',   8: '256',   9: '512'}
    
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    t1 = time.time()
    
    for num in range(len(exponents)):
        num = random.choice(nums)
        correct = False
        while not correct:
            answer = input('2^' + str(num) + '? ')
            if exponents[num] == answer:
                nums.remove(num)
                correct = True
    
    t2 = time.time()
    t = round(t2-t1, 3)
    print("Your time is", t, "seconds.")
    
# quiz()
short_quiz()