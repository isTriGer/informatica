def f(x, s, q):
    if x + s >= 69 and (q == 2 or q == 4):
        return 1
    elif q > 4:
        return 0
    elif x + s >= 69:
        return 0
    if q % 2 == 1:
        return f(x + 1, s, q + 1) or f(x * 2, s, q + 1) or f(x, s + 1, q + 1) or f(x, s * 2, q + 1)
    return f(x + 1, s, q + 1) and f(x * 2, s, q + 1) and f(x, s + 1, q + 1) and f(x, s * 2, q + 1)


for i in range(1, 63):
    if f(6, i, 0) == 1:
        print(i)
        break
