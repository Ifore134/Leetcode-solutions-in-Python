class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans =0
        low=prices[0]
        ind=0
        for i in range(len(prices)):
            if prices[i] < low:
                low =prices[i]
            if prices[i]-low>ans:
                ans=prices[i]-low
        return ans
