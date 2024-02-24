def f(n, m):
    if m == 0:
        d = 1
    else:
        d = n * f(n, m - 1)
    return d


k = 0
for i in range(1, 1000):
    if 100 <= f(i, 2) <= 1000:
        k += 1
print(k)
