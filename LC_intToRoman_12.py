def intToRoman(num):
    values = [ (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    res = ""
    for val, rom in values:
        while num >= val:
            res += rom
            num -= val
    return res

#main
num = 1994
print(intToRoman(num))