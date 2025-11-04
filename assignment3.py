# Example graph for Exercise 2 (update according to the image if needed)
def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    if start == goal:
        return visited

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dfs(graph, neighbor, goal, visited.copy())
            if path:
                return path
    return None

# Example graph for Exercise 2 (update according to the image if needed)
graph2 = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [7],
    5: [],
    6: [8, 9],
    7: [10, 11],
    8: [15],
    9: [],
    10: [],
    11: [],
    15: []
}

path2 = dfs(graph2, 1, 15)
print("DFS Path from 1 to 15:", path2)
