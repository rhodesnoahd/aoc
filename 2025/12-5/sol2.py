import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    lines = file.readlines()

# part 2 solution
ans = 0

cl = []


def sumAns():
    global ans
    for e in cl:
        dash = e.index("-")
        l = int(e[:dash])
        r = int(e[dash + 1 :])
        ans += r - l + 1


def checkOverlap(l, r):
    global cl
    overlap = -1
    for i, e in enumerate(cl):
        dash = e.index("-")
        el = int(e[:dash])
        er = int(e[dash + 1 :])
        if el <= l <= er or el <= r <= er or l <= el <= r or l <= er <= r:
            overlap = min(overlap, i) if overlap != -1 else i
            cl[i] = f"{min(l, el)}-{max(r, er)}"
    return overlap


def compress(i):
    global cl
    clc = cl[: i + 1]  # copy cl thru i
    dash = clc[i].index("-")
    l = int(clc[i][:dash])
    r = int(clc[i][dash + 1 :])
    for j in range(i, len(cl)):
        dash = cl[j].index("-")
        el = int(cl[j][:dash])
        er = int(cl[j][dash + 1 :])
        if el <= l <= er or el <= r <= er or l <= el <= r or l <= er <= r:
            clc[i] = f"{min(l, el)}-{max(r, er)}"
        else:
            clc.extend(cl[j:])  # copy the rest of cl
            break
    cl = clc


for line in lines:
    line = line.strip()

    if len(line) == 0:
        sumAns()
        break

    dash = line.index("-")
    l = int(line[:dash])
    r = int(line[dash + 1 :])
    i = checkOverlap(l, r)
    if i == -1:
        cl.append(line)
        cl = sorted(cl, key=lambda item: int(item[: item.index("-")]))
    else:
        compress(i)


print(ans)
