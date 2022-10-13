"""
https://jiuzhang.com/solutions/knight-shortest-path-ii
"""


class Solution:
    """a simple DP with rolling array (left to right)"""

    # DIRECTIONS = ((-2, 1), (-1, 2), (1, 2), (2, 1)) # knight's moves to the right
    DIRECTIONS = ((-2, -1), (-1, -2), (1, -2), (2, -1))  # knight's moves to the current

    def shortest_path2(self, grid):
        """main logic starts"""
        if not grid or not grid[0]:
            return -1

        n, m = len(grid), len(grid[0])

        # state
        dp = [[float("inf")] * 3 for _ in range(n)]

        # init
        dp[0][0] = 0

        # function
        for j in range(1, m):
            for i in range(n):
                dp[i][j % 3] = float("inf")  # ATTN this is needed for the rolling array
                if grid[i][j]:  # grid[i][j]==1, aka. is a barrier
                    continue
                for delta_x, delta_y in Solution.DIRECTIONS:
                    x, y = i + delta_x, j + delta_y
                    if 0 <= x < n and 0 <= y < m:
                        dp[i][j % 3] = min(dp[i][j % 3], dp[x][y % 3] + 1)

        # answer
        if dp[n - 1][(m - 1) % 3] == float("inf"):
            return -1
        return dp[n - 1][(m - 1) % 3]


solution = Solution()
print(solution.shortest_path2([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))  # 3
print(solution.shortest_path2([[0, 1, 0], [0, 0, 1], [0, 0, 0]]))  # -1
