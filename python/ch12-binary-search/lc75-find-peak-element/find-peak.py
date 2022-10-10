"""
https://www.jiuzhang.com/solutions/find-peak-element
"""


class Solution:
    """
    @param A: An integers list.
    @return: return any of peek positions.
    """

    def find_peak(self, nums):
        """binary search"""
        start, end = 1, len(nums) - 2
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid - 1]:
                end = mid
            elif nums[mid] < nums[mid + 1]:
                start = mid
            else:
                return mid

        if nums[start] < nums[end]:
            return end
        return start


solution = Solution()
print(solution.find_peak([1, 2, 1, 3, 4, 5, 7, 6])) #6, that is element value 7
