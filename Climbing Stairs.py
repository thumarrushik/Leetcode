class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        if n is None:
            return []
        
        Result = [0] * (n +1)
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
            
        first = 2
        second = 1
            
        for a1 in range(2, n,1):
            Result = first + second
            second = first
            first = Result
            
            
            
            
        return Result
        
