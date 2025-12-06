import os

grid = []
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    for line in file:
        grid.append(list(line))
grid[-1].append("\n")

# part 2 solution
ans = 0

eof = False
prob = []
for j in range(len(grid[0])):
    col = []
    for i in range(len(grid) - 1, -1, -1):
        if eof:
            break
        c = grid[i][j]
        if ((c == "+" or c == "*") and len(prob) > 0) or c == "\n":
            if j == len(grid[0]) - 1:
                l = [" "] * len(prob[0])
                prob.append(l)
            op = prob[0][0]
            tmp = 0
            for k in range(len(prob) - 1):
                num = ""
                for l in range(len(prob[k]) - 1, -1, -1):
                    char = prob[k][l]
                    if l == 0:
                        match op:
                            case "+":
                                tmp += int(num)
                            case "*":
                                tmp = int(num) if tmp == 0 else tmp * int(num)
                        break
                    else:
                        num += char
            ans += tmp
            prob = []
            if c == "\n":
                eof = True

        col.append(c)
    prob.append(col)

print(ans)
