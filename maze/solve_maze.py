# 1: wall
# 2: end goal
# 3: start position
# 0: valid path
maze_01 = [
    [1,1,1,2,1,1,1,1],
    [1,0,1,0,0,1,1,1],
    [1,1,0,1,0,0,1,1],
    [1,0,0,0,0,0,0,1],
    [1,3,1,1,1,1,1,1]
]

maze_02 = [
    [1,1,1,1,1,2,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,0,0,1],
    [1,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,1,1,0,1],
    [1,0,1,1,0,0,1,1,0,1],
    [1,1,1,1,3,0,1,1,0,1],
]

# DFS while traversing
# - find start
# - find end
def find_start_end(maze):
    start = None
    end = None

    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if col == 3:
                start = (i, j)
            if col == 2:
                end = (i, j)
    return start, end

# list conditions for valid movement
# - boundaries
# - wall detection
# - visited M[bool]
def is_valid_move(maze, visited, row, col):
    rows = len(maze)
    cols = len(maze[0])
    if (0 <= row < rows) and ((0 <= col < cols) and
         (maze[row][col] != 1)) and not visited[row][col]:
        return True
    return False

def solve_maze(maze, start, end):
    # define directions for loop to recurse
    directions = [(-1,0),
                  (0,-1),
                  (1,0),
                  (0,1)]

    # res container
    paths = []
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

    def dfs(row, col):
        # Success case
        if(row, col) == end:
            paths.append(maze[row][col])
            return True

        if is_valid_move(maze, visited, row, col):
            visited[row][col] = True
            paths.append(maze[row][col])

            for x, y in directions:
                if dfs(row + x, col + y):
                    return True
                # remove last in stack
                paths.pop()
        return False

    start_row, start_col = start
    dfs(start_row, start_col)
    return paths


if __name__ == "__main__":
    maze = maze_02
    start, end = find_start_end(maze)
    solution_path = solve_maze(maze, start, end)
    print(start)
    print(end)
    print(solution_path)




