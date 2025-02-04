class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for c in magazine:
            mag_dict[c] = mag_dict.get(c, 0) + 1
        
        for c in ransomNote:
            if c not in mag_dict or mag_dict[c] == 0:
                return False
            mag_dict[c] -= 1
            
        return True


if __name__ == "__main__":
    s = Solution()
    ransomNote = "aa"
    magazine = "ab"
    print(s.canConstruct(ransomNote, magazine))
    