data = input().split(",")

result = []

for b in data:
    if int(b, 2) % 5 == 0:
        result.append(b)

print(",".join(result))
