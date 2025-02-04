from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1
        
        result.reverse()

        return result


if __name__ == "__main__":
    s = Solution()
    nums = [-4,-1,0,3,10]
    print(s.sortedSquares(nums))