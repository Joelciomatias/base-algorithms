g = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]

il = len(g[0])  # internal length
islands = []

def dfs(g, i, j):
    # Boundary and visited check
    if i < 0 or i >= len(g) or j < 0 or j >= il or g[i][j] == 0:
        return 0
    
    # Mark the current cell as visited
    g[i][j] = 0
    
    # Initialize island size as 1 (counting the current cell)
    size = 1
    
    # Explore all four directions
    size += dfs(g, i - 1, j)  # Up
    size += dfs(g, i + 1, j)  # Down
    size += dfs(g, i, j - 1)  # Left
    size += dfs(g, i, j + 1)  # Right
    
    return size

for i in range(len(g)):
    for j in range(il):
        if g[i][j] == 1:  # Found an unvisited part of an island
            island_length = dfs(g, i, j)
            islands.append(island_length)

islands.sort()
max_island = islands[-1] if islands else 0

print(islands)
print(f'Max island number: {max_island}')
