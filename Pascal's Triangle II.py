class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        Result = [0] * (rowIndex + 1)
        
        Result[0] = 1
        for a1 in range(1, rowIndex + 1,1):
            for b1 in range(a1, 0, -1):
                Result[b1] += Result[b1-1]
                
        return Result
            
