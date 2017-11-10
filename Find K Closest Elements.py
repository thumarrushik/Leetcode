class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        if arr is None:
            return []
        
        low = 0
        high = len(arr)-k
        
        while low <high:
            mid = (low+high)//2
            
            if x - arr[mid] > arr[mid+k] - x:
                low = mid+1
            else:
                high = mid
                
        return arr[low:low+k]
        
