import os
import time

d = {}  # devices
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    for line in file:
        word = line.strip().split(" ")
        key = word[0][: len(word[0]) - 1]
        d[key] = tuple(word[1:])


# part 2 solution
def dfs(path, mem, mem2):
    if (len(mem2), path[-1]) in mem:
        return mem[len(mem2), path[-1]]

    if path[-1] == "out":
        return 1 if len(mem2) == 2 else 0

    if path[-1] in d:
        for device in d[path[-1]]:
            path.append(device)
            if device == "fft" or device == "dac":
                mem2.add(device)
            tmp = dfs(path, mem, mem2)
            path.pop()
            if device == "fft" or device == "dac":
                mem2.remove(device)
            if (len(mem2), path[-1]) in mem:
                mem[(len(mem2), path[-1])] += tmp
            else:
                mem[(len(mem2), path[-1])] = tmp
        return mem[(len(mem2), path[-1])]


start_time = time.perf_counter()

ans = dfs(["svr"], {}, set())

print(ans)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"execution time: {elapsed_time:.4f} seconds")
