def makeLargestSpecial(s):
    parts = []
    balance = start = 0
    for i in range(len(s)):
        balance += 1 if s[i] == '1' else -1
        if balance == 0:
            inner = makeLargestSpecial(s[start + 1 :i])
            parts. append("1" + inner + "0")
            start = i + 1
    parts.sort(reverse = True)
    return "".join(parts)
    
#main
s = "11011000"
print(makeLargestSpecial(s))