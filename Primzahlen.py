x = [x for x in range(2, 1000) if not[y for y in range(2, x//2) if x % y ==0]]
print(x)