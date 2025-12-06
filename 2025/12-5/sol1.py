import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    lines = file.readlines()

# part 1 solution
ans = 0

rl = []
emptyLine = False

for line in lines:
    line = line.strip()

    if len(line) == 0:
        emptyLine = True
        continue

    if not emptyLine:
        rl.append(line)

    else:
        id = int(line)
        for e in rl:
            dash = e.index("-")
            l = int(e[0:dash])
            r = int(e[dash + 1 :])
            if l <= id <= r:
                ans += 1
                break

print(ans)
