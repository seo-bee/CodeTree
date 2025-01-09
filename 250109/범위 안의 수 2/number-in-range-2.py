sum_v,cnt_v = 0,0

for _ in range(10):
    n = int(input())
    if 0 <= n and n <= 200:
        sum_v += n
        cnt_v += 1

print("{0} {1:.1f}".format(sum_v,sum_v/cnt_v))