n = int(input())

for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

for k in range(i-1,-1,-1):
    for j in range(k+1):
        print('*', end=' ')
    print()