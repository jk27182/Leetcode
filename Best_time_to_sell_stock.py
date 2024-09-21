# funktioniert, ist aber zu langsam
# def sell_buy_stocks(prices):
#     slow = 0
#     len_prices = len(prices)
#     max_profit = 0
#     while slow < len_prices:
#         buy = prices[slow]
#         for fast, price in enumerate(prices[slow+1:]):
#             profit = price - buy
#             if profit > max_profit:
#                 max_profit = profit
#         slow += 1

#     return max_profit
def sell_buy_stocks(prices):
    max_profit = 0
    for i, price in enumerate(prices):
        profit = max(prices[i:]) - price
        max_profit = max(profit, max_profit) 
    return max_profit








prices = [7,1,5,3,6,4]
print(sell_buy_stocks(prices))
# profit: 5