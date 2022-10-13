"""
https://www.jiuzhang.com/solutions/longest-continuous-increasing-subsequence-ii
"""


class Solution:
    """
    @param A: An integer matrix
    @return: an integer
    """

    def longest_continuous_increasing_subsequence2(self, A):
        if not A or not A[0]:
            return 0

        n, m = len(A), len(A[0])

        points = []
        for i in range(n):
            for j in range(m):
                points.append((A[i][j], i, j))
        points.sort()

        longest_hash = {}
        for i, point in enumerate(points):
            key = (point[1], point[2])
            longest_hash[key] = 1
            for dx, dy in ((1, 0), (0, -1), (-1, 0), (0, 1)):
                x, y = point[1] - dx, point[2] - dy # prior coordinates
                if (
                    0 <= x < n
                    and 0 <= y < m
                    and (x, y) in longest_hash
                    and A[x][y] < point[0]
                ):
                    longest_hash[key] = max(longest_hash[key], longest_hash[(x, y)] + 1)

        return max(longest_hash.values())


solution = Solution()
print(
    solution.longest_continuous_increasing_subsequence2(
        [
            [1, 2, 3, 4, 5],
            [16, 17, 24, 23, 6],
            [15, 18, 25, 22, 7],
            [14, 19, 20, 21, 8],
            [13, 12, 11, 10, 9],
        ]
    )
)  # 25
print(solution.longest_continuous_increasing_subsequence2([[1, 2], [5, 3]]))  # 4
