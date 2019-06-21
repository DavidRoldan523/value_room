import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time


def download_site(session, url):
    with session.get(url) as response:
        print(response.status_code)


async def get_data_asynchronous():
    sites = ["https://www.jython.org",
             "http://olympus.realpython.org/dice",
            ] * 80

    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            tasks = [loop.run_in_executor(executor, download_site, *(session, site)) for site in sites]
            for response in await asyncio.gather(*tasks):
                pass

def main():
    timee = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_data_asynchronous())
    loop.run_until_complete(future)
    print(f"Finish Process: {time.time() - timee}")

main()