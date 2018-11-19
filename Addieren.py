import asyncio
import random

item = 0


async def one(queue):
    while True:
        item = await queue.get()
        item += rand.int(1,3)
        await asyncio.sleep(random.random())
        item = str(item)
        await queue.put(item)
        print("one:", item)
        queue.task_done()

async def two(queue):
    while True:
        item = await queue.get()
        item += rand.int(1,3)
        await asyncio.sleep(random.random())
        item = str(item)
        await queue.put(item)
        print("two:", item)
        queue.task_done()


async def run(n):
    queue = asyncio.Queue()
    # schedule the consumer
    eins = asyncio.ensure_future(one(queue))
    # run the producer and wait for completion
    await two(queue)
    # wait until the consumer has processed all items
    await queue.join()
    # the consumer is still awaiting for an item, cancel it
    eins.cancel()
    zwei = asyncio.ensure_future(two(queue))
    await one(queue)
    await queue.join()
    zwei.cancel()

loop = asyncio.get_event_loop()
loop.run_until_complete(run(10))
loop.close()