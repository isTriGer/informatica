print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not y and ((x <= w) != z):
                    print(x, y, z, w, 1)
                else:
                    print(x, y, z, w, 0)