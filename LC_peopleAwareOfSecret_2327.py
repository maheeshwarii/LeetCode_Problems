def peopleAwareOfSecret(n, delay, forget):
        m = (n << 1) + 10
        d = [0] * m
        c = [0] * m
        c[1] = 1
        for i in range(1, n + 1):
            if c[i]:
                d[i] += c[i]
                d[i + forget] -= c[i]
                nex = i + delay
                while nex < i + forget:
                    c[nex] += c[i]
                    nex += 1
        mod = 10**9 + 7
        return sum(d[:n + 1]) % mod

#main
n = 6
delay = 2
forget = 4
print(peopleAwareOfSecret(n, delay, forget))