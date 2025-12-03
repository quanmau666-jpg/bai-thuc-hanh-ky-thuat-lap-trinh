nums = list(map(int, input().split(",")))

odds = [x for x in nums if x % 2 != 0]

print(",".join(str(x) for x in odds))
