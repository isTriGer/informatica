k = 1
for i in range(4301614 + 1, 4301717 + 1, 2):
    b = True
    for j in range(3, i // 2, 2):
        if i % j == 0:
            b = False
    if b:
        print(k, i)
        k += 1
