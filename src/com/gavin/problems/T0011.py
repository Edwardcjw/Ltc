# 11. Container With Most Water
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ma = 0
        left = 0
        right = len(height) - 1
        while left < right:
            ma = max(ma, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ma


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
