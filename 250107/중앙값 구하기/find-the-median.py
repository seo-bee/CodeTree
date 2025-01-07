inp = input().split()
li = []
li.append(int(inp[0]))
li.append(int(inp[1]))
li.append(int(inp[2]))

for i in range(0, len(li)-1):
    if li[i] > li[i+1]:
        li[i],li[i+1] = li[i+1],li[i]

print(li[1])