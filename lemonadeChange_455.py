#860
def lemonadeChange(bills):
    five_change = 0
    ten_change = 0
    for bill in bills:
        if bill == 5:
            five_change += 1
        elif bill == 10:
            ten_change += 1
            if five_change == 0:
                return False
            five_change -= 1
        else:
            if ten_change > 0 and five_change > 0:
                ten_change -= 1
                five_change -= 1
            elif five_change >= 3:
                five_change -= 1
            else:
                return False
    return True


#main
bills = [5, 10, 5, 20]
print(lemonadeChange(bills))