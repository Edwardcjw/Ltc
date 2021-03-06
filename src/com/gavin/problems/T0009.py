# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x = x // 10
        return x == y or x == y // 10


s = Solution()
print(s.isPalindrome(1231321))
