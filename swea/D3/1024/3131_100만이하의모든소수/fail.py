N = 1000000
decimals = [0] * N

decimals[0] = 2

idx = 1
number = 3
while number <= N:
    flag = 0
    for i in range(idx):
        if not number // decimals[i]:
            flag = 1
            break
    if not flag:
        decimals[idx] = number
        idx += 1
    number += 2

print(*decimals[:idx])
