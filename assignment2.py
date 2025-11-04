# Example graph for Exercise 3 (alphabetical nodes)
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

# Example graph for Exercise 3 (alphabetical nodes)
graph3 = {
    'root': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': [],
    'E': ['H'],
    'F': ['I', 'J'],
    'G': [],
    'H': ['K', 'L'],
    'I': [],
    'J': ['M'],
    'K': [],
    'L': [],
    'M': []
}

path3 = dfs(graph3, 'root', 'M')
print("DFS Path from root to M:", path3)
