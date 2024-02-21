import re

with open("day05_input.txt") as f:
    data = [i.strip() for i in f.readlines()]


# part 1
def vowel_check(s: str) -> bool:
    return len(re.findall(r"[aeiou]", s)) >= 3


def doubles_check(s: str) -> bool:
    return len(re.findall(r"(\w)\1", s)) >= 1


def forbidden_check(s: str) -> bool:
    return all(["ab" not in s, "cd" not in s, "pq" not in s, "xy" not in s])


count = 0
for d in data:
    if all([vowel_check(d), doubles_check(d), forbidden_check(d)]):
        count += 1
print(count)


# part 2
def pair_check(s: str) -> bool:
    return len(re.findall(r"(\w\w)\w*\1", s)) == 1


def repeat_check(s: str) -> bool:
    return len(re.findall(r"(\w)\w\1", s)) >= 1


count = 0
for d in data:
    if all([pair_check(d), repeat_check(d)]):
        count += 1
print(count)
