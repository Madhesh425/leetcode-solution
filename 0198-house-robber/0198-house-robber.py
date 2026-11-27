class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev2 = 0  # Best total up to i - 2
        prev1 = 0  # Best total up to i - 1

        for val in nums:
            curr = max(prev1, prev2 + val)
            prev2 = prev1
            prev1 = curr

        return prev1