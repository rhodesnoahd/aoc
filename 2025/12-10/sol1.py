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

# part 1 solution
ans = 0


def updateLights(b, lights):
    _lights = list(lights)
    for i in b:
        _lights[i] = "." if _lights[i] == "#" else "#"
    return "".join(_lights)


def backtrack(lights, n, stack):
    global btns
    global sols

    on = len(lights.replace(".", ""))
    if on == 0:
        heapq.heappush(sols, (n, stack[:]))
        return

    elif n == 10:
        return

    # remove btns already pressed in this sol
    _btns = [b for b in btns if b not in stack]

    while _btns:
        b = _btns.pop()

        # press button
        if not sols or (sols and sols[0][0] > n + 1):
            _lights = updateLights(b, lights)
            stack.append(b)
            backtrack(_lights, n + 1, stack)

        # backtrack
        if stack:
            stack.pop()

    return


start_time = time.perf_counter()
for l in m:
    mach = l.split(" ")
    lights = mach[0][1 : len(mach[0]) - 1]
    btns = mach[1 : len(mach) - 1]
    for i in range(len(btns)):
        b = btns[i]
        b = re.sub(r"[()]", "", b)
        btns[i] = tuple(map(int, b.split(",")))

    sols = []
    backtrack(lights, 0, [])
    ans += heapq.heappop(sols)[0]

print(ans)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"execution time: {elapsed_time:.4f} seconds")
