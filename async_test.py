import asyncio
import aiohttp
import time


async def call_api(session, data):
    st_time = time.time()
    async with session.get("http://localhost:8082/long-external-api") as response:
        res = await response.text()
        print(data, res, time.time() - st_time)
        return res


async def exec_task(datas):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for data in datas:
            task = asyncio.create_task(call_api(session, data))
            tasks.append(task)
        await asyncio.gather(*tasks)


def main():
    datas = [i for i in range(100)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(exec_task(datas))


if __name__ == "__main__":
    main()
