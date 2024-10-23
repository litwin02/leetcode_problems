class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        res = 0
        pointer = len(s)-1
        while pointer >= 0:
            if(roman_dict.get(s[pointer-1]) < roman_dict.get(s[pointer]) and pointer-1>=0):
                res += roman_dict.get(s[pointer])-roman_dict.get(s[pointer-1])
                pointer -= 2
                continue
            
            res += roman_dict.get(s[pointer])
            pointer -= 1

        return res
    
s = "MCMXCIV"
sol = Solution
print(sol.romanToInt(sol, s))