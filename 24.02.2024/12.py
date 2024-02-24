for i in range(1, 100):
    n = '1' * i + '2' * i + '3' * i
    while '21' in n or '31' in n or '32' in n:
        if '21' in n:
            n = n.replace('21', '12', 1)
        if '31' in n:
            n = n.replace('31', '13', 1)
        if '32' in n:
            n = n.replace('32', '23', 1)
    if len(n) >= 50 and n[49] == '2':
        print(i*3)
        break
