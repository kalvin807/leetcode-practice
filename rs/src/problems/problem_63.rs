use super::base::Solution;

impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let n = obstacle_grid.len();
        let m = obstacle_grid[0].len();
        let mut memo = vec![vec![0; m]; n];

        memo[0][0] = if obstacle_grid[0][0] == 1 { 0 } else { 1 };

        for i in 1..n {
            memo[i][0] = if obstacle_grid[i][0] == 1 {
                0
            } else {
                memo[i - 1][0]
            };
        }

        for j in 1..m {
            memo[0][j] = if obstacle_grid[0][j] == 1 {
                0
            } else {
                memo[0][j - 1]
            };
        }

        for i in 1..n {
            for j in 1..m {
                if obstacle_grid[i][j] != 1 {
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1];
                }
            }
        }

        memo[n - 1][m - 1]
    }
}
