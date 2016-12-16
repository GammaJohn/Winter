import math

def checkPrime(num):
    for i in range(2, int(math.pow(num, 0.5)) + 1):
        if num % i == 0:
            return False
        
    return True

def findPrime(n):
    count = 0
    current = 1
    while count < n:
        current+=1
        if checkPrime(current):
            count+=1

    return current

nth = 10001
print("the %dth number is %d" % (nth, findPrime(nth)))
