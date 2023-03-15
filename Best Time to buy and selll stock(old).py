class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #plan 1: iterate through the list and for each item iterate again
        # plan 2 call max for every element in the list
        priced = deepcopy(prices)
        max_num =0
        left = prices[0]
        
        for i in range(len(prices)):  
            right = prices[i]
            if(right<left):
                left = right
                continue
            if(right-left>max_num):
                max_num = right-left
            

        return max_num
