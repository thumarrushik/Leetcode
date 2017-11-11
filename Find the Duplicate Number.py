class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None
        
        n_length = len(nums)
        
        a1 = nums[0]
        a2 = nums[nums[0]]
        
        while a1 != a2:
            a1 = nums[a1]
            a2 = nums[nums[a2]]
            
            
        a2 = 0
        while a1 != a2:
            a1 = nums[a1]
            a2 = nums[a2]
            
        return a1
