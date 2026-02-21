def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for i in prices:
        if i < min_price:
            min_price = i
        elif i - min_price > max_profit:
            max_profit = i - min_price
    return max_profit

#main
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))