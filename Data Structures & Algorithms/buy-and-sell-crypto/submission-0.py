class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #left side  we  look for a number less than m
        #if not than we return 0
        #on the right  side we look for a number greater m
        #subtract right val from left val = profit

        l = 0
        r =  1
        profit = 0
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit  = prices[r] -  prices[l]
                maxP = max(maxP,profit)
            else:
                l=r
            r+=1
        return maxP


            

        