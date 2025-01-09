def print_high_to_low(h,l):
    for i in range(h,l-1,-1):
        print(i, end=' ')


a,b = map(int, input().split())

if a >= b:
    print_high_to_low(a,b)
else:
    print_high_to_low(b,a)