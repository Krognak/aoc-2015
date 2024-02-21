with open("day02_input.txt") as f:
    data = [line.strip() for line in f.readlines()]

# part 1
total_area = 0
for d in data:
    l, w, h = map(int, d.split("x"))
    total_area += 2 * l * w + 2 * w * h + 2 * h * l + min([l * w, w * h, h * l])
print(total_area)

# part 2
total_length = 0
for d in data:
    l, w, h = map(int, d.split("x"))
    total_length += 2 * sum(sorted([l, w, h])[:2]) + l * w * h
print(total_length)
