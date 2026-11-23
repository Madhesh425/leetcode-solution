class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(needle), len(haystack)
        if m > n:
            return -1

        # Build LPS (Longest Proper Prefix which is also Suffix) array for needle
        lps = [0] * m
        prefix_len = 0
        i = 1
        while i < m:
            if needle[i] == needle[prefix_len]:
                prefix_len += 1
                lps[i] = prefix_len
                i += 1
            elif prefix_len > 0:
                prefix_len = lps[prefix_len - 1]
            else:
                lps[i] = 0
                i += 1

        # Scan haystack using needle and lps
        i = 0  # index in haystack
        j = 0  # index in needle
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            elif j > 0:
                j = lps[j - 1]
            else:
                i += 1

        return -1
        