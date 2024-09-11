# The function max_profit calculates the maximum profit possible if we buy a share on any day after i, and sell it later
def max_profit(i, price):
    min = float('inf')
    profit = 0
    # For all days after the ith day
    for j in range(i + 1, len(price)):
        if min > price[j]:
            min = price[j]
        else:
            if profit < price[j] - min:
                profit = price[j] - min
    return profit


max = 0
price = [3,3,5,0,0,3,1,4]
for i in range(len(price)):
    for j in range(i+1, len(price)):
        # Calculating the - current profit = profit for buying on day i and selling on day j
        if price[j] - price[i] > 0:
            # max_profit gives the maximum possible profit if we conduct 1 transaction after day j
            # Current profit + max_profit = maximum profit if we conduct 2 transactions, under the condition we buy on day i
            max_p = price[j] - price[i] + max_profit(j, price)
            # Here we are comparing maximum profit on each day and storing the maximum
            if max_p > max:
                max = max_p

print("Maximum possible profit is:", max)
