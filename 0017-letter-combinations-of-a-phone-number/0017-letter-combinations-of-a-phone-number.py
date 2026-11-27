class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        path = []

        def backtrack(idx):
            if idx == len(digits):
                res.append("".join(path))
                return

            for ch in keypad[digits[idx]]:
                path.append(ch)
                backtrack(idx + 1)
                path.pop()

        backtrack(0)
        return res