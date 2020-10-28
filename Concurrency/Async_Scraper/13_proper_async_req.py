import asyncio
import async_timeout
import aiohttp
import time


async def fetch_page(session, url):
    """Coroutine that will create a response and return the response.status

    Args:
        session (asyncio.ClientSession()): Reference to a pool of requests
        url (str): url string

    Returns:
        int: status code
    """
    start = time.time()
    # async_timeout is a function that will terminate/raise exeption if request takes too long
    # in this case 30 seconds
    async with async_timeout.timeout(30):
        # make the session.get(url) call and get it as a response
        async with session.get(url) as response:
            print(f'{url} took {time.time() - start}')
            return response.status

# ----------------------------------------------------------------------------------
# Execute each future yourself and store and return response
async def get_multiple_pages_simple_SLOW(loop, urls):
    pages = []
    # aiohttp.ClientSession(loop=loop) -> create a pool of sessions and pass the asyncio loop so it doesn't create a new loop
    # each session contains a cookie storage
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            result = await fetch_page(session, url)
            pages.append(result)

    return pages
#OR
# GATHER all futures and let asyncio execute them
async def get_multiple_pages_efficient_FAST(loop, urls):
    list_of_futures = []
    # aiohttp.ClientSession(loop=loop) -> create a pool of sessions and pass the asyncio loop so it doesn't create a new loop
    # each session contains a cookie storage
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            list_of_futures.append(fetch_page(session, url))
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

    # ----------------------------------------------------------------------------------
    start = time.time()
    # loop.run_until_complete() -> resumes the Coroutines till complete
    # Run the event loop until a Future is done. Return the Future's result, or raise its exception.
    pages = loop.run_until_complete(get_multiple_pages_simple_SLOW(loop, urls))
    print(f'SLOW took {time.time() - start}') # 1.2

    start = time.time()
    # loop.run_until_complete() -> resumes the Coroutines till complete
    # Run the event loop until a Future is done. Return the Future's result, or raise its exception.
    pages_fast = loop.run_until_complete(get_multiple_pages_efficient_FAST(loop, urls))
    print(f'FAST took {time.time() - start}') # 0.6

    # ----------------------------------------------------------------------------------

    for page in pages_fast:
        print(page)

if __name__ == '__main__':
    main()