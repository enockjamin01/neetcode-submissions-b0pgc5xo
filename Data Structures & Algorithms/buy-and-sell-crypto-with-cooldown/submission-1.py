class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # held=[0]*len(prices)
        # sold=[0]*len(prices)
        # rest=[0]*len(prices)
        # held[0]=-prices[0]
        held=-prices[0]
        sold=0
        rest=0
        for i in range(1,len(prices)):
            new_held=max(held,rest-prices[i])
            new_sold=held+prices[i]
            new_rest=max(sold,rest)
            held=new_held
            sold=new_sold
            rest=new_rest
        return max(sold,rest)