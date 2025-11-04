# Example graph (update this if needed)
from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


graph1 = {
    5: [2, 6],
    2: [7, 8],
    6: [9],
    7: [],
    8: [],
    9: []
}

path1 = bfs(graph1, 5, 8)
print("BFS Path from 5 to 8:", path1)
