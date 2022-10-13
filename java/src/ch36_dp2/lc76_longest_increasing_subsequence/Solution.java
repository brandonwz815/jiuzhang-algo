package ch36_dp2.lc76_longest_increasing_subsequence;

import java.util.Arrays;

/**
 * https://www.jiuzhang.com/solutions/longest-continuous-increasing-subsequence-ii
 * 
 * Time complexity: O(n^2)
 * Space complexity: O(n)
 * 
 */
public class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.longestIncreasingSubsequence(new int[] { 5, 4, 1, 2, 3 }));
        System.out.println(solution.longestIncreasingSubsequence(new int[] { 4, 2, 4, 5, 3, 7 }));
    }

    public int longestIncreasingSubsequence(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        // state
        int[] dp = new int[nums.length];

        // init
        Arrays.fill(dp, 1);

        // function
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        // answer
        int max = 1;
        for (int i = 0; i < nums.length; i++) {
            max = Math.max(max, dp[i]);
        }
        return max;
    }

}
