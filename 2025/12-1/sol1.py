import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
with open(input_file_path, "r") as file:
    lines = file.readlines()

# part 1 solution
ans = 0
dial = 50

for line in lines:
    amount = int(line[1:].strip())

    if line[0] == "L":
        # dial = (dial + (100 - amount)) % 100
        dial = (100 - amount + dial) % 100

    elif line[0] == "R":
        dial = (dial + amount) % 100

    if dial == 0:
        ans += 1

print(ans)
