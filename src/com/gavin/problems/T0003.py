# 3. Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        sub_str = ''
        for i in s:
            if i in sub_str:
                sub_str = sub_str[sub_str.index(i)+1:]+i
            else:
                sub_str += i
                if len(sub_str) > longest:
                    longest = len(sub_str)
        return longest


s = Solution()
r = s.lengthOfLongestSubstring("pwwkew")
print(r)
