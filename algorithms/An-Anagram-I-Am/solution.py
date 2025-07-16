class Solution:
    def solve(self, s0, s1):
        for i in s0:
            if i in s1:
                s0 = s0.replace(i, "", 1)
                s1 = s1.replace(i, "", 1)

        return len(s0) == 0 and len(s1) == 0
