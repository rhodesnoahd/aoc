import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    lines = file.readlines()

# part 2 solution
ans = 0
dial = 50

for line in lines:
    amount = int(line[1:].strip())

    if line[0] == "L":
        ans += (amount + (100 - dial if dial != 0 else 0)) // 100
        dial = (dial + (100 - amount)) % 100

    elif line[0] == "R":
        ans += (amount + dial) // 100
        dial = (dial + amount) % 100

print(ans)
