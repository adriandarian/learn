import itertools


class Solution:
    def solve(self, s):
        if not s:
            return 0
        return max(len(list(v)) for _, v in itertools.groupby(s))
