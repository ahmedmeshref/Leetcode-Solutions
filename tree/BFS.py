from collections import deque

def BFS(root):
    if not root:
        return []

    bfs_out = []
    queue = deque()
    queue.append(root)

    while queue:
        curr_node = queue.popleft()
        bfs_out.append(curr_node.val)

        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)

    return bfs_out