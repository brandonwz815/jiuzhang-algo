"""
https://www.jiuzhang.com/solutions/wildcard-matching
"""


class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def is_match(self, s, p):
        """2D dp"""
        if not s or not p:
            return False

        n, m = len(s), len(p)

        # state
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # init
        dp[0][0] = True
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == '*'  # first row

        # function
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (
                        s[i - 1] == p[j - 1] or p[j - 1] == '?'
                    )
        return dp[n][m]


solution = Solution()
print(solution.is_match("aa", "a"))  # False
print(solution.is_match("aa", "aa"))  # True
print(solution.is_match("aaa", "aa"))  # False
print(solution.is_match("aa", "*"))  # True
print(solution.is_match("aa", "a*"))  # True
print(solution.is_match("ab", "?*"))  # True
print(solution.is_match("aab", "c*a*b"))  # False
