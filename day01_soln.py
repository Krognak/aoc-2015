with open("day01_input.txt") as f:
    data = f.read()

# part 1
floor = 0
for d in data:
    if d == "(":
        floor += 1
    else:
        floor -= 1
print(floor)

# part 2
floor = 0
for i, char in enumerate(data, start=1):
    if char == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        break
print(i)

