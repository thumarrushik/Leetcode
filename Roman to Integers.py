
/*

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.



*/



class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman2int = {'I':1, 'V':5,'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        
        summ = roman2int[s[len(s)-1]]
        for a1 in range(len(s)-2,-1,-1):
            
            if roman2int[s[a1]] < roman2int[s[a1+1]]:
                summ -= roman2int[s[a1]]
            else:
                summ += roman2int[s[a1]]
            
        return summ
        
        
