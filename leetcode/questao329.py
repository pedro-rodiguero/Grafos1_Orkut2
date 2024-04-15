class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        cache = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if not cache[i][j]:
                val = matrix[i][j]
                cache[i][j] = 1 + max(
                    dfs(i + di, j + dj)
                    for di, dj in directions
                    if 0 <= i + di < m
                    and 0 <= j + dj < n
                    and matrix[i + di][j + dj] > val
                )
            return cache[i][j]

        return max(dfs(i, j) for i in range(m) for j in range(n))


## LeetCode Question 329 - Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
