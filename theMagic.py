def findMagic(n):
    numberSum = sum(n)
    n1 = numberSum % 10
    n2 = numberSum // 10
    sumNumber = n1 + n2
    if sumNumber >= 10:
        return findMagic(sumNumber)
    else:
        return sumNumber

        
def sum(n):
    sum = 0
    while n != 0:
        sum += n%10
        n = n//10
    return sum
    
n = 1995
print(findMagic(742839204983789) )
