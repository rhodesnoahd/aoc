import os

grid = []
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "test.txt")
with open(input_file_path, "r") as file:
    for line in file:
        grid.append(list(line.strip()))

# part 1 solution
ans = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        c = grid[i][j]

        if c == "S":
            grid[i + 1][j] = "1"

        elif c == "^" and grid[i - 1][j].isdigit():
            d = int(grid[i - 1][j])
            if j - 1 >= 0:
                if grid[i][j - 1] == ".":
                    grid[i][j - 1] = str(d)
                elif grid[i][j - 1].isdigit():
                    grid[i][j - 1] = str(int(grid[i][j - 1]) + d)
                if grid[i - 1][j - 1].isdigit():
                    grid[i][j - 1] = str(int(grid[i][j - 1]) + int(grid[i - 1][j]))
            if j + 1 <= len(grid[i]) - 1:
                if grid[i][j + 1] == ".":
                    grid[i][j + 1] = str(d)
                elif grid[i][j + 1].isdigit():
                    grid[i][j + 1] = str(int(grid[i][j + 1]) + d)
                if grid[i - 1][j + 1].isdigit():
                    grid[i][j + 1] = str(int(grid[i - 1][j]) + int(grid[i - 1][j]))

        elif c == "." and i - 1 >= 0 and grid[i - 1][j].isdigit():
            d = int(grid[i - 1][j])
            grid[i][j] = str(d)

for j in range(len(grid[-1])):
    c = grid[-1][j]
    if c.isdigit():
        ans += int(c)


print(ans)
