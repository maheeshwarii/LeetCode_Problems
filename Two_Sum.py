nums = list(map(int,input("Enter a list:").split()))
target = int(input("Enter a number:"))
seen = {}
for i, val in enumerate(nums):
    x = target - val
    if x in seen:
        print([seen[x],i])
    seen[val] = i
