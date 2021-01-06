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

headers={"User-Agent": "Requests"}

async def fetch_page(session, source, url):
    if(url is None):
        return (None, None, datetime.today().isoformat()) 
    # async_timeout is a function that will terminate/raise exeption if request takes too long
    # in this case 30 seconds
    async with async_timeout.timeout(30):
        async with session.get(url) as response:
            try:
                availability = await getAvailability(source, response)
                return (response.status, availability, datetime.today().isoformat()) 
            except Exception as e:
                return (response.status, None, datetime.today().isoformat()) 

#-------------------------------------------------------------------------------
async def get_multiple_pages_efficient_FAST(loop, sources):
    list_of_futures = []
    async with aiohttp.ClientSession(loop=loop, headers=headers) as session:
        for source, url in sources:
            list_of_futures.append(fetch_page(session, source, url))

        return await asyncio.gather(*list_of_futures)
# ----------------------------------------------------------------------------------

def main(loop):
    start = time.time()

    sources = []
    for key in RETAILERS:
        metadata = RETAILERS[key]
        if(metadata is not None):
            sources.append((key, metadata["url"]))
        else:
            sources.append((key, None))
    
    results = loop.run_until_complete(get_multiple_pages_efficient_FAST(loop, sources))
    # ----------------------------------------------------------------------------------
    make_history(results)

    return results

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
    except Exception as e:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    main(loop)

