def checkPrime(num):
    for i in range(2, int(num/2) + 1):
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
print("the", nth, "prime number is", findPrime(nth))
