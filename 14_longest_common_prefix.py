class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        min_length = float("inf")
        
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i+=1
        return strs[0][:i]


if __name__ == "__main__":
    s = Solution()
    strs1 = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    print(s.longestCommonPrefix(strs1))
    print(s.longestCommonPrefix(strs2))
