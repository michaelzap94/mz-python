import asyncio
import async_timeout
import aiohttp
import time
import os
from csv import DictWriter

current_dir = os.path.dirname(__file__)
FILENAME = os.path.join(current_dir, 'write_data.csv')

async def fetch_page(session, url, asyncState):
    # async_timeout is a function that will terminate/raise exeption if request takes too long
    # in this case 30 seconds
    async with async_timeout.timeout(30):
        # make the session.get(url) call and get it as a response
        async with session.get(url) as response:
            rawResponse = await response.content.read()
            if(asyncState.headers is None and asyncState.csvwriter is None):
                print('creating headers')
                headers = ['url','rawContent']
                asyncState.csvwriter = DictWriter(
                            asyncState.csv_file,
                            fieldnames=headers,
                            delimiter=",",
                        )
                asyncState.csvwriter.writeheader()

            asyncState.csvwriter.writerow({'url': url, 'rawContent': rawResponse[:10]})

            return response.status

# ----------------------------------------------------------------------------------
# GATHER all futures and let asyncio execute them
async def get_multiple_pages_efficient_FAST(loop, urls, asyncState):
    list_of_futures = []
    # aiohttp.ClientSession(loop=loop) -> create a pool of sessions and pass the asyncio loop so it doesn't create a new loop
    # each session contains a cookie storage
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            list_of_futures.append(fetch_page(session, url, asyncState))
        # GATHER all futures and let asyncio execute them 
        # Then, await for all results -> asyncio.gather() returns list of futures
        # that when 'await' will return a list of returned values from 'fetch_page()' function
        grouped_tasks = asyncio.gather(*list_of_futures) 
        # print(grouped_tasks) # <_GatheringFuture pending>
        results_list = await grouped_tasks # it will return when all tasks have finished
        return results_list
# ----------------------------------------------------------------------------------

def main():
    urls = ['http://google.com','http://example.com','http://tecladocode.com/blog']

    loop = asyncio.get_event_loop()

    csv_file = open(FILENAME, "w", newline='')

    asyncState = type('', (), {})()
    asyncState.csv_file = csv_file
    asyncState.headers = None
    asyncState.csvwriter = None

    start = time.time()
    # loop.run_until_complete() -> resumes the Coroutines till complete
    # Run the event loop until a Future is done. Return the Future's result, or raise its exception.
    pages_fast = loop.run_until_complete(get_multiple_pages_efficient_FAST(loop, urls, asyncState))
    # pages_fast -> whatever get_multiple_pages_efficient_FAST() returned
    print(f'FAST took {time.time() - start}') # 0.6


    csv_file.close()
    if csv_file.closed:
        print('file is closed')
    if asyncState.csv_file.closed:
        print('async file is closed')

    # ----------------------------------------------------------------------------------

    for page in pages_fast:
        print(page)

if __name__ == '__main__':
    main()