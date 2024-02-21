import itertools

from collections import defaultdict

with open("day06_input.txt") as f:
    data = [i.strip() for i in f.readlines()]

# part 1
lights = defaultdict(lambda: 0)
for d in data:
    inst, c1 = d.split("through")[0].split()[-2::]
    c2 = d.split("through")[1]
    y1, x1 = map(int, c1.split(","))
    y2, x2 = map(int, c2.split(","))
    for i, j in itertools.product(range(y1, y2 + 1), range(x1, x2 + 1)):
        if inst == "toggle":
            lights[(i, j)] = (lights[(i, j)] + 1) % 2
        elif inst == "on":
            lights[(i, j)] = 1
        else:
            lights[(i, j)] = 0
lights_on = [1 for k, v in lights.items() if v == 1]
print(sum(lights_on))

# part 2
lights = defaultdict(lambda: 0)
for d in data:
    inst, c1 = d.split("through")[0].split()[-2::]
    c2 = d.split("through")[1]
    y1, x1 = map(int, c1.split(","))
    y2, x2 = map(int, c2.split(","))
    for i, j in itertools.product(range(y1, y2 + 1), range(x1, x2 + 1)):
        if inst == "toggle":
            lights[(i, j)] += 2
        elif inst == "on":
            lights[(i, j)] += 1
        else:
            lights[(i, j)] -= 1
            if lights[(i, j)] < 0:
                lights[(i, j)] = 0
print(sum(lights.values()))
