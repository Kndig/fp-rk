def mygen():
    print("Start")
    yield 1
    for x in range(1,4):
        print("Die Zahl ist")
        yield x
    yield 10

a = mygen()
x = next(a)
print("x: ", x)
