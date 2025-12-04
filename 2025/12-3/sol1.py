import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    lines = file.readlines()

# part 1 solution
ans = 0

for line in lines:
    line = line.strip()
    l, r, seen = 0, int(line[-1]), int(line[-1])
    for i in range(len(line) - 2, -1, -1):
        d = int(line[i])
        if d >= l:
            seen = max(seen, l)
            l = d
            r = max(seen, r)
        else:
            seen = max(seen, d)
    ans += int(str(l) + str(r))

print(ans)
