

# Example graph for Exercise 1 (update it as per your actual diagram)
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

# Example graph for Exercise 1 (update it as per your actual diagram)
graph1 = {
    5: [2, 6],
    2: [7, 8],
    6: [9],
    7: [],
    8: [],
    9: []
}

path1 = dfs(graph1, 5, 8)
print("DFS Path from 5 to 8:", path1)
