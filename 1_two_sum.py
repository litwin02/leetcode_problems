from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]

            if y in h and h[y] != i:
                return [i, h[y]]

if __name__ == "__main__":
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    print(s.twoSum(nums, target))