from typing import List
class Arrays:
    def __init__(self):
        self.buy_sell_stock=self.buy_and_selloptim(prices=[1,2,4])


    # Write a function that takes an array denoting daily stock price and returns the maximum profit that could be
    # made by buying and then selling one share of that stock
    # variant 1 explore difference for each pair, two nested loops

    def buy_and_sell(self, prices: List[float])->float: #time limit exceed on leetcode
        if len (prices)==2:
            max_profit=max(prices[1]-prices[0],0)
            return max_profit
        max_profit=0
        for i in range (len(prices)-1):
            for k in range (i+1,len(prices)):
                current_difference=prices[k]-prices[i]
                if current_difference>max_profit:
                    max_profit=current_difference
        return max_profit


    #There is a linear time constant space solution to this problem.
    #Start by initializing buy price as prices[0] and profit as 0.
    #Now iterate through the prices array. Update profit for every value. If we find that the current value is lesser than the buy value, update the buy value.
    #There are 2 interesting test cases: upward sloping line indicating profit = price[N-1]-price[0]. downward sloping line profit = 0

    def buy_and_selloptim(self, prices: List[float])->float:
        if len(prices):#without this condition leetcode returns error
            buy = prices[0]
            profit = 0
            for p in range(1, len(prices)):
                profit = max(profit, prices[p] - buy)
                buy = min(buy, prices[p])
            return profit
        else:
            return 0






array=Arrays()
print('the end')



