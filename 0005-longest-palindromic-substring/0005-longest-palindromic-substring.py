class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        start = 0
        max_len = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1

        for i in range(len(s)):
            # Odd-length palindrome centered at i
            l1, len1 = expand(i, i)
            if len1 > max_len:
                start, max_len = l1, len1

            # Even-length palindrome centered between i and i + 1
            l2, len2 = expand(i, i + 1)
            if len2 > max_len:
                start, max_len = l2, len2

        return s[start : start + max_len]