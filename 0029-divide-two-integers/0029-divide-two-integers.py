class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)
        a = -abs(dividend)
        b = -abs(divisor)

        quotient = 0
        while a <= b:
            temp = b
            multiple = 1
            while temp + temp >= a:
                temp += temp
                multiple <<= 1
            a -= temp
            quotient += multiple

        res = -quotient if negative else quotient
        return max(INT_MIN, min(INT_MAX, res))