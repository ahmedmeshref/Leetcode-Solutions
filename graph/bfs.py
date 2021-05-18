from collections import deque


def bfs(graph, node):
    seen = set()
    queue = deque()
    queue.append(node)

    while queue:
        c_node = queue.popleft()
        seen.add(c_node)
        for val in graph[c_node]:
            queue.append(val)
    return seen


graph = [[1, 2], [3], [3], []]
print(bfs(graph, 0))
