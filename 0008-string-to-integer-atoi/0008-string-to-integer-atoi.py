class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        n = len(s)
        i = 0

        # 1. Whitespace: ignore leading spaces
        while i < n and s[i] == " ":
            i += 1

        # 2. Signedness: check '-' or '+', default positive
        sign = 1
        if i < n and (s[i] == "-" or s[i] == "+"):
            if s[i] == "-":
                sign = -1
            i += 1

        # 3. Conversion & 4. Rounding: parse digits manually without int()
        num = 0
        while i < n and "0" <= s[i] <= "9":
            digit = ord(s[i]) - ord("0")
            num = num * 10 + digit

            if sign * num <= MIN_INT:
                return MIN_INT
            if sign * num >= MAX_INT:
                return MAX_INT

            i += 1

        return sign * num