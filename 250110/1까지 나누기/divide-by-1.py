n = int(input())
div_n = n

for i in range(1, n+1):
    div_n //= i
    if div_n <= 1:
        print(i)
        break