# 5. Longest Palindromic Substring
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = ["^"]
        for i in s:
            a.append("$")
            a.append(i)
        a.append("$")
        a.append("#")
        p = [1] * (len(a) - 1)
        rmax = 1
        k = 1
        i = 1
        center = 0
        pmax = 0
        while i < len(a) - 1:
            if rmax > i:
                p[i] = min(p[2 * k - i], rmax - i)
            while a[i - p[i]] == a[i + p[i]]:
                p[i] = p[i] + 1
            if p[i] + i > rmax:
                rmax = p[i] + i
                k = i
                if p[i] > pmax:
                    pmax = p[i]
                    center = i
            i = i + 1
        len1 = pmax - 1
        left = (center - pmax + 1) / 2
        return s[left:left + len1]


s = Solution()
print(s.longestPalindrome("abcbac"))
