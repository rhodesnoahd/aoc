import os
import numpy as np
from scipy.optimize import milp, LinearConstraint
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

    A = np.zeros((len(jolts), len(btns)))
    for i in range(len(jolts)):
        for j in range(len(btns)):
            val = 0
            for k in btns[j]:
                if k == i:
                    val = 1
                    break
            A[i, j] = val

    b = np.array(list(jolts))

    # solve
    c = np.ones(A.shape[1])
    B = LinearConstraint(A, lb=b, ub=b)
    total = sum(milp(c, integrality=c, constraints=B).x)

    print(total)
    ans += total

    print(f"current ans: {ans}")
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"execution time: {elapsed_time:.4f} seconds")

print(f"\n{ans}")
total_end_time = time.perf_counter()
elapsed_time = total_end_time - total_start_time
print(f"total execution time: {elapsed_time:.4f} seconds")
