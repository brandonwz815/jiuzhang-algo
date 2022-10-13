package ch36_dp2.lc398_longest_continuous_increasing_subsequence_ii;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * https://www.jiuzhang.com/solutions/longest-continuous-increasing-subsequence-ii
 * 
 */
public class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.longestContinuousIncreasingSubsequence(new int[][] {
                { 1, 2, 3, 4, 5 },
                { 16, 17, 24, 23, 6 },
                { 15, 18, 25, 22, 7 },
                { 14, 19, 20, 21, 8 },
                { 13, 12, 11, 10, 9 }
        })); // 25
        System.out.println(solution.longestContinuousIncreasingSubsequence(new int[][] {
                { 1, 2 },
                { 5, 3 }
        })); // 4
    }

    int[] dx = { 1, 0, -1, 0 };
    int[] dy = { 0, -1, 0, 1 };

    public int longestContinuousIncreasingSubsequence(int[][] nums) {
        if (nums == null || nums[0].length == 0) {
            return 0;
        }
        int n = nums.length, m = nums[0].length;

        List<List<Integer>> points = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                points.add(Arrays.asList(i, j, nums[i][j]));
            }
        }
        points.sort((p1, p2) -> Integer.compare(p1.get(2), p2.get(2)));

        // state + init
        int[][] dp = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                dp[i][j] = 1;
            }
        }

        // function
        for (int i = 0; i < points.size(); i++) {
            List<Integer> list = points.get(i);
            int x = list.get(0);
            int y = list.get(1);

            for (int j = 0; j < 4; j++) {
                int prevX = x - dx[j];
                int prevY = y - dy[j];
                if (prevX >= 0
                        && prevX < n
                        && prevY >= 0
                        && prevY < m
                        && list.get(2) > nums[prevX][prevY]
                        && dp[x][y] < dp[prevX][prevY] + 1) {
                    dp[x][y] = dp[prevX][prevY] + 1;
                }
            }
        }

        // answer
        int longest = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (dp[i][j] > longest) {
                    longest = dp[i][j];
                }
            }
        }
        return longest;
    }

}
