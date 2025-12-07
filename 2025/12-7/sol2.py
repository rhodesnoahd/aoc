import os

grid = []
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    for line in file:
        grid.append(list(line.strip()))

# part 2 solution
ans = 0
mem = {}


def func(i, j):
    if (i, j) in mem:
        return mem[(i, j)]
    if not (0 <= j <= len(grid[i]) - 1):
        return 0
    if i == len(grid) - 1:
        return 1
    if grid[i + 1][j] == "^":
        res = func(i + 1, j - 1) + func(i + 1, j + 1)
        mem[(i, j)] = res
        return res
    return func(i + 1, j)


stop = False
for i in range(len(grid)):
    if stop:
        break
    for j in range(len(grid[i])):
        c = grid[i][j]

        if c == "S":
            ans = func(i + 1, j)
            stop = True
            break

print(ans)
