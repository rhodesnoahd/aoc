import os

grid = []

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    for line in file:
        grid.append(list(line.strip()))

# part 2 solution
ans = 0


def check(i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == "@":
        return 1
    else:
        return 0


n = 1
while n > 0:
    n = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != "@":
                continue
            if (
                check(i - 1, j)  # N
                + check(i - 1, j + 1)  # NE
                + check(i, j + 1)  # E
                + check(i + 1, j + 1)  # SE
                + check(i + 1, j)  # S
                + check(i + 1, j - 1)  # SW
                + check(i, j - 1)  # W
                + check(i - 1, j - 1)  # NW
            ) < 4:
                grid[i][j] = "."
                n += 1
    ans += n

print(ans)
