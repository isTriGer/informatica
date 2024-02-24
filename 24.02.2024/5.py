for n in range(1, 100):
    n_bin = bin(n)[2::]
    if n_bin.count('1') % 2 == '1':
        n_bin = n_bin + '11'
    else:
        n_bin = n_bin + '00'
    r = int(n_bin, 2)
    if r > 130:
        print(r)
        break

