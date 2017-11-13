class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or prices == []:
            return 0
        
        
        minimum = prices[0]
        current = 0
        
        for a1 in range(len(prices)):
            minimum = min(minimum, prices[a1])
            current = max(current, prices[a1] - minimum)
            
        return current
