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

        start, end = 1, max(L)  # the answer is between 1 and max(L) inclusive
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
        pieces = 0
        for i in L:
            pieces += i // length
        return pieces


solution = Solution()
print(solution.wood_cut([232, 124, 456], 7))  # 114


# On line 22, use // instead of /
