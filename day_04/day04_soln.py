import hashlib

with open("day04_input.txt") as f:
    secret = f.read().strip()

# part 1
hash = hashlib.md5(secret.encode()).hexdigest()
i = 1
while hash[0:5] != "00000":
    i += 1
    hash = hashlib.md5(f"{secret}{i}".encode()).hexdigest()
print(i, hash[0:5])

# part 2
hash = hashlib.md5(secret.encode()).hexdigest()
i = 1
while hash[0:6] != "000000":
    i += 1
    hash = hashlib.md5(f"{secret}{i}".encode()).hexdigest()
print(i, hash[0:6])
