def sortVowels(s):
    vowel = [v for v in s if v.lower() in "aeiou"]
    vowel.sort()
    cons = list(s)
    j = 0
    for i, c in enumerate(cons):
        if c.lower() in "aeiou":
            cons[i] = vowel[j]
            j += 1
    return "".join(cons)

#main
s = "lEetcOde"
print(sortVowels(s))