def grade(n):
    if n >= 90:
        print("A", end = " ")
    elif n >= 80:
        print("B", end = " ")
    elif n >= 70:
        print("C", end = " ")
    elif n >= 60:
        print("D", end = " ")
    else:
        print("F", end = " ")


n = int(input())

while n <= 100:
    grade(n)
    n += 1