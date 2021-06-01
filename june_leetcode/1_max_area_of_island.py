def maxAreaOfIsland(grid) -> int:
    max_island = 0

    def islandLength(row, col, curr_length):
        if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] == 0:
            return curr_length

        curr_length += 1
        grid[row][col] = 0
        curr_length = islandLength(row, col + 1, curr_length)
        curr_length = islandLength(row + 1, col, curr_length)
        curr_length = islandLength(row - 1, col, curr_length)
        curr_length = islandLength(row, col - 1, curr_length)
        return curr_length

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                continue
            else:
                curr_island_length = islandLength(i, j, 0)
                if max_island < curr_island_length:
                    max_island = curr_island_length
    return max_island


grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]

print(maxAreaOfIsland(grid))
