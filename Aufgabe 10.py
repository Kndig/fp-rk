import asyncio
import multiprocessing
nbzahl = 0

async def eins(lock):
    global nbzahl
    n = 0
    while n < 10:
        await asyncio.sleep(0.01)
        lock.aquire()
        nbzahl += 1
        lock.release()
        n += 1
        print("1", nbzahl)




async def zwei(lock):
    global nbzahl
    n = 0
    while n < 10:
        await asyncio.sleep(0.01)
        lock.aquire()
        nbzahl += 2
        lock.release()
        n += 1
        print("2", nbzahl)



def main():
    lock = multiprocessing.Lock()
    loop = asyncio.new_event_loop()
    einsi = loop.create_task(eins(lock))
    zweii = loop.create_task(zwei(lock))
    loop.run_until_complete(asyncio.wait([einsi, zweii]))
    loop.close()

main()