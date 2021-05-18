class Solution:
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        stack = [0]
        ans = []
        self.dfs(graph, stack, target, ans)
        return ans

    def dfs(self, graph, stack, target, ans):
        if not stack:
            return

        for ver in graph[stack[-1]]:
            if ver == target:
                ans.append(stack + [target])
                continue

            stack.append(ver)
            self.dfs(graph, stack, target, ans)

        stack.pop()
        return

graph = [[1, 2], [3], [3], []]
s = Solution()
print(s.allPathsSourceTarget(graph))