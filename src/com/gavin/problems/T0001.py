# 1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return [d[diff], i]
            d[nums[i]] = i


s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))
