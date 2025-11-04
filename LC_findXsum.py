def findXsum(self, nums: List[int], k: int, x: int):
    ans = []
    for i in range(len(nums)-k+1):
        window = nums[i:i+k]
        freq = {}
        for j in window:
            freq[j] = freq.get(j, 0) + 1
        top = sorted(freq.items(), key = lambda t:(t[1], t[0]), reverse = True)[:x]
        s = sum(a * b for a, b in top)
        ans.append(s)
    return ans