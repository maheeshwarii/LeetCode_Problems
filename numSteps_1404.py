def  numSteps(s):
    steps = 0
    while s != '1':
        if s[-1] == '0':
            s = s[:-1]
        else:
            i = len(s) - 1
            while i >= 0 and s[i] == '1':
                i -= 1
            if i < 0:
                s = '1' + '0' * len(s)
            else:
                s = s[:i] + '1' + '0' * (len(s) - i - 1)
        steps += 1
    return steps

#main
s = "100"
print(numSteps(s))   