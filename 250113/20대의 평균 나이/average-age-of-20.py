avg, cnt = 0, 0

while True:
    n = int(input())
    if (n % 20) > 9:
        break
    avg += n
    cnt += 1

print(f"{avg / cnt:.2f}")