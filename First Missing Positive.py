class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) is 0:
            return 1
        
        for a1 in range(len(nums)):
            while nums[a1] >0 and nums[a1] < len(nums) and nums[nums[a1] - 1] != nums[a1]:
                nums[nums[a1] -1], nums[a1] = nums[a1], nums[nums[a1]-1]
                
        for b1 in range(len(nums)):
            if nums[b1] != b1+1:
                return b1+1
            
        return len(nums)+1
