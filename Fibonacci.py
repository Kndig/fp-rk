def fibi(n):
    if n <= 2:
        return 1
    if n > 2:
        x = 1
        y = 1
        for i in range(n-2):
            z = y + x
            x = y
            y = z

    return z

print(fibi(5))