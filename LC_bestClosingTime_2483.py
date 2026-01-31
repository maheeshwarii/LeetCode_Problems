def bestClosingTime(customers):
        maxx = 0
        a = 0
        b = 0
        for i in range(len(customers)):
            if customers[i] == "Y":
                a += 1
            else:
                a -= 1
            if a > maxx:
                maxx = a
                b = i+1
        return b

#main
customers = "YYNY"
print(bestClosingTime(customers))