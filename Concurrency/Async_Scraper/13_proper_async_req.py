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
            print(type(response)) # <class 'aiohttp.client_reqrep.ClientResponse'>
            print(response) # <ClientResponse(https://blog.tecladocode.com) [200 OK]>
            print(response.content) 
            # <CIMultiDictProxy('Date': 'Fri, 30 Oct 2020 14:13:48 GMT', 
            # 'Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 
            # 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d4f2b68fad9c8e362ac326fac9ae25fd31604067228; 
            # expires=Sun, 29-Nov-20 14:13:48 GMT; path=/; domain=.tecladocode.com; HttpOnly; SameSite=Lax', 
            # 'X-Powered-By': 'Express', 'Cache-Control': 'public, max-age=0', 'Vary': 'Accept-Encoding', 
            # 'CF-Cache-Status': 'DYNAMIC', 'cf-request-id': '061b7492820000c83bca1d0000000001', 
            # 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 
            # 'Report-To': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report?s=ly7ufT8C4Xyw6H5ECL%2Fe%2BBTGEHqgz8TpHFHHf9tnbyRA9EED%2FHtxqwTVw9QqpJQkDT55itqQY2Nl2pEm539hyjvJweHt%2BDbKnCoZPFEmd1aJUL42rw%3D%3D"}],
            # "group":"cf-nel","max_age":604800}', 'NEL': '{"report_to":"cf-nel","max_age":604800}', 'Server': 'cloudflare', 'CF-RAY': '5ea5bd30c91dc83b-AMS', 'Content-Encoding': 'gzip')>
            
            # print(response.content.read()) # <StreamReader 53134 bytes> <coroutine object StreamReader.read at 0x103b768c0>
            print(await response.content.read())
            print(f'{url} took {time.time() - start}')
            return response.status

# ----------------------------------------------------------------------------------
# Execute each future yourself and store and return response
async def get_multiple_pages_simple_SLOW(loop, urls):
    pages = []
    # aiohttp.ClientSession(loop=loop) -> create a pool of sessions and pass the asyncio loop so it doesn't create a new loop
    # each session contains a cookie storage
    async with aiohttp.ClientSession(loop=loop, auto_decompress=False) as session:
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
    # start = time.time()
    # # loop.run_until_complete() -> resumes the Coroutines till complete
    # # Run the event loop until a Future is done. Return the Future's result, or raise its exception.
    # pages = loop.run_until_complete(get_multiple_pages_simple_SLOW(loop, urls))
    # print(f'SLOW took {time.time() - start}') # 1.2

    start = time.time()
    # loop.run_until_complete() -> resumes the Coroutines till complete
    # Run the event loop until a Future is done. Return the Future's result, or raise its exception.
    pages_fast = loop.run_until_complete(get_multiple_pages_efficient_FAST(loop, urls))
    # pages_fast -> whatever get_multiple_pages_efficient_FAST() returned
    print(f'FAST took {time.time() - start}') # 0.6

    # ----------------------------------------------------------------------------------

    for page in pages_fast:
        print(page)

if __name__ == '__main__':
    main()