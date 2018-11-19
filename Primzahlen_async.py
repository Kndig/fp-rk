import asyncio
import time

delay = 0.001

async def number(name, queue):
    while True:
        # Get a "work item" out of the queue.
        prime = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(delay)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

async def main():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()
    x = [x for x in range(2, 100) if not [y for y in range(2, x // 2) if x % y == 0]]
    queue.put_nowait(x)

    tasks = []
    for i in range(3):
        task = asyncio.create_task(number(f'worker-{i}', queue))
        tasks.append(task)

    await queue.join()

    for task in tasks:
        task.cancel()
        # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print("primes:", x)

asyncio.run(main())