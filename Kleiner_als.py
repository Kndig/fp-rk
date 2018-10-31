def integers():
    n = 1
    while True:
        yield n
        n = n + 2

for x in integers():
    if x > 10:
        break
    print(x)
