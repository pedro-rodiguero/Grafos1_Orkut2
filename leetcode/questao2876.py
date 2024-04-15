class Solution:
    def countVisitedNodes(self, edges):
        n = len(edges)
        memo = [-1] * n
        visited = [False] * n

        def dfs(node, path):
            if visited[node]:
                return 0
            if node in path:
                return len(path) - path.index(node)
            if memo[node] != -1:
                return memo[node]
            path.append(node)
            visited[node] = True
            memo[node] = dfs(edges[node], path) + 1
            path.pop()
            return memo[node]

        return [dfs(i, []) for i in range(n)]


## LeetCode Question 2876 - Count Visited Nodes - https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/
