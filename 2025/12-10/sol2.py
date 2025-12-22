import os
import heapq
import re
import time

m = []  # machines
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    for line in file:
        m.append(line.strip())

# part 2 solution
ans = 0


def updateJolts(coef):
    global btns
    global jolts
    _jolts = list(jolts)
    for i, c in enumerate(coef):
        if c == -1:
            continue
        for j in btns[i]:
            _jolts[j] -= c
            if _jolts[j] < 0:
                return []
    return _jolts


def backtrack(coef, mem, n):
    global btns
    global sols

    _jolts = updateJolts(coef)

    on = len("".join(list(map(str, _jolts))).replace("0", ""))
    if on == 0:
        sol = 0
        for c in coef:
            if c > 0:
                sol += c
        heapq.heappush(sols, (sol, coef[:]))
        return True

    if n >= depth:
        return False

    # current highest joltage requirement (hirq) order
    cmji, hirq, tmp = 0, [], _jolts[:]
    for i in range(len(tmp)):
        imax = tmp.index(max(tmp))
        if i == 0:
            cmji = imax
        hirq.append(imax)
        tmp[imax] *= -1

    # remove buttons that would not decrease current max joltage if pressed
    # sort buttons by _merq to determine coef assignment order
    _btns = []
    for i in range(len(btns)):
        _cmji, _merq = False, ["1"] * len(hirq)
        for j in btns[i]:
            if j == cmji:
                _cmji = True
            if j in hirq:  # huh
                rq = hirq.index(j)
                _merq[rq] = "0"
        if _cmji:
            heapq.heappush(_btns, ("".join(_merq), i))

    while _btns:
        b = heapq.heappop(_btns)
        bi = b[1]
        _btn = btns[bi]

        # start assignment w min jolts button would effect
        mjbp = float("inf")
        for i in _btn:
            mjbp = min(mjbp, _jolts[i])
        domain = [i for i in range(mjbp, 0, -1)]

        for val in domain:
            # perform assignment
            coef[bi] = val
            _jolts = tuple(updateJolts(coef))
            consistent = len(_jolts) != 0

            if consistent and _jolts not in mem:
                mem.add(_jolts)
                if backtrack(coef, mem, n + 1):
                    return True

            # backtrack
            coef[bi] = -1
            if _jolts in mem:
                mem.remove(_jolts)

    return False


count = 0
total_start_time = time.perf_counter()
for l in m:
    count += 1
    start_time = time.perf_counter()
    print(f"\nmachine: {count}")
    print(f"{l}")

    # parse machine
    mach = l.split(" ")
    btns = mach[1 : len(mach) - 1]
    for i in range(len(btns)):
        b = btns[i]
        b = re.sub(r"[()]", "", b)
        btns[i] = tuple(map(int, b.split(",")))
    jolts = tuple(map(int, mach[-1][1 : len(mach[-1]) - 1].split(",")))

    # search
    depth = int((max(jolts) + 3) * 1.25)
    sols = []
    coef = [-1] * len(btns)
    backtrack(coef, set(), 0)
    if sols:
        sol = heapq.heappop(sols)[0]
        print(f"sol: {sol}")
        ans += sol
    else:
        print("sol: not found")
    print(f"current ans: {ans}")
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"execution time: {elapsed_time:.4f} seconds")

print(f"\n{ans}")
total_end_time = time.perf_counter()
elapsed_time = total_end_time - total_start_time
print(f"total execution time: {elapsed_time:.4f} seconds")
