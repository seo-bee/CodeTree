n = int(input())
cnt = 0

while True:
    if n == 1:
        print(cnt)
        break
    elif n % 2 == 0:
        n //= 2
    else:
        n *= 3
        n += 1
    
    cnt += 1