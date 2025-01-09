def print_sum(l,h):
    sum_result = 0
    for i in range(l,h+1):
        if i % 5 == 0:
            sum_result += i
    return sum_result


a,b = map(int, input().split())
res = 0

if a >=b:
    res = print_sum(b,a)
else:
    res = print_sum(a,b)

print(res)