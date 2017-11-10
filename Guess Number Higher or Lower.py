class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        
        while low < high:
            
            mid = (low+high)/2
            
            if guess(mid) == 1:
                low = mid+1
            else:
                high = mid
                
        return low
            
