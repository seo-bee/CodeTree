n = int(input())
sum_v = 0

for i in range(1, n):
    if n % i == 0:
        sum_v += i

print('P') if sum_v == n else print('N')