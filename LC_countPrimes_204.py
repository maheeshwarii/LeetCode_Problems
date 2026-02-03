def countPrimes(n):
    if n <= 2:
        return False
    prime = [True] * n
    prime[0] = prime[1] = False
    c = 0
    for i in range(2, n):
        if prime[i]:
            c += 1
            for j in range(i * 2, n, i):
                prime[j] = False
    return c

#main
n = 10
print(countPrimes(n))