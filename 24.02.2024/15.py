def f(a, x):
    return (a % 7 == 0) and ((240 % x == 0) <= ((not (a % x == 0)) <= (not (780 % x == 0))))


for a in range(1, 1000):
    b = True
    for x in range(1, 100):
        if not f(a, x):
            b = False
            break
    if b:
        print(a)
        break
