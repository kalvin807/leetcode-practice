use super::base::Solution;

impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let (m, n) = (m as usize, n as usize);
        let mut memo = vec![vec![1; m]; n];

        for i in 1..n {
            for j in 1..m {
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1];
            }
        }
        memo[n - 1][m - 1]
    }
}
