class Solution:
    def solve(self, s0, s1):
        s = ''

        if (len(s0) == 0):
            return s1
        elif (len(s1) == 0):
            return s0
        else:
            smaller_s, larger_s = "", ""
            if len(s0) < len(s1):
                smaller_s = s0
                larger_s = s1
            else:
                smaller_s = s1
                larger_s = s0

            for i in range(len(smaller_s)):
                s += s0[i] + s1[i]
            s += larger_s[len(smaller_s):]

        return s
