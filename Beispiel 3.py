# Adapted from https://docs.python.org/3/library/asyncio-task.html

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

delay = 0
ncoro = 10000

def main():
    loop = asyncio.new_event_loop()
    t = []
    for i in range(ncoro):
        t.append(loop.create_task(say_after(delay, 'hi')))

    print(f"started at {time.strftime('%X')}")

    loop.run_until_complete(asyncio.wait(t))

    print(f"finished at {time.strftime('%X')}")

    loop.close()

main()