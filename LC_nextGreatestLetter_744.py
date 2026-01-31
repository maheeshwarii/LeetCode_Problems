def nextGreatestLetter(letters: List[str], target):
        l, r = 0, len(letters)
        while l < r:
            mid = (l + r) >> 1
            if ord(letters[mid]) > ord(target):
                r = mid
            else:
                l = mid + 1
        return letters[l % len(letters)]

#main
letters = ["c","f","j"]
target = "a"
print(nextGreatestLetter(letters, target))

letters = ["c","f","j"]
target = "c"
print(nextGreatestLetter(letters, target))
