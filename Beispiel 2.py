import aiohttp
import asyncio
import urllib

async def print_preview(url):
    # connect to the server
    async with aiohttp.ClientSession() as session:
        # create get request
        async with session.get(url) as response:
            # wait for response
            response = await response.text()

            # print first 3 not empty lines
            count = 0
            lines = list(filter(lambda x: len(x) > 0, response.split('\n')))
            print('-'*80)
            for line in lines[:3]:
                print(line)
            print()
pages = [
        'http://textfiles.com/adventure/amforever.txt',
        'http://textfiles.com/adventure/ballyhoo.txt',
        'http://textfiles.com/adventure/bardstale.txt',
   ]

def print_async():
    tasks =  []
    loop = asyncio.new_event_loop()
    for page in pages:
        tasks.append(loop.create_task(print_preview(page)))

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

def print_sequential():
    contents = ""
    for p in pages:
        contents = contents + urllib.request.urlopen(p).read().decode("utf8")
        #print(contents)

if __name__=='__main__':
    import timeit
    print("Synchronous download")
    t = timeit.timeit('print_sequential()', number=1, globals=globals())
    print(t)
    print("Asynchronous download")
    t = timeit.timeit('print_async()',number=1,globals=globals())
    print(t)