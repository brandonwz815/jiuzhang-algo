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

        # state and init
        dp = [1] * len(nums)

        prev = [-1] * len(nums)

        # function
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        # answer: return max(dp)
        longest, last = 0, -1
        for i in range(len(nums)):
            if dp[i] > longest:
                longest = dp[i]
                last = i

        path = []
        while last != -1:
            path.append(nums[last])
            last = prev[last]
        print(path[::-1])  # ATTN: reverse

        return longest


solution = Solution()
print(solution.longest_increasing_subsequence([5, 4, 1, 2, 3]))  # 3
print(solution.longest_increasing_subsequence([4, 2, 4, 5, 3, 7]))  # 4
