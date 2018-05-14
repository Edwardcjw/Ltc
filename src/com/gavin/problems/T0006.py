# 6. ZigZag Conversion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        len1 = len(s)
        if numRows == 1 or numRows >= len1:
            return s
        s1 = ""
        for i in range(numRows):
            j = i
            while j < len1:
                s1 = s1 + s[j]
                j = j + 2 * (numRows - 1)
                if i != 0 and i != numRows-1:
                    t = j - 2*i
                    if t < len1:
                        s1 = s1 + s[t]
        return s1


s = Solution()
print(s.convert("abcd", 3))
