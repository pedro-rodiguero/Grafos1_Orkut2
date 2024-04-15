class Solution:
    def countVisitedNodes(self, edges):
        n = len(edges)
        visited = [False] * n
        count = [0] * n

        for i in range(n):
            current = i
            while not visited[current]:
                visited[current] = True
                count[i] += 1
                current = edges[current]
            visited = [False] * n

        return count


## LeetCode Question 2876 - Count Visited Nodes - https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/
