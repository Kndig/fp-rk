from math import sqrt

def hypo(n):
    return lambda a : sqrt(n**2+a**2)



print(hypo(3)(4))
