class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewels_set:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    jew = "aA"
    st = "aAAbbbb"
    print(s.numJewelsInStones(jew, st))