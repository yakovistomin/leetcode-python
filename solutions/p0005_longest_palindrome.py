class ExpandFromCenterSolution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = (0, 1)

        def expand(lo: int, hi: int) -> tuple[int, int]:
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                lo -= 1
                hi += 1

            return lo + 1, hi

        for i in range(n - 1):
            if 2 * (n - i) - 1 <= result[1] - result[0]:
                break
            for j in [i, i + 1]:
                lo, hi = expand(i, j)
                if hi - lo > result[1] - result[0]:
                    result = (lo, hi)

        return s[result[0] : result[1]]


class DynamicProgrammingSolution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp: list[list[int]] = [[False] * n for _ in range(n)]
        result = (0, 0)

        for i in range(n):
            dp[i][i] = True

        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = s[i] == s[j] and (diff == 1 or dp[i + 1][j - 1])
                if dp[i][j] and j - i > result[1] - result[0]:
                    result = (i, j)

        return s[result[0] : result[1] + 1]


Solution = ExpandFromCenterSolution
