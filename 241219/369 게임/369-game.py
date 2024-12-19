n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        print(0, end = " ")
    else:
        str_i = str(i)
        if str_i.count("3") > 0 or str_i.count("6") > 0 or str_i.count("9") > 0:
            print(0, end = " ")
        else:
            print(i, end = " ")