

def dfs(seen, graph, node):
    if node in seen:
        return

    seen.add(node)

    for val in graph[node]:
        dfs(seen, graph, val)

    return seen


graph = [[1, 2], [3], [3], []]
print(dfs(set(), graph, 0))
