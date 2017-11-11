class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s is None or len(s) is 0:
            return s
        
        n = len(s)
        s = list(s)
        v = "aeiouAEIOU"
        v = list(v)
        
        low = 0
        high = n -1
        
        while low < high:
            
            while low < high and s[low] not in v:
                low += 1
                
            while low < high and s[high] not in v:
                high -= 1
                
            s[low], s[high] = s[high], s[low]
            
            low += 1
            high -= 1
            
        return "".join(s)
