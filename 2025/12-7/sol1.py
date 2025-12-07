import os

grid = []
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    for line in file:
        grid.append(list(line.strip()))

# part 1 solution
ans = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        c = grid[i][j]

        if c == "S":
            grid[i + 1][j] = "|"

        elif c == "^" and grid[i - 1][j] == "|":
            if j - 1 >= 0 and grid[i][j - 1] == ".":
                grid[i][j - 1] = "|"
            if j + 1 <= len(grid[i]) - 1 and grid[i][j + 1] == ".":
                grid[i][j + 1] = "|"
            ans += 1

        elif c == "." and i - 1 >= 0 and grid[i - 1][j] == "|":
            grid[i][j] = "|"


print(ans)
