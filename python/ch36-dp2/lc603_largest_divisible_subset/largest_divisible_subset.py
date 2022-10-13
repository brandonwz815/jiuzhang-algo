"""
https://www.jiuzhang.com/solutions/largest-divisible-subset

Time complexity: O(n√n)

"""


class Solution:
    def largest_divisible_subset(self, nums):
        """main logic"""
        if not nums:
            return []

        nums = sorted(nums)

        dp, prev = {}, {}
        for num in nums:
            dp[num] = 1
            prev[num] = -1

        last_num = nums[0]
        for num in nums:
            for factor in self.get_factors(num):
                if factor in dp and dp[num] < dp[factor] + 1:
                    dp[num] = dp[factor] + 1
                    prev[num] = factor
                if dp[num] > dp[last_num]:
                    last_num = num

        return self.get_path(prev, last_num)

    def get_factors(self, num):
        """
        get all factors
        time complexity: O(√n)
        """

        if num == 1:
            return []

        factors = []
        factor = 1
        while factor * factor <= num:
            if num % factor == 0:
                factors.append(factor)  # append the smaller factor
                if factor * factor < num and factor != 1:
                    factors.append(
                        num // factor
                    )  # append the bigger factor.  ATTN use "//" to guarantee getting an integer
            factor += 1
        return factors

    def get_path(self, prev, last_num):
        """get a reversed list"""
        path = []
        while last_num != -1:
            path.append(last_num)
            last_num = prev[last_num]
        return path[::-1]


solution = Solution()
print(solution.largest_divisible_subset([1, 2, 3]))  # [1, 2] or [1, 3]
print(solution.largest_divisible_subset([1, 2, 4, 8]))  # [1, 2, 4, 8]
