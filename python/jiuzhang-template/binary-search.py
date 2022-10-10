"""
https://www.jiuzhang.com/solutions/binary-search
"""


class Solution:
    """
    binary search template
    """
    def binary_search(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


solution = Solution()
print(solution.binary_search([1, 2, 3, 4, 5, 10], 3))


# Use "start, end = 0, len(nums) - 1" rather "start, end = 0, len(nums)"
