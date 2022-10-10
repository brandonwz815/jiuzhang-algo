"""
https://www.jiuzhang.com/solutions/wood-cut
"""


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def wood_cut(self, L, k):
        """
        binary search
        """
        if not L:
            return 0

        start, end = 1, min(max(L), sum(L) // 2)
        if start > end:
            return 0

        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_pieces(L, mid) >= k:
                start = mid
            else:
                end = mid

        if self.get_pieces(L, end) >= k:
            return end
        if self.get_pieces(L, start) >= k:
            return start
        return 0

    def get_pieces(self, L, length):
        return sum(l // length for l in L)


solution = Solution()
print(solution.wood_cut([232, 124, 456], 7))  # 114
