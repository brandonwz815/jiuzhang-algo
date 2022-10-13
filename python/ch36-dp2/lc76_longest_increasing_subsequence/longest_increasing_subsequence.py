"""
https://www.jiuzhang.com/solutions/longest-increasing-subsequence

Time complexity: O(n^2)

"""


class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longest_increasing_subsequence(self, nums):
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


solution = Solution()
print(solution.longest_increasing_subsequence([5, 4, 1, 2, 3]))  # 3
print(solution.longest_increasing_subsequence([4, 2, 4, 5, 3, 7]))  # 4
