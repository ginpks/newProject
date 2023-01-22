def findMagic(n):
    numberSum = sum(n)
    if numberSum < 10:
        return numberSum
    else:
        n1 = numberSum % 10
        n2 = numberSum // 10
        return n1 + n2

        
def sum(n):
    sum = 0
    while n != 0:
        sum += n%10
        n = n//10
    return sum
    
n = 1995
print(findMagic(n))
