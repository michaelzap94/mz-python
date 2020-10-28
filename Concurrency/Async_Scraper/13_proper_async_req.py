import asyncio
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
    async with session.get(url) as response:
        print(f'{url} took {time.time() - start}')
        return response.status

async def get_multiple_pages(loop, *urls):
    pages = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            pages.append(await fetch_page(session, url))
    return pages

def main():
    loop = asyncio.get_event_loop()
    urls = ['http://google.com','http://example.com','http://tecladocode.com/blog']

    start = time.time()

    # loop.run_until_complete() -> resumes the Coroutines till complete
    pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
    
    print(f'Total took {time.time() - start}')
    for page in pages:
        print(page)

if __name__ == '__main__':
    main()