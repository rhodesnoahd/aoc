import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    lines = file.readlines()

# part 1 solution
ans = 0


def check(i, j):
    if 0 <= i < len(lines) and 0 <= j < len(lines[i]) and lines[i][j] == "@":
        return 1
    else:
        return 0


for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != "@":
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
            ans += 1

print(ans)
