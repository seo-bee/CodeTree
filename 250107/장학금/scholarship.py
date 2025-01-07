m,f = map(int, input().split())

if m < 90:
    print(0)
elif 95 <= f:
    print(100000)
elif 90 <= f:
    print(50000)
else:
    print(0)