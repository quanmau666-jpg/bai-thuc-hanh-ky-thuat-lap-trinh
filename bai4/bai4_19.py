import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

P = tuple(i for i in range(1_000_000) if is_prime(i))
print("Số lượng số nguyên tố:", len(P))
