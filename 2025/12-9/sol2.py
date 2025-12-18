import os

rt = []  # red tiles
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    for line in file:
        rt.append(tuple(map(int, line.strip().split(","))))

# part 2 solution
ans = 0

pair = []
for i in range(len(rt) - 1):
    for j in range(i + 1, len(rt)):
        pair.append((i, j))

l = list(range(len(rt)))
l.append(0)

for p1, p2 in pair:
    mini, minj = min(rt[p1][0], rt[p2][0]), min(rt[p1][1], rt[p2][1])
    maxi, maxj = max(rt[p1][0], rt[p2][0]), max(rt[p1][1], rt[p2][1])

    prev, elig = [], True
    for e in l:
        i, j = rt[e]

        if prev != []:
            if prev[0] == i:
                minjl, maxjl = min(prev[1], j), max(prev[1], j)
                if mini < i < maxi and (
                    minj < minjl < maxj
                    or minj < maxjl < maxj
                    or minjl < minj < maxjl
                    or minjl < maxj < maxjl
                ):
                    elig = False
                    break
            elif prev[1] == j:
                minil, maxil = min(prev[0], i), max(prev[0], i)
                if minj < j < maxj and (
                    mini < minil < maxi
                    or mini < maxil < maxi
                    or minil < mini < maxil
                    or minil < maxi < maxil
                ):
                    elig = False
                    break

        prev = [i, j]

    if elig:
        ans = max(
            ans, (abs(rt[p1][0] - rt[p2][0]) + 1) * (abs(rt[p1][1] - rt[p2][1]) + 1)
        )

print(ans)
