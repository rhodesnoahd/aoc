import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    lines = file.readlines()

# part 2 solution - BRUTE FORCE
ans = 0

for line in lines:
    line = line.strip()
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    # i, j, k, l, m, n, o, p, q,  r,  s,  t
    d12, d11, d10, d9, d8, d7, d6, d5, d4, d3, d2, d1 = (
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
    )
    for i in range(len(line) + 1 - 12):
        if d12[1] < int(line[i]):
            d12 = [i, int(line[i])]
    for j in range(d12[0] + 1, len(line) + 1 - 11):
        if d11[1] < int(line[j]):
            d11 = [j, int(line[j])]
    for k in range(d11[0] + 1, len(line) + 1 - 10):
        if d10[1] < int(line[k]):
            d10 = [k, int(line[k])]
    for l in range(d10[0] + 1, len(line) + 1 - 9):
        if d9[1] < int(line[l]):
            d9 = [l, int(line[l])]
    for m in range(d9[0] + 1, len(line) + 1 - 8):
        if d8[1] < int(line[m]):
            d8 = [m, int(line[m])]
    for n in range(d8[0] + 1, len(line) + 1 - 7):
        if d7[1] < int(line[n]):
            d7 = [n, int(line[n])]
    for o in range(d7[0] + 1, len(line) + 1 - 6):
        if d6[1] < int(line[o]):
            d6 = [o, int(line[o])]
    for p in range(d6[0] + 1, len(line) + 1 - 5):
        if d5[1] < int(line[p]):
            d5 = [p, int(line[p])]
    for q in range(d5[0] + 1, len(line) + 1 - 4):
        if d4[1] < int(line[q]):
            d4 = [q, int(line[q])]
    for r in range(d4[0] + 1, len(line) + 1 - 3):
        if d3[1] < int(line[r]):
            d3 = [r, int(line[r])]
    for s in range(d3[0] + 1, len(line) + 1 - 2):
        if d2[1] < int(line[s]):
            d2 = [s, int(line[s])]
    for t in range(d2[0] + 1, len(line) + 1 - 1):
        if d1[1] < int(line[t]):
            d1 = [t, int(line[t])]
    ans += int(
        str(d12[1])
        + str(d11[1])
        + str(d10[1])
        + str(d9[1])
        + str(d8[1])
        + str(d7[1])
        + str(d6[1])
        + str(d5[1])
        + str(d4[1])
        + str(d3[1])
        + str(d2[1])
        + str(d1[1])
    )

print(ans)
