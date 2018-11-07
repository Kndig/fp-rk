# Two instances of the same (CPU-intensive) function run cuncurrently

from math import sqrt

tasks = { }

def countdown(n):
    i = n
    while i >= 0:
        print("{} froom countdown".format(i))
        yield i
        i = i - 1
    return True


def init():
    tasks[20] = countdown(20)
    tasks[10] = countdown(10)

def loop():
    exited = 0
    while tasks:
        if exited:
            del tasks[exited]
            exited = 0

        for tid in tasks:
            try:
                x = next(tasks[tid])
            except StopIteration as val:
                print("End")
                exited = tid

# Main Program:
init()
loop()