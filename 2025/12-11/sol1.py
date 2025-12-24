import os
import heapq
import re
import time

d = {}  # devices
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    for line in file:
        word = line.strip().split(" ")
        key = word[0][: len(word[0]) - 1]
        d[key] = tuple(word[1:])


# part 1 solution
def dfs(stack):
    global sols
    top = stack[-1]

    if top == "out":
        sols.append(stack[:])
        return

    if top in d:
        for device in d[top]:
            stack.append(device)
            dfs(stack)
            stack.pop()


ans = 0

start_time = time.perf_counter()

sols = []
dfs(["you"])
ans = len(sols)

print(ans)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"execution time: {elapsed_time:.4f} seconds")
