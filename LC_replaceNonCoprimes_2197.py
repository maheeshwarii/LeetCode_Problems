from math import gcd
def replaceNonCoprimes(nums):
    st = []
    for i in nums:
        st.append(i)
        while len(st) > 1:
            i, j = st[-2:]
            g = gcd(i, j)
            if g == 1:
                break
            st.pop()
            st[-1] = i * j // g
    return st

#main
nums = [6, 4, 3, 2, 7, 6, 2]
print(replaceNonCoprimes(nums))