# 7. Reverse Integer
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        sign = False
        if x < 0:
            if x < -2 ** 31:
                return 0
            a = -x
            sign = True
        else:
            if x > 2 ** 31 - 1:
                return 0
            a = x

        b = True
        while b:
            result += a % 10
            a = a // 10
            if a == 0:
                b = False
            else:
                result *= 10
                if result > 2 ** 31 - 1 or (sign and result < -2 ** 31):
                    b = False
                    result = 0
        if sign:
            result = -result
        return result


s = Solution()
print(s.reverse(123))
