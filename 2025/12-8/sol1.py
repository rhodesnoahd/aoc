import os
import math
import heapq

jb = []  # junction boxes
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    for line in file:
        jb.append(tuple(map(int, line.strip().split(","))))

# part 1 solution
ans = 1

pair = []
for i in range(len(jb) - 1):
    for j in range(i + 1, len(jb)):
        dist = math.dist(jb[i], jb[j])
        heapq.heappush(pair, (dist, i, j))

wc, c = [-1] * len(jb), []
for i in range(1000):
    tmp = heapq.heappop(pair)
    jb1, jb2 = tmp[1], tmp[2]

    if (wc[jb1] != -1 and wc[jb2] != -1) and wc[jb1] == wc[jb2]:
        continue

    elif wc[jb1] == wc[jb2] == -1:
        nc = set(tmp[1:])
        c.append([-len(nc), nc])
        wc[jb1], wc[jb2] = len(c) - 1, len(c) - 1

    elif (wc[jb1] != -1 and wc[jb2] != -1) and wc[jb1] != wc[jb2]:
        l, r = (jb1, jb2) if len(c[wc[jb1]][1]) >= len(c[wc[jb2]][1]) else (jb2, jb1)
        c[wc[l]][1].update(c[wc[r]][1])
        c[wc[l]][0] = -len(c[wc[l]][1])
        rem = wc[r]
        for jbox in c[rem][1]:
            wc[jbox] = wc[l]
        c[rem] = [0, set()]

    elif wc[jb1] != -1 or wc[jb2] != -1:
        l, r = (jb1, jb2) if wc[jb1] != -1 else (jb2, jb1)
        c[wc[l]][1].add(r)
        c[wc[l]][0] = -len(c[wc[l]][1])
        wc[r] = wc[l]

heapq.heapify(c)

for i in range(3):
    s = heapq.heappop(c)
    ans *= -s[0]

print(ans)
