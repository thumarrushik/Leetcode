class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) is 0:
            return []
        Result = []
        
        
        
        for a1 in range(len(nums)):
            nums[abs(nums[a1]) -1] = - abs(nums[abs(nums[a1]) -1])
            
        for b1 in range(len(nums)):
            if nums[b1] > 0:
                Result.append(b1+1)
                
                
        return Result
