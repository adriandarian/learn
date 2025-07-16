class Solution:
    def solve(self, s):
        for i in range(len(s)):
            if s[i] in s[:i]:
                return i

        return -1
