import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    lines = file.readlines()

line = lines[0].split(",")

# part 2 solution
ans = 0

for ids in line:
    dash = ids.index("-")
    l = int(ids[0:dash])
    r = int(ids[dash + 1 :])
    for i in range(l, r + 1):
        id = str(i)
        invalid = False
        for j in range(1, len(id) + 1):  # try ea possible seq len
            if invalid:
                break
            if len(id) % j == 0:  # only continue if evenly divisible
                seq = id[:j]  # sequence to check occurrences of
                end = j
                for k in range(
                    (len(id) - j) // j
                ):  # number of slots left in id to check
                    if invalid:
                        break
                    start = end
                    end = start + j
                    if seq == id[start:end]:  # check match
                        if k + 1 == (len(id) - j) / j:  # check if last slot
                            invalid = True
                    else:
                        break
        if invalid:
            ans += int(id)

print(ans)
