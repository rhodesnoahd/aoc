import os

rt = []  # red tiles
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    for line in file:
        rt.append(tuple(map(int, line.strip().split(","))))

# part 1 solution
ans = 0

pair = []
for i in range(len(rt) - 1):
    for j in range(i + 1, len(rt)):
        pair.append((i, j))

for i, j in pair:
    ans = max(ans, (abs(rt[i][0] - rt[j][0]) + 1) * (abs(rt[i][1] - rt[j][1]) + 1))

print(ans)
