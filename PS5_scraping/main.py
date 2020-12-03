"""
This script will scrape UK retailers to find when the PS5 is available
"""
import asyncio
import async_timeout
import aiohttp
import time
from datetime import datetime

from scrapper import getAvailability
from history_maker import make_history
from constants import RETAILERS

async def fetch_page(session, source, url):
    start = time.time()
    # async_timeout is a function that will terminate/raise exeption if request takes too long
    # in this case 30 seconds
    async with async_timeout.timeout(30):
        async with session.get(url) as response:
            availability = await getAvailability(source, response)
            return (response.status, availability, datetime.today().isoformat()) 

#-------------------------------------------------------------------------------
async def get_multiple_pages_efficient_FAST(loop, sources):
    list_of_futures = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for source, url in sources:
            list_of_futures.append(fetch_page(session, source, url))

        return await asyncio.gather(*list_of_futures)
# ----------------------------------------------------------------------------------

def main():
    start = time.time()

    sources = []
    for key in RETAILERS:
        metadata = RETAILERS[key]
        if(metadata is not None):
            sources.append((key, metadata["url"]))

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(get_multiple_pages_efficient_FAST(loop, sources))
    # ----------------------------------------------------------------------------------
    for result in results:
        make_history(result)

    print(f'FAST took {time.time() - start}') # 0.6

if __name__ == '__main__':
    main()

