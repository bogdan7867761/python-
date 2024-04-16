n = int(input())
a, b = 1, 1
for k in range(n):
    print(a, end=' ')
    a, b = b, a + b
