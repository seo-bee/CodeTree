n = int(input())

cnt = 0

for y in range(1, n+1):
    if (y % 4 != 0) or (y % 100 == 0 and y % 400 != 0):
        pass
    else:
        cnt += 1

print(cnt)