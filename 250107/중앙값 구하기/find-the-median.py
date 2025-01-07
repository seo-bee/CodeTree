inp = input().split()
li = []
li.append(int(inp[0]))
li.append(int(inp[1]))
li.append(int(inp[2]))

for j in range(len(li)-1, 0, -1):
    for i in range(j):
        if li[i] > li[i+1]:
            li[i],li[i+1] = li[i+1],li[i]

print(li[1])