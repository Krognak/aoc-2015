with open("day03_input.txt") as f:
    data = f.read()

# part 1
santa_coord = [0, 0]
visited = [(0, 0)]
for d in data:
    if d == "<":
        santa_coord[1] -= 1
    elif d == ">":
        santa_coord[1] += 1
    elif d == "^":
        santa_coord[0] += 1
    else:
        santa_coord[0] -= 1
    visited.append(tuple(santa_coord))
print(len(set(visited)))

# part 2
santa_coord = [0, 0]
robo_coords = [0, 0]
visited = [(0, 0)]
for d in data[::2]:
    if d == "<":
        santa_coord[1] -= 1
    elif d == ">":
        santa_coord[1] += 1
    elif d == "^":
        santa_coord[0] += 1
    else:
        santa_coord[0] -= 1
    visited.append(tuple(santa_coord))
for d in data[1::2]:
    if d == "<":
        robo_coords[1] -= 1
    elif d == ">":
        robo_coords[1] += 1
    elif d == "^":
        robo_coords[0] += 1
    else:
        robo_coords[0] -= 1
    visited.append(tuple(robo_coords))
print(len(set(visited)))
