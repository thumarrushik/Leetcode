class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        Result = []
        
        for a1 in range(left, right+1):
            b1 = a1
            while b1 > 0:
                if b1%10 == 0 or (a1 % (b1 % 10) != 0):
                    break
                b1 /= 10
                
            if b1 == 0:
                Result.append(a1)
                
        return Result
