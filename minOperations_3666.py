from collections import deque
from bisect import bisect_left

def minOperations(s: str, k: int) -> int:
    n = len(s)

    # ts[0] -> even parity, ts[1] -> odd parity
    ts = [[], []]
    for i in range(n + 1):
        ts[i % 2].append(i)

    cnt0 = s.count('0')
    ts[cnt0 % 2].remove(cnt0)

    q = deque([cnt0])
    ans = 0

    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == 0:
                return ans

            l = cur + k - 2 * min(cur, k)
            r = cur + k - 2 * max(k - n + cur, 0)

            t = ts[l % 2]
            j = bisect_left(t, l)

            while j < len(t) and t[j] <= r:
                q.append(t[j])
                t.pop(j)

        ans += 1

    return -1

#main
s = "110"
k = 1
print(minOperations(s, k))