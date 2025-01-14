a,b,c = map(int, input().split())
bl = False

for i in range(a, b+1):
    if i % c == 0:
        bl = True
    else:
        continue

print('YES') if bl == True else print('NO')