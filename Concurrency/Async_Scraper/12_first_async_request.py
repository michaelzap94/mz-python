import aiohttp # third party that allows async http requests
import asyncio
import time

# aiohttp.ClientSession() - Pool of connections
# session.get(url)

# This is a Courutine that creates a pool of requests(session) and response
# BAD PRACTICE -> we are creating a POOL for EACH request, we should create a pool for all of them: 
# look at 13_proper_async_req.py
async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start} code: {response.status}')
            return response.status

# create an event loop on the asyncio
loop = asyncio.get_event_loop()
# fetch_page('http://google.com') -> will not return the response, it will just return a Coroutine Object
# loop.run_until_complete() -> resumes the Coroutines till complete
loop.run_until_complete(fetch_page('http://google.com'))

# async context manager -> it can have a yield in the __enter__ or __exit__
# it can suspend the execution at the start or end
# __enter__ && __exit__ --BECOMES--> __aenter__ && __aexit__

# MULTIPLE REQUESTS ==============================================================================

# create a list of a bunch of Coroutines
multiple_requests = [fetch_page('http://google.com') for i in range(50)]

start = time.time()
# run_until_complete([ONE COROUTINE]) -> so you can gather multiple using .gather(t1,t2,t3,t4,...)
# loop.run_until_complete() -> resumes the Coroutines till complete
# asyncio.gather(*multiple_requests) -> gather all fetch_page(), and only return when all tasks have finished
result = loop.run_until_complete(asyncio.gather(*multiple_requests))
print(f'multiple_requests took {time.time() - start}')

print(result)