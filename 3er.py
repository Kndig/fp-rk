from itertools import count
dreir = count(step=3)
print(list(next(dreir) for i in range(10)))