# 8. String to Integer (atoi)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        l1 = len(str)
        r = 0
        if l1 == 0:
            return r
        i = 0
        while i < l1 and str[i] == ' ':
            i += 1
        f = False
        if i < l1 and str[i] in ('-', '+'):
            if str[i] == '-':
                f = True
            i += 1
        if f:
            max_num = 2 ** 31
        else:
            max_num = 2 ** 31 - 1

        while i < l1 and '0' <= str[i] <= '9':
            r = r*10 + (int(str[i]) - int('0'))
            if r > max_num:
                r = max_num
                break
            i += 1
        if f:
            r = -r
        return r


s = Solution()
print(s.myAtoi("-935927435203458023"))
