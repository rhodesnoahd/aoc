import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    lines = file.readlines()

line = lines[0].split(",")

# part 1 solution
ans = 0

for ids in line:
    dash = ids.index("-")
    l = int(ids[0:dash])
    r = int(ids[dash + 1 :])
    for i in range(l, r + 1):
        id = str(i)
        if id[: len(id) // 2] == id[len(id) // 2 :]:
            ans += int(id)

print(ans)
