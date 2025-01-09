n = int(input())
sum_v = 0

for _ in range(n):
    i = int(input())
    sum_v += i

print("{0} {1:.1f}".format(sum_v, sum_v/n))