class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        if s is None and len(s) is 0:
            return s
        
        length = len(s)
        s = list(s)
        
        for a1 in range(0,length-1, 2*k):
            temp = s[a1:a1+k]
            s[a1:a1+k] = temp[::-1]
            
        return "".join(s)
