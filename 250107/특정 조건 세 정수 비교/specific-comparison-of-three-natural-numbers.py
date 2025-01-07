a,b,c = map(int, input().split())
print(1,end=" ") if a == min(a,b,c) else print(0, end=" ")
print(1,end=" ") if a == b and b == c else print(0, end=" ")