a,b = map(int, input().split())

print(a//b,end='.')
c = a%b
for _ in range(20):
    c *= 10
    print(c//b,end='')
    c = c%b