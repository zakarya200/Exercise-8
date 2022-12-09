n = int(input("Введите число:"))
def sumfact(n):
    return sum (i for i in range(1, n)if n % i == 0 )
for i in range(n):
    c = sumfact(i)
    if c > i and sumfact(c) == i:
        print(i, c)
