from math import sqrt
def isprime(num):
    for a in range(2,int(sqrt(num))+1):
        if num%a==0:
            return False
    return num>1

for i in range(1,10,1):
    print(isprime(i))