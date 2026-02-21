def countPrimeSetBits(left, right):
    def countSetBits(n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    primes = {2, 3, 5, 7, 11, 13, 17, 19}
    total = 0
    for i in range(left, right + 1):
        if countSetBits(i) in primes:
            total += 1
    return total

#main
left = 6
right = 10
print(countPrimeSetBits(left, right))