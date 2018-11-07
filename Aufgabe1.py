# Pushing to the coroutine with send rather than pulling with yield

# Generator version
def grep_gen(pattern, lines):
    print("Searching for", pattern)
    for line in lines:
        if pattern in line:
            yield line

# Coroutine version
def grep_coro(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


# Generator version
text = ["Hi there, grep", "Do you hear me?", "Ah, you're looking for the generator!"]
it = grep_gen("generator",text)
for answer in it:
    print(answer)

# Coroutine version
coro = grep_coro('coroutine') # Searching for the word "coroutine"
next(coro) # Start / prime the coroutine
coro.send("I love you")
coro.send("Don't you love me?")
coro.send("I love coroutines instead!")