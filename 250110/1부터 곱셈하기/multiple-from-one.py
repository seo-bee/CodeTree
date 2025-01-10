n = int(input())
mul_v = 1

for i in range(1, 11):
    mul_v *= i
    if mul_v >= n:
        print(i)
        break