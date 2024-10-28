import asyncio
import aiohttp
import requests
import time

async def fetch_data_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                raise Exception(f"Error: {response.status}")

async def main_async():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3',
        'https://jsonplaceholder.typicode.com/posts/4',
        'https://jsonplaceholder.typicode.com/posts/5',
    ]

    tasks = [fetch_data_async(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

# Mã sử dụng requests
def fetch_data_sync(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}")

def main_sync():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3',
        'https://jsonplaceholder.typicode.com/posts/4',
        'https://jsonplaceholder.typicode.com/posts/5',
    ]

    results = []
    for url in urls:
        data = fetch_data_sync(url)
        results.append(data)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    start_time_async = time.time()
    asyncio.run(main_async())
    end_time_async = time.time()
    print(f"Async time taken: {end_time_async - start_time_async:.2f} seconds")

    start_time_sync = time.time()
    main_sync()
    end_time_sync = time.time()
    print(f"Sync time taken: {end_time_sync - start_time_sync:.2f} seconds")
