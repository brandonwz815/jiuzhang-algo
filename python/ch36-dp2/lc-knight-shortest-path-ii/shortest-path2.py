"""
https://jiuzhang.com/solutions/knight-shortest-path-ii
"""


class Solution:
    """a simple DP"""

    # DIRECTIONS = ((-2, 1), (-1, 2), (1, 2), (2, 1)) # knight's moves to the right
    DIRECTIONS = ((-2, -1), (-1, -2), (1, -2), (2, -1))  # knight's moves to the right

    def shortest_path2(self, grid):
        if not grid or not grid[0]:
            return -1

        n, m = len(grid), len(grid[0])

        # state
        dp = [[float("inf")] * m for _ in range(n)]

        # init
        dp[0][0] = 0

        # function
        for j in range(m):
            for i in range(n):
                if grid[i][j]:  # grid[i][j]==1, aka. is a barrier
                    continue
                for delta_x, delta_y in Solution.DIRECTIONS:
                    x, y = i + delta_x, j + delta_y
                    if 0 <= x < n and 0 <= y < m:
                        dp[i][j] = min(dp[i][j], dp[x][y] + 1)

        # answer
        if dp[n - 1][m - 1] == float("inf"):
            return -1
        return dp[n - 1][m - 1]


solution = Solution()
print(solution.shortest_path2([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))  # 3
print(solution.shortest_path2([[0, 1, 0], [0, 0, 1], [0, 0, 0]]))  # -1
