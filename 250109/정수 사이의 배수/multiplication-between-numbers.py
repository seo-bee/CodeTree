a,b = map(int, input().split())
sum_val = 0
cnt = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        cnt += 1

print("{0} {1:.1f}".format(sum_val, sum_val/cnt))