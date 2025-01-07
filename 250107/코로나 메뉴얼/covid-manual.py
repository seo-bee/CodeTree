li = []
li.append(input().split())
li.append(input().split())
li.append(input().split())
result = 0

for p in li:
    if p[0] == 'Y' and int(p[1]) >= 37:
        result += 1

if result >= 2:
    print('E')
else:
    print('N')