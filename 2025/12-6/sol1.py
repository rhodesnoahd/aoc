import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "test.txt")
with open(input_file_path, "r") as file:
    lines = file.readlines()

# part 1 solution
ans = 0

a = []

for line in lines:
    a.append(line.strip().split())

for j in range(len(a[0])):
    op = ""
    tmp = 0
    for i in range(len(a) - 1, -1, -1):
        e = a[i][j]
        if i == len(a) - 1:
            op = e
        else:
            match op:
                case "+":
                    tmp += int(e)
                case "*":
                    tmp = int(e) if tmp == 0 else tmp * int(e)
    ans += tmp

print(ans)
